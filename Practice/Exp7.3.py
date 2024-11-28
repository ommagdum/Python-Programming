'''Write a program to overload + operator to add two complex numbers
C1 and C2 and store the result in C3'''

class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imaginary + other.imaginary
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    

C1 = Complex(2,3)
C2 = Complex(1,4)
C3 = C1 + C2

print(f"C1 : {C1}")
print(f"C2 : {C2}")
print(f"C1 + C2  = {C3}")