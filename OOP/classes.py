# class person:
#     def __init__(self, name, age): 
#         """ The __init__() function allows for us to assign values to object properties or other operation """
#         self.name = name
#         self.age = age

#     def greeting(self):
#         print(f"Hello {self.name}")

# p = person("Nick", 22)
# p.name = "Onome"
# p.greeting() #creating an instance of the object
# # print(f"my name is {p.name}, and my age is {p.age}")

#------------------------------------------------------------------------------------------------------------------------------



# class person:
#     def __init__(self, name, age): 
#         """ The __init__() function allows for us to assign values to object properties or other operation """
#         self.name = name
#         self.age = age

#     def __str__(self):
#         """ This controls what should be returned when the class object is represented as a string """
#         return f"{self.name}, ({self.age})"

# p = person("Nick", 22) #creating an instance of the object
# print(p)




class person:
	def __init__(self, firstName, lastName): 
		""" The __init__() function allows for us to assign values to object properties or other operation """
		self.firstName = firstName
		self.lastName = lastName
		

	def printName(self):
		print(f"Hello {self.firstName} {self.lastName}")

class student(person):
	def __init__(self, firstName, lastName, year): 
		""" The __init__() function allows for us to assign values to object properties or other operation """
		# person.__init__(self, firstName, lastName)
		# """ This is to keep the inheritance of the parent class linked to that of the child class """
		super().__init__(firstName, lastName)
		self.firstName = firstName
		self.lastName = lastName
		self.graduatonYear = year

	def welcome(self):
		print(f"Welcome back {self.firstName} {self.lastName} {self.graduatonYear}")

p = person("Nick", "Upaka")
q = student("John", "Doe", 2027)
q.printName() #creating an instance of the object
p.printName()
y = student("Nick", "Upaka", 2015)
y.welcome()






# # def nameAge(name, age):
# """ Trying clearify the uses of functions and classes, when they should be used and when not to be used and how to use them."""
# #     return print(f"{name}, {age}")

# # nameAge("Nick", 15)