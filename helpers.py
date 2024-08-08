import random


class Helpers:
    # Генерируем логин
    @staticmethod
    def generate_login():
        generated_login = f'romanmakarcov9{random.randint(100, 999)}@yandex.ru'
        return generated_login

    # Генерируем пароль
    @staticmethod
    def generate_password():
        generated_password = f'{random.randint(100000, 999999999)}'
        return generated_password

    @staticmethod
    def generate_wrong_password():
        generated_wrong_password = f'{random.randint(0, 99999)}'
        return generated_wrong_password