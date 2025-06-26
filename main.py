import streamlit as st
from components.chat_ui import render_chat_ui
from components.admin_panel import render_admin_panel
from components.whats_new_popup import show_whats_new_popup
from utils.version_utils import get_current_version
from utils.session_tracker import track_session

st.set_page_config(page_title="VOIS Bot", layout="wide")

# Track session
track_session()

# Show "What's New" popup if version updated
show_whats_new_popup()

# Sidebar logo
with st.sidebar:
    st.image("docs/assets/logo.png", use_container_width=True)
    st.markdown(f"**Version:** {get_current_version()}")

# Main UI
st.title("🤖 VOIS Bot – QA Command Center")
tab = st.sidebar.radio("Navigation", ["Chat", "Admin Panel"])

if tab == "Chat":
    render_chat_ui()
elif tab == "Admin Panel":
    render_admin_panel()