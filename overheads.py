from pathlib import Path
import csv
#create a file to csv file
fp = Path.cwd()/"csv_reports/overheads-day-90.csv"
#creating a new file path to create new file 'summary_report.txt'
file_path = Path.cwd()/"summary_report.txt"
#create a function maxoverhead() without any parameter
def maxoverhead():
    #read the csv rile to append overheads from the csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        #skip header
        next(reader)
        #create 2 empty list to store overheads using []
        overheads = []
        header = []
        #append overheads as a list back to each empty list
        for data in reader:
            header.append(data[0])
            overheads.append(float(data[1]))
        #using if function to check if conditions are met
        if max(overheads):
            index = overheads.index(max(overheads))
            with file_path.open(mode='a') as file:
                #using f-strings to print out the output stated in the breif
                file.write(f"[HIGHEST OVERHEADS] {header[index].upper()}: {max(overheads)}%")
