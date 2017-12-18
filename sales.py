# Zachary Goncalves
# Python Learning
# Create a basic Command Line menu that allows an order to be placed and a receipt to be generated. 

# Create Dictionaries of Menu Items
menu_subs = {
		"Ham & Cheese" : 4.00,
		"Italian" : 4.50,
		"American" : 4.50,
        "A Wreck" : 6.50,
		"Chicken Salad" : 4.50,
		"The Works" : 5.00,
		"The Veggie" : 4.00
	}
menu_addons = {
		"Pickles" : 0.25,
		"Tomatoes" : 0.25,
		"Onions" : 0.25,
        "Bacon" : 1.00,
	    "None" : 0.00
	}
menu_drinks = {
		"Water" : 0.00,
		"Fountain Soda" : 1.50,
		"Bottled Soda" : 1.75,
        "None" : 0.00
	}
menu_sides = {
		"Chips" : 1.00,
		"Cookie" : 1.50,
		"Coleslaw Salad" : 2.00,
		"Potato Salad" : 2.50,
        "French Fries" : 1.50,
        "Sweet Potato Fries" : 2.25,
        "None" : 0.00
	}

# Print out dictionary menus
def print_menu(dct):
    print("Menu Items:")
    for item, amount in dct.iteritems():
        print("{} ({})".format(item, amount))
    return "-----------------------"

# Calculate Original Cost
def get_original_cost(main, addon, drink, side):
    first_cost = menu_subs[main]
    second_cost = menu_addons[addon]
    third_cost = menu_drinks[drink]
    side_cost = menu_sides[side]

    original_cost = first_cost + second_cost + third_cost + side_cost

    return original_cost

# Calculate Delivery Cost
def get_delivery_cost(delivery, originalCost):
    total_cost = originalCost
    delivery_cost = 0
    if delivery == 2:
        if total_cost <= 10:
            delivery_cost = 3
        elif total_cost > 10 and total_cost <= 30.01:
            delivery_cost = 2

    return delivery_cost

# Calculate Discount
def get_discount(discount, deliveryCost, originalCost):
    discount_applied = 0
    delivery_cost = deliveryCost
    original_cost = originalCost
    total_cost = delivery_cost + original_cost

    if discount == 1:
        discount_applied = total_cost * .10

    return discount_applied

# Calculate Taxes
def get_taxes(discountApplied, deliveryCost, originalCost):
    taxes = 0
    delivery_cost = deliveryCost
    original_cost = originalCost
    discount_applied = discountApplied

    total_cost = originalCost + deliveryCost - discountApplied

    taxes = total_cost * .06

    return taxes

# Calculate Total Cost after discounts, taxes, and delivery
def get_final_cost(discountApplied, deliveryCost, originalCost, taxes):
    final_cost = 0
    delivery_cost = deliveryCost
    original_cost = originalCost
    discount_applied = discountApplied
    taxes_applied = taxes

    final_cost = original_cost + delivery_cost - discount_applied + taxes_applied

    return final_cost

# Default While Loop to running
asking = True
# Keep track of current receipts
currentReceiptNumber = 1

print('Welcome to The Lions Roar Deli!')

# Loop asking users for the order and then calculating the various numbers, before writing out the values to a text file
while(asking):
    print('Please generate your receipt. \n')

    # Print Main Menu and take selection
    print(print_menu(menu_subs))
    main = raw_input('Please select your sub. ')

    print("----------------------- \n")

    # Print Addons Menu and take selection
    print(print_menu(menu_addons))
    addon = raw_input('Please select your extra addon. ')

    print("----------------------- \n")

    # Print Drinks Menu and take selection
    print(print_menu(menu_drinks))
    drink = raw_input('Please select your drink. ')

    print('----------------------- \n')

    # Print Sides Menu and take selection
    print(print_menu(menu_sides))
    side = raw_input('Please select your side. ')

    print('----------------------- \n')

    # Take in user delivery method and set value to use as parameter
    delivery_method = input('Please select delivery method: 1 (walk in) or 2 (delivery). ')
    if delivery_method == 2:
        delivery = 2

    print('----------------------- \n')

    # Take in user discount eligibility status and set value to use as parameter
    discount_proof = input('Are you affiliated with the university? 1 (yes) 2 (no) ')
    if discount_proof == 1:
        discount = 1

    print('----------------------- \n')

    # Calculate Original Cost
    original_cost = get_original_cost(main, addon, drink, side)
    # Calculate Delivery Cost
    delivery_cost = get_delivery_cost(delivery, original_cost)
    # Calculate Discount Applied
    discount_applied = get_discount(discount, delivery_cost, original_cost)
    # Calculate Taxex
    taxes_applied = get_taxes(discount_applied, delivery_cost, original_cost)
    # Calculate Final Cost
    final_cost = get_final_cost(discount_applied, delivery_cost, original_cost, taxes_applied)

    # Output calculated values
    print('Order Details: \n' + main + ' (extra ' + addon + ') ' + 'with a side of ' + side + ' and ' + drink + ' to drink.')
    print('-----------------------')
    print('Cost: ' + '$' + str(original_cost))
    if delivery == 1:
        print('Delivery Cost: ' + '$' + str(delivery_cost))
    if discount == 2:
        print('University Discount: ' + '$' + str(discount_applied))
    print('Tax: ' + '$' + str(taxes_applied))
    print('----------------------- \n')
    print('Total: ' + '$' + str(final_cost) + '\n' + '\n')
    print('Thank you for your business!')

    # Generate Receipt txt file using above code
    currentReceipt = str(currentReceiptNumber)
    receiptGenerator = open('receipt' + currentReceipt + '.txt','w')
    receiptGenerator.write('Order Details: \n' + main + ' (extra ' + addon + ') ' + 'with a side of ' + side + ' and ' + drink + ' to drink. \n')
    receiptGenerator.write('Cost: ' + '$' + str(original_cost) + '\n')
    if delivery == 1:
        receiptGenerator.write('Delivery Cost: ' + '$' + str(delivery_cost) + '\n')
    if discount == 2:
        receiptGenerator.write('University Discount: ' + '$' + str(discount_applied) + '\n')
    receiptGenerator.write('Tax: ' + '$' + str(taxes_applied) + '\n')
    receiptGenerator.write('Total: ' + '$' + str(final_cost) + '\n' + '\n')
    receiptGenerator.write('Thank you for your business!')
    receiptGenerator.close()

    # Check if user wants to continue loop
    do_continue = raw_input('Would you like to create another receipt? (y/n)')
    if do_continue == 'n':
        asking = False
        print('Thank you, come again!')
    else:
        asking = True
        cost = 0
        discount = 0
        delivery = 0
        tax = 0
        total_cost = 0
        currentReceiptNumber = currentReceiptNumber + 1
