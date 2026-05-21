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
        # التأكد من المفتاح
        api_key = st.secrets.get("ANTHROPIC_API_KEY", "").strip()

        if not api_key:
            st.error("خطأ: مفتاح الـ API مفقود في إعدادات Secrets.")
        else:
            try:
                client = anthropic.Anthropic(api_key=api_key)
                
                # استكشاف النماذج المتاحة تلقائياً في حسابك
                models = client.models.list()
                # اختيار أول نموذج متاح في حسابك لتجنب خطأ 404
                my_model = models.data[0].id
                
                # إرسال الطلب
                response = client.messages.create(
                    model=my_model,
                    max_tokens=800,
                    system="أنتِ لُجّ، مرشدة تعليمية ذكية.",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                
                full_response = response.content[0].text
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"حدث خطأ: {str(e)}")
                st.write("نصيحة: تأكدي أن مفتاح الـ API مأخوذ من مساحة العمل 'Default' وأن البطاقة الائتمانية مفعلة في قسم Billing.")
