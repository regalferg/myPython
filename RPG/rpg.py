#!/usr/bin/python3
""" Author: regaferg | """

def showinstructions():
    #print a menu of commands
    print('''
RPG Game
========
Commands:
    go [direction]
    get [item]
    ''')

def showStatus():
    #print the player's current status
    print('--------------------------')
    print("You are in the " + currentRoom)
    #print the current inventory
    print('Inventory :' + str(inventory))
    #print an item if there is one
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('---------------------------')

#an inventory, initially empty
inventory = []

# a dict linking a room to other rooms
rooms = {
    'Hall':{
        'south':'Kitchen',
        'east': 'Dining Hall',
        'item':'key'
    },
    'Kitchen':{
        'north':'Hall',
        'item': 'monster'
    },
    'Dining Hall':{
        'west':'Hall',
        'south':'Garden',
        'item':'potion'
    },
    'Garden':{
        'north':'Dining Hall'
    }
}

#start the player in the hall
currentRoom = 'Hall'

#initial function call
showinstructions()

#loop forever!
while True:
    showStatus()

#get the player's next move
    move = ''
    while move == '':
        move = input('>')
        move = move.lower().split()

#if they type go first
    if move[0] =='go':
    #check if they are allowed entry
        if move[1] in rooms[currentRoom]:
        #set current room to new room
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door link to a new room
        else:
            print('You shall not pass!')

#if they type get 1st
    if move[0] == 'get':
    #if the room contains an item and the item is the one they want
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add item to inv
            inventory += [move[1]]
        #display a helpful msg
            print('You got a ' + move[1] )
        #delete the item from the room
            del rooms[currentRoom]['item']
    #otherwise if the item isn't there
        else:
        #tell them they can't get it
            print('Cannot get ' + move[1] + '1')
       
## if player enters room with monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has gotcha...GAME OVER!')
        break
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("YOU WIN")
        break