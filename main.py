from fastapi import FastAPI
from typing import Optional
from enum import Enum

# Создание объекта приложения.
app = FastAPI()


class EducationLevel(str, Enum):
    # Укажем значения с большой буквы, чтобы они хорошо смотрелись
    # в документации Swagger.
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образовани'

# Новый эндпоинт: приветствие для автора.


@app.get('/{name}')
def greetings(
        *,
        name: str,
        surname: str,
        age: Optional[int] = None,
        is_staff: bool = False,
        education_level: Optional[EducationLevel] = None,
) -> dict[str, str]:
    result = ' '.join([name, surname, education_level])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}


@app.get('/me')
def hello_author():
    return {'Hello': 'author'}
