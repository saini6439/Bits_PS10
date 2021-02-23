

class maxima_minima:
    def __init__(self):
        self.root = None

    def findmin_max(self, arr, low, high, n):
        # Find index of middle element
        # (low + high)/2
        mid = low + (high - low) / 2
        mid = int(mid)

        # Compare middle element with its
        # neighbours (if neighbours exist)

        if ((mid == 0 or int(arr[mid - 1]) <= int(arr[mid])) and
                (mid == n - 1 or int(arr[mid + 1]) <= int(arr[mid]))):
            name = 'maxima'
            return mid, name

        elif ((mid == 0 or int(arr[mid - 1]) >= int(arr[mid])) and
              (mid == n - 1 or int(arr[mid + 1]) >= int(arr[mid]))):
            name = 'minima'
            if (int(arr[0]) == int(arr[mid])):
                name = 'increasing'
            elif (int(arr[-1]) == int(arr[mid])):
                name = 'decreasing'
            return mid, name
            # If middle element is not peak and
            # its left neighbour is greater
            # than it, then left half must
            # have a peak element
        elif (mid > 0 and int(arr[mid - 1]) < int(arr[mid])):
            return self.findmin_max(arr, low, (mid - 1), n)

            # If middle element is not peak and
            # its right neighbour is greater
            # than it, then right half must
            # have a peak element
        else:
            return self.findmin_max(arr, (mid + 1), high, n)

    # A wrapper over recursive
    # function findPeakUtil()
    def find(self, arr, n):
        return self.findmin_max(arr, 0, n - 1, n)

    def read_alldata(self):
        f = open("inputPS10.txt", "r")
        file1 = open("outputPS13.txt", "w")
        for x in f:
            arr = x.split()
            n = len(arr)
            index, state = self.find(arr, n)
            file1.write(state+" "+arr[index]+"\n")
            print(state, arr[index])


if __name__ == '__main__':
    max_min =maxima_minima()
    max_min.read_alldata()
