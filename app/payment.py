from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, PreCheckoutQuery, Message

from app.database import add_key_to_user, update_subscription, get_user_key
from app.outline import create_new_key
from config.settings import CURRENCY, pay_secret_key, PRICE

router = Router()

@router.callback_query(F.data == "payment")
async def buy_handler(callback: CallbackQuery, bot: Bot):
    await callback.answer('')
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title="Оформление подписки",
        description="Один месяц", 
        payload="1",
        provider_token=pay_secret_key,
        currency=CURRENCY,
        start_parameter="test_bot",
        prices=[{"label": "Один месяц", "amount": PRICE}],
        need_shipping_address=True,
        need_name=True,
        need_email=True,
        send_phone_number_to_provider=True,
        send_email_to_provider=True,
        is_flexible=False
    )


@router.pre_checkout_query()
async def process_pre_checkout_query(
    pre_checkout_query: PreCheckoutQuery,
    bot: Bot
):
    await bot.answer_pre_checkout_query(
        pre_checkout_query.id,
        ok=True,
    )


@router.message(F.successful_payment)
async def successful_payment_handler(message: Message, bot: Bot):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    # Указываем лимит данных в гигабайтах
    data_limit_gb = 200
    existing_key_info = get_user_key(user_id)
    if existing_key_info:
        await message.reply("У вас уже есть активный ключ. Подписка будет продлена.")
        update_subscription(user_id)

    else:
        key_details = create_new_key(
            name=f"{full_name}",
            data_limit_gb=data_limit_gb
        )
        if key_details:
            access_url = key_details.access_url
            key_id = key_details.key_id
            add_key_to_user(user_id, access_url, key_id)
            update_subscription(user_id)
            await message.reply("Ваш VPN ключ успешно создан и привязан к вашему аккаунту.\nВаш ключ:")
            await message.reply(f"{key_details.access_url}")
            
        else:
            await message.reply("Не удалось создать ключ."
                                "Попробуйте снова позже.")
