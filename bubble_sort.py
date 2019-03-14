def bubble_sort(arr):
	
	def swap(i,j):
		arr[i],arr[j] = arr[j],arr[i]

	n = len(arr)
	swapped=True

	x = -1
	while swapped:
		swapped =False
		x = x + 1
		for i in range(1,n-x):
			if arr[i-1]>arr[i]:
				swap(i-1,i)
				swapped = True


	return arr


a= [3,1,5,2,6,4,9,8,7]
b= [5,6,9,8,7,2,4,3,1]
c= [9,7,8,4,6,1,3,2,5]

print(bubble_sort(a))
print(bubble_sort(b))
print(bubble_sort(c))






