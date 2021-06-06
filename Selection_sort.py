#selection sort Algorithm descending
list1= [56,3,43,4,68,0]
print(list1)
for i in range(len(list1)):
    min_var= min(list1[i:])
    min_ind = list1.index(min_var)
    list1[i],list1[min_ind] = list1[min_ind],list1[i]
print(list1)