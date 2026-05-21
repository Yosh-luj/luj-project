import streamlit as st
import anthropic

st.set_page_config(page_title="لُجّ - المرشد الذكي", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### 🤖 لُجّ - المرشد الذكي")

if prompt := st.chat_input("اسأل لُجّ..."):
    with st.chat_message("assistant"):
        api_key = st.secrets.get("ANTHROPIC_API_KEY", "").strip()
        try:
            client = anthropic.Anthropic(api_key=api_key)
            # عرض الموديلات المتاحة فعلياً
            models = client.models.list()
            model_names = [m.id for m in models.data]
            st.error(f"الموديلات المتاحة في حسابك هي: {model_names}")
        except Exception as e:
            st.error(f"خطأ: {e}")
