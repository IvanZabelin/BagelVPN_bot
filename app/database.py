import sqlite3
from datetime import datetime, timedelta


def add_user_to_db(user_id, username, full_name):
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        username TEXT,
        full_name TEXT,
        subscription_end DATE,
        subscription_active BOOLEAN
    )
    ''')

    cursor.execute('''
    INSERT OR IGNORE INTO users (user_id, username, full_name, subscription_end, subscription_active)
    VALUES (?, ?, ?, ?, ?)
    ''', (user_id, username, full_name, None, False))

    conn.commit()
    conn.close()


def update_subscription(user_id):
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    # Получаем текущую дату окончания подписки
    cursor.execute('''
    SELECT subscription_end FROM users WHERE user_id = ?
    ''', (user_id,))
    
    result = cursor.fetchone()
    if result and result[0]:
        # Преобразуем строку в datetime
        current_subscription_end = datetime.fromisoformat(result[0])
        
        # Если текущая подписка ещё активна (т.е. дата окончания в будущем), добавляем дни к существующей дате
        if current_subscription_end > datetime.now():
            new_subscription_end = current_subscription_end + timedelta(days=30)
        else:
            # Если подписка истекла, начинаем отсчет с текущей даты
            new_subscription_end = datetime.now() + timedelta(days=30)
    else:
        # Если подписки не было или она истекла, устанавливаем новую подписку с текущей даты
        new_subscription_end = datetime.now() + timedelta(days=30)

    # Обновляем дату окончания подписки в базе данных
    cursor.execute('''
    UPDATE users
    SET subscription_end = ?, subscription_active = ?
    WHERE user_id = ?
    ''', (new_subscription_end.isoformat(), True, user_id))

    conn.commit()
    conn.close()


def deactivate_subscription(user_id):
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE users
    SET subscription_active = ?
    WHERE user_id = ?
    ''', (False, user_id))

    conn.commit()
    conn.close()


def get_user_info(user_id):
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    # Получаем информацию о пользователе
    cursor.execute('''
    SELECT user_id, username, full_name, subscription_end FROM users
    WHERE user_id = ?
    ''', (user_id,))

    user = cursor.fetchone()
    conn.close()

    if user:
        user_id, username, full_name, subscription_end = user

        # Если подписка не пуста, преобразуем строку в datetime
        if subscription_end:
            subscription_end_date = datetime.fromisoformat(subscription_end)
            days_left = (subscription_end_date - datetime.now()).days
            return {
                'username': username,
                'full_name': full_name,
                'days_left': days_left
            }
        else:
            return {
                'username': username,
                'full_name': full_name,
                'days_left': None
            }
    return None


# Добавление нового ключа для пользователя
def add_key_to_user(user_id, key_id, key_name):
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT OR REPLACE INTO user_keys (user_id, key_id, key_name)
    VALUES (?, ?, ?)
    ''', (user_id, key_id, key_name))

    conn.commit()
    conn.close()


# Получение ключа пользователя
def get_user_key(user_id):
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT key_id, key_name FROM user_keys WHERE user_id = ?
    ''', (user_id,))
    
    key_info = cursor.fetchone()
    conn.close()

    return key_info


def initialize_db():
    conn = sqlite3.connect('bot_users.db')
    cursor = conn.cursor()

    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        username TEXT,
        full_name TEXT,
        subscription_end DATE,
        subscription_active BOOLEAN
    )
    ''')

    # Создание таблицы ключей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        key_id TEXT,
        key_name TEXT,
        FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()

# Вызови эту функцию при запуске приложения
initialize_db()
