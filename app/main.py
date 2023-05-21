import os

from fastapi import FastAPI, APIRouter
from pydantic.types import Optional
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()

# Init FastAPI
app = FastAPI()
router = APIRouter(prefix='/api')

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Database
str_conn = "mysql+pymysql://"+db_user+":"+db_password+"@"+db_host+":"+db_port+"/"+db_name
engine = create_engine(str_conn)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()

# Database Model
Vehicle = Table(
    "vehicle",
    meta,
    Column("id", Integer, primary_key=True),
    Column("plat_number", String(10)),
    Column("description", String(100)),
    Column("status", Integer),
    Column("type", String(10))
)

meta.create_all(engine)
#conn = engine.connect()
conn = SessionLocal()

# Models
class VehicleModel(BaseModel):
    id: Optional[int]
    plat_number: str
    description: str
    status: Optional[int]
    type: str

# Routes
@router.get("/vehicle")
async def get_all():
    items = conn.execute(Vehicle.select()).fetchall()
    response = []
    for vehicle in items:
        response.append({
            "id": vehicle.id,
            "plat_number": vehicle.plat_number,
            "description": vehicle.description,
            "status": vehicle.status,
            "type": vehicle.type,
        })
    return response

@router.get("/vehicle/{vehicle_id}")
async def get(vehicle_id: int):
    result = conn.execute(
        Vehicle.select().where(Vehicle.c.id == vehicle_id)
    ).first()

    return {
        "id": result.id,
        "plat_number": result.plat_number,
        "description": result.description,
        "status": result.status,
        "type": result.type,
    }

@router.post("/vehicle")
async def create(vehicle_obj: VehicleModel):
    new_vehicle = {
        "plat_number": vehicle_obj.plat_number,
        "description": vehicle_obj.description,
        "status": 1,
        "type": vehicle_obj.type,
    }

    query = conn.execute(Vehicle.insert().values(new_vehicle))
    conn.commit()
    result = conn.execute(
        Vehicle.select().where(Vehicle.c.id == query.lastrowid)
    ).first()

    return {
        "id": result.id,
        "plat_number": result.plat_number,
        "description": result.description,
        "status": result.status,
        "type": result.type,
    }

app.include_router(router)

# TODO: Consultar todos los vehiculos [GET]
# TODO: Crear vehiculos [POST]
# TODO: Consultar un vehiculo [Buscar por id]
# TODO: Consultar un vehiculo [Buscar por placa]
# TODO: Editar vehiculos [PUT]