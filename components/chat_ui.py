import streamlit as st
from utils.xlsx_rag import build_rag_chain

@st.cache_resource
def get_chat_chain():
    return build_rag_chain("data/test_assets.xlsx")

def render_chat_ui():
    st.subheader("💬 Chat with Test Data")
    query = st.text_input("Ask something about the test data:")
    if query:
        chain = get_chat_chain()
        result = chain({"query": query})
        st.markdown(f"**VOIS Bot:** {result['result']}")