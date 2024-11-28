class Animal:
    
    alive = True

    def eat(self):
        print("This Animal Is Eating")

    def sleep(self):
        print("This Animal Is Sleeping")

class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

fish.eat()
hawk.sleep()