import streamlit as st
import anthropic

# 1. إعدادات الصفحة
st.set_page_config(page_title="لُجّ - المرشد الذكي", page_icon="📝", layout="wide", initial_sidebar_state="expanded")

# 2. تهيئة الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. التصميم الاحترافي (Soft UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    .stApp { background-color: #F4F7FC; font-family: 'Tajawal', sans-serif !important; }
    [data-testid="stSidebar"] { background-color: #6C5CE7 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    header {visibility: hidden;}
    .card-purple-gradient { background: linear-gradient(135deg, #6C5CE7 0%, #8E7CFF 100%); border-radius: 24px; padding: 30px; color: white; box-shadow: 0 15px 30px rgba(108, 92, 231, 0.2); margin-bottom: 20px; }
    .card-purple-solid { background-color: #7A69ED; border-radius: 24px; padding: 25px; color: white; box-shadow: 0 10px 20px rgba(122, 105, 237, 0.15); margin-bottom: 20px; }
    .card-white { background-color: #FFFFFF; border-radius: 24px; padding: 25px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04); text-align: center; margin-bottom: 20px; }
    .text-dark { color: #2D3436; font-weight: 700; font-size: 22px; margin-top: 10px;}
    .text-gray { color: #A0A5BA; font-size: 14px; font-weight: 500; }
    .icon-box-purple { background-color: #F0EDFF; color: #6C5CE7; width: 50px; height: 50px; border-radius: 14px; display: flex; justify-content: center; align-items: center; font-size: 24px; margin: 0 auto; }
    .progress-bar-bg { background-color: #F0F0F0; border-radius: 10px; height: 6px; margin-top: 15px; overflow: hidden;}
    .progress-bar-fill-green { background-color: #00B894; height: 100%; width: 85%; }
    .progress-bar-fill-pink { background-color: #FF6B8B; height: 100%; width: 45%; }
    .progress-bar-fill-blue { background-color: #0984E3; height: 100%; width: 12%; }
    </style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>لُجّ</h2>", unsafe_allow_html=True)
    st.markdown("🏠 الرئيسية")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("🗺️ خريطتي الدراسية")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("📊 تحليلاتي")

# 5. الشريط العلوي
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <div>
            <h2 style="color: #2D3436; margin: 0; font-size: 28px;">لوحة التحكم</h2>
            <p style="color: #A0A5BA; margin: 0;">أهلاً بك يا بطل، أنت على بُعد 30 يوماً من الاختبار!</p>
        </div>
        <span style="background: white; padding: 10px 20px; border-radius: 20px; color: #6C5CE7; font-weight: bold; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">🏆 1200 نقطة</span>
    </div>
""", unsafe_allow_html=True)

# 6. المحتوى
col_left, col_right = st.columns([2, 1])
with col_left:
    st.markdown("""<div class="card-purple-gradient"><h4>محطتك اليوم 📍</h4><h1>المعيار الثالث - استراتيجيات التدريس</h1></div>""", unsafe_allow_html=True)
with col_right:
    st.markdown("""<div class="card-purple-solid"><h3>💡 تحدي اليوم</h3><p>أي من الآتي يُعد من أدوات التقويم التكويني؟</p></div>""", unsafe_allow_html=True)

# 7. منطقة المحادثة
st.markdown("<h3 style='color: #2D3436; margin-top: 30px;'>🤖 تحدث مع لُجّ (مرشدك الذكي)</h3>", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسأل لُجّ أي سؤال..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        # تنظيف المفتاح من أي فراغات
        api_key = st.secrets.get("ANTHROPIC_API_KEY", "").strip()
        
        if not api_key:
            st.error("خطأ: مفتاح الـ API غير موجود في الإعدادات.")
        else:
            try:
                client = anthropic.Anthropic(api_key=api_key)
                response = client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=800,
                    system="أنتِ لُجّ، مرشدة تعليمية ذكية. إجاباتك دقيقة ومختصرة.",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                full_response = response.content[0].text
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"خطأ في الاتصال: {e}")
