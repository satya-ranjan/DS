#1.starting with the first element(index=0) compare the current element with the next element
#2.if the current element is greater then the next element of the list swap the number
#3.if the current element is less the next element move to the next element .Repeat the step 1

list1= [23,65,6,2,0]
print(list1)#unsorted list
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i] , list1[i+1] = list1[i+1] , list1[i]
print(list1)

