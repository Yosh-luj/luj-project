import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="لُجّ - الرخصة المهنية", page_icon="🤖", layout="wide")

# 2. إدارة حالة المستخدم (Session State)
# هذه المتغيرات تتذكر بيانات المتدرب طوال فترة استخدامه للتطبيق
if 'points' not in st.session_state:
    st.session_state.points = 1000  # رصيد البداية
if 'placement_done' not in st.session_state:
    st.session_state.placement_done = False # هل أجرى اختبار تحديد المستوى؟
if 'current_page' not in st.session_state:
    # إجباره على صفحة تحديد المستوى إذا لم يختبر
    st.session_state.current_page = "تحديد المستوى" if not st.session_state.placement_done else "لوحة القيادة"

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.header("👤 أ. سارة (نسخة تجريبية)")
    st.markdown(f"### 🪙 نقاط لُجّ: `{st.session_state.points}`")
    st.divider()
    
    st.markdown("**القائمة الرئيسية:**")
    # أزرار التنقل بين الصفحات
    if st.button("🏠 لوحة القيادة", use_container_width=True): 
        st.session_state.current_page = "لوحة القيادة"
    if st.button("🏋️ مركز التحدي", use_container_width=True): 
        st.session_state.current_page = "مركز التحدي"
    if st.button("💬 المرشد الذكي", use_container_width=True): 
        st.session_state.current_page = "المرشد الذكي"
        
    st.divider()
    if st.button("🚪 تسجيل الخروج", use_container_width=True):
        st.session_state.clear() # مسح الذاكرة لإعادة التجربة من الصفر
        st.rerun()

# 4. محرك عرض الصفحات (ماذا يظهر في الشاشة الرئيسية؟)

if st.session_state.current_page == "تحديد المستوى":
    st.title("🎯 اختبار تحديد المستوى")
    st.info("مرحباً بك في لُجّ. لننطلق معاً نحو اجتياز الرخصة المهنية. دعينا نحدد نقطة البداية.")
    
    # محاكاة زر بدء الاختبار
    if st.button("ابدأ الاختبار الآن (تجريبي)", type="primary"):
        st.session_state.placement_done = True
        st.session_state.current_page = "لوحة القيادة"
        st.rerun()

elif st.session_state.current_page == "لوحة القيادة":
    st.title("🏠 لوحة القيادة")
    st.success("☀️ صباح الخير أ. سارة! لاحظت أنكِ واجهتِ صعوبة في 'نظريات التعلم المعرفية' أمس. هل نراجعها اليوم؟")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **سؤال اليوم:**\n\nمن هو مؤسس نظرية التطور المعرفي؟\n\n[أجب لتكسب 5 نقاط]")
    with col2:
        st.warning("📈 **تقدم الخطة الدراسية:**\n\nأنتِ في الأسبوع الثاني (تم إنجاز 40%)")

elif st.session_state.current_page == "مركز التحدي":
    st.title("🏋️ مركز تحدي لُجّ")
    st.write("هنا سنقوم ببرمجة زر [توليد سؤال جديد] لاحقاً...")

elif st.session_state.current_page == "المرشد الذكي":
    st.title("💬 المرشد الذكي (لُجّ)")
    st.write("هنا سنعيد دمج كود المحادثة الخاص بـ Claude الذي نجحنا في تشغيله سابقاً...")
