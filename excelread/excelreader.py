#!/usr/bin/python3

import pyexcel

def main():
    excelrecords = pyexcel.iget_records(file_name='portsservice.xls')

    for row in excelrecords:
        print(row['service'],'-',row['ip'], + ':' str(row['port']))


if __name__ == '__main__':
    main()
