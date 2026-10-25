import streamlit as st
import random

# Cài đặt tiêu đề trang web theo ý bạn
st.set_page_config(page_title="ctuong222222 - Game Center", page_icon="🎮")

st.title("🎮 Chào mừng đến với Game của ctuong222222!")
st.write("Trò chơi Đoán Số May Mắn trực tuyến trên Streamlit.")

# Khởi tạo trạng thái trò chơi
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0

st.info("💡 Tôi đã chọn một số ngẫu nhiên từ 1 đến 100. Bạn hãy thử đoán xem đó là số mấy nhé!")

# Ô nhập số của người chơi
guess = st.number_input("Nhập số dự đoán của bạn:", min_value=1, max_value=100, step=1)

if st.button("Đoán ngay!"):
    st.session_state.attempts += 1
    
    if guess < st.session_state.target_number:
        st.warning(f"📉 Số {guess} quá NHỎ! Hãy thử số lớn hơn.")
    elif guess > st.session_state.target_number:
        st.warning(f"📈 Số {guess} quá LỚN! Hãy thử số nhỏ hơn.")
    else:
        st.success(f"🎉 Chúc mừng ctuong222222! Bạn đã đoán đúng số {st.session_state.target_number} sau {st.session_state.attempts} lần thử!")
        if st.button("Chơi ván mới"):
            st.session_state.target_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.rerun()

# Nút đặt lại trò chơi bất cứ lúc nào
if st.button("Làm mới trò chơi"):
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.rerun()
