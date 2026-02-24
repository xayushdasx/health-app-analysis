"""
Health App Analytics — Streamlit dashboard.
Run with: streamlit run dashboard.py
Data is loaded from MySQL (database: health_app). Set MYSQL_PASSWORD env var if needed.
"""

import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mysql.connector

# -----------------------------------------------------------------------------
# Page config and data loading
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="Health App Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_data
def load_data():
    """Load and preprocess data from MySQL; cache to avoid reloading on rerun."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.environ.get("MYSQL_PASSWORD", "ayushdas@06"),
        database="health_app",
    )
    users = pd.read_sql("SELECT * FROM users", conn)
    sessions = pd.read_sql("SELECT * FROM sessions", conn)
    subs = pd.read_sql("SELECT * FROM subscriptions", conn)
    payments = pd.read_sql("SELECT * FROM payments", conn)
    conn.close()

    users["signup_date"] = pd.to_datetime(users["signup_date"])
    sessions["date"] = pd.to_datetime(sessions["date"])
    subs["start_date"] = pd.to_datetime(subs["start_date"])
    payments["date"] = pd.to_datetime(payments["date"])

    return users, sessions, subs, payments


users, sessions, subs, payments = load_data()

# -----------------------------------------------------------------------------
# 1. Overview Metrics
# -----------------------------------------------------------------------------

st.title("Health App Analytics")
st.markdown("---")

st.header("1. Overview Metrics")

total_users = len(users)
total_sessions = len(sessions)
total_subscribers = subs["user_id"].nunique()
successful_payments = payments[payments["status"] == "success"]
total_revenue = successful_payments["amount"].sum()

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Users", f"{total_users:,}")
m2.metric("Total Sessions", f"{total_sessions:,}")
m3.metric("Total Subscribers", f"{total_subscribers:,}")
m4.metric("Total Revenue (₹)", f"{total_revenue:,.0f}")

st.markdown("---")

# -----------------------------------------------------------------------------
# 2. Funnel: Visitors → Consult Users → Subscribers
# -----------------------------------------------------------------------------

st.header("2. Funnel Visualization")

visitors = sessions["user_id"].nunique()
consult_users = sessions[sessions["feature_used"] == "consult"]["user_id"].nunique()
subscriber_count = subs["user_id"].nunique()

funnel_df = pd.DataFrame({
    "Stage": ["Visitors", "Consult Users", "Subscribers"],
    "Count": [visitors, consult_users, subscriber_count],
})

fig_funnel = px.bar(
    funnel_df,
    x="Stage",
    y="Count",
    text="Count",
    color="Count",
    color_continuous_scale="Blues",
)
fig_funnel.update_traces(texttemplate="%{text:,}", textposition="outside")
fig_funnel.update_layout(
    showlegend=False,
    xaxis_title="",
    yaxis_title="Users",
    margin=dict(t=40, b=40),
    height=350,
)
st.plotly_chart(fig_funnel, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 3. Feature Adoption
# -----------------------------------------------------------------------------

st.header("3. Feature Adoption")

feature_users = (
    sessions.groupby("feature_used")["user_id"]
    .nunique()
    .sort_values(ascending=True)
    .reset_index()
)
feature_users.columns = ["feature_used", "unique_users"]

fig_features = px.bar(
    feature_users,
    x="unique_users",
    y="feature_used",
    orientation="h",
    text="unique_users",
)
fig_features.update_traces(texttemplate="%{text:,}", textposition="outside")
fig_features.update_layout(
    xaxis_title="Unique users",
    yaxis_title="Feature",
    margin=dict(t=40, b=40),
    height=350,
)
st.plotly_chart(fig_features, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 4. Conversion by Channel
# -----------------------------------------------------------------------------

st.header("4. Conversion by Channel")

subscriber_ids = set(subs["user_id"])
users_with_channel = users.copy()
users_with_channel["subscribed"] = users_with_channel["user_id"].isin(subscriber_ids)

channel_stats = (
    users_with_channel.groupby("acquisition_channel")
    .agg(users=("user_id", "count"), subscribers=("subscribed", "sum"))
    .reset_index()
)
channel_stats["conversion_rate"] = (
    channel_stats["subscribers"] / channel_stats["users"] * 100
).round(1)

fig_channel = px.bar(
    channel_stats.sort_values("conversion_rate", ascending=True),
    x="conversion_rate",
    y="acquisition_channel",
    orientation="h",
    text="conversion_rate",
)
fig_channel.update_traces(texttemplate="%{text}%", textposition="outside")
fig_channel.update_layout(
    xaxis_title="Conversion rate (%)",
    yaxis_title="Acquisition channel",
    margin=dict(t=40, b=40),
    height=350,
)
st.plotly_chart(fig_channel, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. Engagement Distribution (active_days per user)
# -----------------------------------------------------------------------------

st.header("5. Engagement Distribution")

active_days = (
    sessions.groupby("user_id")["date"]
    .apply(lambda x: x.dt.date.nunique())
    .reset_index(name="active_days")
)

fig_engagement = px.histogram(
    active_days,
    x="active_days",
    nbins=min(50, active_days["active_days"].nunique()),
)
fig_engagement.update_layout(
    xaxis_title="Active days per user",
    yaxis_title="Number of users",
    margin=dict(t=40, b=40),
    height=350,
)
st.plotly_chart(fig_engagement, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 6. Cohort Retention Heatmap
# -----------------------------------------------------------------------------

st.header("6. Cohort Retention")

users["cohort_month"] = users["signup_date"].dt.to_period("M")
sessions_with_cohort = sessions.merge(
    users[["user_id", "cohort_month"]], on="user_id", how="left"
)
sessions_with_cohort["activity_month"] = sessions_with_cohort["date"].dt.to_period("M")

cohort_counts = (
    sessions_with_cohort.groupby(["cohort_month", "activity_month"])["user_id"]
    .nunique()
    .reset_index()
)
cohort_pivot = cohort_counts.pivot(
    index="cohort_month", columns="activity_month", values="user_id"
)
cohort_sizes = users.groupby("cohort_month").size()
retention_pct = cohort_pivot.div(cohort_sizes, axis=0).fillna(0) * 100
retention_pct = retention_pct.round(1)

fig_retention = go.Figure(
    data=go.Heatmap(
        z=retention_pct.values,
        x=[str(c) for c in retention_pct.columns],
        y=[str(i) for i in retention_pct.index],
        colorscale="YlGnBu",
        zmin=0,
        zmax=100,
        text=retention_pct.values,
        texttemplate="%{text}%",
        textfont={"size": 10},
        hovertemplate="Cohort %{y}, Month %{x}<br>Retention: %{z}%<extra></extra>",
    )
)
fig_retention.update_layout(
    xaxis_title="Activity month",
    yaxis_title="Cohort (signup month)",
    height=400,
    margin=dict(t=40, b=80),
)
st.plotly_chart(fig_retention, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 7. Churn vs Engagement (avg sessions)
# -----------------------------------------------------------------------------

st.header("7. Churn vs Engagement")

subs["churn_flag"] = subs["renewal_status"] == "churned"
session_count = (
    sessions.groupby("user_id").size().reset_index(name="session_count")
)
subs_with_sessions = subs.merge(session_count, on="user_id", how="left")
subs_with_sessions["session_count"] = (
    subs_with_sessions["session_count"].fillna(0).astype(int)
)

churn_engagement = (
    subs_with_sessions.groupby("churn_flag")["session_count"]
    .mean()
    .round(2)
    .reset_index()
)
churn_engagement["churn_flag"] = churn_engagement["churn_flag"].map(
    {False: "Retained", True: "Churned"}
)

fig_churn = px.bar(
    churn_engagement,
    x="churn_flag",
    y="session_count",
    text="session_count",
    color="session_count",
    color_continuous_scale="RdYlGn_r",
)
fig_churn.update_traces(textposition="outside")
fig_churn.update_layout(
    xaxis_title="",
    yaxis_title="Avg sessions per user",
    showlegend=False,
    margin=dict(t=40, b=40),
    height=350,
)
st.plotly_chart(fig_churn, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 8. Revenue Trends (monthly)
# -----------------------------------------------------------------------------

st.header("8. Revenue Trends")

success_payments = payments[payments["status"] == "success"].copy()
success_payments["month"] = success_payments["date"].dt.to_period("M").astype(str)
monthly_revenue = (
    success_payments.groupby("month")["amount"].sum().reset_index()
)

fig_revenue = px.line(
    monthly_revenue,
    x="month",
    y="amount",
    markers=True,
)
fig_revenue.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue (₹)",
    margin=dict(t=40, b=80),
    height=350,
)
fig_revenue.update_traces(line_color="#1f77b4")
st.plotly_chart(fig_revenue, use_container_width=True)

st.markdown("---")
st.caption("Health App Analytics Dashboard — data from /data")
