chai_type = ["Green Tea","Kadak Chai", "Black Tea", "White Tea" ,"Kadak Chai"]

specific_chai = list(filter(lambda x: "Kadak Chai" != x, chai_type))

print(specific_chai)