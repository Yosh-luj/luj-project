import streamlit as st
import anthropic

st.set_page_config(page_title="لُجّ - المرشد الذكي", layout="wide")

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

        try:
            client = anthropic.Anthropic(api_key=api_key)
            
            # نستخدم النموذج الذي يعمل فقط وهو Opus
            response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=800,
                system="أنتِ لُجّ، مرشدة تعليمية ذكية.",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            
            full_response = response.content[0].text
            usage = response.usage # استخراج كمية التوكنز المستهلكة
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            # عرض التكلفة بشفافية
            st.caption(f"استهلاك التوكنز لهذه الرسالة: {usage.input_tokens} (مدخل) + {usage.output_tokens} (مخرج)")
            
        except Exception as e:
            st.error(f"خطأ: {e}")
