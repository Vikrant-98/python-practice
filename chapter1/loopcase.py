flavour = ["sweet", "sour", "salty","out of stock", "bitter", "discontinued", "umami"]

for item in flavour:
    if item == "out of stock":
        print(f" Sorry, {item} is currently unavailable.")
        continue
    elif item == "discontinued":
        print(f" Sorry, {item} has been discontinued.")
        break
    else:
        print(f" This is the flavour {item}.")

print(" Thank you for your order.")