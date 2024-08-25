dic={"Model":"C-class","brand":"Mercedes-Benz","Year":2024}
print(dic)
print(dic["brand"])
print(len(dic))
car={"Brand":"TATA Curvv EV",
      "Electric":True, 
      "Year":2024,
      "Color":["Virtual Sunrise","Flame Red","Pristine White","Pure Grey","Empowered Oxide"]}
print(car)
print(type(dic))

#--------------------------------------------------------Access Items-------------------------------------------------------------------------------------------

x=dic.get("Model")
print(x)

x= dic.keys()
print(x)

x=dic.values()
print(x)

car["Year"]=2025
print(car)

x=car.items()
print(x)

#-----------------------------------------------------Remove Items------------------------------------------------------------------------------

dic.pop("Model")
print(car)

car.popitem()
print(car)

print(dic)
print(car)
del car["Electric"]
print(car)
del car

#---------------------------------------------------Nested Dictionaries-----------------------------------------------------------------------


comp1 = {
    "name": "TCS",
    "year": 1968
}
comp2 = {
    "name": "Infosys",
    "year": 1981
}
comp3 = {
    "name": "Wipro",
    "year": 1945
}

mycomp = {
    "comp1": comp1,
    "comp2": comp2,
    "comp3": comp3
}

print(mycomp["comp2"]["name"])

for x, obj in mycomp.items():
    print(x)

for y in obj:
    print(y+':',obj[y])
