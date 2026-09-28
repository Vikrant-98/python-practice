ingrident = ["flour", "sugar", "eggs", "milk", "sugar", "flour","butter"]

unique_ingrident = {item for item in ingrident}

print(unique_ingrident)

dict_ingrident = {
    "gingertea" : ["ginger", "tea", "sugar", "milk"],
    "masalatea" : ["tea", "sugar", "milk", "cardamom", "cinnamon", "ginger"],
    "greentea" : ["green tea", "sugar", "milk"]
}

unique_ingrident = { ing for item in dict_ingrident.values() for ing in item if len(ing) > 5}
print(unique_ingrident)