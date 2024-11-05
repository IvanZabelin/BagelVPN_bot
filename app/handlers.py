from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

import app.keyboards as kb
from app.database import add_user_to_db, get_user_info, get_user_key
from app.payment import router as payment_router

router = Router()
router.include_router(payment_router)


@router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    add_user_to_db(user_id, username, full_name)
    await message.reply(f"Hello, {full_name}!", reply_markup=kb.main)


@router.message(F.text == "Оформить VPN")
async def get_a_vpn(message: Message):
    await message.reply("Оформить VPN", reply_markup=kb.get_a_vpn)


@router.callback_query(F.data == "tariffs")
async def get_tariffs(callback: Message):
    await callback.answer('')
    await callback.message.answer("Тарифы: \nОдин месяц - 150руб.")


@router.message(F.text == "Мой профиль")
async def get_profile(message: Message, bot: Bot):
    user_id = message.from_user.id
    user_info = get_user_info(user_id)
    user_key = get_user_key(user_id) 

    if user_info:
        response_message = (
            f"Имя: {user_info['full_name']}\n"
            f"Юзернейм: {user_info['username']}\n"
        )

        if user_info['days_left'] is not None:
            response_message += f"Осталось дней до конца подписки: {user_info['days_left']}"
        else:
            response_message += "Активных подписок нет"

        if user_key:
            vpn_key = user_key[0]
            response_message += f"\nВаш VPN ключ: {vpn_key}"
    else:
        response_message = "Пользователь не найден"

    await message.reply(response_message)

@router.message(F.text == "📄 Инструкция")
async def get_a_vpn(message: Message):
    await message.reply("📄 Инструкция", reply_markup=kb.devices)