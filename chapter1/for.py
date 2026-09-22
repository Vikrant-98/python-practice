chai_order = ["chai", "milk", "sugar", "ginger", "cardamom", "cinnamon"]

for item in chai_order:
    print(f" This is item {item} in the chai order.")

chai_order2 = ["chai", "milk", "sugar", "ginger", "cardamom", "cinnamon"]
chai_price = [2.5, 1.0, 0.5]
            
for item,price in zip(chai_order2, chai_price):
    print(f" This is item {item} in the chai order.")
    print(f" The price of {item} is ${price:.2f}.")