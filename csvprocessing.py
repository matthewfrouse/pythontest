# input and output csv files
import csv

# define function for writing rows
def writerow(row):
    # output file with append flag set
    with open(r"C:\ETL\Target\targetoutputcsv01.csv", mode='a', newline='') as csv_outputfile:
        csv_writer = csv.writer(csv_outputfile, delimiter=',')
        csv_writer.writerow(row)
        return

# input file
with open(r"C:\ETL\Target\targetinputcsv01.csv", mode='r') as csv_inputfile:
    csv_reader = csv.reader(csv_inputfile, delimiter=',')

    #read input csv file
    input_row_count = 0
    output_row_count = 0
    app_count = 0
    for row in csv_reader:
        if input_row_count ==0:
            #assumes header line present and writes it
            writerow(row)
            input_row_count +=1
            output_row_count +=1
        else:
            # application name is in column H of standard junkshon CSV format - column 8 offset of 7
            appname = row[7]
            #  assume application names are comma+space seperated and convert to list
            applist = list(appname.split(", "))
            if appname =='':
                # appname is blank so output row as is
                writerow(row)
                output_row_count +=1
            else:
                # process list of app names - number of names to process is the len of the list
                appnamecount = len(applist)
                listcount = 0
                while listcount < appnamecount:
                    # overwrite application name field of row with single app name
                    row[7] = applist[listcount]
                    # write row to output CSV
                    writerow(row)
                    output_row_count +=1
                    
                    # increment application count
                    app_count +=1
                    listcount +=1
                
            input_row_count +=1
            
    print(f'Read and Processed {input_row_count} input rows in the input CSV file')
    print(f'Processed {app_count} applications in the input CSV file')
    print(f'Wrote {output_row_count} output rows in the output CSV file')