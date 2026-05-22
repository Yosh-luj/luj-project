import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="لُجّ - الرخصة المهنية", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

# 2. حقن أكواد التصميم (CSS) للوصول لأقرب شكل للصورة
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');


/* إصلاح أزرار القائمة الجانبية لتندمج مع البنفسجي */
    [data-testid="stSidebar"] div.stButton > button {
        background-color: transparent !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        color: white !important;
        border-radius: 8px;
        text-align: right !important;
        justify-content: flex-start !important; /* محاذاة لليمين */
    }
    [data-testid="stSidebar"] div.stButton > button:hover {
        background-color: rgba(255,255,255,0.1) !important;
    }
    /* تمييز زر بدء التدريب الرئيسي ليصبح أبيض */
    [data-testid="stSidebar"] div.stButton > button[kind="primary"] {
        background-color: white !important;
        color: #6A38C2 !important;
        border: none !important;
        font-weight: bold !important;
        justify-content: center !important; /* هذا الزر يبقى بالمنتصف */
    }
    /* توحيد الخط والخلفية */
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    .stApp {
        background-color: #F8F9FE; /* لون رمادي مزرق فاتح جداً مريح للعين */
    }

    /* إصلاح القائمة الجانبية: لون بنفسجي + نصوص بيضاء */
    [data-testid="stSidebar"] {
        background-color: #6A38C2 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* إصلاح مشكلة اختفاء زر القائمة الجانبية (لا نخفي الهيدر بالكامل) */
    header { background-color: transparent !important; }
    #MainMenu, .stDeployButton { visibility: hidden; } /* نخفي الإضافات غير الضرورية فقط */

    /* تصميم العناوين في الصفحة الرئيسية لضمان عدم اختفائها (لون داكن) */
    h1, h2, h3 { color: #1E293B !important; font-weight: 800 !important; }

    /* تصميم البطاقات الملونة (نفس ألوان الصورة) */
    .card-purple {
        background: linear-gradient(135deg, #7C3AED, #4C1D95);
        border-radius: 16px; padding: 25px; color: white;
        box-shadow: 0 10px 15px -3px rgba(124, 58, 237, 0.3);
        height: 140px; display: flex; flex-direction: column; justify-content: center;
    }
    .card-orange {
        background: linear-gradient(135deg, #F97316, #C2410C);
        border-radius: 16px; padding: 25px; color: white;
        box-shadow: 0 10px 15px -3px rgba(249, 115, 22, 0.3);
        height: 140px; display: flex; flex-direction: column; justify-content: center;
    }
    .card-yellow {
        background: linear-gradient(135deg, #EAB308, #A16207);
        border-radius: 16px; padding: 25px; color: white;
        box-shadow: 0 10px 15px -3px rgba(234, 179, 8, 0.3);
        height: 140px; display: flex; flex-direction: column; justify-content: center;
    }
    
    /* نصوص البطاقات الملونة يجب أن تكون بيضاء دائماً */
    .card-purple h3, .card-purple p, .card-orange h3, .card-orange p, .card-yellow h3, .card-yellow p {
        color: white !important; margin: 5px 0;
    }

    /* تصميم البطاقات البيضاء (لأدوات التدريب والقائمة الجانبية اليمنى) */
    .card-white {
        background: white; border-radius: 16px; padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        color: #1E293B; text-align: center; border: 1px solid #E2E8F0;
    }
    
    /* حقل البحث */
    .stTextInput input {
        border-radius: 12px; border: 1px solid #E2E8F0; padding: 12px 20px;
        background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 50px; color: white !important;'>🤖 لُجّ</h1>", unsafe_allow_html=True)
    st.write("---")
    st.button("➕ بدء تدريب جديد", use_container_width=True, type="primary")
    st.write("---")
    
    st.button("🏠 لوحة القيادة", use_container_width=True)
    st.button("🧠 مركز التحدي", use_container_width=True)
    st.button("💬 المرشد الذكي", use_container_width=True)
    st.button("⏱️ محاكي الاختبارات", use_container_width=True)
    st.button("📊 التقارير", use_container_width=True)
    st.button("💳 الباقات", use_container_width=True)

# 4. تقسيم الشاشة الرئيسية إلى عمودين (لجعلها تشبه الصورة: قسم رئيسي أوسط، وقسم أيسر للملف الشخصي)
# 3 أجزاء للقسم الرئيسي الأوسط، وجزء 1 للقسم الأيسر
col_main, col_right = st.columns([3, 1], gap="large")

with col_main:
    st.markdown("<h2>لوحة تحكم لُجّ الذكية</h2>", unsafe_allow_html=True)
    st.text_input("", placeholder="🔍 ابحث عن سؤال، معيار، أو ملزمة...")
    
    st.markdown("<h3 style='margin-top: 30px;'>التقدم في المعايير</h3>", unsafe_allow_html=True)
    
    # البطاقات الملونة الثلاثة
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class='card-purple'>
            <h3 style='font-size: 20px;'>التربوي العام</h3>
            <p>إنجاز 50% | 8 ملفات</p>
            <div style='background: rgba(255,255,255,0.3); height: 6px; border-radius: 3px; margin-top: 10px;'><div style='width: 50%; background: white; height: 100%; border-radius: 3px;'></div></div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='card-orange'>
            <h3 style='font-size: 20px;'>الكمي</h3>
            <p>إنجاز 70% | 12 ملزمة</p>
            <div style='background: rgba(255,255,255,0.3); height: 6px; border-radius: 3px; margin-top: 10px;'><div style='width: 70%; background: white; height: 100%; border-radius: 3px;'></div></div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class='card-yellow'>
            <h3 style='font-size: 20px;'>اللغوي</h3>
            <p>إنجاز 60% | 5 ملفات</p>
            <div style='background: rgba(255,255,255,0.3); height: 6px; border-radius: 3px; margin-top: 10px;'><div style='width: 60%; background: white; height: 100%; border-radius: 3px;'></div></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='margin-top: 30px;'>أدوات التدريب</h3>", unsafe_allow_html=True)
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.markdown("<div class='card-white'><h2 style='margin:0; color:#F59E0B !important;'>⚡</h2><b>التحدي السريع</b><br><span style='color:gray; font-size:12px;'>376 سؤال</span></div>", unsafe_allow_html=True)
    with t2:
        st.markdown("<div class='card-white'><h2 style='margin:0; color:#6A38C2 !important;'>👨‍🏫</h2><b>المعلم الصغير</b><br><span style='color:gray; font-size:12px;'>Teach Back</span></div>", unsafe_allow_html=True)
    with t3:
        st.markdown("<div class='card-white'><h2 style='margin:0; color:#EF4444 !important;'>🔍</h2><b>تحليل الأخطاء</b><br><span style='color:gray; font-size:12px;'>55 خطأ</span></div>", unsafe_allow_html=True)
    with t4:
        st.markdown("<div class='card-white'><h2 style='margin:0; color:#10B981 !important;'>📚</h2><b>الملازم المعتمدة</b><br><span style='color:gray; font-size:12px;'>PDF File</span></div>", unsafe_allow_html=True)

with col_right:
    # بطاقة الملف الشخصي
    st.markdown("""
    <div class='card-white' style='display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 20px;'>
        <div style='background:#f1f5f9; padding: 10px; border-radius: 50%; font-size: 20px;'>👤</div>
        <b>أ. نورة</b>
    </div>
    """, unsafe_allow_html=True)
    
    # بطاقة النقاط
    st.markdown("""
    <div class='card-white' style='margin-bottom: 20px; text-align: center;'>
        <p style='color: gray; margin:0;'>رصيد نقاط لُجّ:</p>
        <h2 style='color: #6A38C2 !important; font-size: 36px; margin: 5px 0;'>2,450</h2>
        <p style='color: gray; font-size: 12px; margin:0;'>النقاط المتبقية لهذا الشهر</p>
    </div>
    """, unsafe_allow_html=True)
    
    # بطاقة التقرير الصباحي
    st.markdown("""
    <div class='card-white' style='background-color: #EEF2FF; border: none; text-align: right; margin-bottom: 20px;'>
        <h4 style='color: #4F46E5 !important; margin-top: 0;'>صباح الخير أ. نورة!</h4>
        <p style='font-size: 14px; color: #334155; line-height: 1.5;'>لاحظت أمس أنكِ واجهتِ صعوبة في 'نظريات التعلم المعرفية'. هل نراجعها اليوم؟</p>
    </div>
    """, unsafe_allow_html=True)
    
    # بطاقة سؤال اليوم
    st.markdown("""
    <div class='card-white' style='background-color: #FFFbeb; border: 1px solid #FDE68A;'>
        <b>💡 سؤال اليوم</b>
        <p style='font-size: 12px; color: gray;'>اربح 10 نقاط</p>
    </div>
    """, unsafe_allow_html=True)
