# ETL Workflow Orchestration with Dagster

A practical introduction to asset-based data orchestration using Dagster.

This repository demonstrates how to build modern ETL pipelines using Dagster’s asset-based approach instead of traditional task-based orchestration.

---

## 📌 Overview

Traditional orchestration tools focus on *tasks*.

Dagster focuses on *data assets*.

An asset is any meaningful data output in your pipeline, such as:

- A database table
- A cleaned dataset
- A report
- A machine learning model
- A dashboard dataset

Dagster understands:
- How assets are created
- What they depend on
- When they need to be refreshed
- Whether they are up-to-date

This allows data teams to manage data workflows more reliably and transparently.

---

## 🧠 Why Asset-Based Orchestration?

Instead of asking:

> "Did my script run?"

You ask:

> "Is my data up-to-date?"

Benefits:

- Automatic dependency tracking
- Recompute only what is necessary
- Built-in data lineage
- Strong observability
- Easier debugging

---

## 🏗 Example Pipeline

This project demonstrates a simple ETL workflow:

1. Extract raw sales data  
2. Transform it into cleaned sales data  
3. Generate a weekly summary report  

Each step is defined as a Dagster asset.

Dagster automatically:
- Determines execution order
- Tracks dependencies
- Logs materializations
- Recomputes downstream assets only when required

---

## 📂 Project Structure

```
dagster-etl-project/
│
├── assets/
│   ├── raw_sales.py
│   ├── cleaned_sales.py
│   └── weekly_report.py
│
├── definitions.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

- Python 3.9+
- Basic understanding of ETL concepts
- Familiarity with Python

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dagster-etl-project.git
cd dagster-etl-project
```

### 2. Create Virtual Environment

```python
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```python
pip install -r requirements.txt
```

Example `requirements.txt`:

```bash
dagster
dagster-webserver
pandas
```

---

## 🚀 Minimal Dagster Example

### assets/raw_sales.py

```python
from dagster import asset
import pandas as pd

@asset
def raw_sales_data():
    data = {
        "product": ["A", "B", "C"],
        "sales": [100, 200, 150]
    }
    return pd.DataFrame(data)
```

---

### assets/cleaned_sales.py

```python
from dagster import asset
import pandas as pd

@asset
def cleaned_sales_data(raw_sales_data):
    df = raw_sales_data.copy()
    df["sales"] = df["sales"] * 1.1
    return df
```

---

### assets/weekly_report.py

```python
from dagster import asset

@asset
def weekly_summary_report(cleaned_sales_data):
    total_sales = cleaned_sales_data["sales"].sum()
    return {"weekly_total_sales": total_sales}
```

---

### definitions.py

```python
from dagster import Definitions
from assets.raw_sales import raw_sales_data
from assets.cleaned_sales import cleaned_sales_data
from assets.weekly_report import weekly_summary_report

defs = Definitions(
    assets=[
        raw_sales_data,
        cleaned_sales_data,
        weekly_summary_report
    ]
)
```

---

## ▶️ Running Dagster

Start Dagster UI:

```
dagster dev
```

Open in browser:


🌐[http://127.0.0.1:3000](http://127.0.0.1:3000)

You will see:

- Asset graph visualization
- Dependency relationships
- Execution logs
- Materialization history

---

## 🔍 Observability Features

Dagster allows you to:

- Visualize asset lineage
- Inspect run logs
- Check freshness
- Debug failures
- Re-materialize specific assets

This removes guesswork from debugging data pipelines.

---

## ⚖️ Dagster vs Airflow (Quick Comparison)

| Feature            | Airflow        | Dagster        |
|-------------------|---------------|---------------|
| Core Concept       | Task          | Asset         |
| Primary Focus      | Execution     | Data Outputs  |
| Dependency Logic   | Manual        | Automatic     |
| Observability      | Basic         | Advanced UI   |

---

## 🧪 Practice Ideas

- Add a database source instead of hardcoded data
- Add scheduling
- Add data quality checks
- Add partitioned assets
- Deploy to production environment

---

## 📚 Learn More

- Official Dagster Documentation  
- Dagster GitHub Repository  

---

## 🎯 Final Takeaway

Dagster shifts orchestration from managing scripts to managing data.

Instead of focusing on code execution, you focus on data reliability, freshness, and lineage.

That mindset aligns directly with modern data engineering best practices.
