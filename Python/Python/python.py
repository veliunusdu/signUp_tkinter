import keyword
import time
import math
import random

#String
from operator import truediv
"""
first_name = "veli"
surname = "unusdu"
print(first_name)
print(f"ismi: {first_name}")

#integer
age =25
quantity = 3

print(f"you are {age} years old")
print(f"you are buying {quantity} items")

#float
price = 10.99
print(f"the price is ${price}")

#boolean
is_student = False  #capital letter first
if is_student:
    print("you are a student")
else:
    print("you are not a student")



# data type can be learned
x = 5
print(type(x))


x = "Python "
y = "is "
z = "awesome "

x = "awesome"
def myFunc():
    print("python is"+ x)


x = 1
y = 2.8

# Convert from int to float
a = float(x)

# Convert from float to int
b = int(y)

print(a)
print(b)


#display a random number
import random
print(random.randrange(1, 10))


#You can use double or single quotes:
print("Hello")
print('Hello')
#Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
"""



"""
name = input("enter your name: ")
result = len(name)
print("the length of name is: " + str(result))

name = name.replace("-", "")
print(name)


name = input("what is your name?")
age = input("how old are you?")
age = int(age)
age = age + 1
print(f"you are {age} years old")

"""




"""
#Slicing
b = "helloworld"
print(b[0:6]) #6 is not included
print(b[-3:-1]) # Negative indexing

# input can be writen in the bracket
age = 36
txt = f"My name is John, I am {age}"
print(txt)

bool("helloo") #default true

is_active = True
if is_active:
    print("it is active")

def myFunction() :
  return True
print(myFunction())


x=5
print(x>3 and x<10)# returns True
print(x>3 or x<10)# returns True
print(not(x>3 and x<6))# returns False (if not)

x="merhaba"
y="merhaba"
if(x is y): #is not
    print("they are same")
"""


'''
fruit = ["apple","orange","banana"]
print(fruit)
print(fruit[2])
print(fruit[0:3]) # 0 to 3 (3 is excluded)
fruit[0] = "pineapple" #changeable

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

print(fruit.index("banana"))

print(len(fruit))

if "banana" in fruit:
    print("yes it is in this list")

fruit.insert(2, "watermelon")
print(fruit)

fruit.append("orange") # add orange at the end of the list

fruit.remove("banana") #Remove the object
fruit.pop(1) # delete specified item
'''



""" finding area
length = input("enter the length")
width = input("enter the width")
length = int(length)
width = int(width)
area = length * width
print(f"the area is {area} cm^3")
"""


"""  adjective game
adjective1 = input("enter an adjective (description):")
noun1 = input("enter a noun(person,place, thing): ")
adjective2 = input("enter an adjective ( description): ")
verb1 = input("enter a verb ending with'ing'")
adjective3 = input("enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo")
print(f"İn an exhibit, I saw a {noun1}")
print(f"{noun1} was { adjective2} and {verb1}")
print(f"I was {adjective3}")
"""

""" finding circumference
radius = float(input("enter the radius of a circle: "))
circumference = 2* 3.14* radius
print(f"the circumference is: {round(circumference)}")
"""

""" if else statement
age = int(input("enter your age :"))
if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You have not been born yet")
else:
    print("You must be 18+ to sign up")
"""

""" temperature converting
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement.")
"""

"""
temp = -5
isSunny = True

if temp >= 28 and isSunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and isSunny:
    print("It is cold outside")
    print("It is sunny")
elif temp < 28 and temp > 0 and isSunny:
    print("It is warm outside")
    print("It is sunny")
else:
    print("It İS too hot, don't go outside")
"""


"""  even odd number
number = int(input("enter a number: "))
number = "EVEN" if number % 2 == 0 else "ODD"
print(number)
"""

"""  one line conditional statement
userRole = "guest"
accessLevel = "full access" if userRole == "admin"  else "Limited access"
print(accessLevel)
"""


"""
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can not be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can not be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can not be less than or equal to zero")

print(principle)
print(rate)
print(time)

total = principle * pow((1+rate/100),time)
print(f"Balance after {time} years: {total:.2f}")
"""

"""
for x in reversed(range(1, 11, 2)):
    print(x)
print("Happy new year")

for y in range(1, 21):
    if y == 13:
        break
    else:
        print(y)
"""


'''
myTime = int(input("Enter the time in seconds: "))
for x in reversed(range(0, myTime)):
    print(x)
    time.sleep(1)   #time sleep saniyeler arası farkın bir olmasını sağlar o olmazsa direkt 54321 yazılır gider ama o varsa her rakam arası bir saniye beklenir
print("Time is up")

'''

'''
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()
'''



'''
numbers = [1,2,3,4,5]
print(numbers[1])
numbers.append(6)
numbers.extend([60,70])  #birden fazla ekleme
numbers.remove(3)
numbers.pop()  #son elemanı siler
len(numbers)        # Eleman sayısı
sum(numbers)        # Sayıların toplamı
min(numbers)        # En küçük
max(numbers)        # En büyük


s = {1,2,2,3}
print(s)  # {1, 2, 3}
s.add(4)
s.update([5, 6])


my_tuple = (1, 2, 3)
print(my_tuple)  # (1, 2, 3)
my_tuple[0] = 10  # ❌ Hata verir: 'tuple' object does not support item assignment
'''




'''
questions= ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in the atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")
options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. horse","D. elephant"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))
answers= ("C","D","A","A","B")
score = 0
guesses = []
question_num = 0


for question in questions:
    print("--------------")
    print("--------------")
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------")
print("    Result    ")
print("---------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions)*100)
print(f"Your score is: {score}%")
'''



'''
capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})
capitals.pop("China")

keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
    print(values)

print(capitals.get("India"))
'''




'''
menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":6.00,
        "fries":2.50,
        "chips":1.00,
        "pretzel":3.50,
        "soda":3.00,
        "lemonate":4.25}

cart = []
total = 0
print("------MENU------ ")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------")
while True:
    food = input("Select an item(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total+menu.get(food)
    print(food, end=" ")

print()
print(f"total is: ${total:.2f} ")
'''


'''
low = 1
high = 20
number = random.randint(low, high)
#number = random.random()  0-1 arası random işler
print(number)
'''



'''
lowestNum = 1
highestNum = 100
answer = random.randint(lowestNum, highestNum)
guesses = 0
isRunning = True
print("----------------")
print("Python Number Guessing Game")
print(f"Select a number between {lowestNum} and {highestNum}")

while isRunning:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowestNum or guess > highestNum:
            print("That number is out of range")
            print(f"Please select a number between {lowestNum} and  {highestNum}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses {guesses}")
'''



'''
import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose.")

    if input("Play again? (y/n): ").lower() != "y":
        running = False
        print("Thanks for playing!")
'''





'''
def happyBirtdday(name, age):
    print(f"HappyBirtday to {name}")
    print(f"You are {age} years old")

happyBirtdday("Bro", 20),
happyBirtdday("Veli", 22),



def add(x, y):
    z = x + y
    return z

def substract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(substract(10,2))
print(divide(10,2))
print(multiply(10,2))



def createName(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

fullName = createName("veli", "ünüşdü")
print(fullName)
'''


'''
default arguments
def netPrice(listPrice, discount=0, tax=0.05):
    return listPrice*(1-discount)*(1+tax)

print(netPrice(500))
print(netPrice(500, 1,0))
'''


'''
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")
count(30,15)



def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
hello("hello", title="mr", last="squarepants", first="spongebob")


for x in range(1, 11)
'''


'''

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}")

# Example usage:
shipping_label("Dr.", "SpongeBob", "Squarepants",
               street="124 Conch Street",
               city="Bikini Bottom",
               state="Pacific Ocean",
               zip="12345")
'''


'''

numbers= [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number, end="-")
'''

'''
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit, end=" ")
'''


'''
students = {"Spongebob", "Patrick", "Squidward"}
student = input("enter a student name:")
if student in students:
    print(f"{student} is in the class")
else:
    print(f"{student} was not found")
'''


'''
grades = {"Sandy":"A",
          "Squidward":"B",
          "Spongebob":"C",
          "Patrick":"D"}
student = input("Enter a student name:")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else: 
    print(f"{student} was not found")
'''

'''
doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

doubles = [x*2 for x in range (1,11)]
print(doubles)
'''

'''
numbers = [1,-3,2,-5,4,6,-7,8]
positive_nums = [num for num in numbers if num > 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]
print(positive_nums)


grades = [82,45,67,89,90,100,76]
passing_grades = [grade for grade in grades if grade >= 70]
print(passing_grades)
'''



''' switch case
def day_of_week(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is monday"
        case 3:
            return "It is tuesday"
        case 4:
            return "It is wednesday"
        case 5:
            return "It is thursday"
        case 6:
            return "It is friday"
        case 7:
            return "It is saturday"
        case _:
            return "NOt a valid day"

print(day_of_week(1))
'''

'''
import myModule
print(myModule.greet("Spongebob"))
'''



'''
sum_even_digits = 0
sum_odd_digits = 0
total = 0

card_number = input("enter your card number: ")
card_number = card_number.replace(" ", "")
card_number = card_number.replace("-", "")
card_number = card_number[::-1]  #reverse the string
print(card_number)

for x in card_number[::2]:
    sum_odd_digits += int(x)

for x in card_number[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("valid")
else:
    print("invalid")ı
'''



'''banking app
def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: $"))
    if amount < 0:
        print("Deposit amount cannot be negative.")
    else:
        print(f"Depositing ${amount:.2f} to your account.")

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > balance:
        print("Insufficient funds for this withdrawal.")
    elif amount < 0:
        print("Withdrawal amount cannot be negative.")
    else:
        print(f"Withdrawing ${amount:.2f} from your account.")
        balance -= amount

balance = 0
is_running = True

while is_running:
    print("Bank Account Menu")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice =="1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Exiting the program.")
        is_running = False
    else:
        print("Invalid choice. Please try again.")
'''



''' slot machine
import random

def spin_row():
    symbols = ["🍒", "🍋", "🍉", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍋":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "⭐":
            return bet * 10
    return 0
def main():
    balance = 100

    print("*****************************")
    print("Welcome to the Slot Machine! ")
    print("Symbols: 🍒, 🍋, 🍉, 🔔, ⭐")
    print("******************************")
    print(f"Your starting balance is: ${balance}")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Enter you bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet =  int(bet)

        if bet > balance:
            print("Insufficient balance")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost this round")
        
        balance += payout

    print(f"Game over! You ran out of money.")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
'''



''' adam asmaca
import random

words = ("apple", "orange","banana","coconut","pineapple")

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", "/  ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def display_man(wrong_guesses):
    print("*********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer():
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    is_running = True

    while is_running:
        display_man(wrong_guesses) 
        display_hint(hint)
        guess = input("Guess a letter:").lower()
       
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("Congratulations! You guessed the word!")
            is_running = False
        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            print(f"Game over! The word was '{answer}'.")
            is_running = False

if __name__== "__main__":
    main()
'''


'''
from Car import Car
car1 = Car("Toyota", 2020, "red", True)
car2 = Car("Honda", 2019, "blue", False)
car3 = Car("Ford", 2021, "black", True)

car1.drive()
car2.stop()
'''

''' İnheritance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass

dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")
mouse = Mouse("Mickey", "Mouse")


print(dog.name)
dog.eat()
dog.sleep()
'''



'''
class Animal:
    def eat(self):
        print("The animal is eating!")

    def sleep(self):
        print("The animal is sleeping!")
    

class Prey(Animal):
    def flee(self):
        print("The prey is fleeing!")

class Predator(Animal):
    def hunt(self):
        print("The predator is haunting!")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class Fish(Prey, Predator):
    def swim(self):
        print("The fish is swimming!")

rabbit = Rabbit()
awk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()
rabbit.eat()
fish.sleep()
'''


'''
from abc import ABC

class Vehicle(ABC):

    def go(self):
        print("The vehicle is going")


    def stop(self):
        print("The vehicle has stopped")

class Car(Vehicle):

    def go(self):
        print("The car is going")

    def stop(self):
        print("The car has stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("The motorcycle is going")

    def stop(self):
        print("The motorcycle has stopped")  

motorcycle = Motorcycle()
motorcycle.go()
'''


'''
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color,filled, width, height):
        super().__init__(color, filled)
        self.height = height
        self.width = width

circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=4)
print(circle.color, circle.filled)
'''



''' polymorphism
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height
    
shapes = [Circle(6), Square(8), Triangle(7, 5)]

for shape in shapes:
    print(f"{shape.area()}cm^2")  # This will print the area of each shape")
'''


''' Nested classes
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"
        
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee = []
    
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employee.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employee]

company = Company("TechCorp")
company.add_employee("Alice", "Software Engineer")
company.add_employee("Bob", "Data Scientist")

for employee in company.list_employees():
    print(employee)
'''


''' static methods
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

result1 = MathOperations.add(5, 10)
result2 = MathOperations.multiply(5,10)
print(f"Addition: {result1}, Multiplication: {result2}")
'''


''' magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Example usage:
v1 = Vector(5, 4)
v2 = v1 * 2
print(f"v2.x = {v2.x}, v2.y = {v2.y}")
'''

''' property
class Temperature:
    def __init__(self, celcius):
        self._celcius = celcius

    @property
    def celcius(self):
        return self._celcius
    
    @celcius.setter
    def celcius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celcius = value

    @celcius.deleter
    def celcius(self):
        del self._celcius

    @property
    def fahrenheit(self):
        return (self._celcius * 9/5) + 32
'''

''' lambda functions
def square(x):
    return x**2

square = lambda x: x**2
print(square(5))


def apply_operation(func, value):
    return func(value)

result = apply_operation(square, 10)
print(f"The result is: {result}")
'''


'''
def c_to_f(temp):
    return (temp*9/5) + 32

celcius = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = list(map(c_to_f, celcius))
print(f"The temperatures in Fahrenheit are: {fahrenheit_temps}")
'''



''' filter functions
grades = [91,32, 83, 44 ,75, 56, 67]

passing_grades = list(filter(lambda grade: grade >= 60, grades))
print(passing_grades)
'''

''' reduce functions
from functools import reduce
prices = [19.99, 5.49, 3.99, 12.99, 7.49]
total = reduce(lambda x, y: x + y, prices)
print(f"The total price is: ${total:.2f}")
'''

''' sorting dictionaries
fruits = {"apple": 105, "banana": 73, "cherry": 69, "date": 354, "elderberry": 247}
fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))
print(fruits)
'''


''' exception handling
try:
    number = int(input("enter a number:"))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Please enter a valid number")
except Exception:
    print("An unexpected error occurred")
finally:
    print("This will always execute, regardless of an error")
    '''

''' time module
import time
start_time = time.perf_counter()
for i in range(1000000):
    pass

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
'''



'''multithreading
import threading
import time

def walk_dog():
    time.sleep(3)
    print("Dog walked")

def take_out_trash():
    time.sleep(2)
    print("Trash taken out")

def get_mail():
    time.sleep(4)
    print("Mail collected")

chore1 = threading.Thread(target=get_mail)
chore1.start()

chore2 = threading.Thread(target=walk_dog)
chore2.start()

chore3 = threading.Thread(target=take_out_trash)
chore3.start()

print("All chores are being done in parallel")
'''



'''
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": data.get("name", "Unknown"),
            "temperature": data.get("main", {}).get("temp", "N/A"),
            "description": data.get("weather", [{}])[0].get("description", "N/A").capitalize(),
            "humidity": data.get("main", {}).get("humidity", "N/A"),
            "wind_speed": data.get("wind", {}).get("speed", "N/A")
        }

        return weather

    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP Error: {e}"}
    except requests.exceptions.RequestException:
        return {"error": "Network error or invalid response"}

# --- Example usage ---
API_KEY = "5cb60781d36ba9675161ad1ffabf2d3e"  # ← Replace this with your actual key
city_name = input("Enter city name: ")
weather_info = get_weather(city_name, API_KEY)

if "error" in weather_info:
    print("Error:", weather_info["error"])
else:
    print(f"\nWeather in {weather_info['city']}:")
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Condition: {weather_info['description']}")
    print(f"Humidity: {weather_info['humidity']}%")
    print(f"Wind Speed: {weather_info['wind_speed']} m/s")
'''


''' PyQt5 GUI Application
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI Application")
        self.setGeometry(0, 0, 400, 300)  # x, y, width, height

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
'''

'''
from tkinter import * 

count = 0  # Initialize count before using it

def click():
    global count
    count += 1
    print(count)

window = Tk()
button = Button(window,
                text = "Click me",
                command = click,
                font = "Arial 20 bold",
                fg = "blue", 
                activeforeground = "red",
                activebackground = "yellow",)

button.pack()
window.mainloop()
'''

'''
from tkinter import * 

def Submit():
    username = entry.get()
    print("Hello"+username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()
entry = Entry(window,
               width=30,
               font="Arial 20 bold",
               fg="blue",
               bg="yellow",
               justify=CENTER)

entry = Entry(window,
              font="Arial 20 bold",
              fg="blue",
              bg="yellow",
              justify=CENTER,
              show="")

entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=Submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
'''

'''
from tkinter import * 

def display():
    if(x.get() == 1):
        print("You agreed to the terms and conditions")
    else:
        print("You did not agree to the terms and conditions")

window = Tk()
x = BooleanVar()

window.title("Checkbox Example")
window.geometry("500x500")
pyton_photo = PhotoImage(file="C:/VsCode/Python/Python/python.png")  # Use a valid image file path
window.pyton_photo = pyton_photo  # Keep a reference to prevent garbage collection

check_button = Checkbutton(window,
                           text="I agree to the terms and conditions",
                           font="Arial 20 bold",
                           variable = x,
                           onvalue=1, 
                           offvalue=0,
                           command=display,
                           image=pyton_photo,
                           compound="left",)
check_button.pack()
window.mainloop()
'''



'''
from tkinter import * 
food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered hamburger")
    elif(x.get()==2):
        print("You ordered hotdog")
    else:
        print("You did not order anything")

window = Tk()
x = IntVar() 
for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                             text=food[index], # add text to radio buttons
                             variable=x,       # groups radiobuttons together
                             value=index, 
                             padx = 30,
                             indicatoron=0, 
                             width = 375,
                             command=order) # add padding to the left
   
   
    radiobutton.pack(anchor=W) # anchor=W aligns the radiobuttons to the left
window.mainloop()
'''


''' scale
from tkinter import * 
def submit():
    print("The temperature is: " + str(scale.get()) + "°C")

window = Tk()
scale = Scale(window, from_=100, to=0, length=300,orient=HORIZONTAL)
scale.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
'''


''' listbox
from tkinter import *
window = Tk()
listbox = Listbox(window,
                  bg="lightgray",
                  fg="blue",
                  font="Arial 20 bold",
                  selectbackground="red")
listbox.pack()

listbox.insert(1, "apple")
listbox.insert(2, "banana")
listbox.insert(3, "cherry")
listbox.insert(END, "orange")  # Add at the end
listbox.insert(0, "kiwi")  # Add at the beginning

listbox.config(height=listbox.size(), width=20)  # Set height to the number of items

def submit():
    selection = listbox.curselection()
    if selection:
        print(listbox.get(selection[0]))
    else:
        print("No item selected")

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()
window.mainloop()
'''

''' mesaagebox
from tkinter import * 
from tkinter import messagebox
def click():
    answer = messagebox.askyesno(title="ask ok cancel", message="Do you want to continue?")
    if answer:
        print("You clicked OK")
    else:
        print("You clicked Cancel")
window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()
window.mainloop()
'''


''' colorchooser
from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor(title="Choose a color")
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)  # Change the background color of the window

window =Tk()
window.geometry("500x500")
button = Button(window, command=click, text="Choose a color")
button.pack()
window.mainloop()
'''

''' text area
from tkinter import *

def submit():
    input = text.get("1.0", END)  # Get all text from the Text widget
    print(input)

window = Tk()
text = Text(window,
            bg="lightgray",
            fg="blue",
            font="Arial 20 bold",
            width=30)
text.pack()
button= Button(window, text="Submit", command=submit)
button.pack()
window.mainloop()
'''

''' tkinter menu
from tkinter import * 

def openFile():
    print("Open file dialog would be implemented here")
def saveFile():
    print("Save file dialog would be implemented here")
def quit():
    print("Exiting the application")
    window.quit()

window =Tk()
menubar = Menu(window)
window.config(menu=menubar)

fileMenu= Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


window.mainloop()
'''


''' tkinter frame
from tkinter import *

window = Tk()

frame= Frame(window, width=300, height=300, bg="lightblue")
frame.place(x=100, y=100)

Button(window, text="W", font=("Consolas",25), width=3).pack(side=TOP)
Button(window, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(window, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(window, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()
'''

''' new window
from tkinter import *

def create_window():
    new_window= Toplevel()
    old_window.destroy()

old_window = Tk()

Button(old_window, text="Create new window", command=create_window).pack()

old_window.mainloop()
'''

''' tabs 
from tkinter import * 
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is Tab 1").pack()
Label(tab2, text="Hello, this is Tab 2").pack()

window.mainloop()
'''

''' grid geometry manager
from tkinter import * 
window = Tk()

firsyNameLabel = Label(window, text="First name: ")
firsyNameLabel.grid(row=0, column=0)
firstNameEntry = Entry(window, width=30)
firstNameEntry.grid(row=0, column=1)

lastNameLabel = Label(window, text="Last name: ")
lastNameLabel.grid(row=1, column=0)
lastNameEntry = Entry(window, width=30)
lastNameEntry.grid(row=1, column=1)

submitButton = Button(window, text="Submit").grid(row=3, column=0, columnspan=2)

window.mainloop()
'''

''' progress bar
from tkinter import * 
from tkinter.ttk import *
import time

def start():
    tasks = 10
    x = 0
    while x < tasks:
        time.sleep(1)
        bar['value'] += 10
        x += 1
        percent.set(f"{int((x/tasks)*100)}%")
        text.set(f"{x}/{tasks} tasks completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()
bar = Progressbar(window, orient=HORIZONTAL, length=200, mode="determinate")
bar.pack(pady=10)
percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

taskLabel = Label(window, textvariable=text)
taskLabel.pack()

button = Button(window, text="download", command=start)
button.pack()

window.mainloop()
'''

''' canvas
from tkinter import * 
window = Tk()

canvas = Canvas(window, height=500, width=500, bg="lightblue")
canvas.create_line(0, 0, 500, 500, fill="red", width=5)
canvas.create_line(0, 500, 500, 0, fill="blue", width=5)
canvas.create_rectangle(50, 50, 450, 450, outline="green", width=5)
canvas.create_oval(100, 100, 400, 400, outline="purple", width=5)
canvas.pack()

window.mainloop()
'''

''' key events
from tkinter import *
def doSomething(event):
    print("You clicked: " + event.keysym)

window = Tk()
label = Label(window, text="Press any key", font=("Helvetica", 100))
label.pack(expand=True, fill="both")

window.focus_set()  # Ensure the window has focus to receive key events
window.bind("<Key>", doSomething)

window.mainloop()
'''

''' mouse events
from tkinter import *

def doSomething(event):
    print("You clicked: " + event.keysym)

window = Tk()

window.bind("<Button-1>", doSomething)
window.bind("<Motion>", doSomething) # Mouse motion event
window.mainloop()
'''

from tkinter import * 
from time import *

def update():
    time_string = strftime("%I:%M:%S")
    time_label.config(text=time_string)
    time_label.after(1000, update)
    

window =Tk()

time_label = Label(window, font=("Arial", 50), fg="blue")
time_label.pack()

update()
window.mainloop()