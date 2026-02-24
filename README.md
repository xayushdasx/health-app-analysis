<<<<<<< HEAD
# 🩺 Health App Growth & Monetization Analytics

End-to-end product analytics project exploring user engagement, retention,
and subscription conversion for a digital health application.

This project combines **SQL-style product thinking, Python analysis, an
interactive Streamlit dashboard, and an Excel dashboard** to uncover growth and monetization insights.

---

## Case Study Walkthrough
<a href="https://www.notion.so/Medicine-App-Monetization-Funnel-Analysis-311bbdae477981d6ac54dadfd06b1016?source=copy_link">
  <img src="https://github.com/user-attachments/assets/6dd166e1-d6c3-4681-9c88-ce151dce5840" width="700"/>
</a>

**Full analysis, insights & product narrative:**  
🔗 **[Medicine App Monetization Funnel Analysis — Notion Case Study](https://www.notion.so/Medicine-App-Monetization-Funnel-Analysis-311bbdae477981d6ac54dadfd06b1016?source=copy_link)**

This includes:

- SQL insights with screenshots
- Python analytics deep-dive
- Visual dashboard walkthrough
- Clear product recommendations

---

## 🎯 Objective

Understand how users interact with core health app features and identify opportunities to:

- Improve activation and retention
- Increase subscription conversion
- Optimize pricing and monetization
- Detect behavioral signals linked to churn

---

## Key Insights

- Feature engagement strongly correlates with subscription conversion
- Most users exhibit low repeat engagement beyond initial sessions
- Engagement depth is a strong predictor of churn
- Pricing impacts both conversion volume and total revenue
- Funnel leakage occurs between feature exploration and subscription

---

## Dataset

Synthetic product dataset simulating real health app behavior across onboarding,
sessions, subscriptions, and payments.

| File | Description |
|------|-------------|
| `users.csv` | Signup data and acquisition channels |
| `sessions.csv` | Feature usage and activity logs |
| `subscriptions.csv` | Plan adoption and lifecycle |
| `payments.csv` | Revenue transactions |

### Where the data comes from

- **Notebook (`analysis.ipynb`)** and **Dashboard (`dashboard.py`)** — Both read from a **MySQL database** (database name: `health_app`, tables: `users`, `sessions`, `subscriptions`, `payments`). You need MySQL running locally with that database and tables populated. Connection uses `mysql.connector` and `pd.read_sql()`; set the `MYSQL_PASSWORD` environment variable (or use the fallback in code) as needed.
- **Excel dashboard** — Built from SQL query outputs exported from MySQL as CSV, then imported into Excel (raw data → pivot tables → dashboard sheet).
- **CSV files** in `data/` are included for reference, backup, or for importing into your own MySQL instance. You do **not** link or host the actual database on GitHub; others set up MySQL locally and load the data (e.g. from these CSVs or a schema/import script) to run the notebook and Streamlit dashboard.

---

## Analysis Components

### Notebook Analysis (`analysis.ipynb`)

- Funnel conversion
- Feature adoption
- Engagement segmentation
- Cohort retention heatmap
- Churn vs engagement
- Pricing simulation

### Python Deep Dive

- Cohort retention heatmap
- Behavioral churn analysis
- Pricing sensitivity simulation
- Engagement distribution

### Interactive Dashboard (`dashboard.py`)

The Streamlit dashboard (MySQL-backed) includes:

1. Overview metrics — users, sessions, subscribers, revenue
2. Funnel visualization — visitor → consult → subscriber
3. Feature adoption insights
4. Conversion by acquisition channel
5. Engagement distribution
6. Cohort retention heatmap
7. Churn vs engagement comparison
8. Monthly revenue trends

### Excel Dashboard

An Excel-based dashboard was created to present key product and monetization insights in a stakeholder-friendly format.

#### Workflow

1. SQL query outputs were exported from MySQL as CSV files.
2. The CSV files were imported into Excel and organized in a structured `raw_data` sheet.
3. Pivot tables were built to aggregate and segment data across acquisition, engagement, and monetization dimensions.
4. Visualizations were created from pivots and arranged into a single dashboard sheet.

#### Dashboard Components

The dashboard includes:

- **KPI Strip** — Visitors, consult users, subscribers, and total revenue
- **Funnel Visualization** — Visitor → Consult → Subscriber conversion flow
- **Acquisition Performance** — Conversion rate by channel
- **Feature Adoption** — Unique users by feature usage
- **Behavioral Conversion** — Feature-level subscription impact
- **Subscription Mix** — Distribution of plan types
- **Revenue Trend** — Monthly successful payment revenue
- **Engagement Segmentation** — Casual, moderate, and power user segments
- **Activation Speed** — Average time to convert

#### Design Approach

- A dedicated dashboard sheet was used for clean presentation
- Gridlines were removed to improve visual clarity
- Consistent chart formatting and layout were applied
- Pivot-based visuals enable filtering and drill-down exploration

This Excel dashboard complements the Python and Streamlit analysis by providing a concise, presentation-ready view of product performance and monetization drivers.

---

## Run Locally

### 1️. Clone the repo

```bash
git clone https://github.com/xayushdasx/health-app-analysis.git
cd health-app-analysis
```

### 2️. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️. Install dependencies

```bash
pip install -r requirements.txt
```

### Prerequisites (Notebook & Dashboard)

- **MySQL** running locally with database `health_app` and tables `users`, `sessions`, `subscriptions`, `payments` (same schema as the CSVs in `data/`). Load the CSVs into MySQL if needed.
- Set `MYSQL_PASSWORD` environment variable, or use the fallback in the notebook/dashboard code.

### Run Notebook

```bash
jupyter notebook analysis.ipynb
```

### Run Dashboard

```bash
python -m streamlit run dashboard.py
```

App opens at **http://localhost:8501** (or the next available port if 8501 is in use).

---

## Skills Demonstrated

- Product analytics & funnel thinking
- Cohort and retention analysis
- Behavioral segmentation
- Monetization and pricing experimentation
- Dashboard development (Streamlit & Excel)
- SQL-to-Excel workflow and pivot-based reporting
- Insight storytelling

---

## 📂 Project Structure

```
health-app-analysis/
├── README.md
├── requirements.txt
├── analysis.ipynb          # Python analysis (MySQL)
├── dashboard.py            # Streamlit dashboard (MySQL)
├── data/                   # CSV exports (reference / MySQL import)
│   ├── users.csv
│   ├── sessions.csv
│   ├── subscriptions.csv
│   └── payments.csv
├── scripts/
│   └── generate_data.py
└── (Excel dashboard)       # Raw data → Pivots → Dashboard sheet
```

---

## Future Extensions

- A/B testing simulations for feature nudges
- Predictive churn modeling
- Dashboard deployment
- Pricing experimentation across tiers

---

=======
# 🩺 Health App Growth & Monetization Analytics

End-to-end product analytics project exploring user engagement, retention,
and subscription conversion for a digital health application.

This project combines **SQL-style product thinking, Python analysis, and an
interactive Streamlit dashboard** to uncover growth and monetization insights.

---

## Case Study Walkthrough
<a href="https://www.notion.so/Medicine-App-Monetization-Funnel-Analysis-311bbdae477981d6ac54dadfd06b1016?source=copy_link">
  <img src="https://github.com/user-attachments/assets/6dd166e1-d6c3-4681-9c88-ce151dce5840" width="700"/>
</a>

**Full analysis, insights & product narrative:**  
🔗 **[Medicine App Monetization Funnel Analysis — Notion Case Study](https://www.notion.so/Medicine-App-Monetization-Funnel-Analysis-311bbdae477981d6ac54dadfd06b1016?source=copy_link)**

This includes:

- SQL insights with screenshots
- Python analytics deep-dive
- Visual dashboard walkthrough
- Clear product recommendations

---

## 🎯 Objective

Understand how users interact with core health app features and identify opportunities to:

- Improve activation and retention
- Increase subscription conversion
- Optimize pricing and monetization
- Detect behavioral signals linked to churn

---

## Key Insights

- Feature engagement strongly correlates with subscription conversion
- Most users exhibit low repeat engagement beyond initial sessions
- Engagement depth is a strong predictor of churn
- Pricing impacts both conversion volume and total revenue
- Funnel leakage occurs between feature exploration and subscription

---

## Dataset

Synthetic product dataset simulating real health app behavior across onboarding,
sessions, subscriptions, and payments.

| File | Description |
|------|-------------|
| `users.csv` | Signup data and acquisition channels |
| `sessions.csv` | Feature usage and activity logs |
| `subscriptions.csv` | Plan adoption and lifecycle |
| `payments.csv` | Revenue transactions |

---

## Analysis Components

### Notebook Analysis (`analysis.ipynb`)

- Funnel conversion
- Feature adoption
- Engagement segmentation
- Cohort retention heatmap
- Churn vs engagement
- Pricing simulation

### Python Deep Dive

- Cohort retention heatmap
- Behavioral churn analysis
- Pricing sensitivity simulation
- Engagement distribution

### Interactive Dashboard (`dashboard.py`)

The Streamlit dashboard includes:

1. Overview metrics — users, sessions, subscribers, revenue
2. Funnel visualization — visitor → consult → subscriber
3. Feature adoption insights
4. Conversion by acquisition channel
5. Engagement distribution
6. Cohort retention heatmap
7. Churn vs engagement comparison
8. Monthly revenue trends

---

## Run Locally

### 1️. Clone the repo

```bash
git clone https://github.com/xayushdasx/health-app-analysis.git
cd health-app-analysis
```

### 2️. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️. Install dependencies

```bash
pip install -r requirements.txt
```

### Run Notebook

```bash
jupyter notebook analysis.ipynb
```

### Run Dashboard

```bash
python -m streamlit run dashboard.py
```

App opens at: **http://localhost:8501**

---

## Skills Demonstrated

- Product analytics & funnel thinking
- Cohort and retention analysis
- Behavioral segmentation
- Monetization and pricing experimentation
- Dashboard development
- Insight storytelling

---

## 📂 Project Structure

```
health-app-analysis/
├── README.md
├── requirements.txt
├── analysis.ipynb
├── dashboard.py
├── data/
│   ├── users.csv
│   ├── sessions.csv
│   ├── subscriptions.csv
│   └── payments.csv
└── scripts/
    └── generate_data.py
```

---

## Future Extensions

- A/B testing simulations for feature nudges
- Predictive churn modeling
- Dashboard deployment
- Pricing experimentation across tiers

---



>>>>>>> 5f1f1b15ebc96eb6baad81f4cf306ec06b4c5843
