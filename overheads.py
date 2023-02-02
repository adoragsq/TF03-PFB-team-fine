from pathlib import Path
import csv
#link file path of overheads to the variable fp
fp = Path.cwd()/"csv_reports/overheads-day-90.csv"
#link the summary report text file to the variable file_path
file_path = Path.cwd()/"summary_report.txt"
#create a function maxoverhead() without any parameter
def maxoverhead():
    '''
    The program will find the highest overhead category in the 'overheads.csv'file
    '''
    #read the csv file to append overheads from the csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    
        reader = csv.reader(file)
        #skip header
        next(reader)
        #create 2 empty list to store overheads and the category using []
        overheads = []
        header = []
        #append overheads as a list back to each empty list
        for data in reader:
            #append the category into the header list
            header.append(data[0])
            #append the percentage into the overheads list
            overheads.append(float(data[1]))
        #using if function to create a conditional statement for the highest overheads
        if max(overheads):
            #find the index of the highest overheads
            index = overheads.index(max(overheads))
            #open the file so that we can append what we want to write
            with file_path.open(mode='a') as file:
                #find the header by using the index that we found previously and making all into caps, then print the maximum overheads
                file.write(f"[HIGHEST OVERHEADS] {header[index].upper()}: {max(overheads)}%")
