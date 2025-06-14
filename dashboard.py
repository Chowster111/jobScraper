import streamlit as st
import json
import os
from datetime import datetime

def load_jobs(filepath):
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r") as f:
        data = json.load(f)

    jobs = list(data.values())
    return sorted(jobs, key=lambda j: j.get("detected_at", ""), reverse=True)

st.set_page_config(page_title="Job Alerts", layout="wide")

st.title("📬 Your Job Alerts Dashboard")

job_file = "./jobsFound/stripe_jobs.json"
jobs = load_jobs(job_file)

if not jobs:
    st.info("No jobs found yet. Run the scraper.")
else:
    for job in jobs:
        st.markdown(f"### [{job['title']}]({job['url']})")
        st.write(f"**Location:** {job['location']} | **Team:** {job['team']}")
        st.write(f"**Detected At:** {job.get('detected_at', 'Unknown')}")
        st.markdown("---")
