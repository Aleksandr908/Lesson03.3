class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа для обычных сотрудников

    # Метод для получения ID пользователя
    def get_user_id(self):
        return self.__user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.__name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администраторов
        self.__users = []  # Список пользователей

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Можно добавлять только объекты класса User.")

    # Метод для удаления пользователя
    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
            print(f"Пользователь {user.get_name()} удален.")
        else:
            print("Пользователь не найден в списке.")

    # Метод для получения списка пользователей
    def get_users(self):
        return [user.get_name() for user in self.__users]

    # Переопределяем метод получения уровня доступа для администратора
    def get_access_level(self):
        return self.__access_level


# Пример использования
if __name__ == "__main__":
    admin = Admin(1, "Глафира")
    user1 = User(2, "Василий")
    user2 = User(3, "Акакий")
    user3 = User(4, "Павсикакий")

    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)

    print("Список пользователей:", admin.get_users())

    admin.remove_user(user1)
    print("Список пользователей после удаления:", admin.get_users())