class Cat:
    def __init__(self, weight, age, name, colour):
        self._name = name
        self._weight = weight
        self._age = age
        self._colour = colour

    def info(self):
        print(
            f"Meno: {self._name},"
            f"Vaha: {self._weight}, "
            f"Vek: {self._age}, "
            f"Farba: {self._colour}"
        )

class Cat(Animal):
    def __init__(self, name, weight, age, colour, lives=9):
        super().__init__(name, weight, age, colour)
        self._lives = lives

    def info(self):
        super().info()
        print(f"Zivoty: {self._lives}")

class Dog(Animal):
    def __init__(self, name, weight, age, colour, breed):
    super().__init__(name, weight, age, colour)
    self._breed = breed

cat = Cat("Jonas", 10, 5, "cierna", 4)
cat.info()
    