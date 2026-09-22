seat_type = input("Enter seat type (economy, business, first): ").lower()

match seat_type:
    case "economy":
        print("You have selected Economy class.")
    case "business":
        print("You have selected Business class.")
    case "first":
        print("You have selected First class.")
    case _:
        print("Invalid seat type.")
        