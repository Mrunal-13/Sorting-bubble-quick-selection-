#code by Mrunal Nimbalkar
#SE ROLL NO:27
#it is the code for quick sort wher input array is given.
array = [45.2,55.4,76.89,53.67,98]
print("array before applying quick sort")
print(array)
def quick_sort(array,low,high):
	if low < high:
		p=partition(array,low,high)#p is the new piot element
		quick_sort(array,low,p-1)#quick sort before pivot elemnet
		quick_sort(array,p+1,high)#quick sort after pivot element


def partition(array,low,high):
	pivot = array[low]
	i = low +1
	j = high

	while True:
		while i <= j and array[i] <= pivot:
			i = i+1
		while i <= j and array[j] >= pivot:
			j = j-1
		if i <= j:
			array[i],array[j] = array[j],array[i]
		else:
			break
	array[low],array[j] = array[j],array[low]
	return j


quick_sort(array,0,len(array)-1)
print("array after sorting is:")
print(array)
print("top five score are:")
print(array[-5:])



