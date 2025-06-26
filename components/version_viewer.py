import streamlit as st
import json

def render_version_history():
    st.subheader("📜 Version History")
    try:
        with open("version_history.json", "r") as f:
            history = json.load(f)
        for entry in reversed(history):
            st.markdown(f"### {entry['version']} – {entry['date']}")
            for item in entry["highlights"]:
                st.markdown(f"- {item}")
    except Exception as e:
        st.error(f"Failed to load version history: {e}")