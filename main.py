# from fastapi import FastAPI, Path, Query
# from typing import Optional
# from enum import Enum

# # Создание объекта приложения.
# app = FastAPI()


# class EducationLevel(str, Enum):
#     # Укажем значения с большой буквы, чтобы они хорошо смотрелись
#     # в документации Swagger.
#     SECONDARY = 'Среднее образование'
#     SPECIAL = 'Среднее специальное образование'
#     HIGHER = 'Высшее образовани'

# # Новый эндпоинт: приветствие для автора.


# @app.get(
#         '/{name}',
#         tags=['common methods', 'greetings'],
#         summary='Общее приветствие',
#         response_description='Полная строка приветствия'
#     )
# def greetings(
#         *,
#         # У параметров запроса name и surname значений по умолчанию нет,
#         # поэтому в первый параметр ставим многоточие, Ellipsis.
#         name: str = Path(
#             ...,
#             min_length=2,
#             max_length=20,
#             description='Можно вводить в любом регистре'
#         ),
#         surname: list[str] = Query(..., min_length=2, max_length=50),
#         cyrillic_string: str = Query(
#             'Здесь только кириллица',
#             regex='^[А-Яа-яЁё ]+$'
#         ),
#         age: Optional[int] = Query(None, gt=4, le=99),
#         is_staff: bool = Query(
#             False,
#             alias='is-staff',
#             include_in_schema=False
#         ),
#         education_level: Optional[EducationLevel] = None,
# ) -> dict[str, str]:
#     """
#     Приветствие пользователя:

#     - **name**: имя
#     - **surname**: фамилия
#     - **age**: возраст (опционально)
#     - **is_staff**: является ли пользователь сотрудником
#     - **education_level**: уровень образования (опционально)
#     """
#     surnames = ' '.join(surname)
#     result = ' '.join([name, surnames])
#     result = result.title()
#     if age is not None:
#         result += ', ' + str(age)
#     if education_level is not None:
#         result += ', ' + education_level.lower()
#     if is_staff:
#         result += ', сотрудник'
#     return {'Hello': result}


# @app.get(
#         '/me',
#         tags=['special methods', 'greetings'],
#         summary='Приветствие автора',
#         description='Приветствие человека по имени и фамилии; '
#                 'опционально указывается возраст, '
#                 'образование и статус сотрудника',
#     )
# def hello_author():
#     return {'Hello': 'author'}

from fastapi import FastAPI, Body

from schemas import Person

app = FastAPI()


# Меняем метод GET на POST, указываем статичный адрес.
@app.post('/hello')
# Вместо множества параметра теперь будет только один - person,
# в качестве аннотации указываем класс Person.
def greetings(
    person: Person = Body(
        ..., examples=Person.Config.schema_extra['examples']
        )) -> dict[str, str]:
    # Обращение к атрибутам класса происходит через точку;
    # при этом будут работать проверки на уровне типов данных.
    # В IDE будут работать автодополнения.
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}
