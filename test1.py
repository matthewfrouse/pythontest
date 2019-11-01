# using pandas to read and write excel and csv files
import pandas
# read excel file into the dataframe
df = pandas.read_excel(r"C:\ETL\Target\targetxl.xlsx", index_col='CI_Name')
# output the data frame
#print(df)
# output  columns
print(df['CI_Application'])
#print(df.sample(5))