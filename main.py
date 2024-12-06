from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from calculator import Calculator, Item
import requests

# count = 0
# аннотации типов
# класс с типами данных параметров

clc = Calculator()

payload = {"x": 11, "y": 12}
response = requests.post("http://127.0.0.1:5000/add", json=payload)
print(response.text)

payload = {"x": 15, "y": 12}
response = requests.post("http://127.0.0.1:5000/sub", json=payload)
print(response.text)

payload = {"x": 15, "y": 2}
response = requests.post("http://127.0.0.1:5000/mul", json=payload)
print(response.text)

payload = {"x": 15, "y": 5}
response = requests.post("http://127.0.0.1:5000/div", json=payload)
print(response.text)
