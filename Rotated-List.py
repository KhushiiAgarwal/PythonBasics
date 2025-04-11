#To rotate a list (or array) n times by k positions, 
# l = [1,2,3,4,5]
# l = input("Enter list: ").split()

def rotate_list(arr, k):
    l = len(arr)
    if l == 0 or l == 1:
        return arr
    # Reduce k to avoid unnecessary rotations
    k = k % l  # In case k > n
    rotated_list = arr[-k:] + arr[:-k]
    
    return rotated_list
l = list(map(int,input("Enter list:").split()))
n=int(input(("Enter value of n"))) #number of rotations
k=int(input(("Enter value of k"))) #positions to rotate per rotation
x = n*k
final = rotate_list(l,x)

print(final)
