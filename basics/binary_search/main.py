

# iterative binary search

def binary_search(arr , target):
    left , right = 0 , len(arr)-1

    while (left <= right ):
        mid = left + right // 2 

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    
    return -1 


def binary_search(arr , target):
    left , right = 0 , len(arr)-1 

    while left <= right :
        mid = left + right // 2 

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target :
            left = mid + 1 
        else :
            right = mid - 1 
    return -1 


# recursive binary search

def recursive_binary_search(arr , left , right , target):
    if (left > right ):
        return -1  

    mid = left + right // 2 

    if arr[mid] == target:
        return mid 
    elif arr[mid] < target:
        return recursive_binary_search(arr,mid+1 , right , target)
    else:
        return recursive_binary_search(arr,left , mid-1 , target)

    
