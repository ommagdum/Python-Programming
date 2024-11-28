'''Write a python program to create a list and perform the
following methods :-a) insert () b) remove () c) append ()
d) len() e) pop() (f) extend()(g) reverse() (h)sort()'''

carList = ['Brezza', 'XUV 700', 'Compass', 'Octavia', 'Superb', 'Virtus']
print(f"Car List : {carList}")

addCar = input("Enter Car To Add : ")
addCar_pos = int(input("Enter Position of Car To Add : "))
carList.insert(addCar_pos, addCar)
print(f"Car List : {carList}")

removeCar = input("Enter Car To Remove : ")
carList.remove(removeCar)
print(f"Car List : {carList}")

appendCar = input("Enter Car To Append : ")
carList.append(appendCar)
print(f"Car List : {carList}")

print(f"Number Of Cars : {len(carList)}")

popCar = int(input("Enter Car Number To Pop : "))
carList.pop(popCar-1)

carList2 = ['Creta', 'Alcazar', 'Verna', 'Sonnet', 'Seltos']
print(f"2nd Car List : {carList2}")

carList.extend(carList2)
print(f"Final Car List : {carList}")

carList.reverse()
print(f"Car List In Reverse: {carList}")
carList.sort()
print(f"Car List Sorted: {carList}")
