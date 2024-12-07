from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from calculator import Calculator, Item

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

# функция-обработчик post запроса сложение
@app.post("/add")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.add(item)}

# функция-обработчик post запроса вычитание
@app.post("/sub")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.sub(item)}

# функция-обработчик post запроса умножение
@app.post("/mul")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.mul(item)}

# функция-обработчик post запроса деление
@app.post("/div")
def get_model(item: Item):
    return {"x": item.x, "y": item.y, "result": clc.div(item)}
