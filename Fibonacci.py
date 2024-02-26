num1=1
num0=0
fib=0
def fibb(numt):
    global num1,num0

    for i in range(numt):
        fib=num1+num0
        num0=num1
        num1=fib
        print(fib)
num=int(input("Enter a num: "))
fibb(num)



