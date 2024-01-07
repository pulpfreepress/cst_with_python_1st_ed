from prettytable import PrettyTable

def main():
	x = PrettyTable()
	x.field_names = ["Object", "Truthy/Falsy"]
	
	x.add_row(["True == True", (True == True)])
	x.add_row(["False == True", (False == True)])
	x.add_row(["1 == True", (1 == True)])
	x.add_row(["0 == True", (0 == True)])
	x.add_row(["-1 == True", (-1 == True)])
	x.add_row(["2 == True", (2 == True)])
	x.add_row(["[] == True", ([] == True)])
	x.add_row(["[[]] == True", ([[]] == True)])
	print(x)
	
	print()

	y = PrettyTable()
	y.field_names = ["Object", "Truthy/Falsy"]
	y.add_row(["if True:", True if True else False])
	y.add_row(["if 1:", True if 1 else False])
	y.add_row(["if 2:", True if 2 else False])
	y.add_row(["if -1:", True if -1 else False])
	y.add_row(["if 0:", True if 0 else False])
	y.add_row(["if []:", True if [] else False])
	y.add_row(["if [[]]:", True if [[]] else False])
	y.add_row(["if {}:", True if {} else False])
	y.add_row(["if {'key':'value'}:", True if {'key':'value'} else False])
	y.add_row(["if '':", True if '' else False])
	y.add_row(["if 'hello':", True if 'hello' else False])
	print(y)
				  

if __name__ == "__main__":
	main()