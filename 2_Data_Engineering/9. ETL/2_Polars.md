# Polars in Data Engineering — Summary & Practical Guide

## What Is Polars?

**Polars** is a fast, modern DataFrame library designed for **high-performance data processing** in Python and Rust. It is built for scalability, low memory usage, and clean transformation logic—making it ideal for real-world data engineering workloads.

---

## Question: Why Do We Need Polars?

### Short Answer  
Because traditional tools struggle with **large, messy, modern datasets**.

### Detailed Answer  
As datasets grow (millions of rows, logs, transactions, time-series data), many tools:

- Load entire datasets into memory
- Use only a single CPU core
- Execute transformations step-by-step
- Become slow, crash-prone, or unreadable

**Polars solves these problems by default** through parallel execution, lazy evaluation, and columnar processing.

---

## Real-World Problems Polars Solves

### 1. Memory Overload
**Problem:** Entire files loaded into RAM  
**Polars Solution:**  
- Columnar execution  
- Streaming & chunked processing  
- Works with datasets larger than RAM  

---

### 2. Sluggish Performance
**Problem:** Single-core, row-by-row processing  
**Polars Solution:**  
- Automatic multi-threading  
- SIMD optimizations  
- Written in Rust for speed and safety  

---

### 3. Complex, Repetitive Code
**Problem:** Long, unreadable transformation pipelines  
**Polars Solution:**  
- Chainable, expressive syntax  
- Clear transformation logic  

---

### 4. Waiting Too Long for Results
**Problem:** Every operation executes immediately  
**Polars Solution:**  
- **Lazy execution**
- Builds an optimized query plan
- Executes only when `.collect()` is called  

---

### 5. Painful Date & Time Handling
**Problem:** Error-prone datetime parsing  
**Polars Solution:**  
- First-class Date & Datetime support  
- Clean, readable APIs  

---

## When Should You Use Polars?

Use Polars if:

- Your dataset has **100k+ rows**
- Performance matters
- RAM is limited
- You build repeatable pipelines
- You want SQL-like clarity in Python

---

## Key Features of Polars

### 1. Built for Speed
- Written in **Rust**
- Multi-core by default
- Safe, crash-free execution

---

### 2. Lazy Execution (Core Superpower)

**Concept:**  
Instead of executing each step immediately, Polars:

1. Collects all transformations
2. Optimizes the full plan
3. Executes once efficiently

#### Polars (Lazy Execution)
```python
import polars as pl

q = (
    pl.scan_csv("sales.csv")
      .filter(pl.col("amount") > 500)
      .group_by("region")
      .agg(pl.col("amount").sum().alias("total_sales"))
)

df = q.collect()
print(df)
```

#### Equivalent SQL
```sql
SELECT region,
       SUM(amount) AS total_sales
FROM sales
WHERE amount > 500
GROUP BY region;
```

---

### 3. Handles Datasets Larger Than RAM
- Processes data in batches
- Ideal for logs, events, historical data

---

### 4. Chainable & Readable Syntax

#### Polars
```python
import polars as pl

df = (
    pl.read_csv("data.csv")
      .filter(pl.col("status") == "Active")
      .with_columns(
          (pl.col("price") * 1.1).alias("adjusted_price")
      )
      .sort("adjusted_price", descending=True)
)
```

#### SQL Equivalent
```sql
SELECT *,
       price * 1.1 AS adjusted_price
FROM data
WHERE status = 'Active'
ORDER BY adjusted_price DESC;
```

---

### 5. Excellent Parquet Support

#### Polars
```python
df = pl.read_parquet(
    "data.parquet",
    columns=["user_id", "signup_date"]
)
```

#### SQL (Parquet Engine)
```sql
SELECT user_id, signup_date
FROM parquet."path/to/data.parquet";
```

##### Why this matters:
Polars reads only required columns, saving memory and time.

---

### 6. Friendly DateTime Handling

#### Polars
```python
df = pl.read_csv("events.csv").with_columns(
    pl.col("timestamp")
      .str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S")
      .alias("event_time")
)
```

#### SQL
```sql
SELECT
  event,
  PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S', timestamp) AS event_time
FROM events;
```

---

### Memory Efficiency

- Uses ~2–4× dataset size in RAM
- Fewer crashes
- Faster experimentation
- Works well on laptops

---

### Hands-On Exercises (With Code)

#### 1. Load a CSV
```python
import polars as pl

df = pl.read_csv("titanic.csv")
print(df.head())
```

#### 2. Clean & Filter Data
```python
df_clean = (
    df.drop_nulls("Age")
      .filter(pl.col("Fare") > 100)
)
```

#### 3. Group & Aggregate
```python
df.group_by("Pclass").agg(
    pl.col("Fare").mean().alias("avg_fare")
)
```

#### 4. Save & Load Parquet
```python
df_clean.write_parquet("cleaned.parquet")
df_new = pl.read_parquet("cleaned.parquet")
```

#### 5. DateTime Conversion
```python
df = pl.read_csv("events.csv").with_columns(
    pl.col("timestamp")
      .str.strptime(pl.Datetime)
)
```

---

### Mini Project: Titanic Dataset (Tasks Only)

#### Scenario
You are given the Titanic dataset and must prepare it for analysis.

##### Tasks

1. Load `titanic.csv` using Polars
2. Drop rows with missing values in:
   - `Age`
   - `Fare`
   - `Embarked`
3. Create a new column `Age_Group`:
   - `< 18` → Child
   - `18–60` → Adult
   - `> 60` → Senior
4. Remove rows where `Fare <= 0`
5. Sort passengers by `Fare` (descending)
6. Save the result as `titanic_cleaned.parquet`
