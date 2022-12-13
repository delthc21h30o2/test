import math


print("Hello welcome to calculator")
print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sqrt")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")
print("enter your choice")

op= input() 

if op== "+" or op== "-" or op== "*" or op== "/" :
    a= int(input("enter first number: "))
    b= int(input("enter second number: "))

else: a=int(input("enter the number: "))


if op== "+": 
    ans= a+b

elif op== "-":
    ans= a-b

elif op== "*":
    ans= a*b

elif op== "/":

    if b== 0:
        ans=("not number")
    else:
        ans= a/b
 
    
elif op== "sqrt":
    ans= math.sqrt(a)

elif op== "sin":
    a=a*math.pi/180
    ans= math.sin(a)

elif op== "cos":
    a=a*math.pi/180
    ans= math.cos(a)

elif op== "tan":
    a=a*math.pi/180
    ans= math.tan(a)

elif op== "cot":
    a=a*math.pi/180
    ans= math.cos(a) / math.sin(a)

elif op== "factorial":
    ans= math.factorial(a)

print(ans)

