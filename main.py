#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
#(`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические
# методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#Дополнительно:Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке
# в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Chirp, chirp")

    def eat(self):
        print(f"{self.name} is eating seeds")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says: Grr, grr")

    def eat(self):
        print(f"{self.name} is eating meat")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says: Sss, sss")

    def eat(self):
        print(f"{self.name} is eating shellfish")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def animal_sound(self):
        for animal in self.animals:
            animal.make_sound()
            print(f"{animal.name} is {animal.age} years old")

    def save_zoo(self, filename):
        """Сохраняем состояние зоопарка в файл"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Zoo saved to {filename}.")

    @staticmethod
    def load_zoo(filename):
        """Загружаем состояние зоопарка из файла"""
        try:
            with open(filename, 'rb') as f:
                zoo = pickle.load(f)
            print(f"Zoo loaded from {filename}.")
            return zoo
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None




# Создаем зоопарк
zoo = Zoo()

# Добавляем животных
lion = Mammal("Lion", 5)
zebra = Mammal("Zebra", 4)
parrot = Bird("Parrot", 3)
snake = Reptile("Snake", 2)

zoo.add_animal(lion)
zoo.add_animal(zebra)
zoo.add_animal(parrot)
zoo.add_animal(snake)

# Сохраняем зоопарк в файл
zoo.save_zoo("zoo_state.pkl")

# Загружаем зоопарк из файла
loaded_zoo = Zoo.load_zoo("../../Users/rnats/PycharmProjects/zoo/zoo_state.pkl")

# Проверка загруженного состояния зоопарка
if loaded_zoo:
    loaded_zoo.animal_sound()
