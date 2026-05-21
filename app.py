import streamlit as st
import anthropic

# 1. إعدادات الصفحة
st.set_page_config(page_title="لُجّ - المرشد الذكي", page_icon="📝", layout="wide")

# 2. تهيئة الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. عرض المحادثة
st.markdown("### 🤖 تحدث مع لُجّ (مرشدك الذكي)")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. معالجة الإدخال
if prompt := st.chat_input("اسأل لُجّ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # استخراج المفتاح
        api_key = st.secrets.get("ANTHROPIC_API_KEY")
        
        if not api_key:
            st.error("مفتاح الـ API غير موجود في الإعدادات.")
        else:
            try:
                client = anthropic.Anthropic(api_key=api_key)
                
                # استخدام نموذج claude-3-haiku-20240307 لأنه الأكثر استقراراً وتوفراً فورياً
                response = client.messages.create(
                    model="claude-3-haiku-20240307", 
                    max_tokens=500,
                    system="أنت لُجّ، مرشدة تعليمية متخصصة في الرخصة المهنية.",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                
                full_response = response.content[0].text
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {e}")
