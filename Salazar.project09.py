#Christopher Salazar
#CSC 110, project 9
# The program maintains a file of friends and his or her ages while handling exceptions
#that might occur



import os

def main():

    #opening the files
    numberOfFriends = open('FriendCount.txt', 'r')
    ageOfFriends    = open('FriendAgeData.txt', 'a')
    numberOfFriends2= open('FriendCount2.txt', 'w')

 

    nameOfFriend = 1

    #the begining of what will be tested if an exception is raise.
    try:

        #this will start the count of how new friends will be added.
        total =0
        #begin the loop as long as nameOfFriend is not empty (pressing enter)
        while nameOfFriend  != '':
            #ask for new friend's name
            nameOfFriend = input('What is your new friend\'s name? ')

            #if user enters a friends name it asks for age
            if nameOfFriend != '':
                newFriendsAge  = int(input('What is your new friend\'s age? '))
                print()
                #write the name and age to the existing FriendAgeData.txt file
                ageOfFriends.write('\n'+ nameOfFriend + '\n')
                ageOfFriends.write(str(newFriendsAge) + '\n')

                #total of new friends added to the FriendCount
                total +=1

        #the loop will add the count already in the FriendCount.txt with the total of new friends and write it to a new file
        for line in numberOfFriends:
            totalCount = total + int(line)
            numberOfFriends2.write(str(totalCount))


    #exception is raised if user tries to write on the only readable FriendCount file.
    except IOError:
        print()
        print('The FriendCount file is only readable.')

    #exception is raised if user enters the incorrect name to write on FriendCount file.
    except NameError:
        print()
        print('The FriendCount file not found.')

    #exception is raised if the item read isn't an integer in FriendCount.          
    except TypeError:
        print()
        print('The item is not an integer.')

    #exception is raised if the user enters anything other than an integer.
    except ValueError:
        print()
        print('Please try whole numbers for friend\'s age. ')

    #exception is raised if any traceback happens while program runs.
    except:
        print()
        print('An error occured. Please try again.')

    #if no exceptions are raised during input of names and ages.       
    else:
        print('Additions to FriendAgeData file completed.')
  
    #close the files
    numberOfFriends.close()
    ageOfFriends.close()
    numberOfFriends2.close()


    #rename the files so the FriendCount file can have the new sum of friends
    os.remove('FriendCount.txt')
    os.rename('FriendCount2.txt', 'FriendCount.txt')




main()




#-----------------------------------Testing-------------------------------------------------
# I began testing my raised exceptions was just by trying to create the exception by
#doing what a user could possibly do that would create the error. I tried to lookup
#the errors on python documentation as the book suggested but I just thought I would
#not understand it as good as if I actually caused the exceptions myself. I tried
#writing on a readable file for example and gathered the exception and created the handle.
#When the program asked for friend names I added special characters numbers and just pressing
#enter and the it was able to pass to the age of friend question where when typing anything other
#than an integer, the exception will be raised asking the user to type in an integer. The way
#I was able to test to see if the number of friends added to the list of friends had a new
#count by creating a different file to see if the right amount of friends were being counted.
# This also gave me the way in renaming the files so the CountFile would retain its name with the
#new count.



#-----------------------------------Summary---------------------------------------------
# I first started the project by creating a pseudocode. This helped me in trying to understand
#the requirements of the program and also getting an idea where everything would go to make sure
#the questions asked would loop around and create a count of how many names were created.
#I first got stuck in trying to create the loop in asking the user the name of friend
#and having it end when pressing enter when asked again for friend's name. I knew it was
#an if statement but had trouble in where to place it. I was able to find it after thinking how
#the program is reading the loop and needed it where it would escape it did not meet a criteria.
#I also got stuck when trying to add up the total number of new friends with the count in the file.
#I managed to get through by using the more simple for loop of reading a line at a time and converting the 4
#in the file as an integer.



# What I don't like would like to fix is learning more about exceptions as the ones I created are
#a bit vague in a way and there could be different things that would raise the same exception in differe
#parts of the program.

#This assignment a good lesson on how to let a user know that what was done has an error and can
#tell them what they need to do so they will not see the error again. Also it is a cleaner way to see
#when an exception is created to the user and a programmer can go back to look into the traceback as
#the traceback is still very helpful in knowing where exactly the problem is located. 
