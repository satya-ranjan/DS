'''
1.Take the list of numbers
2.find out the gap/incrementor
3.create the sublist based on gap and sort them using insertion sort algorithm.
4.reduce gap and repeat step 3
5.stop when gap is 0

'''
def shellSort(alist):
    gap = len(alist)//2
    while gap>0:
        for index in range(gap,len(list1)):
            current_elemnt = alist[index]
            pos = index
            while pos>= gap and current_elemnt<alist[pos-gap]:
                alist[pos] = alist[pos-gap]
                pos = pos-gap
            alist[pos] = current_elemnt
        gap = gap//2 

num = int(input("Enter the no of array you want to input : "))
list1 = [int(input()) for i in range (num)]
shellSort(list1)
print(list1)

