class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def i_love_koalas(self):
        return 'koala'
    # def __init__(self, name, breed):
    #     # Calls the superclass's __init__ method to set up 'name'
    #     super().__init__(name)
    #     self.breed = breed

cj=Dog('bob')
print(cj.i_love_koalas())