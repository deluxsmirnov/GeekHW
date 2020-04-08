class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')



class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки и это {self.title}\n')

class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки, и это {self.title} его можно стереть ластиком\n')

class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки и это {self.title}. Он рисует яркими и толстыми цветами')

pen = Pen()
pen.title = 'ручка'
pen.draw()

penсil = Pencil()
penсil.title = 'карандаш'
penсil.draw()


handle = Handle()
handle.title = 'маркер'
handle.draw()