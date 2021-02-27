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

        # find for maxima in this case
        if ((mid == 0 or int(arr[mid - 1]) <= int(arr[mid])) and
                (mid == n - 1 or int(arr[mid + 1]) <= int(arr[mid]))):
            name = 'maxima'
            return mid, name

        # find for minima, increasing and decreasing in this case
        elif ((mid == 0 or int(arr[mid - 1]) >= int(arr[mid])) and
              (mid == n - 1 or int(arr[mid + 1]) >= int(arr[mid]))):
            name = 'minima'
            if (int(arr[0]) == int(arr[mid])):
                name = 'increasing'
            elif (int(arr[-1]) == int(arr[mid])):
                name = 'decreasing'
            return mid, name

        # in these cases calling recursively
        elif (mid > 0 and int(arr[mid - 1]) < int(arr[mid])):
            return self.findmin_max(arr, low, (mid - 1), n)

        else:
            return self.findmin_max(arr, (mid + 1), high, n)

    # calling a recursive function findmin_max
    def find(self, arr, n):
        return self.findmin_max(arr, 0, n - 1, n)


    # read input data from file inputPS10.txt
    # write output data into outputPS10.txt
    def read_alldata(self):
        input_file = open("inputPS10.txt", "r")
        output_file = open("outputPS10.txt", "w")
        for x in input_file:
            arr = x.split()
            n = len(arr)
            index, state = self.find(arr, n)
            output_file.write(state+" "+arr[index]+"\n")
        input_file.close() # input file closed
        output_file.close() # output file closed

# main function created object of maxima_minima class and call read_alldata() function
if __name__ == '__main__':
    max_min =maxima_minima()
    max_min.read_alldata()
