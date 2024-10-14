'''Write a Python function that takes two lists and returns True if they have at least one common member.'''
list1 = [ ]
list2 = [ ]

size1 = int(input("Enter List Size For List 1 : "))
print(f"Input {size1} Elements For List 1 : ")
for i in range(0, size1):
    ele = input()
    list1.append(ele)

size2 = int(input("Enter List Size For List 2 : "))
print(f"Input {size2} Elements For List 2 : ")
for i in range(0, size2):
    ele = input()
    list2.append(ele)

def commonElement(a,b):
    result = False
    for x in a:
        for y in b:
            if x==y:
                result = True
                return result
    return result

print(f"List 1 : {list1}")
print(f"List 2 : {list2}")


if(commonElement(list1, list2)):
    print("Both The Lists Have At Least One Common Element")
else:
    print("Both The Lists Don't Have At Least One Common Element")
