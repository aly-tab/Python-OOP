def countdown(num):
	newList = []
	for x in range(num, -1, -1):
		newList.append(x)
	return newList

print(countdown(5))

def print_and_return(a):
	print(a[0])
	return(a[1])

print(print_and_return([1,2]))

def first_plus_length(list):
	sum = list[0] + len(list)
	return sum

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
	newList = []
	for x in list:
		if (len(list) > 1 and x > list[1]):
			newList.append(x)
	if (len(newList) < 3):
		return False
	else: 
		return newList

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(size, val):
	list = []
	for x in range(size):
		list.append(val)
	return list

print(length_and_value(4,7))
print(length_and_value(6,2))
