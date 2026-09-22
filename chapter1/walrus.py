flavour = ["sweet", "sour", "salty", "bitter", "umami"]
# flavour_available:= input("Enter a flavour (or type 'exit' to quit): ").lower() not in flavour

while (flavour_available:= input("Enter a flavour (or type 'exit' to quit): ").lower()) not in flavour:
    
    print(f" This is not the flavour {flavour_available}.")

print(f" Thank you for your order. you have selected the flavour {flavour_available}.")