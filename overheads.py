from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports/overheads-day-90.csv"
file_path = Path.cwd()/"summary_report.txt"

def maxoverhead():
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        overheads = []
        header = []
        for data in reader:
            header.append(data[0])
            overheads.append(float(data[1]))
        if max(overheads):
            index = overheads.index(max(overheads))
            with file_path.open(mode='a') as file:
                file.write(f"[HIGHEST OVERHEADS] {header[index].upper()}: {max(overheads)}%")