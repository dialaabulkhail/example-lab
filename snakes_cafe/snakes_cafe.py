msg =  """
       **Welcome to our Cafe**

       *to quit please type 'quit'*

________________________________________
       Menu:

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
________________________________________

What would you like to order?

       """
print(msg)


menu = ["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"] 

orders = [1,2,3,4,5,6,7,8,9,0]
num = 0

for i in orders:
    order = input("> ")
    
    if order == "quit":
        break
    if order in menu:
        num += 1
        print(num, ' order of ' + order + ' have been added to your meal')
    elif order not in menu:
        print("Not on the menu, Please type correctly")
    