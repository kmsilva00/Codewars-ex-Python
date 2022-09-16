arr = [1,2,3,4,6,7,8]

def first_non_consecutive(arr):
    for i in range(0,(len(arr)-1)):
        if arr[i] == arr[i+1]-1:
            continue
        return arr[i+1]
    return None

print(first_non_consecutive(arr))