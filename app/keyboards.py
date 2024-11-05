from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           ReplyKeyboardMarkup, KeyboardButton)

# Клавиатура с кнопками для основного меню
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Оформить VPN')],
    [KeyboardButton(text='Мой профиль')],
    [KeyboardButton(text='📄 Инструкция')],
    [KeyboardButton(text='📢 FAQ')],
], resize_keyboard=True, input_field_placeholder="Выберите опцию")

# Инлайн-клавиатура с тарифами и оплатой
get_a_vpn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тарифы', callback_data='tariffs')],
    [InlineKeyboardButton(text='Оплата', callback_data='payment')],
])

# Инлайн-клавиатура для выбора устройства
devices = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🍏Iphone/Ipad", callback_data="instructions_iphone"),
        InlineKeyboardButton(text="🤖Android", callback_data="instructions_android")
    ],
    [
        InlineKeyboardButton(text="💻Mac", callback_data="instructions_mac"),
        InlineKeyboardButton(text="🖥Windows", callback_data="instructions_windows")
    ],
    [
        InlineKeyboardButton(text="📺Linux", callback_data="instructions_linux")
    ],
    
])
