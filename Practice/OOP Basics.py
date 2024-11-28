
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" Is Driving")

    def stop(self):
        print("This "+self.model+" is Stopped")


car_1 = Car("Maruti Suzuki","BREZZA","2023","Arctic Pearl White")
car_2 = Car("Mahindra", "XUV 700", "2024", "Jasper Red")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive() 
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive() 
car_2.stop()