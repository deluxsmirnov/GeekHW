class Worker:
    def __init__(self, name, surname, positional, __income):
        self.name = name
        self.surname = surname
        self.positional = positional
        self.__income = __income

class Rectangle(Worker):
    def __init__(self, name, surname, positional, __income):
        super().__init__(name, surname, positional, __income)

    def get_full_name(self):
        print(self.name)

    def get_total_income(self):
        sum = self._Worker__income
        print (int(sum['wage']) + int(sum['bonus']))


Serezha = Rectangle('Serezha', 'Kukushka', 'engener', {'wage': 20000, 'bonus': 10000})
Serezha.get_full_name()
Serezha.get_total_income()


Oleg = Rectangle('Oleg', 'Galashov', 'engener', {'wage': 35000, 'bonus': 14000})
Oleg.get_full_name()
Oleg.get_total_income()


