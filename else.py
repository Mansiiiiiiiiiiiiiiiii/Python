#The else block will NOT be executed if the loop is stopped by a break statement.

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("No i")
print("\n")

#----------------------------------------------------------While loop------------------------------------------------------------------------------

i=1
while i<6:
    print(i)
    i +=1
else:
    print("i is no longer in the list")

#------------------------------------------------------For loop--------------------------------------------------------------------------------

for x in range(6):
    print(x)
else:
    print("Finally finished")