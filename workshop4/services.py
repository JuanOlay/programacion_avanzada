import uvicorn 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String ,select 
from sqlalchemy.orm import sessionmaker 
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware #se importa la libreria para poder hacer peticiones desde cualquier origen

app = FastAPI()

#se agrega el middleware para permitir peticiones desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

#se hizo comentario la base de datos para que no de problemas
"""
engine = create_engine('postgresql://postgres:postgres@localhost:5432/public')
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))
"""
#se elimino app=FasApi() repetido

# Datos de ejemplo para productos
products = [
    {"id": 1, "name": "Producto 1", "description": "Descripción del producto 1"},
]

#se cambio el nombre de la raiz para que no haya problemas al acceder
@app.get("/get_products")
def get_products():
    # se hace comentario para no haber problemas de llamados al no estar algunos obketos o funciones de la bases de datos
    """
    query = products.select()
    result = session.execute(query)
    products = result.fetchall()
    """
    return products

@app.post("/products")
def create_product(name: str, description: str):
    # se hace comentario para no haber problemas de llamados al no estar algunos obketos o funciones de la bases de datos
    """
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    """
    return {"message": "Product created successfully"}
    
if __name__ == "__main__":
    #se cambio el puerto porque salia ocupado o sin permisos con el comando netstat -an para identificar cuales estan libres
    uvicorn.run(app, host="0.0.0.0", port=3702)
