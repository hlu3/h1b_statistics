#!/usr/bin/python
 
#import functions 
from sorting import sort_number
from sorting import sort_alpha
from files import write_file
from files import read_file
from cleanData import clean_data


# Give path of the file to read 
file_name = 'h1b_input.csv'
#file_name = 'H1B_FY_2014.csv'
#file_name = 'H1B_FY_2015.csv'
#file_name = 'H1B_FY_2016.csv'
file_name = './input/' + file_name

# read in raw data
rawData = read_file(file_name)

#clean the data
#extract data only with certified visa applications and count numbers for each occupation and state 
total, job, state = clean_data(rawData)


#sort occupations and states based on numbers
jobsort = sort_number(job)
statesort = sort_number(state)

#sort occupations and states alphabetically with equal numbers       
jobsort = sort_alpha(jobsort)
statesort = sort_alpha(statesort)


#output top 10 occupations to a file       
fileName = './output/top_10_occupations.txt'
header = 'TOP_OCCUPATIONS'+';'+'NUMBER_CERTIFIED_APPLICATIONS'+';'+'PERCENTAGE'
write_file(fileName,header,jobsort,total)
#output top 10 states to a file  
fileName = './output/top_10_states.txt' 
header = 'TOP_STATES' + ';' + 'NUMBER_CERTIFIED_APPLICATIONS' + ';' + 'PERCENTAGE'
write_file(fileName,header,statesort,total)

