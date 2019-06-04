#!/usr/bin/python3
"""Author: regalferg"""

import json
import urllib.request

##URL for API
MAJORTOM = 'http://api.open-notify.org/astros.json'



def main():
    ##Call the webservice
    res = urllib.request.urlopen(MAJORTOM)
    ##Strip JSON data from response
    jstring = res.read()
    # print(jstring)
    ##convert string to json
    resJSON = json.loads(jstring.decode('utf-8'))
    ##parse json
    print("\n\nPeople in Space: ",resJSON['number'])
    astropeople = resJSON.get('people')
    for spaceperson in astropeople:
        print(spaceperson['name'] + " on the " + spaceperson['craft'])
 
    #Display parsed data
  




if __name__ == "__main__":
    main()