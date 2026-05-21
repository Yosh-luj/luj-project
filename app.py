import streamlit as st
import anthropic

# 1. إعدادات الصفحة
st.set_page_config(page_title="لُجّ - المرشد الذكي", layout="wide")

# 2. تهيئة الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### 🤖 تحدث مع لُجّ (مرشدك الذكي)")

# 3. عرض رسائل المحادثة السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. منطقة إدخال الأسئلة
if prompt := st.chat_input("اسأل لُجّ..."):
    # عرض سؤال المستخدم فوراً
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # الرد من المساعد
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # التأكد من المفتاح
        raw_key = st.secrets.get("ANTHROPIC_API_KEY", "")
        api_key = raw_key.strip()
        
        if not api_key:
            st.error("خطأ: مفتاح الـ API غير موجود في إعدادات Secrets.")
        else:
            try:
                client = anthropic.Anthropic(api_key=api_key)
                
                # استدعاء النموذج
                response = client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=500,
                    system="أنتِ لُجّ، مرشدة تعليمية ذكية. إجاباتك دقيقة وداعمة.",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                
                full_response = response.content[0].text
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"حدث خطأ: {str(e)}")
