import streamlit as st
import pandas as pd
import os

def render_analytics():
    st.subheader("📈 Session Analytics")
    log_file = "logs/session_log.csv"
    if os.path.exists(log_file):
        df = pd.read_csv(log_file)
        st.dataframe(df.tail(100), use_container_width=True)
        st.metric("Total Sessions", len(df))
    else:
        st.warning("No session logs found.")