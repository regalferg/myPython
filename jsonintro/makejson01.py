#!/usr/bin/python
"""Author regalferg | Email: Nada || Python Practice"""

# python has no jsonbatteries in ze box, we need to import
import json

def main():
    ##blob of data
    hitchhikers = [{"name":'Zaphod Beeblebrox','species':'Betelgeusian'}, \
            {'name': 'Arthur Dent','species':'human'}]

    ##Display python data in terminal
    print(hitchhikers)

    ##open a file in write mode
    zfile = open('galaxyguide.json','w')


    ##use the json library
    json.dump(hitchhikers,zfile)

    ##close file
    zfile.close()

main()
