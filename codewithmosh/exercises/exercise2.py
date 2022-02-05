# def fizz_buzz(input):
#     if (input % 3) == 0:
#         message = "Fizz"

#     elif (input % 5) == 0:
#         message = "Buzz"

#     if (input % 3) == 0 and (input % 5) == 0:
#         message = "FizzBuzz"

#     else:
#         message = input

#     return message

def fizz_buzz(input):

    if (input % 3) == 0 and (input % 5) == 0:
        return "FizzBuzz"

    elif (input % 3) == 0:
        return "Fizz"

    elif (input % 5) == 0:
        return "Buzz"

    else:
        return input


print("Start.")
print(fizz_buzz(15))
print("Done.")
