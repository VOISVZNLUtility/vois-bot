import streamlit as st
import yaml
from components.chat_ui import render_chat_ui
from components.admin_panel import render_admin_panel
from components.whats_new_popup import show_whats_new_popup
from utils.version_utils import get_current_version
from utils.session_tracker import track_session

# App layout
st.set_page_config(page_title="VOIS Bot", layout="wide")

# Track session
track_session()

# Show What's New
show_whats_new_popup()

# Load user roles from config
with open("users.yaml") as f:
    user_config = yaml.safe_load(f)

# Sidebar – Logo and version
with st.sidebar:
    st.image("docs/assets/logo.png", use_container_width=True)
    st.markdown(f"**Version:** {get_current_version()}")
    username = st.text_input("🔐 Enter Username")
    role = None
    if username in user_config.get("users", {}).get("admin_roles", []):
        role = "admin"
    elif username in user_config.get("users", {}).get("end_users", []):
        role = "end_user"
    else:
        st.warning("Enter a valid username to proceed.")

# Main UI logic
if role:
    st.title("🤖 VOIS Bot – QA Command Center")
    if role == "admin":
        tab = st.sidebar.radio("Navigation", ["Chat", "Admin Panel"])
    else:
        tab = "Chat"

    if tab == "Chat":
        render_chat_ui()
    elif tab == "Admin Panel":
        render_admin_panel()
else:
    st.stop()