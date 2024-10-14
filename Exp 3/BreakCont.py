# Demonstrating break, continue, and pass
for i in range(1, 11):
    if i == 5:
        pass  # Do nothing when i is 5, just pass
        print(f"Pass statement executed at i={i}")
    elif i == 7:
        continue  # Skip the rest of the loop when i is 7
    elif i == 9:
        break  # Exit the loop when i is 9
    
    print(f"Current value of i: {i}")