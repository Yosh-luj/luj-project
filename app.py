import streamlit as st
import anthropic 

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="لُجّ - الرخصة المهنية", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

# الاتصال بـ Claude الآمن
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

# 2. حقن التنسيقات المتطورة (CSS) - ثيم السحابة المضيئة والنظيفة
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    
    /* إعدادات الخط والاتجاه العام */
    html, body, [class*="css"] { 
        font-family: 'Tajawal', sans-serif !important; 
        direction: rtl; 
    }
    
    /* خلفية المنصة الفاتحة والنظيفة جداً */
    .stApp { 
        background-color: #F8F9FE; 
    }
    
    /* تخصيص القائمة الجانبية بشكل عصري متناسق مع الثيم */
    [data-testid="stSidebar"] { 
        background: linear-gradient(180deg, #6A38C2, #4C1D95) !important; 
        box-shadow: 5px 0 25px rgba(106, 56, 194, 0.1);
    }
    [data-testid="stSidebar"] * { 
        color: white !important; 
    }
    
    /* تحويل أزرار القائمة الجانبية إلى كبسولات ناعمة (Pill Shapes) */
    [data-testid="stSidebar"] .stButton > button {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border-radius: 24px !important;
        padding: 10px 20px !important;
        justify-content: flex-start !important;
        transition: all 0.3s ease !important;
        font-weight: 500 !important;
        margin-bottom: 5px;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255,255,255,0.1);
    }

    /* إخفاء زوائد وعناصر Streamlit الافتراضية */
    header { background-color: transparent !important; }
    #MainMenu, .stDeployButton { visibility: hidden; }

    /* تصميم البطاقة السحابية الزجاجية الناعمة (Airy Glassmorphism) */
    .airy-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.6);
        border-radius: 24px;
        padding: 30px 25px;
        box-shadow: 0 10px 35px rgba(139, 92, 246, 0.05);
        text-align: right;
        direction: rtl;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .airy-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 45px rgba(139, 92, 246, 0.12);
    }

    /* أرقام مئوية ضخمة بتدرج لوني مضيء ومشّع */
    .gradient-number {
        font-size: 46px;
        font-weight: 900;
        background: linear-gradient(135deg, #8B5CF6, #D946EF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 10px 0;
        line-height: 1;
    }
    
    .card-title {
        color: #1E293B;
        font-size: 18px;
        font-weight: 700;
        margin: 0 0 8px 0;
    }
    .card-text {
        color: #64748B;
        font-size: 13px;
        margin: 0;
    }

    /* حل مشكلة ظهور نصوص المحادثة بلون باهت (إجبار اللون الداكن الواضح) */
    [data-testid="stChatMessage"] {
        background-color: white !important;
        border-radius: 18px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02) !important;
        margin-bottom: 12px !important;
    }
    [data-testid="stChatMessage"] * {
        color: #1E293B !important;
        font-size: 15px !important;
    }
    
    /* تنسيق صندوق المدخلات لشريط البحث والمحادثة */
    .stTextInput input, .stChatInput textarea {
        border-radius: 16px !important;
        border: 1px solid #E2E8F0 !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. إدارة حالة المستخدم (الذاكرة)
if 'current_page' not in st.session_state: st.session_state.current_page = "لوحة القيادة"
if 'messages' not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "أهلاً أ. نورة! كيف أساعدكِ اليوم في التحضير للرخصة المهنية؟"}]

# 4. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 45px; font-weight: 900; margin-bottom: 25px;'>🤖 لُجّ</h1>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 لوحة القيادة", use_container_width=True): st.session_state.current_page = "لوحة القيادة"
    if st.button("💬 المرشد الذكي", use_container_width=True): st.session_state.current_page = "المرشد الذكي"

# 5. محرك عرض الصفحات والواجهات
if st.session_state.current_page == "لوحة القيادة":
    st.markdown("<h2 style='color: #1E293B; font-weight: 800; margin-bottom: 25px;'>لوحة تحكم لُجّ الذكية</h2>", unsafe_allow_html=True)
    
    # توزيع بطاقات المعايير الثلاثة بنظام التصميم الجديد المستوحى من الصورة
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="airy-card">
            <h2 class="gradient-number">50%</h2>
            <h3 class="card-title">التربوي العام</h3>
            <p class="card-text">تم مراجعة وتغطية معايير النظريات وطرق التدريس العامة بنجاح.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="airy-card">
            <h2 class="gradient-number" style="background: linear-gradient(135deg, #3B82F6, #8B5CF6); -webkit-background-clip: text;">70%</h2>
            <h3 class="card-title">المعيار الكمي</h3>
            <p class="card-text">تقدم ممتاز في حل المسائل الحسابية الحيوية وتحليل البيانات الإحصائية المعقدة.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="airy-card">
            <h2 class="gradient-number" style="background: linear-gradient(135deg, #F97316, #EC4899); -webkit-background-clip: text;">60%</h2>
            <h3 class="card-title">المعيار اللغوي</h3>
            <p class="card-text">تغطية شاملة لقواعد الإملاء، النحو، وآليات التعبير اللغوي السليم.</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == "المرشد الذكي":
    st.markdown("<h2 style='color: #1E293B; font-weight: 800; margin-bottom: 25px;'>💬 المرشد الذكي</h2>", unsafe_allow_html=True)
    
    # عرض صندوق المحادثة
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): 
            st.markdown(m["content"])
    
    # استقبال المدخلات والربط الفعلي بمحرك السحابة
    if prompt := st.chat_input("اكتبي سؤالك التربوي هنا..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): 
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("لُجّ تصيغ الإجابة..."):
                response = client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=1000,
                    system="أنتِ لُجّ، مدربة خبيرة ومستشارة متخصصة في اختبارات الرخصة المهنية للمعلمين في المملكة العربية السعودية. إجاباتك تتميز بالعمق الأكاديمي، الصياغة الواضحة، والاعتماد الكلي على المعايير المعتمدة لسلامة المحتوى واللغة العربية الصريحة.",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                ai_reply = response.content[0].text
                st.markdown(ai_reply)
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})
