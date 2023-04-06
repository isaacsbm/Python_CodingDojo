#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Will return the number 5 since the function is being asked to exit and return 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# This code is being incorrectly called, the corrected code is below: 
def number_of_military_branches():
    return 5
print(number_of_military_branches())
# This will correctly call the function, as there is no function called  "number_of_days_in_a_week_silicon_or_triangle_sides"

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# This will print 5 as the return statement tells our code to exit right away and ignore the rest of the code

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Again, this will print 5 as the return statement tells our code to exit right away and ignore the rest of the code

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# This will print 5 for the function and then none as you are not calling anything into the parameter inside "x"

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# This will print first inside the function 3 and 5 instead of adding the two as you would like. In order to correctly call it as you
# would like it to. In order to correctly call the function, use a return statmenet with b+c:
def add(b,c):
    return b+c
print(add(1,2) + add(2,3))

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Will print 25 because you are returning the total of b and c together. However, you are calling the string of both as well which
# can be used to change the value of the item, so you could call a different class in your print statement without getting an error

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# The aboe code has an issue with indentation, the corrected code is below:
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Return 7 does not need to be included since there is no if,else,elif statement to consider it. 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# This will print first 7, then 14, then 21. You running through the statment if b<c  return 7 else return 14, return 3 is not considered
# since there is no elif, else, or if statement surronding it. The last print statmenet adds the function twice togther

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Will return b+c which is 8 here, ignoring return 10 as you are exiting the function right after you run the return

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# You will print, 500, 500, 300, and then 500. First you are printing b which is 500, then you run the functions which sets b to 300
# and prints it again but you are printing b from outside the function because the function is not being called  so it is 500
# Finally you print b set to 300 and then you call b again but this time after the function  is called which resets to 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# You are printing 500,500,300,and 500 again same as above but this time returning b in the function

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# You are printing 500,500,300,and 300 this time because you are setting b to the function

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# You are printing 1,3,5 as they are all printed and bar() is 3 so you will print it inside the function foo() as called
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# You are printing 1,3,5, and 10. When you call y which is set to foo() you run the function foo which print 1, runs x=bar() which is
# printing 3 then returning 5 and then finally exiting the function with a return 10.
