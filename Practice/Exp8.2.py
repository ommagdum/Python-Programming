'''Write a program which infinitely prints natural numbers in
given range. Raise the StopIteration exception after
displaying first 10 numbers to exit from the program.'''

try:
    start_range = int(input("Enter Start Of The Range (Other Than 0) : "))
    end_range = int(input("Enter End Of The Range : "))
    count = 0
    for i in range(start_range, end_range+1):
        print(i)
        count += 1
        if(count == 10): raise StopIteration("Displayed The First 10 Numbers.")

except StopIteration as e:
    print(f"Error : {e}")
    