1. The program satisfies the requirements of directory structure and output format
   I put my own test files under the directory of your-own-test_1
   by doing ./run_tests, it shows:  2 of 2 tests passed

2. To run the program, simply submit the shell script by: 
   qsub run.sh

3. under the directory of src are my programs:
   h1b_counting.py: is the main function, where it clearly shows the procedure taken
                    to complete the prot. It calls modules/functions of reading a csv file, 
                    saving raw data, cleaning and extracting useful data, sorting the data and 
                    finally write the top 10 occupations and states to other files.
    
   files.py: includs two functions of read_file and write_file
             read_file is to read the csv file and save the raw data with the information f 
             CASE_STATUS, SOC_NAME, and WORKSITE_STATE
             write_file is to write the top 10 occupations and states to files of 
             top_10_occupations.txt and top_10_occupations.txt

   cleanDatapy: is to extract the data only with certified visa applications, and count the numbers
                for each occupation and state.

   sorting.py:  includes two functions of sort_number and sort_alpha
                sort_number is to sort occupations and states based on their numbers
                sort_alpha is to sort occupations and staes which have equal numbers alphabetically
