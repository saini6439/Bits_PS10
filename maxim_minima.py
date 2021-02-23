# Python3 program for the above approach

# Function to find all the local maxima
# and minima in the given array arr[]

def findLocalMaximaMinima(n, arr):

	# Empty lists to store points of
	# local maxima and minima
	mx = []
	mn = []

	# Checking whether the first point is
	# local maxima or minima or neither
	if(arr[0] > arr[1]):
		mx.append(0)
	elif(arr[0] < arr[1]):
		mn.append(0)

	# Iterating over all points to check
	# local maxima and local minima
	for i in range(1, n-1):

		# Condition for local minima
		if(arr[i-1] > arr[i] < arr[i + 1]):
			mn.append(i)

		# Condition for local maxima
		elif(arr[i-1] < arr[i] > arr[i + 1]):
			mx.append(i)

	# Checking whether the last point is
	# local maxima or minima or neither
	if(arr[-1] > arr[-2]):
		mx.append(n-1)
	elif(arr[-1] < arr[-2]):
		mn.append(n-1)

		# Print all the local maxima and
		# local minima indexes stored
	if(len(mx) > 0):
		print("maxima",mx)
	else:
		print("There are no points of Local maxima.")

	if(len(mn) > 0):
		print("Points of Local minima are : ", end ='')
		print(*mn)
	else:
		print("There are no points of Local minima.")

# Driver Code
if __name__ == '__main__':

	# Given array arr[]
	arr = [8,7,6,5,4,3,2,1]


	# Function Call
	findLocalMaximaMinima(len(arr), arr)
