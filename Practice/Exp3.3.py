# Demonstrate use of break, continue and pass

for i in range(1, 11):
    if i > 5:
        break

    print(i)

for i in range(1, 11):

    if i == 5:
        pass 
        print(f"Pass Executed at {i}th iteration")
    

for i in range(1, 11):
    if i % 2 != 0:
        continue
    else:
        print(i)