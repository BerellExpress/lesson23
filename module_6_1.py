class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def feed(self):
        self.fed = True

    def eat(self, food):
        if food.is_edible():
            print(f"{self.name} съел {food.name}")
            self.feed()
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


    def is_alive(self):
        return self.alive

    def is_fed(self):
        return self.fed

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

    def set_edibility(self, is_edible):
        self.edible = is_edible

    def is_edible(self):
        return self.edible


class Mammal(Animal):
    def feed(self):
        self.fed = True

    def eat(self, food):
        if food.is_edible():
            print(f"{self.name} съел {food.name}")
            self.feed()
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    pass

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)

    a1.eat(p1)
    a2.eat(p2)

    print(a1.alive)
    print(a2.fed)