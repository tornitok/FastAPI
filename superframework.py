from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class PrompterHint(BaseModel):
    actor: str
    replica: str

    class Config:
        schema_extra = {
            'examples': {
                'single_surname': {
                    'summary': 'Одна фамилия',
                    'description': 'Одиночная фамилия передается строкой',
                    'value': {
                        'actor': 'Медведь',
                        'replica': 'Колобок, колобок, я тебя съем!',
                    },
                },
                'multiple_surnames': {
                    'summary': 'Несколько фамилий',
                    'description': 'Несколько фамилий передаются списком',
                    'value': {
                        'actor': 'Гамлет',
                        'replica': 'Бедный Йорик! Я знал его, Горацио.',
                    },
                },
                'invalid': {
                    'summary': 'Некорректный запрос',
                    'description': 'Возраст передается только целым числом',
                    'value': {
                        'actor': 'Рагин',
                        'replica': 'Покой и довольство человека не вне его, а в нём самом.',
                    },
                },
            }
        }


@app.post('/give-a-hint')
def send_prompt(
    hint: PrompterHint = Body(
        ..., examples=PrompterHint.Config.schema_extra['examples']
    )
) -> dict:
    return hint.dict()
