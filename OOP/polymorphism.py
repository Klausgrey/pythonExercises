# class car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(f"You drive a {self.brand} a {self.model}")

# class boat:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(f"You sail a {self.brand} a {self.model}")

# class plane:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(f"You fly a {self.brand} a {self.model}")


# x = car("Toyata", 2022)
# y = boat("Titanic", 1992)
# z = plane("Air Peace", 2001)

# for a in (x, y, z):
#     a.move()



class vehicles:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"You drive a {self.brand} a {self.model}")

class car(vehicles):
    pass

class boat(vehicles):
    # def move(self):
    #     print(f"You sail a {self.brand} a {self.model}")
    pass

class plane(vehicles):
    # def move(self):
    #     print(f"You fly a {self.brand} a {self.model}")
    pass



x = car("Toyata", 2022)
y = boat("Titanic", 1992)
z = plane("Air Peace", 2001)

for a in (x, y, z):
    print(a.brand)
    print(a.model)
    a.move()