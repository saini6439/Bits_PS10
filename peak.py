# A binary search based function
# that returns index of a peak element
def findmin_max(arr, low, high, n):
    # Find index of middle element
    # (low + high)/2
    mid = low + (high - low) / 2
    mid = int(mid)

    # Compare middle element with its
    # neighbours (if neighbours exist)

    name=''
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        print("maxima")
        return mid

    elif ((mid == 0 or arr[mid - 1] >= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] >= arr[mid])):
        print("minima")
        return mid
        # If middle element is not peak and
        # its left neighbour is greater
        # than it, then left half must
        # have a peak element
    elif (mid > 0 and arr[mid - 1] < arr[mid]):
        return findmin_max(arr, low, (mid - 1), n)


        # If middle element is not peak and
        # its right neighbour is greater
        # than it, then right half must
        # have a peak element
    else:
        return findmin_max(arr, (mid + 1), high, n)


# A wrapper over recursive
# function findPeakUtil()
def find(arr, n):
    return findmin_max(arr, 0, n - 1, n)


# Driver code
#arr = [17 ,15 ,13 ,11 ,9 ,7 ,5 ,3] #  3
arr = [3 ,5 ,7 ,9 ,11, 13 ,15 ,17] # 3
#arr = [3 ,5 ,7 ,9 ,8 ,7 ,6 ,5] #9
#arr = [17 ,15 ,13 ,11 ,12 ,13 ,14 ,15] #11


n = len(arr)
print("Index of a peak point is", arr[find(arr, n)])
