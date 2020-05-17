from random import choice

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        police_car = ''
        if self.is_police == True:
            return f'Машина марки {self.name} цветом {self.color} поехала и она полицейская'
        else:
            return f'Машина марки {self.name} цветом {self.color} поехала и она не полицейская'


    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self):
        direction = ['влево', 'вправо']
        return f'Машина {self.name} повернула {choice(direction)}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Машина превысила скорость 60, текущая скорость {self.speed}"

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Машина превысила скорость 40, текущая скорость {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


sportcar = SportCar(180, 'red', 'ferrari', False)
print(sportcar.go())
print(sportcar.show_speed())
print(sportcar.turn())
print(sportcar.stop())

print()

police = PoliceCar(180, 'white-blue', 'lada', True)
print(police.go())
print(police.show_speed())
print(police.turn())
print(police.stop())

print()

car_town = TownCar(80, 'Black', 'BMW', False)
print(car_town.go())
print(car_town.show_speed())
print(car_town.turn())
print(car_town.stop())


print()

car_work = WorkCar(88, 'white-blue', 'Honda', False)
print(car_work.go())
print(car_work.show_speed())
print(car_work.turn())
print(car_work.stop())