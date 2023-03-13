from aiogram import types


kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(
    types.KeyboardButton("Книги"),
    types.KeyboardButton("Кружки")
)


async def show_categories(message: types.Message):
    await message.reply("Наши товары", reply_markup=kb)


async def show_category_books(message: types.Message):
    kb_books = types.InlineKeyboardMarkup()
    kb_books.add(
        types.InlineKeyboardButton(text="Книга 1", url='https://google.com')),
    kb_books.add(
        types.InlineKeyboardButton(text="Книга 2", callback_data='book')
    )
    await message.answer("Наши книги", reply_markup=kb_books)


async def show_book(callback: types.CallbackQuery):
    await callback.message.answer("Это инфо о самой интересной книге")