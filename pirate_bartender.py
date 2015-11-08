import random
from subprocess import call


questions = {
	"strong": "Do ye like yer drinks strong?",
	"salty": "Do ye like it with a salty tang?",
	"bitter": "Are ye a lubber who likes it bitter?",
	"sweet": "Would ye like a bit of sweetness with you poisen?",
	"fruity": "Are ye one for a fruity finish?"
	}

ingredients = {
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	"sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"]
	}



def order_drink():
	"""Function to ask the customer what characteristics they would like in their drink"""	
	drink_order = {'customer_name':'','strong':'','salty':'','bitter':'','sweet':'','fruity':''}
	customer_name = input("Hello Sir! What is your name? ")
	drink_order["customer_name"] = customer_name
	print(drink_order["customer_name"])
	print("\n")

	for key in questions:
		
		while drink_order[key] != "YES" and drink_order[key] != "NO":
			call(["clear"])
			print("Please answer yes or no")
			drink_order[key] = input(questions[key]).upper()
			if drink_order[key] == 'Y':
				drink_order[key] = 'YES'
			if drink_order[key] == 'N':
				drink_order[key] = 'NO'

	return(drink_order)


def make_drink(customer_order):
	"""Function used to create drink from flavors selected by customer"""
	drink_made = dict(strong='',salty='',bitter='',sweet='',fruity='')	
	for key in customer_order:
		if customer_order[key] == "YES":
			drink_made[key] = random.choice(ingredients[key])

	return(drink_made)
		
if __name__ == '__main__':

	call(["clear"])
	drink_order = order_drink()
	drink_made = make_drink(drink_order)
	print(drink_order["customer_name"])

	#print("\n Drink Ordered: " + str(drink_order))

	#print("\n Drink Made: " + str(drink_made.values()))
	
	drink = []
	for key in drink_made:
		if drink_made[key] != '':
			drink.append(drink_made[key])


call(['clear'])
print('Your drink your majesty!')
number_of_ingredients = len(drink)
display_drink = ''
num = 1
for ingredient in drink:
	if num < number_of_ingredients:
		display_drink += ingredient
		display_drink += ', '
		num += 1
	else:
		display_drink += ' with '
		display_drink += ingredient

print(display_drink)
	
