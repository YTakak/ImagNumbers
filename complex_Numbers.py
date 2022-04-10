"""
This code is developed to implement complex number operations
Currently addition, substraction, division and multiplication functions in the rectangular form are available.
But other properties like arithmetics in polar form will also be implemented. Conjugation, matrix operations are other functionality that will be added soon  
"""
class cmplxNumber:
    '''Generates a Complex Number with complexNumber(real,imag) i.e real + imag*i'''
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

def add(num1, num2):   
    '''Adds Two Complex Numbers with and returns output'''
    real = num1.real + num2.real
    imag = num1.imag + num2.imag
    return cmplxNumber(real,imag)

def substract(num1,num2):
    '''Substracts Two Complex Numbers (num1,num2) and returns output (num1-num2)'''
    real = num1.real - num2.real
    imag = num1.imag - num2.imag
    return cmplxNumber(real,imag)     

def multiply(num1,num2):  
    '''Multiplies Two Complex Numbers (num1,num2) and returns output (num1*num2)'''  
    real = num1.real*num2.real - num1.imag*num2.imag 
    imag = num1.real*num2.imag + num1.imag*num2.real 
    return cmplxNumber(real,imag)    

def divide(num1,num2):
    '''Divides Two Complex Numbers (num1,num2) and returns output (num1/num2)'''  
    if(num2.real == 0 & num2.imag==0):
        raise ValueError("divide by zero error!!")
    else:
        real = round((num1.real*num2.real + num1.imag*num2.imag) / (num2.real**2 + num2.imag**2) ,4)
        imag = round((num1.imag*num2.real - num1.real*num2.imag) / (num2.real**2 + num2.imag**2) ,4)
        return cmplxNumber(real,imag)  