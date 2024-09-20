from fastapi import FastAPI

from routes import init_routes

import uvicorn

app = FastAPI()

@app.get('/ola')
def hello():
    return 'testee'

init_routes(app)

if __name__ == '__main__':

    uvicorn.run(app, host='0.0.0.0' , port=8000)

    """abra http://127.0.0.1:8000/docs e http://127.0.0.1:8000/redoc"""
    """rodar aplicação: uvicorn main: app --reload """
