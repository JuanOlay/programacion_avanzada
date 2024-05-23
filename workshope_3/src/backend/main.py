"""This file  has theentry point implementtion for RESTapi services."""
from fastapi import FastAPI
from workshop1 import Vehiculo, Motor

app = FastAPI()

@app.get("/")
async def read_root():
    """This service lets get the root of the API"""

    return {"Hello": "World"}

@app.post("/new_engine")
def new_engine(engine : Motor):
    engine_json = engine.to_json()
    Motor.crear_motor(engine_json)

    
@app.post("new_vehicle")
def save_vehicle(vehicle : Vehiculo):
    vehicle_json = vehicle.to_json()
    Vehiculo.crear_vehiculo(vehicle_json)

@app.get("/view_engines")
def view_eengines():
    """This service lets view all events"""
    return Motor.engines

@app.get("/view_engines")
def view_eengines():
    """This service lets view all events"""
    return Motor.engines
