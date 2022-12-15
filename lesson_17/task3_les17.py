def greatest_common_divisor(a, b):
    while a % b != 0:
        new_a = a
        new_b = b
        a = new_b
        b = new_a % new_b
    return b


class Fraction:
    def __init__(self, top, bottom):
        if not isinstance(top, int):
            raise TypeError('The top number must be an integer')
        elif not isinstance(bottom, int):
            raise TypeError('The bottom number must be an integer')
        elif bottom == 0:
            raise ZeroDivisionError("The bottom number of a Fraction can't be a zero")
        else:
            self.top = top
            self.bottom = bottom

    def __str__(self):
        return f'{self.top}/{self.bottom}'

    def __add__(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        gcd = greatest_common_divisor(new_top, new_bottom)
        return Fraction(new_top//gcd, new_bottom//gcd)

    def __sub__(self, other):
        new_top = self.top * other.bottom - self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        gcd = greatest_common_divisor(new_top, new_bottom)
        return Fraction(new_top // gcd, new_bottom // gcd)

    def __mul__(self, other):
        new_top = self.top * other.top
        new_bottom = self.bottom * other.bottom
        gcd = greatest_common_divisor(new_top, new_bottom)
        return Fraction(new_top // gcd, new_bottom // gcd)

    def __truediv__(self, other):
        new_top = self.top * other.bottom
        new_bottom = self.bottom * other.top
        gcd = greatest_common_divisor(new_top, new_bottom)
        return Fraction(new_top // gcd, new_bottom // gcd)

    def __eq__(self, other):
        first_n = self.top * other.bottom
        second_n = other.top * self.bottom
        return first_n == second_n

    def __lt__(self, other):
        first_n = self.top * other.bottom
        second_n = other.top * self.bottom
        return first_n < second_n

    def __gt__(self, other):
        first_n = self.top * other.bottom
        second_n = other.top * self.bottom
        return first_n > second_n


x = Fraction(1, 2)
y = Fraction(1, 4)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x + y == Fraction(3, 4))
print(x + y > Fraction(3, 4))
print(x + y < Fraction(3, 4))
