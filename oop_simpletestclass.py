class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hello", self.name)

    @classmethod
    def how_many(cls):
        print('How many is there?')


p = Person('Soikat')
print(p.say_hi())
