def fact(numt):
    if(numt==1 or numt==0 or num<0):
        return 1
    return(numt*fact(numt-1))
num=int(input("Enter a num: "))
fac=fact(num)
print(fac)
