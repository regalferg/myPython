#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def pygraph(booktoread):

    mdf = pd.read_excel(booktoread,sheet_name='Sheet1')
    menMeans = mdf['mins']
    menMeans = tuple(menMeans.values) # this produces a tuple from the mins col
    quarters = mdf['quarter']
    quarters = tuple(quarters.values)

    N = 4
    #menMeans = (20, 35, 30, 35)
    menStd = (2, 3, 4, 1)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.30       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, yerr=menStd)#blue bottom values

    plt.ylabel('Outage Mins')
    plt.title('Outage Mins per Quarter')
    plt.xticks(ind, quarters)
    plt.yticks(np.arange(0, 201, 15))
    plt.legend((p1[0],), ('Mins',))

    now = datetime.datetime.now()
    plt.savefig(now.strftime('%Y-%m-%d-outage.png'))
    plt.show()


    


