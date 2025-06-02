#Remove all non-digit char and check if sum is prime.
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)):
        if(num%i == 0):
            return False
    return True

str = input()
sum = 0
for i in str:
    if i.isdigit():
        sum = sum + int(i)
res = isprime(sum)       
print(res)
