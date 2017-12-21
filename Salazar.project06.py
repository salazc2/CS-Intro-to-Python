#Christopher Salazar
#project 06
#CSC 110
#This program calculates the payment report of an auto loan when inserting certain data.



#the main function calls the other functions.
def main():

    #calls the getLoanInfo function and returns loanAmount and ratePerPeriod as a variable
    loanAmount, ratePerPeriod = getLoanInfo()

    #calls the loanTermMenu function anad returns the numberOfPeriods as a variable
    numberOfPeriods = loanTermMenu()

    #calls the payment function with parameters and returns the payment amount as a variable
    paymentAmount = payment(loanAmount, ratePerPeriod, numberOfPeriods)

    #calls the displayPmtReport function with paramaters
    displayPmtReport(loanAmount, ratePerPeriod, numberOfPeriods, paymentAmount)


#define function. Asks for loan amount and interest rate
def getLoanInfo():
    loanAmount     = int(input('Enter loan amount: '))
    annualInterest = float(input('Enter annual interest rate: '))
    ratePerPeriod = (annualInterest/100)/12
    return loanAmount, ratePerPeriod
    print()


#define loanTermMenu. Prompts user to choose from menu
def loanTermMenu():
        
    menuChoice = -99
    while menuChoice < 0 or menuChoice > 5:
        print('-' * 20)
        print('Loan report menu')
        print('-' * 20)
        print('1.  One year')
        print('2.  Two years')
        print('3.  Three years')
        print('4.  Four years')
        print('5.  Five years')
        print('0.  Exit')
        print()
        menuChoice = int(input('Choice:'))
        if menuChoice == 0:
            main()              #prompts the user back to getLoanInfo if exits with 0
    numberOfPeriods = menuChoice * 12   # calculates the numberOfPeriods by choosing the years of loans
    return numberOfPeriods
   


#define payment with paramaters that are passed along to calculate paymentAmount, interst paid a month,
#principlepayment and balance that is being subracted by every passing period
def payment(PV, ratePerPeriod, numberOfPeriods):
        
        paymentAmount = (ratePerPeriod * PV) / (1 - (1 + ratePerPeriod)**-numberOfPeriods)

        balance = PV
        interestMonth = format((balance * ratePerPeriod), ',.2f')

        principlePayment = format((paymentAmount - interestMonth), ',.2f')

        balance -= principlePayment

        return paymentAmount,interestMonth, principleAmount, balance


#define displayPmtReport. Prints out the title of the report and then the info from the payment function
#into a way to tell the user how much each period payment is reporting
def displayPmtReport(PV, ratePerPeriod, numberOfPeriods, paymentAmount):
        print('Pmt#', 'PmtAmt','Int','Princ','Balance', sep='     ')
        print('-' * len('Pmt#'), '-' * len('PmtAmt'), '-' * len('Int'), '-' * len('Princ'), '-' * len('Balance'), sep='     ')
        for period in range(1, numberOfPeriods + 1):    #loop starts from first period until the numberOfPeriods from the return of function loanTermMenu
            print(period, paymentAmount, interestMonth, principleAmount, balance, sep='     ')

        
        continueChoice = input('Press <Enter> to continue')
        
        if continueChoice == '':        #if user presses enter, he or she is prompted back to the beginning of the program
            loanTermMenu()

main()




#-------------Testing--------------

#My testing was pretty limited as I was unable to give the proper and complete ouput of the program.
#I got frustrated through the 4 days of working this program. I got confused in how to pass on the
#the appropriate variables to different functions. I kept getting the message of subtracting
#a float and a string. I keept checking that every variable was written the same on every line.
#For the first part of the questions asking for the amount and interest rate, the program would error
#out if I pressed enter or a letter. When asking to choose from the menu, the program will error out if
#I entered a letter or just pressed entered. I couldn't test anymore as I couldn't figure out how to pass
#the variables to the appropriate functions.

#----------------Summary-------------

#I first wrote the pseudocode on paper so I could get a good grasp on where everything connected. I was intimidated
#by the amount of calls needed to be made so I thought it would have been a good idea to start like this.
#I went over the provided material regarding loops and the book to get a better feel of it as the lab
#was a good start to understanding it. I got stuck trying to pass all the variables to the functions and then using  that
#to create a loop in the display report. Unfortunately this time I did not get unstuck.
#It was difficult to figure out the loop for the balance.

#I tried testing the program part by part. I was able to get to display what I wanted up to the loanTermMenu and
#also confirmed that the numberOfPeriods was being returned from the defined function by testing the part on a
#separate file. The loanAmount and ratePerperiod were also being passed along. I couldn't figure out how
#they were not passing along to defined payment.

#Could you please send me the video for this project so I can learn how to create this file. The frustration
#and need to learn how this program's code looks like is very intriguing . Hopefully from the video I can learn
#how to pass along the variables to the functions and creating the loops.

#For the next assignment I will try to get more tutoring at the learning center as I was only able to attend one during
#the week. Please forward me the video for this project when available. Thank you. 


