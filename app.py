import streamlit as st
import anthropic 

# 1. إعدادات الصفحة
st.set_page_config(page_title="لُجّ - الرخصة المهنية", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

# الاتصال بـ Claude
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

# 2. حقن CSS (نفس التصميم السابق)
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif !important; direction: rtl; }
    .stApp { background-color: #F4F7FC; }
    [data-testid="stSidebar"] { background-color: #6A38C2 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .card-purple { background: linear-gradient(135deg, #7C3AED, #4C1D95); border-radius: 16px; padding: 20px; color: white; height: 130px; }
    .card-orange { background: linear-gradient(135deg, #F97316, #C2410C); border-radius: 16px; padding: 20px; color: white; height: 130px; }
    .card-yellow { background: linear-gradient(135deg, #EAB308, #A16207); border-radius: 16px; padding: 20px; color: white; height: 130px; }
    .card-white-center { background: white; border-radius: 16px; padding: 20px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03); text-align: center; border: 1px solid #E2E8F0; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. الحالة
if 'current_page' not in st.session_state: st.session_state.current_page = "لوحة القيادة"
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "أهلاً أ. نورة! كيف أساعدك اليوم؟"}]

# 4. القائمة الجانبية
with st.sidebar:
    st.markdown("<h1>🤖 لُجّ</h1>", unsafe_allow_html=True)
    if st.button("🏠 لوحة القيادة"): st.session_state.current_page = "لوحة القيادة"
    if st.button("💬 المرشد الذكي"): st.session_state.current_page = "المرشد الذكي"

# 5. الصفحات
if st.session_state.current_page == "لوحة القيادة":
    st.markdown("<h2>لوحة تحكم لُجّ</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='card-purple'><h3>التربوي العام</h3><p>إنجاز 50%</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='card-orange'><h3>الكمي</h3><p>إنجاز 70%</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='card-yellow'><h3>اللغوي</h3><p>إنجاز 60%</p></div>", unsafe_allow_html=True)

elif st.session_state.current_page == "المرشد الذكي":
    st.markdown("<h2>💬 المرشد الذكي</h2>", unsafe_allow_html=True)
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    
    if prompt := st.chat_input("اكتبي سؤالك..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1000,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            ai_reply = response.content[0].text
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
