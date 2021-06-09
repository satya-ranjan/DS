# 1.select the pivot element
# 2.find out the correct position of pivot element in the list by rearranging it
# 3.divide the list based on pivot element
# 4.sort the sublist recusively  
def pivot_place(list1,first,last):
    pivot = list1[first]
    left = first+1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left = left+1
        while left <= right and list1[right] >= pivot:
            right = right-1
        if right<left:
            break
        else:
            list1[left],list1[right] = list1[right],list[left]
    list1[first],list1[right] = list1[right],list1[first]
    return right

def quicksort(list1,first,last):
    if first < last:
                p = pivot_place(list1,first,last)
                quicksort(list1,first,p-1)
                quicksort(list1,p+1,last)
list1 = [65,78,57,0,84,9378,89]
n = len(list1)
quicksort(list1,0,n-1)
print(list1)
     
