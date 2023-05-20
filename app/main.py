from typing import Union

from fastapi import FastAPI

from config.migrations.vehicles_migration import migrate

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id, "q": q
    }

@app.get("/migration")
def migration():
    migrate()



@app.get("/vehicles")
def index():
    return [
        {'a': 'Item 1'},
        {'b': 'Item 2'},
        {'c': 'Item 3'},
        {'d': 'Item 4'},
    ]

# conn = connection.conn

# TODO: Consultar todos los vehiculos [GET]
# TODO: Crear vehiculos [POST]
# TODO: Consultar un vehiculo [Buscar por id]
# TODO: Consultar un vehiculo [Buscar por placa]
# TODO: Editar vehiculos [PUT]
