import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="لُجّ - الرخصة المهنية", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

# 2. حقن أكواد التصميم (CSS) لتحويل شكل المنصة بالكامل
custom_css = """
<style>
    /* استيراد خط عربي عصري (تجوال) */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

    /* تطبيق الخط على كامل المنصة */
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
    }

    /* تغيير لون الخلفية الرئيسي (رمادي فاتح جداً مريح للعين) */
    .stApp {
        background-color: #f4f5f9;
    }

    /* تخصيص القائمة الجانبية (بنفسجي مشرق) */
    [data-testid="stSidebar"] {
        background-color: #6A38C2 !important;
    }
    
    /* تغيير لون نصوص القائمة الجانبية إلى الأبيض */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* تخصيص شكل الأزرار (زوايا دائرية وظل خفيف) */
    div.stButton > button:first-child {
        background-color: #8B5CF6;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(139, 92, 246, 0.2);
    }
    
    div.stButton > button:first-child:hover {
        background-color: #7C3AED;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(139, 92, 246, 0.3);
        color: white;
    }

    /* تصميم البطاقات البيضاء العائمة (Cards) */
    .white-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.03);
        margin-bottom: 20px;
    }

    /* تصميم البطاقة البنفسجية البارزة */
    .purple-card {
        background: linear-gradient(135deg, #8B5CF6, #6A38C2);
        color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(106, 56, 194, 0.3);
        margin-bottom: 20px;
    }

    /* إخفاء القوائم العلوية والسفلية الخاصة بـ Streamlit لتبدو كمنصة خاصة */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. إدارة حالة المستخدم (الذاكرة)
if 'points' not in st.session_state:
    st.session_state.points = 2450
if 'current_page' not in st.session_state:
    st.session_state.current_page = "لوحة القيادة"

# 4. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 40px;'>🤖 لُجّ</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # زر مميز لإنشاء تدريب جديد
    st.button("➕ بدء تدريب جديد", use_container_width=True)
    st.write("---")
    
    st.markdown("**القائمة الرئيسية**")
    if st.button("🏠 لوحة القيادة", use_container_width=True): st.session_state.current_page = "لوحة القيادة"
    if st.button("🧠 مركز التحدي", use_container_width=True): st.session_state.current_page = "مركز التحدي"
    if st.button("💬 المرشد الذكي", use_container_width=True): st.session_state.current_page = "المرشد الذكي"
    if st.button("⏱️ محاكي الاختبارات", use_container_width=True): st.session_state.current_page = "محاكي الاختبارات"

# 5. عرض محتوى الصفحة بناءً على الاختيار
if st.session_state.current_page == "لوحة القيادة":
    
    # شريط البحث العلوي وملف المستخدم
    col_search, col_profile = st.columns([3, 1])
    with col_search:
        st.text_input("", placeholder="🔍 ابحث عن سؤال، معيار، أو ملزمة...")
    with col_profile:
        st.markdown("<div class='white-card' style='padding: 10px; text-align: center; border-radius: 12px;'>👤 <b>أ. نورة</b></div>", unsafe_allow_html=True)

    st.write("### 🚀 وصول سريع (التقدم في المعايير)")
    
    # البطاقات الملونة (نفس فكرة الصورة التي أرفقتها)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='purple-card'>
            <h3 style='color: white; margin-top: 0;'>التربوي العام</h3>
            <p style='color: #e2e8f0;'>8 ملفات | إنجاز 50%</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='white-card' style='border-left: 5px solid #F59E0B;'>
            <h3 style='margin-top: 0; color: #1e293b;'>الكمي</h3>
            <p style='color: #64748b;'>12 ملزمة | إنجاز 70%</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='white-card' style='border-left: 5px solid #10B981;'>
            <h3 style='margin-top: 0; color: #1e293b;'>اللغوي</h3>
            <p style='color: #64748b;'>5 ملفات | إنجاز 60%</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("### ⚡ أدوات التدريب")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='white-card' style='text-align: center;'>⚡<br><b>التحدي السريع</b></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='white-card' style='text-align: center;'>👨‍🏫<br><b>المعلم الصغير</b></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='white-card' style='text-align: center;'>🔍<br><b>تحليل الأخطاء</b></div>", unsafe_allow_html=True)

else:
    st.title(st.session_state.current_page)
    st.info("جاري بناء هذه الصفحة...")
