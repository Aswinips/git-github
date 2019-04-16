list_num=[1,2,3,'str',4,5,'str2','str3',6,7,5,3,'5']
print('Check type of object', type(list_num))
print(len(list_num),': is the length of list_num')
range_list=range(len(list_num))
print(range_list,': is range of list_num')
print(list_num[1:4])
'''#filter by Integers

# Method--->1
list_int=[e for e in list_num if isinstance(e, int)]
print(list_int)
# Method--->2
list_int1=[e for e in list_num if type(e) == type(1)]
print(list_int1)
# Method--->3
for e in range_list:
    if int==type(list_num[e]):
        print(list_num[e])
# Method--->4
for e in range_list:
    if str != type(list_num[e]):
        print(list_num[e])
# Method--->5
for e in range_list:
    if int == type(list_num[e]):
        print(list_num[e])
        continue
# Method--->6
for e in range_list:
    if str != type(list_num[e]):
        print(list_num[e])
        break   '''
        
#filter by Strings

# Method--->1
# Method--->1
list_str=[e for e in list_num if isinstance(e, str)]
print(list_str)

#Finding duplicate values in a given list

#list_num=[1,2,3,'str',4,5,'str2','str3',6,7,5,3,'5']
'''dup_list=[]
for e in list_num:
    if list_num.count(e)>=2:
        dup_list.append(e)
print(dup_list) 
# Method--->2        
dup_list=[x for x in list_num if list_num.count(x)>1]
print(dup_list)
# Method--->3
dup_list=set([x for x in list_num if list_num.count(x)>1])
print(dup_list)'''

#Add,remove

'''
list_num.append('Aswini')
print(list_num)
#list_num.remove('str') # str will be delete
#list_num.remove(3) # 3 will be deleted
list_num.pop(3) # index of 3rd character will be delete
print(list_num) 

list_rotate=[1,2,3,4]
list_range=range(len(list_rotate)) #list_range=range(len(list_rotate)-1) output-->[2,3,4,1]
for i in list_range:                 #list_range=range(len(list_rotate)-2) output-->[2, 3, 1, 4]
    if i<3:
        temp=list_rotate[i]
        list_rotate[i]=list_rotate[i+1]
        list_rotate[i+1]=temp
    #else:       #output-->[2,3,4,1]
        #break
print(list_rotate)  '''

#ascii
list_asc=['Aswini','Amar','Reddy']
range_list=range(len(list_asc))
range_list_0=range(len(list_asc[0]))
range_list_1=range(len(list_asc[1]))
range_list_2=range(len(list_asc[2]))
print(range_list,range_list_0,range_list_1,range_list_2)
sum_1=0
sum_2=0
sum_3=0
for i in range_list:
    if i==0:
        for j in range_list_0:
            sum_1=sum_1+ord(list_asc[i][j])
    if i==1:
        for j in range_list_1:
            sum_2=sum_2+ord(list_asc[i][j])
    if i==2:
        for j in range_list_1:
            sum_3=sum_3+ord(list_asc[i][j])
print('Asci value of Aswini is:', sum_1)
print('Asci value of Amar is:', sum_2)
print('Asci value of Reddy is:', sum_3)
















