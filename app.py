import streamlit as st

# 1. إعدادات الصفحة - القائمة مطوية تلقائياً لتناسب الجوال
st.set_page_config(
    page_title="رخصتي المهنية", 
    page_icon="📚", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. كود التصميم (CSS) - التجاوب مع الجوال
st.markdown("""
    <style>
    /* تصميم الزر العائم للروبوت */
    .float-btn {
        position: fixed;
        width: 60px;
        height: 60px;
        bottom: 40px;
        right: 40px;
        background-color: #1E3A8A;
        color: white;
        border-radius: 50px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
        font-size: 30px;
        line-height: 60px;
        z-index: 100;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .float-btn:hover { transform: scale(1.1); background-color: #2563EB; }

    /* تحسينات للجوال */
    @media only screen and (max-width: 600px) {
        .float-btn { width: 50px; height: 50px; bottom: 20px; right: 20px; font-size: 20px; line-height: 50px; }
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.2rem !important; }
    }
    
    /* تصميم الصناديق */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border: 1px solid #F1F5F9;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.02);
    }
    </style>
    <div class="float-btn" title="اسأل مرشدك الذكي!">🤖</div>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("رخصتي المهنية 📝")
    st.write("---")
    st.button("🏠 الرئيسية (لوحة التحكم)", use_container_width=True)
    st.button("🗺️ خريطتي الدراسية 🔴", use_container_width=True)
    st.button("📚 مكتبة المعايير", use_container_width=True)
    st.button("⏱️ محاكي الاختبارات", use_container_width=True)
    st.button("📊 تحليلاتي المتقدمة", use_container_width=True)

# 4. شريط التنقل العلوي
col_right, col_space, col_left = st.columns([2, 1, 2])
with col_right:
    st.markdown("👤 **أهلاً بك يا بطل** | 🔔 | ⚡ سلسلة: 5 أيام")
with col_left:
    st.markdown("<div style='text-align: left;'>🏆 النقاط: <b>1200</b> | ⚙️ | 🚪</div>", unsafe_allow_html=True)

st.write("---")

# 5. المحتوى الرئيسي
st.header("مرحباً، أنت على بُعد 30 يوماً من اختبار الرخصة المهنية! 🚀")

st.write("**إنجازك من الخطة المخصصة (60%)**")
st.progress(60)
st.write("<br>", unsafe_allow_html=True)

# 6. بطاقة المهمة
st.info("""
### 📍 محطتك اليوم: المعيار الثالث - استراتيجيات التدريس (الجزء الثاني)
⏱️ **الوقت المتوقع:** 20 دقيقة | 🎯 **الهدف:** إتقان التعلم التعاوني والنشط.
""")
st.button("◀️ ابدأ المذاكرة الآن", type="primary", use_container_width=True)

st.write("<br>", unsafe_allow_html=True)

# 7. الإحصائيات
st.subheader("📈 أداؤك السريع")
w_col1, w_col2, w_col3 = st.columns(3)
with w_col1: st.metric(label="إجابات صحيحة", value="85%")
with w_col2: st.metric(label="وقت المذاكرة", value="4 ساعات")
with w_col3: st.metric(label="مفاهيم أُنجزت", value="12")

st.write("<br>", unsafe_allow_html=True)

# 8. التحدي السريع
st.subheader("💡 سؤال اليوم السريع:")
st.write("**أي من الآتي يُعد من أدوات التقويم التكويني داخل الحصة؟**")
answer = st.radio("اختر الإجابة الصحيحة:", 
                  ("الاختبار النهائي", "الأسئلة الشفوية", "المقابلة الشخصية", "السجل القصصي"), 
                  index=None)

if answer == "الأسئلة الشفوية":
    st.success("إجابة صحيحة يا بطل! 👏")
    st.balloons()
