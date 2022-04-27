import decimal
import numpy as np
from scipy import optimize
import sys

# Implementation des Schulrundens
def round_school(n, digits=0):
    return float(decimal.Decimal(n*10**digits).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))/10**digits

def f(x):
    return a*x**3+b*x**2+c*x+d

# f_2 ist die zweite Ableitung von f
def f_2(x):
    return a*x*6+b*2

def Beispiel1():
    result = optimize.newton(f_2,10)
    result = round_school(result, 2)
    print(result)

def Beispiel2():
    result = optimize.newton(f_2,10)
    result = f(result)
    result = round_school(result)
    print(int(result))

# Beispiel drei wird mit Matplotlib gerendert und dann abgebildet
#def Beispiel3():


if len(sys.argv) < 6:
    print("not enough arguments")
    quit()

try:
    a,b,c,d = [float(coefficient) for coefficient in sys.argv[2:]]
except:
    print("wrong input")
    quit()

if sys.argv[1] == "1":
    Beispiel1()
elif sys.argv[1] == "2":
    Beispiel2()
else:
    print("falsche Beispiel Nummer")