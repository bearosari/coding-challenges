
list= [1, 2, 3, 4, 5]
newlist= []

length= len(list)
product= 1
value= 0

for i in list:
    #print(i)
    product *=i

for i in list:
    value= product/i
    #print(value)
    newlist.append(value)


print(list)
print(newlist)
