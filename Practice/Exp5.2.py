'''Write a Python function that takes two lists and returns True
if they have at least one common member.'''

def CommonMember():
    l1 = []
    l1_size = int(input("Enter Size Of List 1 : "))
    print(f"Enter {l1_size} Elements : ")
    for i in range (1, l1_size + 1):
        item = input(">")
        l1.append(item)

    l2 = []
    l2_size = int(input("Enter Size Of List 2 : "))
    print(f"Enter {l2_size} Elements : ")
    for i in range (1, l2_size + 1):
        item = input(">")
        l2.append(item)

    for i in l1:
        for j in l2:
            if i == j:
                print("True")


CommonMember()
    
