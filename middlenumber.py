x=int(raw_input("Enter x: "))
y=int(raw_input("Enter y: "))
z=int(raw_input("Enter z: "))

if x<y and x>z:
    print x

if x>y and x<z:
    print x

if y<x and y>z:
    print y

if y>x and y<z:
    print y

if z>x and z<y:
    print z
if z<x and z>y:
    print z

raw_input()
