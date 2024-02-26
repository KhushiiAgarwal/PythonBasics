def fibb(numt):
    if(numt==1):
        return 1
    if(numt<0 or numt==0 ):
        return 0
    else:
        return(fibb(numt-1)+fibb(numt-2))
num=int(input("Enter a num: "))
fib=fibb(num)
print(fib)


