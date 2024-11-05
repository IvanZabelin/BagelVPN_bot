from config.settings import client


# функция для переработки гигабайт в байты
def gb_to_bytes(gb: float):
    bytes_in_gb = 1024 ** 3  # 1 гб = 1024^3 байт
    return int(gb * bytes_in_gb)


# получение информации о всех ключах
def get_keys():
    return client.get_keys()


# Получение информации по конкретному ключу
def get_key_info(key_id: str):
    return client.get_key(key_id)


# создание нового ключа
def create_new_key(name: str = None, data_limit_gb: float = None):
    return client.create_key(name=name, data_limit=gb_to_bytes(data_limit_gb))


# обновление лимита данных
def update_data_limit(key_id: str, data_limit_gb: float):
    return client.add_data_limit(key_id, gb_to_bytes(data_limit_gb))


# снятие лимита данных
def delete_data_limit(key_id: str):
    return client.delete_data_limit(key_id)


# удаление ключа
def delete_key(key_id: str):
    return client.delete_key(key_id)


# получение технической информации о сервере
def get_service_info():
    return client.get_server_information()
