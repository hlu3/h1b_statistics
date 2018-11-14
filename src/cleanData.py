#!/usr/bin/python

def clean_data(rawData):
    
    list_job = list()   #create list to save SOC_NAME
    list_njob = list()   #create list to save SOC_NAME number
    list_state = list()   #create list to save WORKSITE_STATE
    list_nstate = list()   #create list to save WORKSTE_STATE number

    for i in range(len(rawData)):
        if rawData[i][0] == 'CERTIFIED':

           #save OCCUPATIONS names and numbers
           if rawData[i][1] in list_job:
              index = list_job.index(rawData[i][1]) 
              list_njob[index] += 1   #increase occupation number if it is already in the list
           else: 
              list_job.append(rawData[i][1])  #add occupation to the list if it is the firt time to show
              list_njob.append(1)

           #save states names and numbers
           if rawData[i][2] in list_state:
              index = list_state.index(rawData[i][2]) #increase state number if it is already in the list
              list_nstate[index] += 1
           else:
              list_state.append(rawData[i][2]) #add state to the list if it is the firt time to show
              list_nstate.append(1)
    

    
    #calculate total numbers of certified visa applications
    total = sum(list_njob)    

    #copy cleaned data to 2D arrays for sorting
    job = []
    for i in range(len(list_job)):
        job.append([])
        job[i].append(list_job[i])
        job[i].append(list_njob[i])
    
    state = []
    for i in range(len(list_state)):
        state.append([])
        state[i].append(list_state[i])
        state[i].append(list_nstate[i])
  
    return total, job, state;
 








