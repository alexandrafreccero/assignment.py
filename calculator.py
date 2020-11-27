'''
start try catch block before user input. 
get two numbers from user: num1 and num2
input 3 from user= let user choose +*-/
if stements :  answer= +  = num1 + num2
if input == "+":
    do smth
elif input == ...

create function/method that iterates list;[] 0-50,50-100
# create if elif 
# answer in first loop, iterates for loop list [] 0-50,50-100, 100and decides answer
answer leads to print line:
1<50 printa ”Less then fifty”
50 printa ”Fifty”
mer än 50 men mindre än 100 ”Almost a hundred”
100 printa ut ”Spot on!”
mer än 100 printa ”Missed the spot!”
add elif: retry
end with catch exception  "Something went wrong, retry"
'''
try:
    num_1 = int(input("enter a digit: "))
    num_2 = int(input("enter a digit: "))
except:
    print( "you did not enter a digit, please try again")
    exit()

user_input = input(" choose +,-,* or /")

result = None
if user_input == "+":
    result = num_1 + num_2
elif user_input == "-":
    result = num_1 - num_2
elif user_input == "/":
    result = num_1 / num_2   
elif user_input == "*":
    result = num_1 * num_2 
else: 
    print(" Something went wrong, try again")
    exit()

# everything below could be in a function

if result >= 1 and result < 50:
    print("less than 50")
elif 50 < result and result < 100:
    print("Almost a hundred")
elif result == 50:
    print("Fifty")
elif result == 100:
    print("Spot on!")
else:
    print(" Result is out of range.")



