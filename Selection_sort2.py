list1=[22,498,0,8,43,3,3]
print(list1)
for i in range (len(list1)-1):
    m_ind= i
    for j in range(i+1,len(list1)):
        if list1[j] < list1[m_ind]:
            m_ind = j

#If the value is in proper indix no need to do the swaping
    if list1[i] != list1[m_ind]:
        list1[i],list1[m_ind]=list1[m_ind],list1[i]
print(list1)