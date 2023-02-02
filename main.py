from pathlib import Path
import cashonhand
import overheads
import profitloss
file_path = Path.cwd()/"summary_report.txt"

def main():
    '''
    - run all 3 function of overheads, cash on hand, and profit and loss
    '''
    overheads.maxoverhead()
    cashonhand.cashonhand()
    profitloss.profitloss()


main()