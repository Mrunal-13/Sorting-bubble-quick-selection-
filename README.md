# SORTING TECHNIQUES
## Table of contents 
1)[Introduction](#Introduction)

1)[Bubble Sort](#Bubble-Sort)
  
   i)[Introduction](#Introduction)
  
   ii)[What is bubble sort?](#What-is-bubble-sort?)
  
   iii)[Algorithm of bubble sort](#Algorithm-of-bubble-sort)
  
   iv)[analysis and uses of bubble sort](#analysis-and-uses-of-bubble-sort)
  
2)[Quick Sort](#Quick-Sort)
  
   i)[Introduction](#Introduction)
  
   ii)[What is quick sort?](#What-is-quick-sort?)
  
   iii)[Algorithm of quick sort](#Algorithm-of-quick-sort)
  
   iv)[analysis and uses of quick sort](#analysis-and-uses-of-quick-sort)

3)[Selection Sort](#selection-sort)

  i)[Introduction](#Introduction)
  
  ii)[What is selection Sort](#selection-sort)
  
  iii)[Algorithm of selection sort](#algorithm-of-selection-sort)
  
  iv)[Analysis and uses of selection sort](#Analysis-and-uses-of-selection-sort)
  
4)[Summary](#Summary)

5)[Acknowledgment](#Acknowledgment)


## Introduction
Sorting is a process of ordering or placing a list of elements from a collection in some kind of order. It is nothing but storage of data in sorted order. Sorting can be done in ascending and descending order. It arranges the data in a sequence to make operations on data easier.The day to day example of sorting is dictionary (searching word in dictionary in alphabetical order.)Sorting technique depends on the situation. It depends on two parameters.

1. Execution time of program that means time taken for execution of program.
2. Space that means space taken by the program.

Sorting techniques are differentiated by their efficiency and space requirements.

There are different sorting algorithms what they do is take lists of items as input data, perform specific operations on those lists and deliver ordered data.

Sorting can be performed using several techniques: 

1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Quick Sort
5. Heap Sort


Here we have three among them bubble sort,quick sort,selection sort.

## Bubble sort

### Introduction
    
   Bubble sort is simply an algorithm that repeatedly iterates the list.In each iteration,it compares one element of list to adjacent element and swaps if it is placed in wrong    order.Each ietration is called as pass and pass through the list is repeated until the list is sorted.
   The larger element is bubbled to end of list and smaller is bubbled to top of the list.
   
### What is bubble sort?

   The basic defination of bubble sort is given in above introduction.
   lets see what is actual working behind bubble sort
   
   lets take example to sort the list  5 2 3 4 9.
   
   **First pass**
   
   (**5**,**2**,3,4,9)-->(**2**,**5**,3,4,9)-->>it compared 0th and 1st element and swapped because 5>2.
   
   (2,**5**,**3**,4,9)-->(2,**3**,**5**,4,9)
   
   (2,3,**5**,**4**,9)-->(2,3,**4**,**5**,9)
   
   (2,3,4,**5**,**9**)-->(2,3,4,**5**,**9**)-->it does not swap 5 and 9 as 5<9.
   
   (2,3,4,5,8) since we got sorted array in first pass.we can skip other passes or perform it.
   if other two passes are performed than it will just iterate and not swap elements.
   the final array generated in last pass will be sorted array.
   
   
### Algorithm of bubble sort


   step 1:- start
   
   step 2:-take inside the array of numbers to perform bubble sort on.
   
   step 3:- find length of array.
   
   step 4:- intialize the counter i from i to n-1.
   
   step 5 ;- if num>adjecent num then swap
   
   step 6;- else do not swap
   
   step 7:- return to step 4 and increment i till all passes are done.
   
   step 8 ;-print sorted array.
   
   step 9;- stop
   
   
   The algorithm can be optimized according to your ideas this the basic approach which covers all the passes.
   
   **peusdo code**
     array=[]
     print(array)
     
    def bubblesort(array):
        for i =0 to i=length of array:
            for j=0 to length of array -i-1:
                  if array at j >array at j+1:
                    ( array[j],array[j+1])=(array[j+1],array[j])
        print(array)

     bubblesort(array)
                
   
   
### Analysis and uses of bubble sort
 
 It leads to some intresting theoritical problems.it is also the fact that it has catchy name.In computer graphics bubble sort has capability to determine the small errors.
 it is not widely used.
 
 **time complexity of bubble sort**
 
 *best case* : - O(n)
 
 *worst case*:-   O(n^2)
 
 *average case* :-  O(n^2)
 
 
 ## Quick Sort
 
 
   
   
   
