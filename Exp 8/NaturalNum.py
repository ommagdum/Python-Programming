# Write a program which infinitely prints natural numbers in given range. 
# Raise the StopIteration exception after displaying first 10 numbers to exit from the program. 
class NaturalNumbers:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 10:
            raise StopIteration("Reached 10 numbers. Stopping iteration.")
        if self.current <= self.end:
            self.count += 1
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration("End of range reached.")

# Prompt user for range input
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create an iterator instance and print the first 10 numbers
try:
    natural_numbers = NaturalNumbers(start, end)
    for num in natural_numbers:
        print(num)
except StopIteration as e:
    print(e)