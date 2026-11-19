#list
fruits = ["apple", "mango", "kiwi"]
fruits.append("banana")
fruits.insert(1, "berry")
print(fruits)
fruits[2] = "papaya"
print(fruits)
fruits.remove("apple")
print(fruits)
print(fruits[-1])
print(fruits[:2])


#tuple
contact = ("abc", "674647656", 21, "student")
name, number, age, designation = contact
print(age)
print(name)

#set
names = {"abc", "def", "hgi", "abc"}
names.add("xyz")
names.discard("abc")
print(names)


#dict
student = {
  "name" : "ram",
  "dept" : "CSE",
  "age" : 18,
  "cgpa" : 9,
}
print(student["name"])
print(student.get("age"))
student["city"] = "banglore"
student["cgpa"] = 8
student.pop("age")
print(student)
for key, value in student.items():
  print(key, ":", value)
print(student.keys())
print(student.values())



#function
def greet():
  print("welcome")
greet()
def greeting(message):
  print(message)
greeting("welcome")
def add(a,b):
  return a+b
print(add(5,10))

def calc(a,b):
  return a+b,a*b
total, product = calc(10,20)
print(total, product)


#default argument
def greeting(name = "guest"):
  print("welcome", name)
greeting("ram")
greeting()


#keyword
def student_info(name, age, city):
  print(name, age, city)
student_info(age = 25, name = "abc", city = "banglore")


#oops
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    return f"{self.name} says boww"

  def display(self):
    print(f"Name: {self.name}, Age: {self.age}")


dog1 = Dog("moxie", 3)
dog2 = Dog("boxy", 5)
dog1.display()
dog2.display()
print(dog1.bark())


#parent class
class Animal:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(f"Name: {self.name}, Age: {self.age}")

class Dog(Animal):

  def __init__(self, name, age):
    super().__init__(name, age)

  def bark(self):
    return f"{self.name} says boww"

dog1 = Dog("moxie", 3)
dog2 = Dog("boxy", 5)
dog1.display()
dog2.display()
print(dog1.bark())












