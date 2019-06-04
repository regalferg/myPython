#!/usr/bin/python3
"""Author: regalferg"""

import requests

##URL for API
MAJORTOM = 'http://api.open-notify.org/astros.json'



def main():
    try:
        ##Call the webservice
        res = requests.get(MAJORTOM)
        ##convert string to json
        resJSON = res.json()
        ##parse json
        print("\n\nPeople in Space: ",resJSON['number'])
        astropeople = resJSON.get('people')
        for spaceperson in astropeople:
            print(spaceperson['name'] + " on the " + spaceperson['craft'])
    except:
        print("API is unavailable at the moment")
        exit()

    

if __name__ == "__main__":
    main()
