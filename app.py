import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="رخصتي المهنية", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")

# 2. تهيئة ذاكرة "حالة الوضع" (Session State)
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# دالة لتبديل الوضع عند الضغط على الزر
def toggle_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# 3. أكواد التصميم (CSS) - تتغير برمجياً حسب الوضع
dark_theme_css = """
    <style>
        .stApp { background-color: #121212 !important; color: #FFFFFF !important; }
        .stMarkdown, h1, h2, h3, p, label { color: #FFFFFF !important; }
        div[data-testid="metric-container"] { background-color: #1E1E1E !important; border: 1px solid #333 !important; }
        div[data-testid="stInfo"] { background-color: #1A2A42 !important; color: white !important; }
    </style>
""" if st.session_state.dark_mode else ""

st.markdown(f"""
    {dark_theme_css}
    <style>
    .float-btn {{ position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px; background-color: #1E3A8A; color: white; border-radius: 50px; text-align: center; font-size: 30px; line-height: 60px; z-index: 100; cursor: pointer; transition: 0.3s; }}
    .float-btn:hover {{ transform: scale(1.1); background-color: #2563EB; }}
    @media only screen and (max-width: 600px) {{
        .float-btn {{ width: 50px; height: 50px; bottom: 20px; right: 20px; font-size: 20px; line-height: 50px; }}
    }}
    div[data-testid="metric-container"] {{ background-color: #FFFFFF; border: 1px solid #F1F5F9; padding: 20px; border-radius: 12px; }}
    </style>
    <div class="float-btn" title="اسأل مرشدك الذكي!">🤖</div>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية
with st.sidebar:
    st.title("لُجّ - رخصتي المهنية 📝")
    st.button("🏠 الرئيسية", use_container_width=True)
    st.button("🗺️ خريطتي الدراسية", use_container_width=True)
    st.button("📊 تحليلاتي", use_container_width=True)

# 5. شريط التنقل العلوي (مع زر الوضع الليلي)
col_right, col_mid, col_left = st.columns([3, 1, 2])
with col_right: 
    st.markdown("👤 **أهلاً بك يا بطل** | 🔔 إشعارات")
with col_mid:
    # زر تبديل الوضع يتغير شكله النصي حسب الحالة
    btn_icon = "☀️ نهاري" if st.session_state.dark_mode else "🌙 ليلي"
    st.button(btn_icon, on_click=toggle_mode, use_container_width=True)
with col_left: 
    st.markdown("<div style='text-align: left;'>🏆 النقاط: 1200</div>", unsafe_allow_html=True)

st.write("---")

# 6. المحتوى الرئيسي وشريط التقدم
st.header("مرحباً، أنت على بُعد 30 يوماً من اختبار الرخصة المهنية! 🚀")
st.progress(60)
st.write("<br>", unsafe_allow_html=True)

# 7. بطاقة المهمة
st.info("### 📍 محطتك اليوم: المعيار الثالث - استراتيجيات التدريس\n🎯 الهدف: إتقان التعلم التعاوني والنشط.")
st.button("◀️ ابدأ المذاكرة الآن", type="primary", use_container_width=True)

st.write("<br>", unsafe_allow_html=True)

# 8. الإحصائيات
st.subheader("📈 أداؤك السريع")
c1, c2, c3 = st.columns(3)
c1.metric("إجابات صحيحة", "85%")
c2.metric("وقت المذاكرة", "4 ساعات")
c3.metric("مفاهيم أُنجزت", "12")

st.write("<br>", unsafe_allow_html=True)

# 9. التحدي السريع
st.subheader("💡 سؤال اليوم السريع:")
st.write("**أي من الآتي يُعد من أدوات التقويم التكويني داخل الحصة؟**")
answer = st.radio("اختر الإجابة الصحيحة:", ("الاختبار النهائي", "الأسئلة الشفوية", "المقابلة الشخصية"), index=None)

if answer == "الأسئلة الشفوية":
    st.success("إجابة صحيحة يا بطل! 👏")
    st.balloons()
