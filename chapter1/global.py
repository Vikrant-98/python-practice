spices = "Ginger" 

def ChaiSpices():
    
    spices = 1
    def inner():
        nonlocal spices
        spices = 34

    inner()
    print(f"inner spices {spices}")

ChaiSpices()
print(f"outer spices {spices}")