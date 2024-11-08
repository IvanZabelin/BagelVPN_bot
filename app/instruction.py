from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.keyboards import devices


router = Router()


@router.callback_query(F.data == "instructions_iphone")
async def get_iphone(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    text = (
        "1️⃣ <b>Установите бесплатное приложение "
        "<a href='https://apps.apple.com/ru/app/outline-app/id1356177741'>"
        "Outline(ссылка)</a> из App Store</b>\n\n"
        "2️⃣ <b>Добавьте в приложение ключ, нажав на плюсик в правом верхнем углу</b>\n\n"
        '3️⃣ <b>Нажмите "Подключиться" и получайте удовольствие 🤤</b>'
    )
    await callback.message.answer(
        text=text,
        reply_markup=devices,
        disable_web_page_preview=True,
        parse_mode='HTML'
    )


@router.callback_query(F.data == "instructions_android")
async def get_iphone(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    text = (
        "1️⃣ <b>Установите бесплатное приложение "
        "<a href='https://play.google.com/store/apps/details?id=org.outline.android"
        ".client'>"
        "Outline(ссылка)</a> из Google Play</b>\n\n"
        "2️⃣ <b>Добавьте в приложение ключ, нажав на плюсик в правом верхнем углу</b>\n\n"
        '3️⃣ <b>Нажмите "Подключиться" и получайте удовольствие 🤤</b>'
    )
    
    await callback.message.answer(
        text=text,
        reply_markup=devices,
        disable_web_page_preview=True,
        parse_mode='HTML'
    )


@router.callback_query(F.data == "instructions_mac")
async def get_iphone(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    text = (
        "1️⃣ <b>Установите бесплатное приложение "
        "<a href='https://apps.apple.com/us/app/outline-app/id1356178125'>"
        "Outline(ссылка)</a> из App Store</b>\n\n"
        "2️⃣ <b>Добавьте в приложение ключ, нажав на плюсик в правом верхнем углу</b>\n\n"
        '3️⃣ <b>Нажмите "Подключиться" и получайте удовольствие 🤤</b>'
    )  
    await callback.message.answer(
        text=text,
        reply_markup=devices,
        disable_web_page_preview=True,
        parse_mode='HTML'
    )


@router.callback_query(F.data == "instructions_windows")
async def get_iphone(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    text = (
        "1️⃣ <b>Перейдите на сайт "
        "<a href='https://getoutline.org/'>"
        "Outline(ссылка)</a></b>\n\n"
        "2️⃣ <b>Нажмите Скачать Outline -> Скачать Outline Client -> Выберите Windows и нажмите Скачать</b>\n\n"
        "3️⃣ <b>Добавьте в приложение ключ, нажав на плюсик в правом верхнем углу</b>\n\n"
        '4️⃣ <b>Нажмите "Подключиться" и получайте удовольствие 🤤</b>'
    ) 
    await callback.message.answer(
        text=text,
        reply_markup=devices,
        disable_web_page_preview=True,
        parse_mode='HTML'
    )


@router.callback_query(F.data == "instructions_linux")
async def get_iphone(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    text = (
        "1️⃣ <b>Перейдите на сайт "
        "<a href='https://getoutline.org/'>"
        "Outline(ссылка)</a></b>\n\n"
        "2️⃣ <b>Нажмите Скачать Outline -> Скачать Outline Client -> Выберите Linux и нажмите Скачать</b>\n\n"
        "3️⃣ <b>Добавьте в приложение ключ, нажав на плюсик в правом верхнем углу</b>\n\n"
        '4️⃣ <b>Нажмите "Подключиться" и получайте удовольствие 🤤</b>'
    )
  
    await callback.message.answer(
        text=text,
        reply_markup=devices,
        disable_web_page_preview=True,
        parse_mode='HTML'
    )
