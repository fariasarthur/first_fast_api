from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from first_fast_api.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá, tabacudo'}


@app.get('/secundario', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    message_html = """
    <html>
        <head>
            <title>CHAMUYEIRO</title>
        </head>
        <body>
            <h1>SOY ASI UN TABACUDO</h1>
        </body>
    </html>
    """

    return message_html
