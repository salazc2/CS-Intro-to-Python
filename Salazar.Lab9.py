#Christopher Salazar
#CSC 110, Lab 9
#The program asks the user for his/her age, and handles exceptions assigning it a value of -99.


def main():

    try:
        userAge = int(input('What is your age? '))

    except ValueError:
        userAge = -99
        print(userAge)

    else:
        print(userAge)


main()







#------------------------------instructions-----------------------------------------------

#Write a program that uses Exception Handling.  The program should ask the
#user for his/her age, storing the integer result in a variable called userAge.
#If the string-to-integer conversion generates an exception, assign the value -99
#to userAge.  If the conversion succeeds, the user's age should be successfully stored
#in userAge.

#Examples:

#User enters                    userAge (integer), at end of program
#29                                  29
#thirty                              -99
