"""Скрипт наповнення бази даних"""
from datetime import datetime, date, timedelta
from random import randint
import sqlite3
from faker import Faker

disciplines = [
    "Вища математика",
    "Дискретна математика",
    "Лінійна алгебра",
    "Програмування",
    "Теорія імовірності",
    "Історія України",
    "Англійська мова",
    "Креслення"
]

groups = ['E331', 'TP-05-1', 'KN-51']
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
fake = Faker()
# створюємо з'єднання з базою даних hw_6_data_base.db
connect = sqlite3.connect('hw_6_data_base.db')
# Для виконання операторів SQLite3 спочатку встановлюється з'єднання, а потім створюється об'єкт курсора
cur = connect.cursor()
# Тепер можна використовувати об'єкт курсора для виклику методу execute() для виконання будь-яких запитів SQL


def seed_teachers():
    """Додає рандомних вчителів до таблиці"""

    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers (fullname) VALUES(?);"  # додати до таблиці "teachers" в поле "name"
    # додає записи в таблицю
    cur.executemany(sql, zip(teachers,))  # zip(teachers,) поверне кортеж типу ('name_of_teacher',)


def seed_disciplines():
    """Додає дисципліни рандомно до таблиці"""

    sql = "INSERT INTO disciplines (name, teacher_id) VALUES(?, ?);"  # тут для VALUES треба призначити два аргументи,
    # вони вказуються у вигляді кортежів (через zip) далі (аргументи cur.executemany мають бути iterable)
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))
    # iter дасть результат - список значень від 1 до NUMBER_TEACHERS, кількість значень у списку - len(disciplines)


def seed_groups():
    """Додає групи рандомно до таблиці"""

    sql = "INSERT INTO groups (name) VALUES(?);"
    cur.executemany(sql, zip(groups,))


def seed_students():
    """Додає студентів рандомно до таблиці"""

    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students (fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def seed_grades():
    # задамо дати початку та закінчення навчання
    start_date = datetime.strptime('2023-01-09', '%Y-%m-%d')
    end_date = datetime.strptime('2023-06-15', '%Y-%m-%d')
    sql = "INSERT INTO grades (discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?);"

    def get_list_date(start: date, end: date) -> list[date]:
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:  # сб та нд додаватися не будуть
                result.append(current_date)
            current_date += timedelta(1)
        return result
    list_dates = get_list_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]  #5 - це кількість студентів, яких оцінюють протягом уроку
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day.date()))  # day.date() чомусь підкреслює, але все спрацьовую коректно
    cur.executemany(sql, grades)


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        connect.close()

