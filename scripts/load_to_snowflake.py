
import os
import pandas as pd
import sqlalchemy as sa
from sqlalchemy.engine import URL

# Reads .streamlit/secrets.toml if desired, but keep minimal example here:
ACCOUNT   = os.getenv("SNOWFLAKE_ACCOUNT", "XXXXXX")
USER      = os.getenv("SNOWFLAKE_USER", "USER")
PASSWORD  = os.getenv("SNOWFLAKE_PASSWORD", "PASS")
ROLE      = os.getenv("SNOWFLAKE_ROLE", "ACCOUNTADMIN")
WAREHOUSE = os.getenv("SNOWFLAKE_WH", "COMPUTE_WH")
DATABASE  = os.getenv("SNOWFLAKE_DB", "NADHAFAH_DB")
SCHEMA    = os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC")

# Build connection using snowflake-sqlalchemy
from snowflake.sqlalchemy import URL as SFURL
engine = sa.create_engine(SFURL(
    account=ACCOUNT,
    user=USER,
    password=PASSWORD,
    role=ROLE,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
))

def load_csv(table_name, csv_path):
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Loaded {csv_path} into {table_name}")

if __name__ == "__main__":
    base = os.path.join(os.path.dirname(__file__), "..", "data", "mock")
    os.makedirs(base, exist_ok=True)
    files = {
        "workers": os.path.join(base, "workers.csv"),
        "tasks": os.path.join(base, "tasks.csv"),
        "checkins": os.path.join(base, "checkins.csv"),
        "complaints": os.path.join(base, "complaints.csv"),
    }
    for tbl, path in files.items():
        load_csv(tbl, path)
    print("Done.")
