from fastapi import FastAPI
import uvicorn

# Создание объекта приложения.
app = FastAPI(docs_url='/swagger')


# Декоратор, определяющий, что GET-запросы к основному URL приложения
# должны обрабатываться этой функцией.
@app.get('/')
def read_root():
    return {'Hello': 'FastAPI'}



if __name__ == '__main__':
    # Команда на запуск uvicorn.
    # Здесь же можно указать хост и/или порт при необходимости,
    # а также другие параметры.
    uvicorn.run('main:app', reload=True)
