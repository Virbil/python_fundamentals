arr = [9,6,7,1,5,3,2,0,4,8]

def selection_sort(arr):
    
    for i in range(len(arr)):
        # isolates the first value to compare to the rest of the list
        min_index = i
        for j in range(i, len(arr)):
            # find the lowest number in the rest of the list
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(arr))