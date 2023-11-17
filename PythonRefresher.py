
# variable
x = 1

# conditional statement
if x > 2:
    print('Hello World')
if x <= 1:
    print('Goodbye World')


# Python is case-sensitive. These are all considered different variables:
Pork = 23
PORK = 42
pork = 80


# variables should be mnemonic. Meaning, variables should make sense for humans.
matt_height = 6.9
bill_height = 5.10
nan_height = 6.2


# expressions

    # Addition
aa = 3 + 3
    # Subtraction
ss = 4 - 2
    # Multiplication
mm = 8 * 4
    # Division
dd = 5 / 2
    # Power
pp = 3 ** 3
    # Remainder
rr = 10 % 4

# Type

    # string
'its me'
    # integer
10
    # floating point number
3.9


# Type Conversions

# float - converts to floating point number
orc = 30
print(float(orc))


# converting user input - Type in a name to be greeted
name = input("Enter your name")
print("Hello " + name)


# concatenation

print("Farewell" + " Planet")



# comparison operators

L = 20

# < Less than
if L < 20 :
    print('Less Than')

# <= Less than or Equal to
if L <= 20 :
    print('Less Than or Equal to')

# == Equal to - Asks if a value is equal to another value.
if L == 20 :
    print('It is Equal')

# >= Greater than or Equal to
if L >= 20 :
    print('Greater Than or Equal to')

# > Greater than
if L > 20 :
    print('Greater Than')

# != Not equal
if L != 20 :
    print('Not Equal')


# Nested Decisions
uuu = 298
if uuu > 49 :
    print('more than 49')
    if uuu < 49 :
        print('Less than 100')
print('Nested')


#Two-way Decisions with else:

zil = 239

if zil > 238 :
    print('Huge')
else :
    print('smaller')


# Multi-way

pol = 302

if pol == 230 :
    print('oh no')
elif pol < 200 :
    print('yowza')
else :
    print('there it is')


# Try - Skips to except if try condition isn't met.

bbb = 233

try:
    bbb == 200
    print('This is a string')
except:
    bbb > 200
    print('Oh')



# Try - Tries a conversion then uses the except if it fails.

astr = 'Hello Bob'

try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)


# Try example - Put in hours and rate to determine pay.
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print(xp)

# Try example 2 - Put in value to get grade.
score = input("Enter Score: ")
try:
    scored = float(score)
    if scored >= 0.9:
        print("A")
    elif scored >= 0.8:
        print("B")
    elif scored >= 0.7:
        print("C")
    elif scored >= 0.6:
        print("D")
    else:
        print("F")
except ValueError:
    print("Please enter a value between 0 and 1.")


# def - Creates your own function to easily reuse. Example:

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

try:
    hrs = float(input("Enter Hours: "))
    rate_per_hour = float(input("Enter Rate per Hour: "))
    total_pay = computepay(hrs, rate_per_hour)
    print("Pay:", total_pay)
except ValueError:
    print("Please enter valid numerical values for hours and rate.")




# Infinite Loop

# n = 5

# while n > 0 :
#    print('Doug')
#    print('Funnie')


# iteration - Example with friend as the iteration

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')
