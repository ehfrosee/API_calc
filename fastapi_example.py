from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from calculator import Calculator, Item

#count = 0
# аннотации типов
# класс с типами данных параметров 

clc = Calculator()

# создаем объект приложения
app = FastAPI()

# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:5000/
@app.get("/")
def root():
    #count += 1
    return {"message": "Hello FastAPI"}

# функция, которая обрабатывает запрос по пути "/about"
@app.get("/about")
def about():
    return {"message": "Страница с описанием проекта"}

# функция-обработчик с параметрами пути
@app.get("/users/{id}")
def users(id):
    return {"user_id": id}

# функция-обработчик post запроса с параметрами
@app.post("/add")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.add(item)}

@app.post("/sub")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.sub(item)}

@app.post("/mul")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.mul(item)}

@app.post("/div")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.div(item)}
