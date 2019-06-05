#!/usr/bin/python3
"""Author: moi"""

import requests

MYAPI = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key='

def keyreturn():
    with open("/Users/fergch9/Documents/Python/myPython/PythonAPI/nasa.key") as keyfile:
        mykey = keyfile.read()
        return mykey

def main():
    #harvest api key from file
    nasakey = keyreturn()
    #append our key to MYAPI
    res = requests.get(MYAPI + nasakey)
    asteroidz = res.json()
    
    #call api
    #print(asteroidz["near_earth_objects"])
    for bigrocks in asteroidz["near_earth_objects"]:
        if bigrocks["is_potentially_hazardous_asteroid"]:
            print("Name - ",bigrocks["name"])
            print("Proximity - ",bigrocks["close_approach_data"])
            print("Size - ",bigrocks["estimated_diameter"], end="\n*****\n")
            
        # else:
        #     print("No worries")

    #pull json off responsels


    #decode json - loop across 'near_earth_object' to reveal asteroids

    #only display those that may pose a danger to Zach
if __name__ == "__main__":
    main()



   
   
