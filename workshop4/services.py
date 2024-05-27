import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String ,select
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"


engine = create_engine('postgresql://postgres:postgres@localhost:5432/public')
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

#se elimino app=FasApi() repetido

#se cambio el nombre de la raiz para que no haya problemas al acceder
@app.get("/get_products")
def get_products():
    # Usé select() en lugar de products.select()
    query = select(products)
    result = session.execute(query)
    products_list = result.fetchall()
    # Convertí los resultados a una lista de diccionarios
    return [{"id": product.id, "name": product.name, "description": product.description} for product in products_list]

@app.post("/products")
def create_product(name: str, description: str):
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    #se cambio el puerto porque salia ocupado o sin permisos con el comando netstat -an para identificar cuales estan libres
    uvicorn.run(app, host="0.0.0.0", port=3702)