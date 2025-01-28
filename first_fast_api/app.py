from http import HTTPStatus

from fastapi import FastAPI

from first_fast_api.schemas import UserDB, UserPublic, UserSchema

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
