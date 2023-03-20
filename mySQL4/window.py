from tkinter import *
from tkinter import ttk
from config import user, password_user
from mysql.connector import connect, Error


def new_window_staff():
    window2 = Tk()
    window2.title('Просмотр информации о сотрудниках')
    window2.geometry('800x600')

    frame1 = Frame(
        window2,
        padx=10,
        pady=10
    )
    frame1.pack(expand=True)

    window2.mainloop()

def new_window_guest():
    try:
        with connect(
                host="localhost",
                user=user,
                port=3307,
                password=password_user,
                database="staff",
        ) as connection:
            with connection.cursor() as cursor:
                select_columns = "SELECT second_name, first_third_name, post, t_number FROM users"
                cursor.execute(select_columns)
                list_rows_guest = [' '.join(row) for row in cursor.fetchall()]
                connection.commit()

    except Error as e:
        print(e)
    list_guest_preview = []
    for i in range(len(list_rows_guest)):
        list_guest_preview += list_rows_guest[i] + '\n'
    list_guest = ''
    counter_ = 0
    counterS = 0
    for j in list_guest_preview:
        symbol = j
        if j == ' ' and prev_symbol != '.' and prev_symbol != ':':
            counter_ += 1
            if counter_ == 3:
                j = ', Должность: '
            elif counter_ == 4:
                j = ', Номер телефона: '
        elif j == '\n':
            counter_ = 0
            counterS = 0
            j = ''
        if counterS == 0:
            list_guest += '\n' + 'ФИО: '
        list_guest += j
        counterS += 1
        prev_symbol = symbol

    window3 = Tk()
    window3.title('Просмотр информации о сотрудниках')
    window3.geometry('800x600')

    frame2 = Frame(
        window3,
        padx=10,
        pady=10
    )
    frame2.pack(expand=True)

    welcome_lb = Label(
        frame2,
        text="Вы вошли как гость\n"
    )
    welcome_lb.grid(row=1, column=1)

    preview_list_guest_lb = Label(
        frame2,
        text="Список сотрудников:"
    )
    preview_list_guest_lb.grid(row=2, column=1)

    list_guest_lb = Label(
        frame2,
        text=list_guest[:-5],
        justify=LEFT,
        font="TkTooltipFont"
    )
    list_guest_lb.grid(row=3, column=1)

    enter_btn_staff = Button(
        frame2,
        text='Выйти',
        command=lambda:[window3.destroy(), start_window()]
    )
    enter_btn_staff.grid(row=4, column=1)

    window3.mainloop()

def new_window_clerk():
    try:
        with connect(
                host="localhost",
                user=user,
                port=3307,
                password=password_user,
                database="staff",
        ) as connection:
            with connection.cursor() as cursor:
                select_columns = "SELECT second_name, first_third_name, post, address, t_number FROM users"
                cursor.execute(select_columns)
                list_rows_guest = [' '.join(row) for row in cursor.fetchall()]
                connection.commit()

    except Error as e:
        print(e)
    list_guest_preview = []
    for i in range(len(list_rows_guest)):
        list_guest_preview += list_rows_guest[i] + '\n'
    list_guest = ''
    counter_ = 0
    counterS = 0
    for j in list_guest_preview:
        symbol = j
        if j == ' ' and prev_symbol != '.' and prev_symbol != ':' and prev_symbol != ',' and prev_symbol not in 'т':
            counter_ += 1
            if counter_ == 3:
                j = '; Должность: '
            elif counter_ == 4:
                j = '; Адрес: '
            elif counter_ == 5:
                j = '; Номер телефона: '
        elif j == '\n':
            counter_ = 0
            counterS = 0
            j = ''
        if counterS == 0:
            list_guest += '\n' + 'ФИО: '
        list_guest += j
        counterS += 1
        prev_symbol = symbol

    window_clerk = Tk()
    window_clerk.title('Просмотр информации о сотрудниках')
    window_clerk.geometry('800x600')

    frame_clerk = Frame(
        window_clerk,
        padx=10,
        pady=10
    )
    frame_clerk.pack(expand=True)

    welcome_lb = Label(
        frame_clerk,
        text="Вы вошли как секретарь\n"
    )
    welcome_lb.grid(row=1, column=1)

    preview_list_guest_lb = Label(
        frame_clerk,
        text="Список сотрудников:"
    )
    preview_list_guest_lb.grid(row=2, column=1)

    list_guest_lb = Label(
        frame_clerk,
        text=list_guest[:-5],
        justify=LEFT,
        font="TkTooltipFont"
    )
    list_guest_lb.grid(row=3, column=1)

    enter_btn_staff = Button(
        frame_clerk,
        text='Выйти',
        command=lambda: [window_clerk.destroy(), start_window()]
    )
    enter_btn_staff.grid(row=4, column=1)

    window_clerk.mainloop()

def new_window_director():
    try:
        with connect(
                host="localhost",
                user=user,
                port=3307,
                password=password_user,
                database="staff",
        ) as connection:
            with connection.cursor() as cursor:
                select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                cursor.execute(select_columns)
                list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                select_second_name = "SELECT second_name FROM users"
                cursor.execute(select_second_name)
                global second_name_column
                second_name_column = tuple(cursor.fetchall())

                list_guest_preview = []
                for i in range(len(list_rows_guest)):
                    list_guest_preview += list_rows_guest[i] + '\n'
                list_guest = ''
                counter_ = 0
                counterS = 0
                for j in list_guest_preview:
                    symbol = j
                    if j == ' ' and prev_symbol != '.' and prev_symbol != ':' and prev_symbol != ',' and prev_symbol not in 'т':
                        counter_ += 1
                        if counter_ == 3:
                            j = '; Должность: '
                        elif counter_ == 4:
                            j = '; Адрес: '
                        elif counter_ == 5:
                            j = '; Номер телефона: '
                        elif counter_ == 6:
                            j = '; Логин: '
                        elif counter_ == 7:
                            j = '; Пароль: '
                    elif j == '\n':
                        counter_ = 0
                        counterS = 0
                        j = ''
                    if counterS == 0:
                        list_guest += '\n' + 'ФИО: '
                    list_guest += j
                    counterS += 1
                    prev_symbol = symbol

                def button_delete():
                    value = choose_to_delete.get()
                    select_value = "DELETE FROM users WHERE second_name = " + "'" + value + "'"
                    cursor.execute(select_value)

                    select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                    cursor.execute(select_columns)
                    list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                    select_second_name = "SELECT second_name FROM users"
                    cursor.execute(select_second_name)
                    global second_name_column
                    second_name_column = tuple(cursor.fetchall())

                    global list_guest_preview
                    list_guest_preview = []
                    for i in range(len(list_rows_guest)):
                        list_guest_preview += list_rows_guest[i] + '\n'
                    list_guest = ''
                    counter_ = 0
                    counterS = 0
                    for j in list_guest_preview:
                        symbol = j
                        if j == ' ' and prev_symbol != '.' and prev_symbol != ':' and prev_symbol != ',' and prev_symbol not in 'т':
                            counter_ += 1
                            if counter_ == 3:
                                j = '; Должность: '
                            elif counter_ == 4:
                                j = '; Адрес: '
                            elif counter_ == 5:
                                j = '; Номер телефона: '
                            elif counter_ == 6:
                                j = '; Логин: '
                            elif counter_ == 7:
                                j = '; Пароль: '
                        elif j == '\n':
                            counter_ = 0
                            counterS = 0
                            j = ''
                        if counterS == 0:
                            list_guest += '\n' + 'ФИО: '
                        list_guest += j
                        counterS += 1
                        prev_symbol = symbol

                    list_guest_lb['text'] = list_guest[:-5]
                    connection.commit()
                    window_director.update()
                    return 0

                def button_add():
                    value1 = second_name_en.get()
                    value2 = ft_name_en.get()
                    value3 = post_en.get()
                    value4 = address_en.get()
                    value5 = t_number_en.get()
                    value6 = login_enter.get()
                    value7 = password_enter.get()
                    add_values = "INSERT INTO users (second_name, first_third_name, post, address, t_number, login, password)\
                    VALUES\
                        ('"+ value1 +"', '"+ value2 +"', '"+ value3 +"', '"+ value4 +"', '"+ value5 +"', '"+ value6 +"', '"+ value7 +"')"
                    cursor.execute(add_values)

                    select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                    cursor.execute(select_columns)
                    list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                    global list_guest_preview
                    list_guest_preview = []
                    for i in range(len(list_rows_guest)):
                        list_guest_preview += list_rows_guest[i] + '\n'
                    list_guest = ''
                    counter_ = 0
                    counterS = 0
                    for j in list_guest_preview:
                        symbol = j
                        if j == ' ' and prev_symbol != '.' and prev_symbol != ':' and prev_symbol != ',' and prev_symbol not in 'т':
                            counter_ += 1
                            if counter_ == 3:
                                j = '; Должность: '
                            elif counter_ == 4:
                                j = '; Адрес: '
                            elif counter_ == 5:
                                j = '; Номер телефона: '
                            elif counter_ == 6:
                                j = '; Логин: '
                            elif counter_ == 7:
                                j = '; Пароль: '
                        elif j == '\n':
                            counter_ = 0
                            counterS = 0
                            j = ''
                        if counterS == 0:
                            list_guest += '\n' + 'ФИО: '
                        list_guest += j
                        counterS += 1
                        prev_symbol = symbol
                    list_guest_lb['text'] = list_guest[:-5]
                    connection.commit()
                    select_second_name = "SELECT second_name FROM users"
                    cursor.execute(select_second_name)
                    global second_name_column
                    second_name_column = tuple(cursor.fetchall())
                    window_director.update()
                    return 0

                def button_fill():
                    select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                    cursor.execute(select_columns)
                    list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                    for i in range(len(list_rows_guest)):
                        for j in range(len(list_rows_guest)):
                            if second_name_en.get() == str(list_rows_guest[i].split()[j]):
                                select_to_fill = "SELECT * FROM users WHERE second_name = '" + list_rows_guest[i].split()[0] + "'"
                                cursor.execute(select_to_fill)
                                Get = cursor.fetchall()
                                ft_name_en.delete(0, END)
                                post_en.delete(0, END)
                                address_en.delete(0, END)
                                t_number_en.delete(0, END)
                                login_enter.delete(0, END)
                                password_enter.delete(0, END)
                                ft_name_en.insert(0, Get[0][2])
                                post_en.insert(0, Get[0][3])
                                address_en.insert(0, Get[0][4])
                                t_number_en.insert(0, Get[0][5])
                                login_enter.insert(0, Get[0][6])
                                password_enter.insert(0, Get[0][7])

                def button_update():
                    update_post = "UPDATE users SET post = '" + post_en.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_address = "UPDATE users SET address = '" + address_en.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_t_number = "UPDATE users SET t_number = '" + t_number_en.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_login = "UPDATE users SET login = '" + login_enter.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_password = "UPDATE users SET password = '" + password_enter.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    cursor.execute(update_post)
                    cursor.execute(update_address)
                    cursor.execute(update_t_number)
                    cursor.execute(update_login)
                    cursor.execute(update_password)
                    connection.commit()

                    select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                    cursor.execute(select_columns)
                    list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                    list_guest_preview = []
                    for i in range(len(list_rows_guest)):
                        list_guest_preview += list_rows_guest[i] + '\n'
                    list_guest = ''
                    counter_ = 0
                    counterS = 0
                    for j in list_guest_preview:
                        symbol = j
                        if j == ' ' and prev_symbol != '.' and prev_symbol != ':' and prev_symbol != ',' and prev_symbol not in 'т':
                            counter_ += 1
                            if counter_ == 3:
                                j = '; Должность: '
                            elif counter_ == 4:
                                j = '; Адрес: '
                            elif counter_ == 5:
                                j = '; Номер телефона: '
                            elif counter_ == 6:
                                j = '; Логин: '
                            elif counter_ == 7:
                                j = '; Пароль: '
                        elif j == '\n':
                            counter_ = 0
                            counterS = 0
                            j = ''
                        if counterS == 0:
                            list_guest += '\n' + 'ФИО: '
                        list_guest += j
                        counterS += 1
                        prev_symbol = symbol
                    list_guest_lb['text'] = list_guest[:-5]
                    connection.commit()

                window_director = Tk()
                window_director.title('Просмотр информации о сотрудниках')
                window_director.geometry('1200x600')

                welcome_lb = ttk.Label(
                    text="Вы вошли как директор\n"
                )
                welcome_lb.place(x=600, y=150, anchor='center')

                preview_list_guest_lb = ttk.Label(
                    text="Список сотрудников:"
                )
                preview_list_guest_lb.place(x=600, y=200, anchor='center')

                list_guest_lb = ttk.Label(
                    text=list_guest[:-5],
                    justify=LEFT
                )
                list_guest_lb.place(x=600, y=300, anchor='center')

                enter_btn_staff = ttk.Button(
                    text='Выйти',
                    command=lambda: [window_director.destroy(), start_window()]
                )
                enter_btn_staff.place(x=600, y=600, anchor='s')

                choose_to_delete = ttk.Combobox(
                    values=second_name_column
                )
                choose_to_delete.place(x=1000, y=500, anchor='center')

                delete_btn_staff = ttk.Button(
                    text='Удалить',
                    command=button_delete
                )
                delete_btn_staff.place(x=1000, y=550, anchor='center')

                post_en = ttk.Entry()
                post_en.place(x=300, y=20, anchor='nw')

                ft_name_en = ttk.Entry()
                ft_name_en.place(x=150, y=20, anchor='nw')

                second_name_en = ttk.Combobox(
                    values=second_name_column
                )
                second_name_en.place(x=0, y=20, anchor='nw')

                address_en = ttk.Entry()
                address_en.place(x=450, y=20, anchor='nw')

                t_number_en = ttk.Entry()
                t_number_en.place(x=600, y=20, anchor='nw')

                login_enter = ttk.Entry()
                login_enter.place(x=750, y=20, anchor='nw')

                password_enter = ttk.Entry()
                password_enter.place(x=900, y=20, anchor='nw')

                add_btn_staff = ttk.Button(
                    text='Добавить',
                    command=button_add
                )
                add_btn_staff.place(x=1150, y=20, anchor='ne')

                second_name_lb = ttk.Label(text="Фамилия:")
                second_name_lb.place(x=0, y=0, anchor='nw')

                ft_name_lb = ttk.Label(text="Имя и отчество:")
                ft_name_lb.place(x=150, y=0, anchor='nw')

                post_lb = ttk.Label(text="Должность:")
                post_lb.place(x=300, y=0, anchor='nw')

                address_lb = ttk.Label(text="Адрес:")
                address_lb.place(x=450, y=0, anchor='nw')

                t_number_lb = ttk.Label(text="Номер телефона:")
                t_number_lb.place(x=600, y=0, anchor='nw')

                login_lb = ttk.Label(text="Логин:")
                login_lb.place(x=750, y=0, anchor='nw')

                password_lb = ttk.Label(text="Пароль:")
                password_lb.place(x=900, y=0, anchor='nw')

                fill_btn_staff = ttk.Button(
                    text='Заполнить',
                    command=button_fill
                )
                fill_btn_staff.place(x=1150, y=50, anchor='ne')

                alter_btn_staff = ttk.Button(
                    text='Изменить',
                    command=button_update
                )
                alter_btn_staff.place(x=1150, y=80, anchor='ne')

                choose_user_lb = ttk.Label(
                    text='Выберите пользователя:',
                )
                choose_user_lb.place(x=1000, y=480, anchor='center')

                window_director.update()
                window_director.mainloop()
                connection.commit()

    except Error as e:
        print(e)

def new_window_deputy_director():
    try:
        with connect(
                host="localhost",
                user=user,
                port=3307,
                password=password_user,
                database="staff",
        ) as connection:
            with connection.cursor() as cursor:
                select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                cursor.execute(select_columns)
                list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                select_second_name = "SELECT second_name FROM users"
                cursor.execute(select_second_name)
                global second_name_column
                second_name_column = tuple(cursor.fetchall())

                list_guest_preview = []
                for i in range(len(list_rows_guest)):
                    list_guest_preview += list_rows_guest[i] + '\n'
                list_guest = ''
                counter_ = 0
                counterS = 0
                for j in list_guest_preview:
                    symbol = j
                    if j == ' ' and prev_symbol != '.' and prev_symbol != ':' and prev_symbol != ',' and prev_symbol not in 'т':
                        counter_ += 1
                        if counter_ == 3:
                            j = '; Должность: '
                        elif counter_ == 4:
                            j = '; Адрес: '
                        elif counter_ == 5:
                            j = '; Номер телефона: '
                        elif counter_ == 6:
                            j = '; Логин: '
                        elif counter_ == 7:
                            j = '; Пароль: '
                    elif j == '\n':
                        counter_ = 0
                        counterS = 0
                        j = ''
                    if counterS == 0:
                        list_guest += '\n' + 'ФИО: '
                    list_guest += j
                    counterS += 1
                    prev_symbol = symbol

                def button_fill():
                    select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                    cursor.execute(select_columns)
                    list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                    for i in range(len(list_rows_guest)):
                        for j in range(len(list_rows_guest)):
                            if second_name_en.get() == str(list_rows_guest[i].split()[j]):
                                select_to_fill = "SELECT * FROM users WHERE second_name = '" + list_rows_guest[i].split()[0] + "'"
                                cursor.execute(select_to_fill)
                                Get = cursor.fetchall()
                                ft_name_en.delete(0, END)
                                post_en.delete(0, END)
                                address_en.delete(0, END)
                                t_number_en.delete(0, END)
                                login_enter.delete(0, END)
                                password_enter.delete(0, END)
                                ft_name_en.insert(0, Get[0][2])
                                post_en.insert(0, Get[0][3])
                                address_en.insert(0, Get[0][4])
                                t_number_en.insert(0, Get[0][5])
                                login_enter.insert(0, Get[0][6])
                                password_enter.insert(0, Get[0][7])

                def button_update():
                    update_post = "UPDATE users SET post = '" + post_en.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_address = "UPDATE users SET address = '" + address_en.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_t_number = "UPDATE users SET t_number = '" + t_number_en.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_login = "UPDATE users SET login = '" + login_enter.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    update_password = "UPDATE users SET password = '" + password_enter.get() + "' WHERE second_name = '" + second_name_en.get() + "'"
                    cursor.execute(update_post)
                    cursor.execute(update_address)
                    cursor.execute(update_t_number)
                    cursor.execute(update_login)
                    cursor.execute(update_password)
                    connection.commit()

                    select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                    cursor.execute(select_columns)
                    list_rows_guest = [' '.join(row) for row in cursor.fetchall()]

                    list_guest_preview = []
                    for i in range(len(list_rows_guest)):
                        list_guest_preview += list_rows_guest[i] + '\n'
                    list_guest = ''
                    counter_ = 0
                    counterS = 0
                    for j in list_guest_preview:
                        symbol = j
                        if j == ' ' and prev_symbol != '.' and prev_symbol != ':' and prev_symbol != ',' and prev_symbol not in 'т':
                            counter_ += 1
                            if counter_ == 3:
                                j = '; Должность: '
                            elif counter_ == 4:
                                j = '; Адрес: '
                            elif counter_ == 5:
                                j = '; Номер телефона: '
                            elif counter_ == 6:
                                j = '; Логин: '
                            elif counter_ == 7:
                                j = '; Пароль: '
                        elif j == '\n':
                            counter_ = 0
                            counterS = 0
                            j = ''
                        if counterS == 0:
                            list_guest += '\n' + 'ФИО: '
                        list_guest += j
                        counterS += 1
                        prev_symbol = symbol
                    list_guest_lb['text'] = list_guest[:-5]
                    connection.commit()

                window_director = Tk()
                window_director.title('Просмотр информации о сотрудниках')
                window_director.geometry('1200x600')

                welcome_lb = ttk.Label(
                    text="Вы вошли как заместитель директора\n"
                )
                welcome_lb.place(x=600, y=150, anchor='center')

                preview_list_guest_lb = ttk.Label(
                    text="Список сотрудников:"
                )
                preview_list_guest_lb.place(x=600, y=200, anchor='center')

                list_guest_lb = ttk.Label(
                    text=list_guest[:-5],
                    justify=LEFT
                )
                list_guest_lb.place(x=600, y=300, anchor='center')

                enter_btn_staff = ttk.Button(
                    text='Выйти',
                    command=lambda: [window_director.destroy(), start_window()]
                )
                enter_btn_staff.place(x=600, y=600, anchor='s')

                post_en = ttk.Entry()
                post_en.place(x=300, y=20, anchor='nw')

                ft_name_en = ttk.Entry()
                ft_name_en.place(x=150, y=20, anchor='nw')

                second_name_en = ttk.Combobox(
                    values=second_name_column
                )
                second_name_en.place(x=0, y=20, anchor='nw')

                address_en = ttk.Entry()
                address_en.place(x=450, y=20, anchor='nw')

                t_number_en = ttk.Entry()
                t_number_en.place(x=600, y=20, anchor='nw')

                login_enter = ttk.Entry()
                login_enter.place(x=750, y=20, anchor='nw')

                password_enter = ttk.Entry()
                password_enter.place(x=900, y=20, anchor='nw')

                second_name_lb = ttk.Label(text="Фамилия:")
                second_name_lb.place(x=0, y=0, anchor='nw')

                ft_name_lb = ttk.Label(text="Имя и отчество:")
                ft_name_lb.place(x=150, y=0, anchor='nw')

                post_lb = ttk.Label(text="Должность:")
                post_lb.place(x=300, y=0, anchor='nw')

                address_lb = ttk.Label(text="Адрес:")
                address_lb.place(x=450, y=0, anchor='nw')

                t_number_lb = ttk.Label(text="Номер телефона:")
                t_number_lb.place(x=600, y=0, anchor='nw')

                login_lb = ttk.Label(text="Логин:")
                login_lb.place(x=750, y=0, anchor='nw')

                password_lb = ttk.Label(text="Пароль:")
                password_lb.place(x=900, y=0, anchor='nw')

                fill_btn_staff = ttk.Button(
                    text='Заполнить',
                    command=button_fill
                )
                fill_btn_staff.place(x=1150, y=50, anchor='ne')

                alter_btn_staff = ttk.Button(
                    text='Изменить',
                    command=button_update
                )
                alter_btn_staff.place(x=1150, y=20, anchor='ne')

                window_director.update()
                window_director.mainloop()
                connection.commit()

    except Error as e:
        print(e)


def start_window():
    global window1
    window1 = Tk()
    window1.title("Вход в аккаунт")
    window1.geometry('800x600')

    frame = Frame(
        window1,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    login_lb = Label(
        frame,
        text="Логин:"
    )
    login_lb.grid(row=3, column=2)

    password_lb = Label(
        frame,
        text="Пароль:"
    )
    password_lb.grid(row=5, column=2)

    global login_en
    login_en = Entry(
        frame,
    )
    login_en.grid(row=4, column=2)

    global password_en
    password_en = Entry(
        frame,
    )
    password_en.grid(row=6, column=2)

    enter_btn_staff = Button(
        frame,
        text='Войти как сотрудник',
        command=lambda:[transision_staff(), transision_clerk(), transision_director(), transision_deputy_director()]
    )
    enter_btn_staff.grid(row=7, column=2)

    enter_btn_guest = Button(
        frame,
        text='Войти как гость',
        command=transision_guest
    )
    enter_btn_guest.grid(row=8, column=2)

    window1.mainloop()

def transision_staff():
    login = str(login_en.get())
    password = str(password_en.get())

    if login == 'login' and password == 'password':
        window1.destroy()
        new_window_staff()
    else:
        pass


def transision_clerk():
    try:
        with connect(
                host="localhost",
                user=user,
                port=3307,
                password=password_user,
                database="staff",
        ) as connection:
            with connection.cursor() as cursor:
                select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password \
                FROM users"
                cursor.execute(select_columns)
                list_rows_guest = [' '.join(row) for row in cursor.fetchall()]
                count_clerk = ' '.join(list_rows_guest).count('Секретарь')
                get_login = "SELECT login FROM users WHERE post = 'Секретарь'"
                cursor.execute(get_login)
                login_pr = cursor.fetchall()
                get_password = "SELECT password FROM users WHERE post = 'Секретарь'"
                cursor.execute(get_password)
                password_pr = cursor.fetchall()
                login = str(login_en.get())
                password = str(password_en.get())
                connection.commit()
    except Error as e:
        print(e)
    for j in range(count_clerk):
        if "('" + login + "',)" == str(login_pr[j]) and "('" + password + "',)" == str(password_pr[j]):
            window1.destroy()
            new_window_clerk()
            break
        else:
            continue

def transision_director():
    try:
        with connect(
                host="localhost",
                user=user,
                port=3307,
                password=password_user,
                database="staff",
        ) as connection:
            with connection.cursor() as cursor:
                select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                cursor.execute(select_columns)
                list_rows_guest = [' '.join(row) for row in cursor.fetchall()]
                count_director = ' '.join(list_rows_guest).count('Директор')
                count_directora = ' '.join(list_rows_guest).count('Директора')
                get_login = "SELECT login FROM users WHERE post = 'Директор'"
                get_password = "SELECT password FROM users WHERE post = 'Директор'"
                cursor.execute(get_login)
                login_pr = cursor.fetchall()
                cursor.execute(get_password)
                password_pr = cursor.fetchall()
                login = str(login_en.get())
                password = str(password_en.get())
                connection.commit()
    except Error as e:
        print(e)
    for j in range(count_director-count_directora):
        if ("('" + login + "',)" == str(login_pr[j]) and "('" + password + "',)" == str(password_pr[j])):
            window1.destroy()
            new_window_director()
            break
        else:
            pass

def transision_deputy_director():
    try:
        with connect(
                host="localhost",
                user=user,
                port=3307,
                password=password_user,
                database="staff",
        ) as connection:
            with connection.cursor() as cursor:
                select_columns = "SELECT second_name, first_third_name, post, address, t_number, login, password FROM users"
                cursor.execute(select_columns)
                list_rows_guest = [' '.join(row) for row in cursor.fetchall()]
                count_zam_directora = ' '.join(list_rows_guest).count('Зам. Директора')
                get_login = "SELECT login FROM users WHERE post = 'Зам. Директора'"
                get_password = "SELECT password FROM users WHERE post = 'Зам. Директора'"
                cursor.execute(get_login)
                login_pr = cursor.fetchall()
                cursor.execute(get_password)
                password_pr = cursor.fetchall()
                login = str(login_en.get())
                password = str(password_en.get())
                connection.commit()
    except Error as e:
        print(e)
    for j in range(count_zam_directora):
        if ("('" + login + "',)" == str(login_pr[j]) and "('" + password + "',)" == str(password_pr[j])):
            window1.destroy()
            new_window_deputy_director()
            break
        else:
            pass

def transision_guest():
    window1.destroy()
    new_window_guest()




