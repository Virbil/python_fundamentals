arr = [9,6,7,1,5,3,2,0,4,8]

def insertion_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr)-1-j):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(insertion_sort(arr))