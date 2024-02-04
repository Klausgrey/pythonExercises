import random

x = dir(random) 
""" The "dir" function lists all the function name in a module"""
print(x)

import greetings # The file name
""" Imported a loacl file as a module that does a particular function in this case we just greeted the user """

x = "Nick"
greetings.greet(x)

