#Project: CIS 177 WEEK 10 PROJECT
#Project Location: projects\cis177\SquareChairPizza
#File: SquareChairPizza.py
#Purpose: Customer Tracking System for Square Chair Pizza
#         using a dict to store customer data
#Revision: 1.0 / 1 APR 2017
#Created: 1 APR 2017
#Author: Rick Miller <rick@rickthegeek.com>

custDict = {} # Dictionary storing the customer database

userChoice = '' # This will be the user's choice from the main menu

# This routine will ask for the number and name and address, and add it to the dict
# NOTE: Phone numbers will have the dashes deleted to allow for the fact that some users
# may enter 603-555-1212 and others might enter 6035551212. This (and the fact we are storing the number
# as a string, will also allow for the entry of international numbers, just in case 
# we get customers from other countries.
# Also, if the user enters the exact number of an entry already in the databse, it will replace the entry
# with the entry the user enters here.
def addCustomer():
    custPhoneNumber = input('Please enter the custoner\'s telephone number -> ').replace('-','')
    custNameAddress = input('Please enter the customer\'s name and address -> ')
    custDict[custPhoneNumber] = custNameAddress
    print('Added!')

# Here, we are looking up a customer by phone number. Again, we are stripping out the dashes, since
# we stored the number in the dict without dashes. If the key is not found (the number is not in the dict)
# we return an error. Note: We are checking if the cust number is IN the cust dict first, to avoid an errror
# by trying to delete a key that doesn't exist.
def lookUpCustomer():
    custPhoneNumber = input('Please enter the customer\'s phone number to look up -> ').replace('-','')
    if custPhoneNumber in custDict: # see if the key exists...
        print('\nCustomer\'s number:', custPhoneNumber, ' \nCustomer\'s address:', custDict[custPhoneNumber]) # ... if so, print it
    else: # ...if not
        print('\nSorry, not found')

# This is where we are deleting a customer record. Again, we are stripping out the dashes and doing a check if
# the cust number is a ket IN the dict, so we avoid an error by trying to delete a record that doesn't exist.
def deleteCustomer():
    custPhoneNumber = input('Please enter the customer\'s number to delete from the system -> ').replace('-','')
    # if custPhoneNumber in custDict: # check if the key exists
    deletedName = custDict.pop(custPhoneNumber, 'invalid') # if so delete it...
    if deletedName != 'invalid':    
        print(deletedName, 'deleted!') # ...and tell the user
    else: # if the key doesn't exist...
        print('\nSorry, not found')

# This routine simply prints the customer list, by stepping through with a "for" loop and making the output look
# a little bit neater.
def printList():
    if len(custDict) > 0: # check if there are any entries in the dict
        print('\nCustomer list:\n') # if there are, print them out
        for (number, address) in custDict.items(): # ...by stepping through the dict ...
            print('Number:', number, 'Address:', address) # ...and printing them neatly on screen
    else: # there are no entries in the dict
        print('\nList is empty')

# This routine simply prints the menu of available options for the program. I'm just putting it here to make it easier to
# display the menu upon reuqest.
def printMenu():
    print('Welcome to Square Chair Pizza\'s Customer Management System')
    print('There are',len(custDict), 'customers on file.')
    print('\nOptions')
    print('-------')
    print('\nA - Add a customer to the database')
    print('L - Look up a customer by telephone number')
    print('D - Delete a customer from the database')
    print('P - Print the entire custonmer database')
    print('Q - Quit the program')


# *** MAIN PROGRAM ROUTINE STARTS HERE ***

# First, show the user the menu
printMenu()
while userChoice != 'q': # Program repeats until the user chooses 'q' to quit
    userChoice = input('\nPlease enter your selection (\'?\' for menu) -> ')
    if userChoice == '' : # if the user just presses "enter" without an entry, set userChoice to 'x' for an invalid entry to avoid an invalid index when looking up userChoice[0]
        userChoice = 'x'
    else:
        userChoice = userChoice[0].lower() # take the first character the user enters and make it lowercase
    if userChoice == 'a': # and we branch here based on the user's entry
        addCustomer()
    elif userChoice == 'l':
        lookUpCustomer()
    elif userChoice == 'd':
        deleteCustomer()
    elif userChoice =='p':
        printList()
    elif userChoice =='?':
        printMenu()
    elif userChoice =='q':
        print('End of program') # if user enters 'q' the else option won't happen and the loop stops because userchoice is 'q'
    else: # user made an invalid entry, tell the user and re-display the menu
        print('\nSorry, invalid selection, try again\n')
        printMenu()

