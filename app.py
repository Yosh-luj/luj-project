import streamlit as st
import anthropic

# ==========================================
# 1. إعدادات الصفحة الأساسية والتصميم (CSS)
# ==========================================
st.set_page_config(page_title="لُجّ - الرخصة المهنية", page_icon="🤖", layout="wide")

# تصميم CSS لضبط الاتجاه من اليمين لليسار (RTL) وتحسين شكل الأزرار
st.markdown("""
<style>
    * { direction: rtl; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
    .progress-card { background-color: #1e293b; padding: 20px; border-radius: 15px; text-align: center; color: white; border: 1px solid #334155; }
    .progress-number { font-size: 36px; font-weight: bold; color: #c084fc; }
    .lock-icon { color: #94a3b8; font-size: 24px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. تهيئة قاعدة البيانات الوهمية (Session State)
# ==========================================
if 'tier' not in st.session_state:
    st.session_state.tier = 'الاستكشاف (مجانية)'
if 'points' not in st.session_state:
    st.session_state.points = 50
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 لوحة القيادة"

def upgrade_tier(new_tier, new_points):
    st.session_state.tier = new_tier
    st.session_state.points = new_points
    st.success(f"تمت الترقية بنجاح! باقتك الآن: {new_tier}، ورصيدك: {new_points} نقطة.")

# ==========================================
# 3. القائمة الجانبية (Sidebar Navigation)
# ==========================================
with st.sidebar:
    st.title("🤖 منصة لُجّ")
    st.caption("الذكاء الاصطناعي لاجتياز الرخصة المهنية")
    st.divider()
    
    # التنقل بين الأقسام
    st.session_state.current_page = st.radio(
        "القائمة الرئيسية",
        ["🏠 لوحة القيادة", "🧠 مركز التحدي", "💬 المرشد الذكي", "📊 التقارير التحليلية"]
    )
    
    st.divider()
    
    # محفظة النقاط والباقات
    st.markdown(f"**الباقة:** {st.session_state.tier}")
    st.metric(label="النقاط الذكية المتاحة 🪙", value=st.session_state.points)
    
    # أزرار الترقية الوهمية (لتجربة فتح الأقفال)
    with st.expander("💳 إدارة الاشتراك (تجريبي)"):
        if st.button("باقة التمكين (99 ر.س)"):
            upgrade_tier('التمكين', 2000)
        if st.button("باقة الضمان VIP (399 ر.س)"):
            upgrade_tier('الضمان VIP', 6000)

# ==========================================
# 4. محتوى الأقسام بناءً على اختيار المستخدم
# ==========================================

# --- القسم الأول: لوحة القيادة ---
if st.session_state.current_page == "🏠 لوحة القيادة":
    st.header("مرحباً بكِ أ. نورة! 🌟")
    st.info("💡 **إشعار ذكي:** لاحظنا أنكِ بحاجة لمراجعة قوانين (الإحصاء التربوي) اليوم لرفع نسبة إنجازك.")
    
    # بطاقات التقدم
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="progress-card"><div class="progress-number">50%</div><div>التربوي العام</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="progress-card"><div class="progress-number" style="color:#5eead4;">70%</div><div>الكمي</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="progress-card"><div class="progress-number">60%</div><div>اللغوي</div></div>', unsafe_allow_html=True)
    
    st.write("---")
    # زر البدء السريع الموجه
    if st.button("🚀 ابدأ مذاكرة اليوم (الخطة الموجهة)", type="primary"):
        st.success("تم توجيهك لخطة اليوم: مراجعة الإحصاء التربوي + حل 10 أسئلة (هذا الزر سينقلك لاحقاً لصفحة المذاكرة).")

# --- القسم الثاني: مركز التحدي ---
elif st.session_state.current_page == "🧠 مركز التحدي":
    st.header("🧠 مركز التحدي (التدريب الحر)")
    st.write("هنا يمكنك التدريب بحرية وبدون استهلاك نقاط من محفظتك الذكية.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("📖 بنك الأسئلة الشامل (مجاني)", use_container_width=True)
        st.button("⏱️ محاكي اختبار قياس (مجاني)", use_container_width=True)
    with col2:
        # تطبيق نظام (القفل الذكي) على ميزة المعلم الصغير
        if st.session_state.tier == 'الضمان VIP':
            st.button("🎓 ميزة المعلم الصغير (مفتوحة)", type="primary", use_container_width=True)
        else:
            st.button("🔒 ميزة المعلم الصغير (تتطلب ترقية VIP)", disabled=True, use_container_width=True)
            st.caption("رقّي لباقة الضمان لتفعيل ميزة الشرح الصوتي للذكاء الاصطناعي.")

# --- القسم الثالث: المرشد الذكي (الشات بوت الفعلي) ---
elif st.session_state.current_page == "💬 المرشد الذكي":
    st.header("💬 المرشد الذكي (لُجّ)")
    st.caption("اسأل، استفسر، واطلب تفنيد المشتتات. (كل سؤال يخصم 5 نقاط)")
    
    # تهيئة عميل كلاود
    try:
        client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    except Exception as e:
        st.error("⚠️ لم يتم العثور على مفتاح Anthropic. يرجى التأكد من ملف secrets.toml")
        st.stop()

    # عرض المحادثات السابقة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # استقبال سؤال المستخدم
    if prompt := st.chat_input("اكتب سؤالك هنا (مثال: ما الفرق بين التقويم التكويني والختامي؟)"):
        
        # 1. التحقق من الرصيد
        if st.session_state.points < 5:
            st.error("🔒 لقد استنفدت نقاطك الذكية! لا يمكن إرسال السؤال.")
            st.info("يرجى شحن محفظتك أو الترقية من القائمة الجانبية للاستمرار.")
        else:
            # 2. عرض سؤال المستخدم وحفظه
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # 3. الاتصال بكلاود (مع التوجيه الصارم ليكون خبيراً بالرخصة المهنية)
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                try:
                    response = client.messages.create(
                       # استخدمي هذا السطر في دالة client.messages.create
                        model="claude-haiku-4-5-20251001",
                        max_tokens=1000,
                        system="أنت لُجّ، مساعد ذكي وخبير متخصص في معايير الرخصة المهنية للمعلمين في السعودية (هيئة تقويم التعليم والتدريب). إجاباتك دقيقة، تربوية، وتركز على تبسيط المفاهيم التربوية والكمية واللغوية بأسلوب يشبه أسئلة قياس.",
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ]
                    )
                    full_response = response.content[0].text
                    message_placeholder.markdown(full_response)
                    
                    # 4. خصم النقاط بعد نجاح الإجابة
                    st.session_state.points -= 5
                    
                    # حفظ إجابة البوت
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                    
                    # تحديث الصفحة لعرض الرصيد الجديد في القائمة الجانبية
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الاتصال بالمرشد الذكي: {e}")

# --- القسم الرابع: التقارير ---
elif st.session_state.current_page == "📊 التقارير التحليلية":
    st.header("📊 تحليلات الأداء")
    st.write("هنا سيتم عرض الرسوم البيانية لتطور أدائك الزمني في المعايير المختلفة.")
    st.info("سيتم تفعيل هذه الشاشة بعد حلك لأول محاكاة اختبار في مركز التحدي.")
