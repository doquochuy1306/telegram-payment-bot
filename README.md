# Telegram Payment Bot

Đây là một bot Telegram mẫu tích hợp thanh toán qua MoMo.  
Các tính năng bao gồm:
- **/start**: Chào mừng người dùng.
- **/pay**: Hiển thị thông tin thanh toán qua MoMo.

## Hướng dẫn deploy trên Railway

1. Tạo repo chứa toàn bộ các file trên.
2. Đăng nhập vào [Railway.app](https://railway.app) và tạo Project mới từ repo GitHub.
3. Thêm các biến môi trường (TELEGRAM_TOKEN, MOMO_NUMBER, GROUP_LINK) trong mục Settings → Variables.
4. Railway sẽ tự động build và khởi chạy bot. Kiểm tra log để đảm bảo bot hoạt động.

## Lưu ý

- Cập nhật token và thông tin thanh toán nếu cần.
- Bạn có thể mở rộng các tính năng của bot (tự động thêm/kick thành viên, thông báo gia hạn, …).
