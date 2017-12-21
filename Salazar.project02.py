#Christopher Salazar
#10/12/2015
# This program calculates the amount of supplies needed to buy given
#the number of customers the pizza company expects.
import math #

#Input number of customers expected
expected_clients = int(input('How many customers do you expect? '))

print()
#Calculations of the amount of supplies used
#amount of sizes of pizza per number of customers
number_of_pizzas = expected_clients * 1.5
amount_Large_pizzas = number_of_pizzas *.75
amount_medium_pizzas = number_of_pizzas *.15
amount_small_pizzas = number_of_pizzas *.10
#size of pizza per square inch A=pi*r^2 total per size
large_Pizzasize = (3.14 * 9**2) * amount_Large_pizzas
medium_Pizzasize = (3.14 * 6**2) * amount_medium_pizzas
small_Pizzasize = (3.14 * 4.5**2) * amount_small_pizzas
total_sqrinch = large_Pizzasize + medium_Pizzasize + small_Pizzasize
#Dough (lb) used per sqr inch
total_dough = total_sqrinch * (1/70)
#Cheese (lb) used per sqr inch
cheese_total = total_sqrinch * (1/60)
#Sauce (oz) used per sqr inch
sauce_total = total_sqrinch * (1/5)
oz_per_can = 96/10
cans_of_sauce = (sauce_total)/ oz_per_can
#Pepperoni (lb) used per sqr inch
#65 percent of total pizza is pepperoni
pepperoni = (total_sqrinch * .65) * (1/64)
#Garlic oil (oz) per linear inch C = pi*d
garlic_largeP = (3.14*18) * (1/64)
garlic_mediumP = (3.14*12) * (1/64)
garlic_smallP = (3.14*9) * (1/64)
garlic_totallarge = amount_Large_pizzas * garlic_largeP
garlic_totalmedium = amount_medium_pizzas * garlic_mediumP
garlic_totalsmall = amount_small_pizzas * garlic_smallP
total_garlic = (garlic_totallarge + garlic_totalmedium + garlic_totalsmall)/oz_per_can

# Output of the number of ingridients by number of customers
print('Supplies for', format(expected_clients, ','), 'customers:',)
print('Dough (lbs):\t', format(math.ceil(total_dough), '7,'),sep='')
print('Sauce (cans):\t', format(math.ceil(cans_of_sauce), '7,'),sep='')
print('Cheese (lbs):\t', format(math.ceil(cheese_total), '7,'),sep='')
print('Pepperoni (lbs):', format(math.ceil(pepperoni), '7,' ),sep='')
print('Garlic oil (cans):', format(math.ceil(total_garlic), '5,'),sep='')

#cheese_pizza = (number_of_pizzas * .35) - not important since all pizzas have cheese

#   I first wrote down a pseudocode to get my thought wrapped around how to calculate
#all the ingredients needed to have Pete's Pizza running. I felt if I just did the assignment
#on the fly that I would probably type too much information in the code and somehow
#make it complicated. The begining is where I got stuck, trying to figure out how to multiply
#what. I first started to multiply every size with the fraction of pound or ounce of ingredient
#separately which was adding too many lines and felt that maybe I could make this smaller.
#Also trying to figure out the percentage of pepperoni used in the problem gave me some
#issues. I was typing too much for each different size and I was getting confused. I was able
#to figure it out by just getting the total square inches of pizza ordered and multplying that with
#the percentage of pepperoni to get the total square inch needed. I did run into an alignment issue but
#I was able to fix that by using a combination of \t and format.

#   I tested my program supply by supply. As soon as I thought I figured out the math in getting the
#right amount of ingredients I would then add the output value and see if it made sense. I did minor
#mistakes from my point of view where I kept forgetting a comma to separate things or a parentheses.
#I would like to learn more of different ways to come up with the math. I feel like I am missing something
#even though I'm using all the suggestions giving in the book and the examples provided on moodler. Also
#my format could use work. I would like to learn more of formatting to make it look more presentabl as I think
#that I didn't do much testing and that an error will pop out where I was not expecting.

#I did run into an error when just pressing enter when asking 'How many customers do you expect?' There was another
#error when entering letters but that is because I set up the input as int.

#   I learned a lot more of how useful programming can be to just do somewhat simple calculations for a real
#business that could use this type of program. I got more comfortable in typing the code and feel more encouraged.
#I just hope my calculations were done correctly. I don't think I would do anything differently on the next project.
#I just need to keep practicing so everything that we are learning as we go I remember and not overlook or forget. 
