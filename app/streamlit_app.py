
import os
import pandas as pd
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Nadhafah Ops", page_icon="🧹", layout="wide")

st.title("🧹 Nadhafah Ops — Operational Cleaning Dashboard (MVP)")

# Mock data load (replace with Snowflake query later)
mock_dir = os.path.join(os.path.dirname(__file__), "..", "data", "mock")
workers = pd.read_csv(os.path.join(mock_dir, "workers.csv"))
tasks = pd.read_csv(os.path.join(mock_dir, "tasks.csv"))
checkins = pd.read_csv(os.path.join(mock_dir, "checkins.csv"))
complaints = pd.read_csv(os.path.join(mock_dir, "complaints.csv"))

col1, col2, col3 = st.columns(3)
col1.metric("Workers", len(workers))
col2.metric("Locations", tasks['location'].nunique())
col3.metric("Check-ins today", (pd.to_datetime(checkins['timestamp']).dt.date == datetime.now().date()).sum())

st.subheader("Recent check-ins")
st.dataframe(checkins.sort_values("timestamp", ascending=False).head(20), use_container_width=True)

st.subheader("Complaints summary")
st.dataframe(complaints.groupby("location")["text"].count().reset_index(name="complaints"), use_container_width=True)

st.info("This is a placeholder dashboard reading CSVs. Swap with Snowflake queries when ready.")
