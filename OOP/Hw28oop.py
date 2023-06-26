# Создать класс и вызвать пять объектов этого класса.
class Auto:
    def __init__(self, model, name):
        self.model=model
        self.name=name
    def data1(self):
        print('ваш выбор это автомобиль '+self.model+' марки '+self.name)
auto1=Auto('q7','audi')
auto1.data1()
auto2=Auto('m3',"BMW")
auto2.data1()
auto3=Auto('ceed','KIA')
auto3.data1()
auto4=Auto('H3','HAMMER')
auto4.data1()
auto5=Auto('camaro','chevrolet')
auto5.data1()