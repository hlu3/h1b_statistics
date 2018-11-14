#!/usr/bin/python

import csv
from itertools import islice

def read_file(fileName):
    # read the file
    f = open(fileName,'r')
    reader = csv.reader(f, delimiter=';')

    # Get the colomn size of the data
    ncol = len(next(reader))

    # Get indexes of CASE_STATUS, SOC_NAME, WORKSITE_STATE in the first row (header)
    f.seek(0)
    for row in islice(reader,1):
        for i in range(ncol):
            if row[i] == 'CASE_STATUS' or row[i] == 'STATUS':
               n_status = i
            if row[i] == 'SOC_NAME' or row[i] == 'LCA_CASE_SOC_NAME':
               n_job = i
            if row[i] == 'WORKSITE_STATE' or row[i] == 'LCA_CASE_WORKLOC2_STATE':
               n_state = i
    
    i = 0
    rawData = []
    for row in reader: 
        rawData.append([])
        rawData[i].append(row[n_status])
        rawData[i].append(row[n_job])
        rawData[i].append(row[n_state])
        i += 1

    f.close()
    return rawData





def write_file(fileName,header,lsort,total):

    fw = open(fileName,'w')
    fw.write(header + '\n')

    #in case the ccupations/states are less than 10
    if len(lsort) < 10:
       outputN = len(lsort)
    else:
       outputN = 10

    #output occupation/states names, numbers, and percentage
    for i in range(outputN):
        percent = 100.0 * float(lsort[i][1])/float(total)
        percent = round(percent,1)
        fw.write(lsort[i][0] + ';' + str(lsort[i][1]) + ';' + str(percent) + '%' + '\n')

    fw.close()
