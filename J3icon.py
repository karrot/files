k=int(raw_input("Enter k: "))


x="x"
star="*"
space=" "


for i in range(0,k):
    print star*k+x*k+star*k
for i in range(0,k):
    print space*k+x*k+x*k
for i in range(0,k):
    print star*k+space*k+star*k
