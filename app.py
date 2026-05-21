import streamlit as st
import anthropic

st.set_page_config(page_title="لُجّ", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### 🤖 لُجّ - المرشد الذكي")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسأل لُجّ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        api_key = st.secrets.get("ANTHROPIC_API_KEY", "").strip()

        if not api_key:
            st.error("خطأ: مفتاح الـ API مفقود في الإعدادات.")
        else:
            try:
                client = anthropic.Anthropic(api_key=api_key)
                response = client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=800,
                    system="أنتِ لُجّ، مرشدة تعليمية ذكية.",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                full_response = response.content[0].text
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"خطأ: {e}")
