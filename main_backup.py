# A binary search based function
# that returns index of a peak element
def findmin_max(arr, low, high, n):
    # Find index of middle element
    # (low + high)/2
    mid = low + (high - low) / 2
    mid = int(mid)

    # Compare middle element with its
    # neighbours (if neighbours exist)


    if ((mid == 0 or int(arr[mid - 1]) <= int(arr[mid])) and
            (mid == n - 1 or int(arr[mid + 1]) <= int(arr[mid]))):
        name='maxima'
        return mid,name

    elif ((mid == 0 or int(arr[mid - 1]) >= int(arr[mid])) and
            (mid == n - 1 or int(arr[mid + 1]) >= int(arr[mid]))):
        name='minima'
        if(int(arr[0])==int(arr[mid])):
            name = 'decreasing'
        elif(int(arr[-1])==int(arr[mid])):
            name = 'increasing'
        return mid,name
        # If middle element is not peak and
        # its left neighbour is greater
        # than it, then left half must
        # have a peak element
    elif (mid > 0 and int(arr[mid - 1]) < int(arr[mid])):
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
#arr = [17 ,15 ,13 ,11 ,9 ,7 ,5 ,3]
#arr = [3 ,5 ,7 ,9 ,11, 13 ,15 ,17]
#arr = [3 ,5 ,7 ,9 ,8 ,7 ,6 ,5]
#arr = [17 ,15 ,13 ,11 ,12 ,13 ,14 ,15]
#arr = ['17', '15', '13', '11', '9', '7', '5', '3']
#arr = ['3', '5', '7', '9', '11', '13', '15', '17']
#arr = ['3', '5', '7', '9', '8', '7', '6', '5']
#arr = ['17', '15', '13', '11', '12', '13', '14', '15']





def read_alldata():
    f = open("inputPS10.txt", "r")
    for x in f:
        arr = x.split()
        n = len(arr)
        index, state = find(arr, n)
        print(state, arr[index])


read_alldata()







# arr=[17,15,13,11,12,13,14,15]
# arr1=sorted(arr)
# print(arr,arr1)
#
# def Reverse(lst):
#     lst.reverse()
#     return lst
#
# if(arr==arr1):
#     print("true",arr[0])
# elif(arr==Reverse(arr1)):
#     print("decreasing",arr1[-1])
#
