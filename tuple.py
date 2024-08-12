tup =(1,2,76,342,32,"green",True)
print(type(tup),tup)
print(tup[0])
print(tup[-1])
print(tup[2])
if 342 in tup:
    print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)
countries = ("United States","United Kingdom","Japan","Yemen","India")
temp = list(countries)
temp.append("Qatar")      #add items
temp.pop(3)               #remove items
temp[2]="Denmark"         #change item
countries = tuple(temp)
print(countries)
countries=("Afghanistan","Bangladesh","Bhutan","India")
countries2=("Iran","Maldives","Nepal")
southAsia = countries + countries2
print(southAsia)
#Tuple method
Tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = Tuple1.count(3)
print("Count of 3 in Tuple1 is:",res)
