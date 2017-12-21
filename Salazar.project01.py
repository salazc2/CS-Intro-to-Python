# Christopher Salazar, 2nd of October 2015
#CSC 110 Fall 2015
# Water analysis report

# User interface input
initials = input('Enter your initials:' )
report_date = input('Enter date for report:' )
arsenic_level = (input('Enter arsenic level found:'))

print()

# Outpout of water analysis
print('Water Analysis Report:')
print()
print('Contaminant\tResults\tUnits\tMCL\tDate\t\tAnalyst')

#amount of characters for the row of info on each column
#Contaminant = 11, Results = 7, Units = 5, MCL=3, Date = 4, Analyst = 7

print('-----------\t-------\t-----\t---\t----\t\t-------')

#Results of the Water analyst report with input
print('Arsenic','\t',arsenic_level,'\t','ug/L','\t','10','\t', report_date,'\t',initials)
      


print()
print()
print()
print()


print('* \"MCL\" stands for Maximum Contaminant Level (as determined by the EPA).')
print('* ug/L indicates micrograms per liter.')

# Summary:

# The way I began to work on this project was to do a small outline with comments
#on what would go where. I also made sure my comments made sense in explaining what
#my code is trying to put out. The place that I got stuck was aligining the characters
#in the water analysis report output. I could not get the outputs of the date, arsenic level
#and initals to align precisely with the previous two rows.

# I tested the program two lines at a time to make sure I knew what was going right and
#what was not. I used various methods in chapter section 2.8 in trying to align my columns
#correctly. The spacing was not working for me very well and the book only gave
#a few ways of fixing this issue. Using \t, sep='', or end=''. I tried just pressing enter
#on every input question and the results were badly aligned with the skipped inputs. I also tried typing print and
#end='' for each output line but it was still miss aligned just as using \t or sep=''.
#I also tried spacing to have every column to have at least 12 characters but the format
#didn't work. I tried the spacing width format function of ex: '12.f' but I realized that it
#only worked for numbers and not letters so that the initals and date are not too long but I did
#try format ('12') which worked with letters but the alignment was bad. I ended up adding another \t
#after the date because that was the only output that was too long. There will be some problems if
#the date is written in letters which would make the alignment wrong compared to numbers.

#What I learned from this assignment is that it will take some sort of logical processing for me
#in thinking of ways to make things look neat and precise. I would like to learn more about formatting and
#making things a cleaner. Next time I will do some sort of flowchart to be better prepared in my thought
#process. 


