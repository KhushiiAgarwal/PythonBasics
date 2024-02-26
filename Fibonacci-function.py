def fibb(numt):
    if numt == 1:
        return [1]
    elif numt < 0 or numt == 0:
        return []
    else:
        series = fibb(numt - 1)
        series.append(sum(series[-2:]))
        return series

num = int(input("Enter a num: "))
fib_series = fibb(num)
print("Fibonacci Series:", fib_series)
