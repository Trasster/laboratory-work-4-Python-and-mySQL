from config import user, password_user
from mysql.connector import connect, Error
from window import start_window

try:
    with connect(
        host="localhost",
        user=user,
        port=3307,
        password=password_user,
        database="staff",
    ) as connection:

        def create_table():
            with connection.cursor() as cursor:
                create = """
                CREATE TABLE IF NOT EXISTS users
                (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    second_name VARCHAR(50),
                    first_third_name VARCHAR(50),
                    post VARCHAR(50),
                    address VARCHAR(50),
                    t_number VARCHAR(50),
                    login VARCHAR(32),
                    password VARCHAR(32)
                );
                """
                cursor.execute(create)
                connection.commit()

        def insert_into_db():
            with connection.cursor() as cursor:
                truncate = "TRUNCATE TABLE users"
                insert_data_users = """
                INSERT INTO users (second_name, first_third_name, post, address, t_number, login, password)
                VALUES
                    ("Колесников", "Гарри Лукьянович", "Директор", "ул. Донская, д.8, стр.1", "+7(911)-567-38-21", "login1", "password1"),
                    ("Зыков", "Мирон Всеволодович", "Зам. Директора", "Проспект Вернадского, д.43, кв.29", "+7(987)-666-75-21", "login2", "password2"),
                    ("Терентьев", "Мирослав Авдеевич", "Зам. Директора", "ул. Удальцова, д.87, кв.5", "+7(981)-876-11-22", "login3", "password3"),
                    ("Власова", "Нева Альвиановна", "Секретарь", "ул. Солнечная, д.17, кв.89", "+7(419)-556-98-97", "login4", "password4"),
                    ("Крылова", "Любовь Кирилловна", "Секретарь", "ул. Хуторская, д.10, кв.199", "+7(981)-761-63-63", "login5", "password5")
                """
                cursor.execute(truncate)
                cursor.execute(insert_data_users)
                connection.commit()

        create_table()
        insert_into_db()

except Error as e:
    print(e)

start_window()