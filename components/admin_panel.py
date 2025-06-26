import streamlit as st
from components.analytics import render_analytics
from components.version_viewer import render_version_history

def render_admin_panel():
    st.header("🛠️ Admin Panel")
    tabs = st.tabs(["Reservation Manager", "Analytics", "Version History"])

    with tabs[0]:
        st.info("Reservation Manager coming soon...")  # Placeholder for now

    with tabs[1]:
        render_analytics()

    with tabs[2]:
        render_version_history()