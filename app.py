import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="لُجّ - المرشد الذكي", page_icon="📝", layout="wide", initial_sidebar_state="expanded")

# 2. حقن CSS مخصص لمطابقة صورة التصميم (Soft UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    
    /* خلفية التطبيق العامة (رمادي مائل للأزرق الفاتح جداً) */
    .stApp {
        background-color: #F4F7FC;
        font-family: 'Tajawal', sans-serif !important;
    }

    /* تلوين القائمة الجانبية بالبنفسجي (مثل الصورة) */
    [data-testid="stSidebar"] {
        background-color: #6C5CE7 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* إخفاء الهيدر الافتراضي لـ Streamlit */
    header {visibility: hidden;}

    /* البطاقة البنفسجية المتدرجة (Overview) */
    .card-purple-gradient {
        background: linear-gradient(135deg, #6C5CE7 0%, #8E7CFF 100%);
        border-radius: 24px;
        padding: 30px;
        color: white;
        box-shadow: 0 15px 30px rgba(108, 92, 231, 0.2);
        margin-bottom: 20px;
    }

    /* البطاقة الوردية المتدرجة (My Jogging -> محاكاة) */
    .card-pink-gradient {
        background: linear-gradient(135deg, #FF6B8B 0%, #FF8E9E 100%);
        border-radius: 24px;
        padding: 25px;
        color: white;
        box-shadow: 0 15px 30px rgba(255, 107, 139, 0.2);
        margin-bottom: 20px;
    }

    /* البطاقة البنفسجية الصغيرة (Daily Jogging) */
    .card-purple-solid {
        background-color: #7A69ED;
        border-radius: 24px;
        padding: 25px;
        color: white;
        box-shadow: 0 10px 20px rgba(122, 105, 237, 0.15);
        margin-bottom: 20px;
    }

    /* البطاقات البيضاء السفلية (Stats) */
    .card-white {
        background-color: #FFFFFF;
        border-radius: 24px;
        padding: 25px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
        text-align: center;
        margin-bottom: 20px;
    }

    /* نصوص البطاقات البيضاء */
    .text-dark { color: #2D3436; font-weight: 700; font-size: 22px; margin-top: 10px;}
    .text-gray { color: #A0A5BA; font-size: 14px; font-weight: 500; }
    
    /* الأيقونات داخل البطاقات البيضاء */
    .icon-box-purple {
        background-color: #F0EDFF;
        color: #6C5CE7;
        width: 50px; height: 50px;
        border-radius: 14px;
        display: flex; justify-content: center; align-items: center;
        font-size: 24px; margin: 0 auto;
    }

    /* شريط التقدم داخل البطاقات البيضاء */
    .progress-bar-bg { background-color: #F0F0F0; border-radius: 10px; height: 6px; margin-top: 15px; overflow: hidden;}
    .progress-bar-fill-green { background-color: #00B894; height: 100%; width: 85%; }
    .progress-bar-fill-pink { background-color: #FF6B8B; height: 100%; width: 45%; }
    .progress-bar-fill-blue { background-color: #0984E3; height: 100%; width: 12%; }
    
    /* تصميم الزر العائم (🤖) */
    .float-btn {
        position: fixed; width: 60px; height: 60px; bottom: 30px; left: 30px;
        background-color: #FFFFFF; color: #6C5CE7; border-radius: 50px;
        text-align: center; font-size: 30px; line-height: 60px; z-index: 1000; cursor: pointer;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border: 2px solid #F4F7FC;
    }
    </style>
    
    <div class="float-btn" title="اسأل لُجّ!">🤖</div>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>لُجّ</h2>", unsafe_allow_html=True)
    st.markdown("🏠 الرئيسية")
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("🗺️ خريطتي الدراسية")
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("📊 تحليلاتي")
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("⚙️ الإعدادات")

# 4. الشريط العلوي (Top Header)
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <div>
            <h2 style="color: #2D3436; margin: 0; font-size: 28px;">لوحة التحكم</h2>
            <p style="color: #A0A5BA; margin: 0;">أهلاً بك يا بطل، أنت على بُعد 30 يوماً من الاختبار!</p>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <span style="background: white; padding: 10px 20px; border-radius: 20px; color: #6C5CE7; font-weight: bold; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">🏆 1200 نقطة</span>
            <img src="https://api.dicebear.com/8.x/notionists/svg?seed=احمد" style="width: 45px; height: 45px; border-radius: 50%; background: white; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. تخطيط الأعمدة (محاكاة للصورة: يسار عريض، يمين أقل عرضاً)
col_left, col_right = st.columns([2, 1])

with col_left:
    # البطاقة البنفسجية الكبيرة (محاكاة لـ Overview)
    st.markdown("""
        <div class="card-purple-gradient">
            <h4 style="margin:0; opacity: 0.9;">محطتك اليوم 📍</h4>
            <h1 style="margin: 10px 0;">المعيار الثالث - استراتيجيات التدريس</h1>
            <p style="opacity: 0.8; font-size: 16px;">الهدف: إتقان التفريق بين التعلم التعاوني والنشط.</p>
            <div style="margin-top: 30px; background: rgba(255,255,255,0.2); padding: 15px; border-radius: 15px; display: inline-block;">
                <span style="font-size: 14px;">الوقت المتوقع</span><br>
                <span style="font-size: 24px; font-weight: bold;">20 دقيقة</span>
            </div>
            <div style="margin-top: 20px;">
                <button style="background: white; color: #6C5CE7; border: none; padding: 12px 30px; border-radius: 25px; font-weight: bold; cursor: pointer; font-family: 'Tajawal', sans-serif;">▶ ابدأ المذاكرة الآن</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # البطاقة البنفسجية الصغيرة (محاكاة لـ Daily Jogging)
    st.markdown("""
        <div class="card-purple-solid">
            <h3 style="margin: 0; font-size: 18px;">💡 تحدي اليوم</h3>
            <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">أي من الآتي يُعد من أدوات التقويم التكويني؟</p>
            <div style="background: rgba(255,255,255,0.2); padding: 8px 15px; border-radius: 12px; margin-top: 10px; font-size: 14px;">الأسئلة الشفوية</div>
            <div style="background: rgba(255,255,255,0.1); padding: 8px 15px; border-radius: 12px; margin-top: 5px; font-size: 14px;">الاختبار النهائي</div>
        </div>
    """, unsafe_allow_html=True)

    # البطاقة الوردية (محاكاة لـ My Jogging)
    st.markdown("""
        <div class="card-pink-gradient">
            <h3 style="margin: 0; font-size: 18px;">🎯 إنجاز الأسبوع</h3>
            <h1 style="margin: 10px 0; font-size: 36px;">12</h1>
            <p style="margin: 0; opacity: 0.9;">مفهوم تم إتقانه</p>
        </div>
    """, unsafe_allow_html=True)

# 6. البطاقات البيضاء السفلية الثلاث (محاكاة لـ Bicycle Drill, etc.)
col_w1, col_w2, col_w3 = st.columns(3)

with col_w1:
    st.markdown("""
        <div class="card-white">
            <div class="icon-box-purple">✔️</div>
            <div class="text-dark">85%</div>
            <div class="text-gray">إجابات صحيحة</div>
            <div class="progress-bar-bg"><div class="progress-bar-fill-green"></div></div>
        </div>
    """, unsafe_allow_html=True)

with col_w2:
    st.markdown("""
        <div class="card-white">
            <div class="icon-box-purple">⏱️</div>
            <div class="text-dark">4 ساعات</div>
            <div class="text-gray">وقت المذاكرة</div>
            <div class="progress-bar-bg"><div class="progress-bar-fill-pink"></div></div>
        </div>
    """, unsafe_allow_html=True)

with col_w3:
    st.markdown("""
        <div class="card-white">
            <div class="icon-box-purple">📚</div>
            <div class="text-dark">12 معيار</div>
            <div class="text-gray">متبقي للاختبار</div>
            <div class="progress-bar-bg"><div class="progress-bar-fill-blue"></div></div>
        </div>
    """, unsafe_allow_html=True)
