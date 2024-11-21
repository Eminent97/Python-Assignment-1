user_input1 = int(input("Please enter a number: "))
operation = input("Please Enter an operator(+, -, /, *, %, **,): ")
user_input2 = int(input("Please enter another number: "))

if operation == '+':
    result = user_input1 + user_input2
    print(f"{user_input1} + {user_input2} = {result}")

elif operation == '/':
    result = user_input1 / user_input2
    print(f"{user_input1} / {user_input2} = {result}")

elif operation == '-':
    result = user_input1 - user_input2
    print(f"{user_input1} - {user_input2} = {result}")

else:
    result = user_input1 * user_input2
    print(f"{user_input1} * {user_input2} = {result}")