def factorial(n):
    return reduce(lambda x,y:x*y,[1]+range(1,n+1))
    
j=int(raw_input("Enter j: "))

if j<4:
    print "0"

else:
    nf=factorial(j)
    r=factorial(4)
    nr=factorial(j-4)
    print nf/nr*r
    
