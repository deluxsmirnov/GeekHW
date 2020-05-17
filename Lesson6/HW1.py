from time import sleep
from termcolor import colored

class TrafficLight:
    __color = ''
    def traffic_light(self):
        i = 0
        while i < 80:
            print(colored('Загорелся красный цвет сфетофора', 'red'))
            sleep(7)
            print(colored('Загорелся желтый цвет сфетофора', 'yellow'))
            sleep(2)
            print(colored('Загорелся зеленый цвет сфетофора', 'green'))
            sleep(7)
            print(colored('Загорелся желтый цвет сфетофора', 'yellow'))
            sleep(2)
            i += 1


go = TrafficLight()
go.traffic_light()

