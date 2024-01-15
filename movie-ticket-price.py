age = input("child,senior,adult,family,group : ")
days = input("weekdays,weekends : ")
members = int(input("enter members : "))
def chd(child):
    return child
def adl (adult):
    return adult 
def sen(senior):
    return senior 
if age == "child":
    result = chd("child")
    if days == "weekdays":
        price = 300*members
        print(f"Total price is {price}")
    else :
        price = 500*members
        print(f"Total price is {price}")
elif age == "senior":
    result = sen("senior")
    if days == "weekdays":
        price = 500*members
        print(f"total price is {price}")
    else :
        price = 700*members
        print(f"total price is {price}")
elif age == "adult":
    result = adl ("adult")
    if days == "weekdays":
        price = 700*members
        print(f"Total price is {price}")
    else :
        price = 1000*members
        print(f"Total price is {price}")
elif age == "family":
    result = adl("family")
    if days == "weekdays":
        y = 700*members
        discount = y*0.15
        discount1 = y-discount
        print(f"Total price is {discount1}")
    else :
        z = 1000*members
        discount = z*0.15 
        discount1 = z-discount
        print(f"Total price is {discount1}")
elif age == "group":
    result = adl("group")
    if days == "weekdays":
        y = 700*members
        discount = y*0.10
        discount1 = y-discount
        print(f"Total price is {discount1}")
    else:
        z = 1000*members
        discount = z*0.10
        discount1 = z-discount
        print(f"Total price is {discount1}")