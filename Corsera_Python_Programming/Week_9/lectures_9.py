#=====================================================================================
#class Complex:
#    def __init__(self, re=0, im=0):
#        self.re = re
#        self.im = im
#    def __str__(self):
#        return str(self.re) + '+' + str(self.im) + 'i'
#    def __add__(self, other):
#        result = Complex(self.re + other.re, self.im + other.im)
#        return result
#    def __mul__(self, other):
#        if isinstance(other, Complex):
#            re = self.re * other.re - self.im * other.im
#            im = self.re * other.im + other.re * self.im
#        elif isinstance(other, int) or isinstance(other, float):
#            re = self.re * other
#            im = self.im * other
#        return Complex(re, im)
#a = Complex()
#b = Complex(1, 1)
#c = Complex(2, 3)
#print(b * 1.2)
#=====================================================================================
#class Complex:
#    def __init__(self, re=0, im=0):
#        self.re = re
#        self.im = im
#    def __str__(self):
#        return str(self.re) + '+' + str(self.im) + 'i'
#    def __add__(self, other):
#        result = Complex(self.re + other.re, self.im + other.im)
#        return result
#    def __mul__(self, other):
#        if isinstance(other, Complex):
#            re = self.re * other.re - self.im * other.im
#            im = self.re * other.im + other.re * self.im
#        elif isinstance(other, int) or isinstance(other, float):
#            re = self.re * other
#            im = self.im * other
#        return Complex(re, im)
#    __rmul__ = __mul__
#a = Complex()
#b = Complex(1, 1)
#c = Complex(2, 3)
#print(2 * b)
#=====================================================================================
#class ComplexError(BaseException):
#    def __init__(self, complex, other):
#        self.first = complex
#        self.second = other
#class Complex:
#    def __init__(self, re=0, im=0):
#        self.re = re
#        self.im = im
 #   def __str__(self):
#        return str(self.re) + '+' + str(self.im) + 'i'
#    def __add__(self, other):
#        result = Complex(self.re + other.re, self.im + other.im)
#        return result
#    def __mul__(self, other):
#        if isinstance(other, Complex):
#            re = self.re * other.re - self.im * other.im
#            im = self.re * other.im + other.re * self.im
#        elif isinstance(other, int) or isinstance(other, float):
#            re = self.re * other
#            im = self.im * other
#        else:
#            error = ComplexError(self, other)
#            raise error
#        return Complex(re, im)
#    __rmul__ = __mul__
#class Point(Exception):
 #   def lenght(self):
 #       return(self.re**2 + self.im**2)**0.5
#a = Complex()
#b = Complex(1, 1)
#c = Complex(2, 3)
#try:
#    print(1.2 * b)
#except ComplexError as ce:
#    print('Multiolication Error, first param:', ce.first,
#          'second param: ', ce.second, sep = '')
#=====================================================================================
class ComplexError(BaseException):
    def __init__(self, complex, other):
        self.first = complex
        self.second = other
class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __str__(self):
        return str(self.re) + '+' + str(self.im) + 'i'
    def __add__(self, other):
        result = Complex(self.re + other.re, self.im + other.im)
        return result
    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + other.re * self.im
        elif isinstance(other, int) or isinstance(other, float):
            re = self.re * other
            im = self.im * other
        else:
            error = ComplexError(self, other)
            raise error
        return Complex(re, im)
    __rmul__ = __mul__
class Point(Complex):
    def lenght(self):
        return(self.re**2 + self.im**2)**0.5
    def __str__(self):
        return str((self.re, self.im))
p1 = Complex(1, 1)
print(p1)


































