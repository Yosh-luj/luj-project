import streamlit as st

st.set_page_config(page_title="رخصتي المهنية", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .float-btn { position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px; background-color: #1E3A8A; color: white; border-radius: 50px; text-align: center; font-size: 30px; line-height: 60px; z-index: 100; cursor: pointer; }
    </style>
    <div class="float-btn">🤖</div>
""", unsafe_allow_html=True)

st.title("رخصتي المهنية 📝")
st.write("مرحباً بك في منصتك التعليمية.")
st.progress(60)

st.info("📍 محطتك اليوم: المعيار الثالث - استراتيجيات التدريس")
if st.button("◀️ ابدأ المذاكرة الآن"):
    st.write("جاري التحميل...")
