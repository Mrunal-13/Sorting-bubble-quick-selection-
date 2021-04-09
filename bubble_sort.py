#This code is applying bubble sort on the array by using python.
#performed by Mrunal D.Nimbalkar
array=[55,65,5,9,30.58]
print(array)
print("The array sorted by bubble sort is")
def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                (array[j],array[j+1])=(array[j+1],array[j])
    print(array)

bubblesort(array)
                
                
