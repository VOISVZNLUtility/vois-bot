import streamlit as st
import json
import os

def show_whats_new_popup():
    version_file = "version_history.json"
    seen_flag = "logs/.seen_version"

    if not os.path.exists(version_file):
        return

    with open(version_file, "r") as f:
        history = json.load(f)
    latest = history[-1]

    if os.path.exists(seen_flag):
        with open(seen_flag, "r") as f:
            seen = f.read().strip()
        if seen == latest["version"]:
            return

    with st.sidebar.expander("🆕 What's New", expanded=True):
        st.markdown(f"### {latest['version']} – {latest['date']}")
        for item in latest["highlights"]:
            st.markdown(f"- {item}")

    with open(seen_flag, "w") as f:
        f.write(latest["version"])