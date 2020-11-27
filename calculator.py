try:
    num_1 = int(input("enter a digit: "))
    num_2 = int(input("enter a digit: "))
except:
    print("you did not enter a digit, please try again")
    exit()

user_input = input("choose +,-,* or /")

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
    print("Something went wrong, try again")
    exit()

if 1 <= result < 50:
    print("less than 50")
elif result == 50:
    print("Fifty")
elif 50 < result < 100:
    print("Almost a hundred")
elif result == 100:
    print("Spot on!")
else:
    print("Result is out of range!")
