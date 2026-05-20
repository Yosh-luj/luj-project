import streamlit as st

st.set_page_config(
    page_title="رخصتي المهنية", 
    page_icon="📚", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .float-btn {
        position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
        background-color: #1E3A8A; color: white; border-radius: 50px;
        text-align: center; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
        font-size: 30px; line-height: 60px; z-index: 100; cursor: pointer;
    }
    @media only screen and (max-width: 600px) {
        .float-btn { width: 50px; height: 50px; bottom: 20px; right: 20px; font-size: 20px; line-height: 50px; }
    }
    div[data-testid="metric-container"] {
        background-color: #FFFFFF; border: 1px solid #F1F5F9;
        padding: 20px; border-radius: 12px;
    }
    </style>
    <div class="float-btn" title="اسأل مرشدك الذكي!">🤖</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("رخصتي المهنية 📝")
    st.button("🏠 الرئيسية", use_container_width=True)
    st.button("🗺️ خريطتي الدراسية", use_container_width=True)

col_right, col_left = st.columns(2)
with col_right: st.markdown("👤 **أهلاً بك يا بطل**")
with col_left: st.markdown("<div style='text-align: right;'>🏆 النقاط: 1200</div>", unsafe_allow_html=True)

st.write("---")
st.header("مرحباً، أنت على بُعد 30 يوماً من اختبار الرخصة المهنية! 🚀")
st.progress(60)

st.info("### 📍 محطتك اليوم: المعيار الثالث - استراتيجيات التدريس\n🎯 الهدف: إتقان التعلم التعاوني.")
st.button("◀️ ابدأ المذاكرة الآن", type="primary", use_container_width=True)

st.subheader("📈 أداؤك السريع")
c1, c2, c3 = st.columns(3)
c1.metric("إجابات صحيحة", "85%")
c2.metric("وقت المذاكرة", "4 ساعات")
c3.metric("مفاهيم أُنجزت", "12")
