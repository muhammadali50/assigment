menu = ["biryani","russian salad","alfredo pasta"," "]
for i in menu:
    print(i)
select_item = input("Slect item : ")
num_people = int(input("Enter peoples : "))
quantity = int(input("Enter quantity : "))
def itm(item):
    return item
def pri(price,quantity):
    return price*quantity 
if select_item == "biryani":
    result = itm(select_item)
    total_price = pri(200,quantity)
    print(f"Price of biryani 200pkr")
    print(f"Total price is {total_price}pkr")
elif select_item == "russian salad":
    result = itm(select_item)
    total_price = pri(400,quantity)
    print(f"Price of russian salad 400pkr")
    print(f"Total price is {total_price}pkr")
elif select_item == "alfredo pasta":
    result = itm(select_item)
    total_price = pri(700,quantity)
    print(f"Price of alfredo pasta 700pkr")
    print(f"Total price is {total_price}pkr")
dis = total_price*0.15
discount = int(total_price-dis)
print(f"After 15 % discount = {discount}pkr")
tax = discount*0.08
tax_1 = int(discount+tax)
print(f"Total bill include 8% tax = {tax_1}pkr")
each_people = int(tax_1/num_people)
print(f"Bill price for each person is {each_people}pkr")