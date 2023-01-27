from abc import abstractmethod
import time


class Auto:
    brand = "brand"
    age = 0
    color = ""
    mark = ""
    weight = 0

    def __init__(self, brand, age, color="white", mark="stock", weight=3500):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @abstractmethod
    def move(self):
        print("MOVE")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        return self.age


class Truck(Auto):
    max_load = 3500

    def move(self):
        print("Attention!")
        super().move()

    pass

    def load(self):
        time.sleep(1)
        print("load...")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, max_speed, color="white", mark="stock", weight=3500):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max speed is {self.max_speed}')


my_truck = Truck("MAN", 7)
friends_truck = Truck("Mercedes", 3, color="black")
print("\nПерегрузка оператора move: ")
my_truck.move()
print("\nДобавили атрибут load: ")
friends_truck.load()
print("\nУнаследованный атрибут stop: ")
my_truck.stop()

my_car = Car("Audi", 13, 240, mark="TT")
dads_car = Car("Volvo", 9, 180, color="gray")
print(f'Моей {my_car.color} {my_car.brand} {my_car.mark} исполнилось {my_car.birthday()}!')
print("\nПерегрузка оператора move: ",)
dads_car.move()
