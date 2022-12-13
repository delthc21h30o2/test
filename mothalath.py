a=float (input("side1: "))
b=float (input("side2: "))
c=float (input("side3: "))

if a<b+c:
    d="ok"
elif b<a+c:
    d="ok"
elif c<a+b:
    d="ok"
else: "impossible"

print(d)