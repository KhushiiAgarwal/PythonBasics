#To rotate a list (or array) n times by k positions, 
l = [1,2,3,4,5]
total = 5
n=3
k=2
x = n*k
def rotate_list(arr, k):
    n = len(arr)
    
    # If the list is empty or contains one element, no rotation needed
    if n == 0 or n == 1:
        return arr
    
    # Reduce k to avoid unnecessary rotations
    k = k % n  # In case k > n
    
    # Rotate using slicing
    rotated_list = arr[-k:] + arr[:-k]
    
    return rotated_list
