def ChaiSpices():

    spices = "Elaichi"
    def inner():
        #nonlocal spices
        spices = "Cinnamon"

    inner()
    print(spices)

ChaiSpices()