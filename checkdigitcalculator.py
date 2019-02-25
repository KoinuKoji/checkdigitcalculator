###UPC/GTIN Check Digit Finder###
###For use with Retail-Link pulls or any file with UPC/GTINs needing a check digit###
###Have CSV file with a UPC or GTIN column and will add a new file with both written together###
### Python 3.+ ###

### Cody Cox 2-25-19 ###

import csv

outputfile = open('gtin_ouput.csv', 'w', newline='')
outputwriter = csv.writer(outputfile)
## Open file containing UPC/GTIN/VNPK UPC and move to Checker
def file_read():
    file = open('gtin_input.csv','r')
    with file:
        reader = csv.DictReader(file)
        for row in reader:
            upc = str(row['Input'])
            checker(upc)
## Checks if the UPC/GTIN is valid and moves to the check_digit
def checker(upc):
    if (len(str(upc))==11) or (len(str(upc))==13) and upc.isnumeric():
        gtin_check_digit(upc)
    elif (len(upc)==9) and gtin.isnumeric():
        gtin = "00" + upc
        gtin_check_digit(upc)
    else:
        outputwriter.writerow([upc, 'INVALID UPC/GTIN'])
## Main check digit finder, writes to file
def gtin_check_digit(upc):
    odds = 0
    evens = 0
    upc = str(upc)
    for x, char in enumerate(upc):
        num = x+1
        if num % 2 == 0:
            evens += int(char)
        else:
            odds += int(char)
    total = (odds * 3) + evens
    ceiling = total % 10
    check_digit = 10 - ceiling
    if check_digit == 10:
        check_digit = 0
        print(upc, upc + str(check_digit))
        outputwriter.writerow([upc, (upc+str(check_digit))])
    else: 
        print(upc, upc+str(check_digit))
        outputwriter.writerow([upc, (upc+str(check_digit))])

file_read()
