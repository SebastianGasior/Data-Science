#A list named "menu" was created in this code to keep track of the different items 
#that are available on the cafe's menu. 
#Additionally, two dictionaries, "stock" and "price", were created to store the stock values and prices of each item.
#The code then computes the total worth of the stock in the cafe. 
#It does this by iterating through the items in the menu, 
#multiplying the corresponding values from the "stock" and "price" dictionaries, 
#and storing the result in a list comprehension. The sum() function is then used to calculate the total value.
#Finally, the result is printed using formatted string literals. 
#The :.2f notation is included after the variable to ensure that the output is rounded to two decimal places.

# create a list of menu items
menu = ["coffee", "tea", "sandwich", "cake"]

# create a dictionary holding stock values for each item on the menu
stock = {"coffee": 100, "tea": 50, "sandwich": 75, "cake": 30}

# create a dictionary holding price values for each item on the menu
price = {"coffee": 2.5, "tea": 2, "sandwich": 4.5, "cake": 3.5}

# calculate the total stock worth in the cafe
total_stock_worth = sum([stock[item] * price[item] for item in menu])

# print out the result
print(f"The total stock worth in the cafe is ${total_stock_worth:.2f}")
