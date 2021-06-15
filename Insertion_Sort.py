'''
Algorithm:
1.consider the first elementto be sorted and rest to be unsorted.
2.take the first element in the unsorted part(u1) and compare it with sorted part element(s1).
3.if u1<s1 then insert u1 in the correct index.else leave it as it is.
4.take the next element in the unsorted part and compare with sorted elements.
5.repeat 3 and 4 untill all the element are sorted.
'''
def insertionSort(my_list):
    for index in range(1,len(my_list)):
        current_element = my_list[index]
        pos = index
        while current_element < my_list[pos-1] and pos>0:
            my_list[pos] = my_list[pos-1]
            pos = pos-1
        my_list[pos] = current_element
list1= [2,4,5,6,7]
insertionSort(list1)
print(list1)

