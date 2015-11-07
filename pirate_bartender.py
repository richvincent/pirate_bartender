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

def make_drink():
	customer_name = input("Hello Sir! What is your name? ")
	print(customer_name)
	print("\n")

	for values in questions.values():
		print(values)




	


