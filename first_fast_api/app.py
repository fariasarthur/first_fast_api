from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from first_fast_api.schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump(),  # transformando user em dicionário
    )

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_users(user: UserSchema, user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(
        id=user_id,
        **user.model_dump(),  # transformando user em dicionário
    )

    database[user_id - 1] = user_with_id
