from pydantic import BaseModel
class Item(BaseModel):
    x: float
    y: float

class Calculator:
    """
    Класс калькулятор
    Калькулятор выполняет 4 операции сумма, разность, деление и умножение
    """

    @classmethod
    def add(self, item:Item):
        return item.x + item.y

    def sub(self, item:Item):
        return item.x - item.y

    def mul(self, item:Item):
        return item.x * item.y

    def div(self, item:Item):
        return item.x / item.y
