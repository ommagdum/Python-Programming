# Write a program to overload + operator to add two complex numbers C1 and C2 and store the result in C3
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overloading the + operator
    def __add__(self, other):
        # Adding real parts and imaginary parts separately
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return Complex(real_part, imaginary_part)

    def __str__(self):
        # Formatting the complex number as a string
        return f"{self.real} + {self.imaginary}i"

# Example usage
C1 = Complex(3, 2)
C2 = Complex(1, 7)

# Adding two complex numbers using overloaded + operator
C3 = C1 + C2

# Display the result
print("C1 =", C1)
print("C2 =", C2)
print("C3 = C1 + C2 =", C3)
