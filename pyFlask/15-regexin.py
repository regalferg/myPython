#!/usr/bin/python3

import re

def main():
    with open('testcap.txt','r') as testcap:
        for line in testcap:
            regmatch = re.search(r"^Contact:\ssip:\+(\d+)@\[(.*)\]:?(\d+)?", line)
            if regmatch:
                print(regmatch)#display match
                print(regmatch.group())##display full match
                print(regmatch.group(1))##display digitsh
                print(regmatch.group(2))##display ipv6
                print(regmatch.group(3))##display port
                 
           # else:
            #    print('Not Found')


if __name__ == '__main__':
    main()
