import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Công cụ tính tiền gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề ứng dụng
st.title("💰 Công Cụ Tính Tiền Gửi Tiết Kiệm")
st.write("Nhập thông tin tiền gửi của bạn để so sánh kết quả giữa **Lãi đơn** và **Lãi kép**.")

st.divider()

# Nhập dữ liệu từ người dùng
col1, col2 = st.columns(2)

with col1:
    so_tien_gui = st.number_input(
        "Số tiền gửi ban đầu (VNĐ):", 
        min_value=0.0, 
        value=100000000.0, 
        step=1000000.0,
        format="%.0f"
    )
    
    so_thang = st.number_input(
        "Số tháng gửi (tháng):", 
        min_value=1, 
        value=12, 
        step=1
    )

with col2:
    lai_suat_nam = st.number_input(
        "Lãi suất (%/năm):", 
        min_value=0.0, 
        max_value=100.0, 
        value=6.0, 
        step=0.1,
        format="%.2f"
    )

# Nút tính toán
if st.button("Tính toán", type="primary", use_container_width=True):
    # Chuyển đổi lãi suất tháng từ lãi suất năm
    r_thang = (lai_suat_nam / 100) / 12

    # 1. Tính Lãi Đơn
    # Công thức: Tổng tiền = Tiền gốc + (Tiền gốc * Lãi suất tháng * Số tháng)
    tien_lai_don = so_tien_gui * r_thang * so_thang
    tong_tien_lai_don = so_tien_gui + tien_lai_don

    # 2. Tính Lãi Kép (nhập gốc hàng tháng)
    # Công thức: Tổng tiền = Tiền gốc * (1 + Lãi suất tháng)^Số tháng
    tong_tien_lai_kep = so_tien_gui * ((1 + r_thang) ** so_thang)
    tien_lai_kep = tong_tien_lai_kep - so_tien_gui

    # Chênh lệch
    chenh_lech = tien_lai_kep - tien_lai_don

    st.divider()
    st.subheader("📊 Kết quả tính toán")

    # Hiển thị kết quả bằng dạng cột
    res_col1, res_col2 = st.columns(2)

    with res_col1:
        st.markdown("### 🔹 Lãi Đơn")
        st.metric("Tiền lãi nhận được", f"{tien_lai_don:,.0f} VNĐ")
        st.metric("Tổng tiền thu về", f"{tong_tien_lai_don:,.0f} VNĐ")

    with res_col2:
        st.markdown("### 🔸 Lãi Kép (Nhập gốc tháng)")
        st.metric("Tiền lãi nhận được", f"{tien_lai_kep:,.0f} VNĐ")
        st.metric("Tổng tiền thu về", f"{tong_tien_lai_kep:,.0f} VNĐ")

    st.info(f"💡 **Chênh lệch:** Phương thức **Lãi kép** giúp bạn sinh lời nhiều hơn **Lãi đơn** là **{chenh_lech:,.0f} VNĐ** sau {so_thang} tháng.")

# Hướng dẫn chân trang
st.caption("Lưu ý: Công thức lãi kép ở đây áp dụng cho trường hợp tiền lãi được cộng dồn vào gốc theo từng tháng.")
