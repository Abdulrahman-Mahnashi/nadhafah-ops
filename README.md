
# Nadhafah Ops

AI-powered operational workforce platform for cleaning/tea service teams. This repo contains:
- Data pipeline (CSV → Snowflake) with lightweight dbt models
- ML layer for absence prediction and complaint classification
- Streamlit dashboard MVP

## Quickstart

### 1) Setup
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Configure Snowflake
Create `.streamlit/secrets.toml` with your Snowflake credentials:
```toml
[connections.snowflake]
account = "XXXXXX"
user = "YOUR_USER"
password = "YOUR_PASSWORD"
role = "ACCOUNTADMIN"
warehouse = "COMPUTE_WH"
database = "NADHAFAH_DB"
schema = "PUBLIC"
```

### 3) Load mock data
```bash
python scripts/load_to_snowflake.py
```

### 4) dbt transforms
```bash
# from the dbt_project directory
dbt deps
dbt seed
dbt run
dbt test
```

### 5) Run dashboard
```bash
streamlit run app/streamlit_app.py
```

## Repo structure
```
nadhafah-ops/
├─ app/
│  └─ streamlit_app.py
├─ data/
│  └─ mock/ (CSV samples)
├─ dbt_project/
│  ├─ dbt_project.yml
│  └─ models/
│     ├─ staging/
│     │  ├─ stg_checkins.sql
│     │  ├─ stg_workers.sql
│     │  ├─ stg_tasks.sql
│     │  └─ stg_complaints.sql
│     └─ marts/
│        ├─ fct_worker_productivity.sql
│        └─ fct_location_hygiene.sql
├─ docs/
│  └─ architecture-diagram.md
├─ scripts/
│  └─ load_to_snowflake.py
├─ .gitignore
├─ requirements.txt
└─ LICENSE
```

---

Made with stubborn love for operational teams.
