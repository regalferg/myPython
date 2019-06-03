#!/usr/bin/python
"""Author regalferg | Email: Nada || Python Practice"""

# python has no jsonbatteries in ze box, we need to import
import json

def main():
    ##open a file in write mode
    with open('jonsnow.json','r') as gotdata: #'w' = write, 'r' = read', 'a' = append
        jonsnow = gotdata.read()
        GOTpy = json.loads(jonsnow) 
    print(GOTpy["name"])
    print(GOTpy["url"])
    print(GOTpy["titles"][0])
    #print(GOTpy["aliases"])

    #parse jonsnow file for ...
    for gotalias in GOTpy["aliases"]:
            print(gotalias)
                
        #display char name
    
        #display char alias/titles
        #display the API for ???
        

if __name__ == "__main__":  
    main()
