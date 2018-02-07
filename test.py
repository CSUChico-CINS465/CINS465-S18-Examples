'''print("Hello World")

x=2
y=2.0
x="string"
print(x+str(y))'''
# print("Hi")

# array=["a","b","c"]
# print(array)
# array.append("d")
# print(array)

# if 0=="0":
#     print(True)
#     print("Hi")
# elif array[0]=="0":
#     print("else True")
# else:
#     print(False)

# x=0
# while x<len(array):
#     print(array[x],end='')
#     x+=1
# print()

# for elm in range(len(array)):
#     print(array[elm])

d = {} #empty dictionary
y = [] #empty list
z = () #empty tuple

# z=[(1,2,3),[4,5,6],"a"]
# print(z)

# d = {"key":"value"}
# d["key2"]=[]
# d["key2"]+=[1]
# d["key3"]={"k1":1,"k2":2}
# print(d.keys())
# for elm in d:
#     print(d[elm])

# head = {}
# head["head"] = {"value":1, "next":{}}

# def fun(c, p="Hello", d="bob"):
#     print(d)
#
# for n in range(5):
#
#     fun("Bye", d="hi")

# try:
#     a = range(5)
#     for n in range(6):
#         print(a[n])
# except:
#     print("Exception Occurred")

class Human:
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called magic methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self.age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "{name}: {message}".format(
                    name=self.name,
                    message=msg
                )
    def getAge(self):
        return self.age

p1 = Human("Mike")
p2 = Human("Bob")
print(p1.say("Hello"))
print(p2.say("World"))

class Student(Human):

    def __init__(self, name, age, year):
        Human.__init__(self,name)
        self.age=age
        self.year=year

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "{name} {year}: {message}".format(
                    name=self.name,
                    year=self.year,
                    message=msg
                )

p1 = Student("Bob2", 30, 2020)
print(p1.say("Hi"))
print(p1.getAge())
print(p2.getAge())
