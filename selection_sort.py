def selection_sort(arr):
	for i in range(len(arr)):
		minimum = i

		for j in range(i+1,len(arr)):
			if arr[j] < arr[minimum]:
				minimum = j


		arr[i],arr[minimum] =arr[minimum],arr[i]

	return arr


a= [3,1,5,2,6,4,9,8,7]
b= [5,6,9,8,7,2,4,3,1]
c= [9,7,8,4,6,1,3,2,5]

print(selection_sort(a))
print(selection_sort(b))
print(selection_sort(c))