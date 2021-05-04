arr = [9,6,7,1,5,3,2,0,4,8]

def selection_sort(arr):
    
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)-1):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(arr))