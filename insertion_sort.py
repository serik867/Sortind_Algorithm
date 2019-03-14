def insertion_sort(arr,simulation = False):

	for i in range(len(arr)):
		cursor =arr[i]
		pos = i


		while pos > 0 and arr[pos-1]>cursor:

			arr[pos] = arr[pos-1]
			pos=pos-1

		arr[pos]= cursor

	return arr


a= [3,1,5,2,6,4,9,8,7]
b= [5,6,9,8,7,2,4,3,1]
c= [9,7,8,4,6,1,3,2,5]

print(insertion_sort(a))
print(insertion_sort(b))
print(insertion_sort(c))