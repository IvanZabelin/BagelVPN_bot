import asyncio
import sqlite3
from datetime import datetime
from app.database import deactivate_subscription, get_user_key
from app.outline import delete_key


async def check_subscriptions():
    while True:
        conn = sqlite3.connect('bot_users.db')
        cursor = conn.cursor()

        # Получаем всех пользователей с истекшими подписками
        cursor.execute('''SELECT user_id FROM users WHERE subscription_end IS NOT NULL AND subscription_end < ?''', (datetime.now(),))
        users_to_deactivate = cursor.fetchall()

        for (user_id,) in users_to_deactivate:
            deactivate_subscription(user_id)

            # Получаем ключ пользователя
            user_key = get_user_key(user_id)

            if user_key:
                key_id = user_key[0]
                
                # Удаляем ключ на сервере Outline
                delete_key(key_id)

        conn.close()

        # Проверяем каждую ночь
        await asyncio.sleep(86400)
