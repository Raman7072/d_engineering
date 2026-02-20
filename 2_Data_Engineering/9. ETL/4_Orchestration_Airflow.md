# Airflow – Your First Taste of DAG-Based Data Workflows

## 🚀 Summary

### What Is Apache Airflow?

**Apache Airflow** is an open-source workflow orchestration tool that allows you to define, schedule, and monitor data pipelines using Python.

It helps automate tasks like:
- Extracting data
- Transforming data
- Loading data into warehouses
- Updating dashboards
- Sending alerts

Instead of manually running scripts, Airflow schedules and manages everything for you.

> Think of it as a **choreographer for your data pipelines**.

---

## 🧩 DAG-Based Workflow

At the core of Airflow is a **DAG (Directed Acyclic Graph)**.

### What is a DAG?

- **Directed** → Tasks have a direction (A → B → C)
- **Acyclic** → No loops allowed
- **Graph** → A flow of connected tasks

Each DAG defines:
- Tasks
- Order of execution
- Dependencies between tasks

### Example Workflow
```python
[Extract CSV] >> [Clean Data] >> [Load to DB] >> [Send Slack Alert]
```

---

### Example Airflow DAG Code

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extracting data...")

def transform():
    print("Transforming data...")

def load():
    print("Loading data...")

with DAG(
    dag_id="simple_etl_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    task_extract = PythonOperator(
        task_id="extract_task",
        python_callable=extract
    )

    task_transform = PythonOperator(
        task_id="transform_task",
        python_callable=transform
    )

    task_load = PythonOperator(
        task_id="load_task",
        python_callable=load
    )

    task_extract >> task_transform >> task_load
```

---

### 🗄 Metadata Database
Airflow stores all workflow information in a **metadata database**, including:
- Existing DAGs
- Task execution history
- Failures
- Scheduled runs
- Logs and retries

This acts as Airflow’s “brain,” enabling:
- Smart retries
- cheduling
- Monitoring

Without this database, Airflow cannot function properly.

---

### 🌐 Webserver UI
Airflow includes a built-in web interface that allows you to:
- View DAG graphs
- Check execution history
- Inspect logs
- Trigger runs manually
- Pause/unpause DAGs

This makes debugging and monitoring much easier compared to manually checking logs via SSH.

---

### 🔐 Roles and Permissions (RBAC)
Airflow supports **Role-Based Access Control (RBAC)**.

You can assign roles such as:

- **Admin** → Full system control
- **Developer** → Create and modify DAGs
- **Viewer** → Monitor w

This ensures:
- Security
- Controlled access
- Safe team collaboration

---

### 🐳 DockerOperator
The DockerOperator allows tasks to run inside Docker containers.

#### Why Use It?
- Isolated environments
- Custom dependencies
- Reproducibility
- Clean execution

#### Example
```python
from airflow.providers.docker.operators.docker import DockerOperator

docker_task = DockerOperator(
    task_id="run_model_training",
    image="pytorch/pytorch:1.13-cuda11.8-cudnn8-runtime",
    command="python train.py",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge"
)
```

---

### ⏳ Sensors – Event-Based Waiting
Sensors are special tasks that **wait for a condition before continuing**.

Examples:
- Wait for a file in S3
- Wait for a SQL table update
- Wait for an API response

##### Example: File Sensor
```python
from airflow.sensors.filesystem import FileSensor

wait_for_file = FileSensor(
    task_id="wait_for_file",
    filepath="/data/input.csv",
    poke_interval=60,
    timeout=600
)
```

Sensors make pipelines reactive instead of purely time-based.

---

### ✅ Answers to the “Try This Out!” Section
#### 1️⃣ Sketch Your Morning Routine as a DAG
```
Wake Up
   ↓
Brush Teeth
   ↓
Make Coffee
   ↓
Check Emails
```

In Airflow-style dependency:
```python
wake_up >> brush_teeth >> make_coffee >> check_emails
```

---

#### 2️⃣ Real Workflow Example
##### Scenario: Weekly productivity summary
Workflow:
1. Pull daily task logs
2. Calculate total time spent
3. Generate summary report
4. Email manager

Airflow-style:
```python
pull_logs >> calculate_time >> generate_report >> email_manager
```

---

#### 3️⃣ Explore the Airflow UI
When you open the Airflow UI, you’ll see:
- DAG Graph View
- Grid View (task history)
- Logs per task
- Trigger buttons
- Pause/Resume controls

---

#### 4️⃣ “Astronomer Airflow Docker tutorial” – What You’ll Learn
You’ll typically see how teams:
- Run Airflow inside Docker containers
- Use docker-compose for local development
- Deploy Airflow in production
- Manage dependencies cleanly

---

#### 5️⃣ Three Things I’d Automate Using Airflow
Here are 3 practical ideas:
1. Daily weather data collection and dashboard update
2. Weekly expense tracking and budget summary
3. Automated ML model retraining every month

---

### 📚 Learn More
- Airflow Official Documentation
- DAG Concepts
- Operators and Sensors
- Scheduling & Time Concepts
- Production Deployment Strategies

---

### 🏁 Final Takeaway
Airflow is not just a scheduler.

It is:
- A workflow orchestrator
- A monitoring tool
- A failure-handling system
- A production-ready automation platform
If you understand DAGs, operators, scheduling, and the metadata database — you understand the foundation of modern data engineering workflows.
