# 🩺 Health App Growth & Monetization Analytics

End-to-end product analytics project exploring user engagement, retention,
and subscription conversion for a digital health application.

This project combines **SQL-style product thinking, Python analysis, and an
interactive Streamlit dashboard** to uncover growth and monetization insights.

---

## Case Study Walkthrough
<img width="368" height="137" alt="image" src="https://github.com/user-attachments/assets/6dd166e1-d6c3-4681-9c88-ce151dce5840" />
[![Case Study](https://github.com/user-attachments/assets/6dd166e1-d6c3-4681-9c88-ce151dce5840)](https://www.notion.so/Medicine-App-Monetization-Funnel-Analysis-311bbdae477981d6ac54dadfd06b1016?source=copy_link)

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


