s ={2,4,6,8}
print(s)
#To determine how many items a set has
print(len(s))

mansi = set()
print(type(mansi))

#loop items
for x in s:
    print(x)


#---------------------------------------------ADD SET ITEMS-------------------------------------------------------------------

#Add items
s.add("orange")
print(s)

#--------------------------------------------REMOVE SET ITEMS--------------------------------------------------------------------------------------------------

#remove items
#If the item to remove does not exist, remove() will raise an error.
#If the item to remove does not exist, discard() will NOT raise an error.
s.discard(8)
print(s)

del x

cities1={"London","Mexico City","Shanghai"}
cities2={"Rio de Janerio","Beijing","Sao Paulo"}
cities3= cities1.union(cities2)
print(cities3)
cities3= cities1.intersection(cities2)
print(cities3)
cities1.intersection_update(cities2)
print(cities1)
cities3=cities1.symmetric_difference(cities2)
print(cities3)
