num1 = 42 #variable declaration: Number
num2 = 2.3 #variable declaration: Number
boolean = True #variable declaration: Boolean
string = 'Hello World' #variable declaration: String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration: List of Strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration: Dictionary of Strings, Numbers, and Booleans
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration: Tuple of Strings
print(type(fruit)) #type check: Tuple
print(pizza_toppings[1]) #List - access value
pizza_toppings.append('Mushrooms') #List - add value
print(person['name']) #Dictionary - access value
person['name'] = 'George' #Dictionary - change value
person['eye_color'] = 'blue' #Dictionary - add value
print(fruit[2]) #Tuple - access value

if num1 > 45: #if
    print("It's greater")
else: #else
    print("It's lower")

if len(string) < 5: #if
    print("It's a short word!")
elif len(string) > 15: #else if
    print("It's a long word!")
else: #else
    print("Just right!")

for x in range(5): #for loop - start
    print(x) 
#end
for x in range(2,5): #for loop - start
    print(x)
#end
for x in range(2,10,3): #for loop - start
    print(x)
#end
x = 0 #variable declaration: Number
while(x < 5): #while loop - start
    print(x)
    x += 1 #increment
#end
pizza_toppings.pop() #List - delete value - end
pizza_toppings.pop(1) #List - delete value - Index 1

print(person)
person.pop('eye_color') #Dictionary - remove value
print(person)

for topping in pizza_toppings: #for loop - start
    if topping == 'Pepperoni': #if
        continue #continue
    print('After 1st if statement')
    if topping == 'Olives': #if
        break

def print_hello_ten_times(): #function - no parameter
    for num in range(10): #for loop - start
        print('Hello')
    #end
print_hello_ten_times() #function call

def print_hello_x_times(x): #function - parameter x
    for num in range(x): #for loop - start
        print('Hello')
    #end
print_hello_x_times(4) #function call - argument 4

def print_hello_x_or_ten_times(x = 10): #function - paramater (x=10)
    for num in range(x): #for loop - start
        print('Hello')
    #end
print_hello_x_or_ten_times() #function call - no argument
print_hello_x_or_ten_times(4) #function call - argument 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)