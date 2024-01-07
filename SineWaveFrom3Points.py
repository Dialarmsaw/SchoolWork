x1 = float(input("Give x1 >>> "))
y1 = float(input("Give y1 >>> "))

x2 = float(input("Give x2 >>> "))
y2 = float(input("Give y2 >>> "))

x3 = float(input("Give x3 >>> "))

A = (y1-y2)/2

B = x3 - x1

C = x1 - (B/2)

D = (y1+y2)/2

print("y=", A, "sin(2pi/", B, "(x-", C, ")) +", D)
