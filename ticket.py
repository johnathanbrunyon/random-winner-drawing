#!/usr/bin/env python3


import random as rand
import json

# initialize ticketDict
ticketDict = {}

# Load the initial data from json
try:
    with open('ticket_list.json', 'r') as f:
        ticketDict = json.load(f)
        print("Data Loaded")
        print(ticketDict)
except:
    print("No Data Loaded From Json")

# Method to check if a string can be converted to int if so convert it to an int.
def CheckValidInt(question):
    convert = 0
    userInput = input(question)
    iter = 0
    while iter < 1:
        try:
            convert = int(userInput)
            iter = 1
        except:
            print("Please enter an integer")
            userInput = input(question)
    return convert

# Menu and option loop
iterator = 0
while iterator < 1:
    # Menu
    print("1. Add A New Ticket")
    print("2. Add Entries")
    print("3. Check Amount Of Entries On A Ticket")
    print("4. Pick A Random Winner")
    print("5. Exit")
    answer = CheckValidInt("Pick A Menu Option: ")
    
    # If statements implementing logic for each menu option
    if answer == 1:
        ticket = CheckValidInt("Enter the ticket number: ")
        # Prevents duplicate tickets
        if ticket in ticketDict:
            print("Ticket Already Exists Enter A Different Ticket!")
        else:
            # Adds ticket to dicitonary
            ticketDict.update({ticket: 1})
            print("Ticket #" + str(ticket) + " has been added!")
    elif answer == 2:
        # Add entires for specified toicket to dictionary 
        ticket = CheckValidInt("Enter the ticket number: ")
        answer = CheckValidInt("How many entires would you like to add? ")
        if ticket in ticketDict:
            ticketDict[ticket] += answer
        else:
            # Error checking for non-existent ticket
            print("Ticket does not exist")
    elif answer == 3:
        # Check how many entires a specific ticket has
        ticket = CheckValidInt("Enter the ticket number: ")
        if ticket in ticketDict:
            print(str(ticket) + " has " + str(ticketDict[ticket]) + " entries")
        else:
            print("Ticket does not exist.")
    elif answer == 4:
        # Initialize ticket list for drawing
        ticketList = []
        # For loop adds each ticket to list as many times as there is entires for each ticket
        for key in ticketDict:
            iter = 0
            while iter < int(ticketDict[key]):
                ticketList.append(key)
                iter += 1
            # Draws the winner
            randomInt = rand.randint(0, len(ticketList) - 1)
            print(str(ticketList[randomInt]) + " is a winning ticket!")
    elif answer == 5:
        # Saves the data when closing the program
        with open('ticket_list.json', 'w') as f:
            json.dump(ticketDict, f)
            exit()
    else:
        # Error checking for menu
        print("Enter A Valid Menu Option")
    

