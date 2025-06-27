from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = '8095094481:AAGwxcMZKFRBnbgrF4nf_tMcaDT-0YvECZE'
ADMIN_ID = 6766312057  # например: 123456789

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(
    KeyboardButton("💻 IT"),
    KeyboardButton("📈 SMM и Маркетинг"),
    KeyboardButton("🤖 Нейросети и AI"),
    KeyboardButton("🎨 Дизайн и графика"),
)
main_kb.add(KeyboardButton("🔓 Доступ ко всем курсам"))

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    text = (
        "Привет! 👋\n\n"
        "У нас есть приватные каналы с полезными курсами по разным направлениям:\n\n"
        "💻 IT\n"
        "📈 Маркетинг и SMM\n"
        "🤖 Нейросети и AI\n"
        "🎨 Дизайн и графика\n\n"
        "Выбирай, что интересно, и получи доступ к материалам. ⬇️"
    )
    await message.answer(text, reply_markup=main_kb)

@dp.message_handler(lambda message: message.text in [
    "💻 IT", "📈 SMM и Маркетинг", "🤖 Нейросети и AI", "🎨 Дизайн и графика"
])
async def handle_topic(message: types.Message):
    topic = message.text
    text = (
        f"Ты выбрал {topic} ✅\n\n"
        f"💳 Стоимость доступа: *5000₸ навсегда*\n\n"
        f"Переведи на Kaspi и отправь чек сюда для получения доступа:\n"
        f"📱 Kaspi Gold: 777 123 4567 (Имя Фамилия)"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "🔓 Доступ ко всем курсам")
async def handle_all_access(message: types.Message):
    text = (
        "Ты выбрал полный доступ ко всем курсам ✅\n\n"
        "💳 Стоимость: *10 000₸ навсегда*\n\n"
        "Включает:\n"
        "✅ IT\n✅ SMM/Маркетинг\n✅ Нейросети/AI\n✅ Дизайн/Графика\n\n"
        "Переведи на Kaspi и отправь чек сюда:\n"
        "📱 Kaspi Gold: 777 123 4567 (Имя Фамилия)"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message_handler(content_types=types.ContentType.ANY)
async def handle_receipt(message: types.Message):
    user = message.from_user
    caption = f"Чек от @{user.username or 'без username'} (ID: {user.id})"

    if message.photo:
        await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=caption)
        await message.reply("✅ Чек отправлен на проверку. Ожидай подтверждения.")
    elif message.document and message.document.mime_type.startswith("image/"):
        await bot.send_document(chat_id=ADMIN_ID, document=message.document.file_id, caption=caption)
        await message.reply("✅ Чек отправлен на проверку. Ожидай подтверждения.")
    else:
        await message.reply("⚠️ Пожалуйста, отправь изображение чека или скриншот как фото или файл.")

if __name__ == '__main__':
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)
