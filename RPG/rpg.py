#!/usr/bin/python3
""" Author: regaferg | """
import random, time

playerHP = 150
beholderHP = 200

def showinstructions():
    #print a menu of commands
    print('''
Castle Escape!
========
Commands:
    go [direction]
    get [item]
========
Collect the key and potion and escape to safety!
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
def playerHit():
    time.sleep(1)
    global beholderHP
    print('What do you?' )
    playerAtk = input("> ").lower()
    while playerAtk == 'attack':
        beholderHP = beholderHP - random.randrange(10,50)
        print('The beholder now has ' + str(beholderHP) + ' hitpoints remaining!')
        return beholderHP
def beholderHit():
    global playerHP
    time.sleep(1)
    playerHP = playerHP - random.randrange(15,50)
    print('Player now has ' + str(playerHP)+ " Hitpoints remaining")
    return playerHP


def doBattle():
    while playerHP != 0 or beholderHP !=0:
        playerHit()
        beholderHit()
        if playerHP <=0:
            print("You have been given another chance!")
            break
        if beholderHP <=0:
            print('You have slain the beholder, continue your quest!')
            continue
   
    

#an inventory, initially empty
inventory = []


# a dict linking a room to other rooms
rooms = {
    'Castle Entrance':{
    'south':'Hall'
    },
    'Hall':{
        'south':'Toilets',
        'east': 'Dining Hall',
        'north':'Castle Entrance'
    },
    'Toilets':{
    'north':'Hall',
    'south':'Kitchen',
    'item':'key'
    },
    'Kitchen':{
        'north':'Toilets',
        'item': 'beholder'
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
currentRoom = 'Castle Entrance'

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
       
## if player enters room with beholder
    # if 'item' in rooms[currentRoom] and 'beholder' in rooms[currentRoom]['item']:
    #     print('A beholder has appeared!')
    #     print("Attack or go the way you came to run away")

    if move[0]=='attack':
        print("Battle Started")
        doBattle()
    
        
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("YOU ESCAPED, GAME OVER")
        break