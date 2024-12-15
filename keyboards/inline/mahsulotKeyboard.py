from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import course_callback

# 1-usul
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text="Kurslar💻", callback_data="courses"),
          InlineKeyboardButton(text="Kitoblar📚", callback_data='books')
        ],
        [
            InlineKeyboardButton(text="🎥Kun.uz youtube sahifasiga link", url="https://www.youtube.com/@kunuz_official")
        ],
        [
            InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=""),
        ]
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="Foydali bot"),
        ]
    ],

)


#kurslar uchun
# 2-usul
courseMenu = InlineKeyboardMarkup(row_width=1)
entry = InlineKeyboardButton(text="Entry dasturlash", callback_data=course_callback.new(item_name="entry"))
courseMenu.insert(entry)
python = InlineKeyboardButton(text="Python dasturlash", callback_data=course_callback.new(item_name='entry'))
courseMenu.insert(python)