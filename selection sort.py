#selection sort by Mrunal Nimbalkar
#provided an array which will sort it by an algo of an selection sort.
array=[5,20,9,85,12]
print("The array given for sorting is: ",array)
n=len(array)
def selection_sort(array,n):
    for i in range(0,n):
        mini=i
        for j in range(i+1,n):
            if array[j]<array[mini]:
                mini=j
        if array[mini] != array[i]:
            array[i],array[mini] = array[mini],array[i]
        print("array after ",i,"th itration")
        print(array)
selection_sort(array,n)
print("array after sorting is: ")
print(array)
print("thank you,\ncodes by Mrunal Nimbalkar")
print("directed by Mangesh Manke Sir")
