#This selection sort Algorithm Can be applicable for duplicate number 

list1=[22,498,0,8,43,3,3]
print(list1)
for i in range (len(list1)-1):
    min_val=min(list1[i:])
    min_ind= list1.index(min_val,i)
#Is the value is in proper indix no need to do the swaping
    if list1[i] != list1[min_ind]:
        list1[i],list1[min_ind]=list1[min_ind],list1[i]
print(list1)