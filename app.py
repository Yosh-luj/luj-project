import streamlit as st
import anthropic # تأكدي من تثبيت المكتبة: pip install anthropic

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="لُجّ - الرخصة المهنية", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

# --- إعداد مفتاح كلاود ---

# الاتصال بمحرك Claude بشكل آمن باستخدام مفتاحك المخزن في Secrets
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

# 2. حقن أكواد التصميم (CSS) القوة الضاربة (مع دعم اللغة العربية RTL)
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl; /* إجبار المنصة كاملة على اليمين لليسار */
    }
    
    .stApp { background-color: #F4F7FC; }

    /* --- القائمة الجانبية --- */
    [data-testid="stSidebar"] { background-color: #6A38C2 !important; }
    [data-testid="stSidebar"] * { color: white !important; }

    [data-testid="stSidebar"] .stButton > button {
        background-color: transparent !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: white !important;
        border-radius: 12px !important;
        justify-content: flex-start !important; 
        padding-right: 15px !important;
        transition: 0.3s;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: rgba(255,255,255,0.15) !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
    }

    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background-color: white !important;
        color: #6A38C2 !important;
        font-weight: 900 !important;
        border: none !important;
        justify-content: center !important; 
    }

    header { background-color: transparent !important; }
    #MainMenu, .stDeployButton { visibility: hidden; }

    /* --- البطاقات --- */
    .card-white-center {
        background: white; border-radius: 16px; padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        color: #1E293B; text-align: center; border: 1px solid #E2E8F0;
    }
    
    .card-white-right {
        background: white; border-radius: 16px; padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        text-align: right; border: 1px solid #E2E8F0;
        direction: rtl;
    }

    .card-purple { background: linear-gradient(135deg, #7C3AED, #4C1D95); border-radius: 16px; padding: 20px; color: white; box-shadow: 0 10px 15px -3px rgba(124, 58, 237, 0.3); height: 130px; text-align: right;}
    .card-orange { background: linear-gradient(135deg, #F97316, #C2410C); border-radius: 16px; padding: 20px; color: white; box-shadow: 0 10px 15px -3px rgba(249, 115, 22, 0.3); height: 130px; text-align: right;}
    .card-yellow { background: linear-gradient(135deg, #EAB308, #A16207); border-radius: 16px; padding: 20px; color: white; box-shadow: 0 10px 15px -3px rgba(234, 179, 8, 0.3); height: 130px; text-align: right;}
    
    .card-purple h3, .card-purple p, .card-orange h3, .card-orange p, .card-yellow h3, .card-yellow p { color: white !important; margin: 5px 0; }
    h1, h2, h3 { color: #1E293B !important; font-weight: 800 !important; text-align: right; }
    
    .stTextInput input { border-radius: 12px; border: 1px solid #E2E8F0; padding: 12px 20px; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.02); text-align: right; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. إدارة حالة المستخدم (الذاكرة و التوجيه)
if 'points' not in st.session_state: st.session_state.points = 2450
if 'placement_done' not in st.session_state: st.session_state.placement_done = False
if 'current_page' not in st.session_state:
    # يوجه المستخدم الجديد إجبارياً لاختبار تحديد المستوى
    st.session_state.current_page = "تحديد المستوى" if not st.session_state.placement_done else "لوحة القيادة"
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "مرحباً أ. نورة! أنا لُجّ، مساعدتك الذكية للرخصة المهنية. كيف يمكنني مساعدتك؟"}]

# 4. القائمة الجانبية
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 50px; color: white !important; margin-bottom: 20px;'>🤖 لُجّ</h1>", unsafe_allow_html=True)
    st.button("➕ بدء تدريب جديد", use_container_width=True, type="primary")
    st.write("---")
    
    # أزرار التنقل (تغير قيمة current_page)
    if st.button("🏠 لوحة القيادة", use_container_width=True): st.session_state.current_page = "لوحة القيادة"
    if st.button("🧠 مركز التحدي", use_container_width=True): st.session_state.current_page = "مركز التحدي"
    if st.button("💬 المرشد الذكي", use_container_width=True): st.session_state.current_page = "المرشد الذكي"
    if st.button("⏱️ محاكي الاختبارات", use_container_width=True): st.session_state.current_page = "محاكي الاختبارات"

# ==========================================
# 5. محرك عرض الصفحات (Routing Logic)
# ==========================================

if st.session_state.current_page == "تحديد المستوى":
    st.markdown("<h2>🎯 اختبار تحديد المستوى السريع</h2>", unsafe_allow_html=True)
    st.info("للتعرف على مستواكِ وبناء خطتكِ الدراسية، أجيبي على هذه الأسئلة التأسيسية:")

    with st.form("placement_test_form"):
        st.write("---")
        q1 = st.radio("1. عندما يربط المعلم المعلومات الجديدة بالمعلومات السابقة للمتعلم، فهو يطبق نظرية:", ["السلوكية", "البنائية", "المعرفية", "الاجتماعية"], index=None)
        q2 = st.radio("2. الكلمة التي كُتبت همزتها بشكل صحيح فيما يلي هي:", ["إستغفار", "إبتسام", "استخراج", "إنتصار"], index=None)
        
        st.write("---")
        submitted = st.form_submit_button("إرسال الإجابات وبناء خطتي 🚀", type="primary")

        if submitted:
            if q1 and q2:
                st.session_state.placement_done = True
                st.session_state.current_page = "لوحة القيادة"
                st.success("تم تحليل إجاباتك بنجاح! جاري توجيهك...")
                st.rerun()
            else:
                st.warning("الرجاء الإجابة على جميع الأسئلة قبل الإرسال.")

elif st.session_state.current_page == "لوحة القيادة":
    col_main, col_right = st.columns([3, 1.2], gap="large")

    with col_main:
        st.markdown("<h2>لوحة تحكم لُجّ الذكية</h2>", unsafe_allow_html=True)
        st.text_input("", placeholder="🔍 ابحث عن سؤال، معيار، أو ملزمة...")
        
        st.markdown("<h3 style='margin-top: 30px;'>التقدم في المعايير</h3>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("""<div class='card-purple'><h3>التربوي العام</h3><p>إنجاز 50% | 8 ملفات</p><div style='background: rgba(255,255,255,0.3); height: 6px; border-radius: 3px; margin-top: 10px;'><div style='width: 50%; background: white; height: 100%; border-radius: 3px;'></div></div></div>""", unsafe_allow_html=True)
        with c2: st.markdown("""<div class='card-orange'><h3>الكمي</h3><p>إنجاز 70% | 12 ملزمة</p><div style='background: rgba(255,255,255,0.3); height: 6px; border-radius: 3px; margin-top: 10px;'><div style='width: 70%; background: white; height: 100%; border-radius: 3px;'></div></div></div>""", unsafe_allow_html=True)
        with c3: st.markdown("""<div class='card-yellow'><h3>اللغوي</h3><p>إنجاز 60% | 5 ملفات</p><div style='background: rgba(255,255,255,0.3); height: 6px; border-radius: 3px; margin-top: 10px;'><div style='width: 60%; background: white; height: 100%; border-radius: 3px;'></div></div></div>""", unsafe_allow_html=True)

        st.markdown("<h3 style='margin-top: 30px;'>أدوات التدريب</h3>", unsafe_allow_html=True)
        t1, t2, t3, t4 = st.columns(4)
        with t1: st.markdown("<div class='card-white-center'><h2 style='margin:0; color:#F59E0B !important;'>⚡</h2><b>التحدي السريع</b><br><span style='color:gray; font-size:12px;'>376 سؤال</span></div>", unsafe_allow_html=True)
        with t2: st.markdown("<div class='card-white-center'><h2 style='margin:0; color:#6A38C2 !important;'>👨‍🏫</h2><b>المعلم الصغير</b><br><span style='color:gray; font-size:12px;'>Teach Back</span></div>", unsafe_allow_html=True)
        with t3: st.markdown("<div class='card-white-center'><h2 style='margin:0; color:#EF4444 !important;'>🔍</h2><b>تحليل الأخطاء</b><br><span style='color:gray; font-size:12px;'>55 خطأ</span></div>", unsafe_allow_html=True)
        with t4: st.markdown("<div class='card-white-center'><h2 style='margin:0; color:#10B981 !important;'>📚</h2><b>الملازم المعتمدة</b><br><span style='color:gray; font-size:12px;'>PDF File</span></div>", unsafe_allow_html=True)

    with col_right:
        st.markdown("<div class='card-white-right' style='display: flex; align-items: center; justify-content: flex-start; gap: 10px; margin-bottom: 20px;'><div style='background:#f1f5f9; padding: 10px; border-radius: 50%; font-size: 20px;'>👤</div><b>أ. نورة</b></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-white-center' style='margin-bottom: 20px;'><p style='color: gray; margin:0;'>رصيد نقاط لُجّ:</p><h2 style='color: #6A38C2 !important; font-size: 36px; margin: 5px 0;'>{st.session_state.points:,}</h2><p style='color: gray; font-size: 12px; margin:0;'>النقاط المتبقية</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='card-white-right' style='background-color: #EEF2FF; border: none; margin-bottom: 20px;'><h4 style='color: #4F46E5 !important; margin-top: 0;'>صباح الخير أ. نورة!</h4><p style='font-size: 14px; color: #334155; line-height: 1.6;'>لاحظت أمس أنكِ واجهتِ صعوبة في 'نظريات التعلم المعرفية'. هل نراجعها اليوم؟</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='card-white-right' style='background-color: #FFFbeb; border: 1px solid #FDE68A;'><b>💡 سؤال اليوم</b><p style='font-size: 12px; color: gray; margin:0;'>اربح 10 نقاط</p></div>", unsafe_allow_html=True)

elif st.session_state.current_page == "المرشد الذكي":
    st.markdown("<h2>💬 المرشد الذكي (لُجّ)</h2>", unsafe_allow_html=True)
    st.info("أنا لُجّ، مساعدتك الذكية لاجتياز الرخصة المهنية. اسأليني أو الصقي أي سؤال هنا! (التكلفة: 5 نقاط)")

    # عرض أزرار التفعيل السريعة
    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)
    if btn_col1.button("🧩 بسط لي الفكرة", use_container_width=True): st.session_state.prompt_action = "بسط لي الفكرة التالية بشكل مبسط ومناسب لمعلم:"
    if btn_col2.button("🏫 اعطني مثال تطبيقي", use_container_width=True): st.session_state.prompt_action = "أعطني مثالاً تطبيقياً من داخل الفصل الدراسي على:"
    if btn_col3.button("🔍 تفنيد المشتتات", use_container_width=True): st.session_state.prompt_action = "قم بتفنيد المشتتات وتحليل الخيارات الخاطئة للسؤال التالي:"
    if btn_col4.button("🎯 الربط بالمعيار", use_container_width=True): st.session_state.prompt_action = "ما هو المعيار المهني في اختبار الرخصة الذي يقيسه هذا السؤال:"

    st.write("---")

    # عرض المحادثة
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="🤖" if message["role"] == "assistant" else "👤"):
            st.markdown(message["content"])

    # مربع إدخال النص (الاتصال بـ Claude API)
    if prompt := st.chat_input("اكتبي سؤالك هنا..."):
        
        # إضافة إجراء الزر السريع إذا تم اختياره
        if 'prompt_action' in st.session_state:
            full_prompt = f"{st.session_state.prompt_action}\n{prompt}"
            del st.session_state.prompt_action
        else:
            full_prompt = prompt

        st.session_state.messages.append({"role": "user", "content": full_prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(full_prompt)

        # الاتصال بـ Anthropic (Claude-Haiku)
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("لُجّ تفكر..."):
                try:
                    response = client.messages.create(
                        model="claude-3-haiku-20240307",
                        max_tokens=1000,
                        system="أنتِ لُجّ، مدربة خبيرة في اختبارات الرخصة المهنية للمعلمين في السعودية. إجاباتك يجب أن تكون دقيقة، تربوية، وباللغة العربية.",
                        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                    )
                    ai_reply = response.content[0].text
                    st.markdown(ai_reply)
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                    
                    # خصم النقاط من الذاكرة
                    st.session_state.points -= 5
                    
                except Exception as e:
                    st.error(f"حدث خطأ في الاتصال: تأكدي من صحة مفتاح API. التفاصيل: {e}")

else:
    st.title(st.session_state.current_page)
    st.info("جاري بناء هذه الصفحة... (مثل مركز التحدي والتقارير)")
