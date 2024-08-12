l = [3,5,6,"Mansi",True,6,7,2,32,345,23]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[-3]) #Negative index
print(l[len(l)-3])#Positive index
print(l[5-3]) #Positive index
print(l[2]) #Positive index
if 7 in l:
    print("Yes")
elif("kumari" in l):
    print("No")
else:
    print("No")
if "Man" in "Mansi":
    print("Yes")
print(l[1:])
print(l[1:-1])
print(l[1:4])
print(l[1:4:2])
print(l[1:8])
print(l[1:8:3])
lst = [i for i in range(4)]
print(lst)
lst1 = [i*i for i in range(4)]
print(lst1)
lst2 = [i*i for i in range(10)]
print(lst2)
lst2 = [i*i for i in range(10) if i%2 ==0]
print(lst2)
l = [1,2,4,6]
l.append(7)
print(l)
l=[11,45,1,2,4,6]
print(l)
l.sort()
print(l)
l.sort(reverse = True)
print(l)
print("Index of 1",l.index(1))
print("Number of",l.count(1))
#copy function
m = l.copy()
m[0] = 0
print(l)
l.insert(1,899)
print(l)
