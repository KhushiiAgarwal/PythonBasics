# You have a apples and b bananas, you wonder how many fruits you have in total.

#Input: The first line has two space separated numbers: a and b
# Output: single line containing the total number of fruits you have
# Constraints
# 1 <= a <= 100
# 1 <= b <= 100

a,b= map(int, input().split())
if 1<=a<=100 and 1<=b<=100:
    print(a+b)
