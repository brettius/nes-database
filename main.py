import database
import pickle
import re

GET = 1
ALL = 2
ADD = 3
CHANGE = 4
DELETE = 5
QUIT = 6

FILENAME = 'data.dat'

def main():
	NESdatabase = load_database()
	
	choice = 0
	
	while choice != QUIT:
		
		choice = get_menu()
		
		if choice == GET:
			look_up(NESdatabase)
		elif choice == ALL:
			get_all(NESdatabase)
		elif choice == ADD:
			add(NESdatabase)
		elif choice == CHANGE:
			change(NESdatabase)
		elif choice == DELETE:
			delete(NESdatabase)
			
	save(NESdatabase)

def look_up(NESdatabase):
	name = input('Enter a game title')
	
	print(NESdatabase.get(name, 'That game is not found'))
	
def get_all(NESdatabase):
	for k, v in NESdatabase.items():
		print(v)

def add(NESdatabase):
	name = input('Name: ')
	category = input('Category: ')
	
	year_entry = True
	
	while year_entry == True:
		
		try:
			
			year = input('Year: ')
			
			check_valid_date = re.compile(r'^[12](\d){3}')
			
			passed_test = check_valid_date.search(year)
	
			result = (passed_test.group())
			
			record = database.NES(name,category,result)
			
			year_entry = False
			
		except:
			
			print('Date not in correct format')
			continue

	#Checks if it already exists
	
	if name not in NESdatabase:
		NESdatabase[name] = record
		print('Entered')
	else:
		print('Already exists')
		
		
def change(NESdatabase):
	name = input('Enter a title')
	
	if name in NESdatabase:
		
		category = input('Enter a new category')
		
		year = input('Enter a new year')
		
		record = database.NES(category,year)
		
		#Update entry
		
		NESdatabase[name] = record
		print('Updated')
		
	else:
		print('Title not found')
		
def delete(NESdatabase):
	
	name = input('Enter a title')
	
	#If title found, delete title
	
	if name in NESdatabase:
		del NESdatabase[name]
		
		print('Title deleted')
	
	else:
		print('Title not found')
		
def load_database():
	try:
		input_file = open(FILENAME, 'rb')
		
		nes_database = pickle.load(input_file)
		
		input_file.close()

	except IOError:
		
		nes_database = {}
		
	return nes_database		
	
#Pickels object and saves it to file
def save(NESdatabase):
	
	output_file = open(FILENAME, 'wb')
	
	pickle.dump(NESdatabase, output_file)
	
	output_file.close()
	
def get_menu():
	print()
	print('Menu')
	print('-------------------------------------------------------------')
	print('1. Look up game')
	print('2. See all games')
	print('3. Add new game')
	print('4. Change exisiting game')
	print('5. Delete a game')
	print('6. Quit program')
	print()
	
	choice = int(input('Enter a choice'))
	
	#Validating number entered using comparison operator
	
	while choice < GET or choice > QUIT:
		choice = int(input('Please enter a valid choice'))
		
	return choice
	
main()

	
		
