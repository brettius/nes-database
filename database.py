#Create a class to hold information about an NES cartridge

class NES:
	def __init__(self, name, category, year):
		self.__name = name
		self.__category = category
		self.__year = year 
		
	#Set the attributes
		
	def set_name(self):
		self.__name = name
		
	def set_category(self):
		self.__category = category
		
	def set_year(self):
		self.__year = year
		
	#Provide methods to get the attributes
	
	def get_name(self):
		return self.__name
	
	def get_category(self):
		return self.__category
		
	def get_year(self):
		return self.__year
		
	#Return database information as a string
	
	def __str__(self):
		return 'Name: ' + self.__name + '\tCategory: '+ self.__category + \
		'\tYear: ' + self.__year
		
	
		
	
