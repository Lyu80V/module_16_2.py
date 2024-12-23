

import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/user/admin")                     #маршрут к главной странице
async def admin() -> str:
    return 'Вы вошли как администратор'

@app.get("/users/{user_id}")               #маршрут к страницам пользователей, используя параметр в пути
async def get_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user/{username}/{age}')                          #маршрут к страницам пользователей, передавая данные в адресной строке
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter username', example='24')]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

@app.get("/")                              #маршрут к главной странице
async def read_root() -> str:
    return 'Главная страница'


if __name__ == '__main__':
    uvicorn.run('module_16_2:app', host='127.0.0.1', port=8000, reload=True)
