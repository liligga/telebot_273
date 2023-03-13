from aiogram import executor
import logging
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.basic_handlers import (
    start,
    info,
    hello
)
from handlers.shop import (
    show_categories,
    show_category_books,
    show_book
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_category_books, Text(equals="Книги"))
    dp.register_callback_query_handler(show_book, Text(equals="book"))
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(info, commands=["info"])
    # в самом конце
    dp.register_message_handler(hello)
    executor.start_polling(dp)
