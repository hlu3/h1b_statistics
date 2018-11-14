#!/usr/bin/pythaona

from operator import itemgetter

def sort_number(List):

   #sort the list based on numbers
   List = sorted(List, key = itemgetter(1), reverse = True)

   return List






def sort_alpha(lsort):
    cout = 0   #total occupations/states number has been sorted
    check = lsort[0][1]   #maximum number
    strin = list()  #create a list to save occupations/states with the equal number
    while cout < 10:  #stop sorting if top ten are obtained
          same = 0   #count how many occupations/states have the equal number
          for i in range(len(lsort)):
              if lsort[i][1] == check:
                 same += 1
                 strin.append(lsort[i][0])  #save occupations/states with the equal number
                 index2 = i  #last index of occupution/state has equal number
                 if same == 1:
                    index1 = i  #first index of occupation/state has equal number

          strin = sorted(strin) #sort occupations/states alphabetically with equal numbers
          for i in range(len(strin)):
              lsort[index1+i][0] = strin[i] #save sorted occupations/states into original array
          while len(strin) > 0 : strin.pop() #claer the slit for next loop

          cout += same #total number of occuputions/states have been sorted
          if cout >= len(lsort):
             break;
          else:
             check = lsort[index2+1][1] #next loop for occupations/states with equal number
    
    return lsort
