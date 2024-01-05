
def quicksort_partition(arr, start, end):
    """
    Partition function for quicksort algorithm.
    Rearranges elements in the array around a pivot element.

    Parameters:
        - arr (list): The list to be sorted.
        - start (int): The starting index of the subarray.
        - end (int): The ending index of the subarray.

    Returns:
        Index of pivot element : int
    """
    #choose the pivot for partitioning. (the last element)
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot to its correct position
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i



def find_minimum(arr, start, end, a):
    """
    This function is used to find the ath minimum value.

    Parameters:
        - arr (list): The list where we need to find the ath minimum. 
        - start (int): The starting index of the subarray. (Use 0 when normally calling the function)
        - end (int): The ending index of the subarray. (Use len(arr)-1 when normally calling the function)
        - a (int): The target index for the minimum element. 
    
    Returns:
    int: The ath minimum element.
    """
    # This is added for edge cases where the subarray length is 1. (The subarray only contains the target value)
    if len(arr[start:end + 1]) == 1:
        return arr[0]
    if start < end:
        # Find the pivot
        pivot = quicksort_partition(arr, start, end)
        if len(arr) == 1:
            return arr[0]
        # Check if the pivot is equal to index 'a'
        if pivot == a:
                # We return the minimum value
            return arr[pivot]
            
        elif pivot < a:
            # If pivot is less than a, search in the right subarray since searching in the left subarray cannot find the a value.
            return find_minimum(arr, pivot + 1, end, a)
        elif pivot > a:
            # If pivot is bigger than a, search in the left subarray since searching in the right subarray cannot find the a value.
            return find_minimum(arr, start, pivot - 1, a)

        

def find_minimum_maximum(arr, a):
    """
    Using the find_minimum function, get both the ath minimum and maximum values.

    Parameters:
        - arr (list): The array to find the ath minimum and maximum value in.
        - a (int): The target index
    """
    # We have to find the maximum too, so create the a_max variable (The index for the ath maximum value)
    a_max = len(arr) -a

    # Find the minimum and maximum values
    minimum = find_minimum(arr, 0, len(arr)-1, a-1)
    maximum = find_minimum(arr, 0, len(arr)-1, a_max)
    return minimum, maximum


# Example usage:
# array = [9, 3, 8, 4, 7, 6, 1, 5, 2, 10]
# a = 3
# minimum, maximum = find_minimum_maximum(array, a)
# print(f"Minimum: {minimum}, Maximum: {maximum}")
# expected output : Minimum: 3, Maximum: 8