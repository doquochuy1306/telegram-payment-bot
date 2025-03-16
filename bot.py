import os
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Cấu hình logging để theo dõi log hoạt động
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Lấy biến môi trường
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MOMO_NUMBER = os.getenv("MOMO_NUMBER")
GROUP_LINK = os.getenv("GROUP_LINK")  # Link nhóm Telegram (nếu cần dùng trong thông báo)

# Hàm xử lý lệnh /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Chào mừng bạn đến với Bot Thanh Toán của chúng tôi!")

# Hàm xử lý lệnh /pay để hiển thị thông tin thanh toán qua MoMo
def pay(update: Update, context: CallbackContext) -> None:
    text = f"Để thanh toán, vui lòng chuyển tiền qua MoMo:
SĐT: {MOMO_NUMBER}
Chủ TK: Đỗ Quốc Huy"
    update.message.reply_text(text)

# Hàm chính chạy bot
def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("pay", pay))

    # Khởi động bot
    updater.start_polling()
    logger.info("Bot đã khởi động...")
    updater.idle()

if __name__ == '__main__':
    main()
