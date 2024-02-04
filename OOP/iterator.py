# mytuple = ("Banana", "Apple", "Orange")
# for x in mytuple:
#     print(x)
# print(next(tp))
# print(next(tp))
# print(next(tp))



# string = "Nicholas"

# mystr = iter(string)

# print(next(mystr), end="")
# print(next(mystr), end="")
# print(next(mystr), end="")
# print(next(mystr), end="")
# print(next(mystr), end="")
# print(next(mystr), end="")
# print(next(mystr), end="")
# print(next(mystr))


class iterator:
    def __iter__(self):
        self.a = 1
        return self   # Must always return the iterator object which is the method itself
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x # Must return the nexr item in the sequence 
        else:
            raise StopIteration

p = iterator()
q = iter(p)


for q in p:
    print(q)


# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
