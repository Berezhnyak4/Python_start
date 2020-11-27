"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
 running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
 светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
 составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
  зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт."""
#OpenDataScience

from time import sleep


class TraffikLight:
    __color=["Красный", "Желтый", "Зеленый"]
    __time=[7,2,3] #добавил второй атрибут чтобы не указывать в ручную время
    def runnind(self):
        i=0
        while i < 3:
            print(f'Горит {TraffikLight.__color[i]}, {TraffikLight.__time[i]} секунд')
            if i == 0:
                sleep(TraffikLight.__time[i])
            elif i == 1:
                sleep(TraffikLight.__time[i])
            elif i == 2:
                sleep(TraffikLight.__time[i])
                i-=3
            i+=1
TraffikLight=TraffikLight()
TraffikLight.runnind()


"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
 Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать 
 защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного 
 полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
  асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""
class RoadtotheDreem():
    def __init__(self, leght, width):
        self.leght = leght
        self.wigth = width

    def mass(self):
        return f'{self.leght}m * {self.wigth}m * {self.volume}кг * {self.cm}см = {self.leght * self.wigth * self.volume * self.cm/1000} т'

class MassCount(RoadtotheDreem):
    def __init__(self, _length, _width, volume, cm):
        super().__init__(_length, _width)
        self.volume = volume
        self.cm = cm
road = MassCount(20, 5000, 25, 5)
print(road.mass())

"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
 position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на 
 словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать
  класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения 
  полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить 
  работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить
   значения атрибутов, вызвать методы экземпляров)."""
class Worker():
    pro_dict={"wage": 500, "bonus": 100}
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'
    def get_total_income(self):
        return f'Profit: {sum(self._income.values())}'
I = Position("Igor", "Spchkin", "pro", 500, 200)
print(I.position)
print(I.get_full_name())
print(I.get_total_income())
"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
 name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что
  машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, 
  SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
   текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
   При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении 
   скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
 выведите результат. Выполните вызов методов и также покажите результат."""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'Машина {self.name} поехала со скоростью {self.speed} км/ч'
    def stop(self):
        return f'Машина {self.name} остановилась'
    def turn_r(self):
        return f'Машина {self.name} повернула вправо'
    def turn_l(self):
        return f'Машина {self.name} повернула влево'
    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed} км/ч'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость выше 40 км/ч'
        else:
            return f'Машина {self.name} едет со скоростью {self.speed} км/ч'
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость выше 60 км/ч'
        else:
            return f'Машина {self.name} едет со скоростью {self.speed} км/ч'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'Внимание едет {self.name} полицейская машина!'
        else:
            return (f'Машина {self.name} не полицейская')
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 110:
            return f'Скорость выше 110 км/ч, притормози!'
        else:
            return f'Машина {self.name} едет со скоростью {self.speed} км/ч'
meren = SportCar(140, 'белый', 'новый мерен', False)
oka = TownCar(35, 'черная', 'ока', False)
lada = WorkCar(50, 'баклажан', 'лада-седан', True)
ford = PoliceCar(110, 'ментовской',  'форд', True)
print(lada.turn_l())
print(f'Когда {oka.turn_r()}, тогда {meren.stop()}')
print(f'{lada.go()}')
print(f'{lada.name} цвета {lada.color}')
print(f' {meren.name} полицейская тачка? {meren.is_police}')
print(f'А {lada.name}  полицейская тачка? {lada.is_police}')
print(meren.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
 title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” 
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из
  классов реализовать переопределение метода draw. Для каждого из классов методы должен 
  выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
   метод для каждого экземпляра."""
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Pensil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Делаем контур и тени'
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Делаем фон'
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Росчерк пера'
begin = Stationery('Шедевр')
pen = Pen("Подпись")
fon = Handle("Фон")
black = Pensil("Рисуем контуры")
print(begin.draw())
print(fon.draw())
print(black.draw())
print(pen.draw())


