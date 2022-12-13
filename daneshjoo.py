from lib2to3.pgen2.token import GREATER
from locale import normalize


name=input("enter your name   ")
lastname=input("enter your lastname   ")
city=input("enter your city   ")
s1=float(input("input s1: "))
s2=float(input("input s2: "))
s3=float(input("input s3: "))

ave = (s1 + s2 + s3)/3

if ave>17:
    m= "great"
elif 17>ave>12:
    m="normal"
elif ave<12:
    m="fail"

print("Hello ", name, lastname, "from", "your average is: ", ave, "you are ", m)