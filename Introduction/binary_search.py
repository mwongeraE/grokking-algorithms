def binary_search(list, item):
	# Keep track of low and high
	low = 0 
	high = len(list)-1

	while low <= high :
		# Check the middle item
		mid = (low + high)
		guess = list[mid]

		# Found the item
		if guess == item:
			return mid
		
		# If guess was too high
		if guess > item :
			high = mid - 1
		else :
			low = mid + 1
	return None

# Test
my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3)
print binary_search(my_list, -1)
print binary_search(my_list, 7)