class Road:
    """Если не знать, что используется защита, то выводится будет всегда 0 и не будет ошибки"""
    _lenght = 0
    _width = 0
    def formula(self):
        return f'При длине полотна {self._lenght}м и ширине {self._width}м с учётом массы асфальта 25кг и толщиной 5см расход асфальта = {self._lenght * self._width * 25 * 5}т'

obj = Road()
obj._width = 20
obj._lenght = 30

print(obj.formula())
