import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Đọc API Key từ file .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Kiểm tra API Key
if not GEMINI_API_KEY:
    st.error("API Key không được tìm thấy! Vui lòng kiểm tra file .env.")
    st.stop()

# Khởi tạo Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")  # Sử dụng mô hình Gemini Pro

# Header Streamlit
st.title("Viết bài từ tiêu đề với Gemini")

title = st.text_input("Nhập tiêu đề bài viết:")

if st.button("Tạo bài viết"):
    if title:
        with st.spinner("🔄 Đang tạo bài viết..."):
            prompt = f"Viết một bài viết dài khoảng 1200 từ về chủ đề: {title}"
            
            try:
                # Gọi API Gemini để tạo nội dung
                response = model.generate_content(prompt)
                article = response.text
                
                # Hiển thị bài viết
                st.subheader("Bài viết hoàn chỉnh:")
                st.write(article)
            
            except Exception as e:
                st.error(f"❌ Lỗi khi gọi Gemini API: {e}")
    else:
        st.warning("⚠️ Vui lòng nhập tiêu đề bài viết!")
