#!/usr/bin/python3

import csv
import json

def main():
    jsonf = open('superbirths.json','w')


    with open ('heroinfo.csv') as csvf:
        reader = csv.DictReader(csvf)
        json.dump(list(reader),jsonf)
    jsonf.close()

if __name__ == '__main__':
    main()

