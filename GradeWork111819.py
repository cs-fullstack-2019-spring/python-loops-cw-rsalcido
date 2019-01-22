# Exercise 1:
#
# Print -20 to and including 50. Use any loop you want.
#
def main():
#     number1()
#     number2()
#     problem3()
    problem4()
# # #
# def number1():
#     for num in range (51):
#         if num %2==-20:
#             print(num)
#
#
#
#
# if __name__ == '__main__':
#     main()


#
#     Exercise 2:

# Create a loop that prints even numbers from 0 to and including 20.
# def number2():
#     for num in range(21):
#         if num %2 ==0:
#             print(num)


# Exercise 3:
#
# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.

#
# def problem3():
#     a= int(input("Please enter a number"))
#     b= int(input("Please enter a number"))
#     c= int(input("Please enter a number"))
#     n = (a+b+c)
#     print(a, "+", b, "+", c, "=", n)



# Exercise 4:
#
# Password Checker - Ask the user to enter a password.
# Ask them to confirm the password. If it's not equal, keep asking until it's correct or they enter 'Q' to quit.


def problem4():
    pass1= input(" Please enter your password.")
    password=""
    attempt=0



    while(attempt != "Q"):
        password=input("Please enter your password")
        if(password =="Q"):
            break


if __name__ == '__main__':
    main()