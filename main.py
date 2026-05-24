import streamlit as st
import random

# إعدادات الصفحة (تظهر في تبويب المتصفح)
st.set_page_config(page_title="لعبة صيد الأرقام", page_icon="🎮")

st.title("🎯 لعبة صيد الرقم السري")
st.write("مرحباً بكِ! هل يمكنكِ تخمين الرقم الذي يفكر فيه الكمبيوتر؟")

# استخدام "Session State" لحفظ الرقم حتى لو أعيد تحميل الصفحة
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

# مكان إدخال الرقم
guess = st.number_input("أدخلي تخمينك (من 1 إلى 100):", min_value=1, max_value=100, step=1)

if st.button("تحقق من الإجابة"):
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.warning("⬆️ أكبر قليلاً!")
    elif guess > st.session_state.secret_number:
        st.warning("⬇️ أصغر قليلاً!")
    else:
        st.success(f"🎊 تهانينا! الرقم هو {st.session_state.secret_number}")
        st.balloons() # تأثير بالونات رائع للفوز
        if st.button("لعب مرة أخرى"):
            del st.session_state.secret_number
            st.rerun()

st.info(f"عدد المحاولات الحالية: {st.session_state.attempts}")