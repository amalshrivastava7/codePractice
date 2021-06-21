import pandas as pd

## Read csv

df = pd.read_csv("/Users/amal/Desktop/C2C.csv")

## Print columns in a dataframe

# print(df.columns)


## Index or specify row, columns to select

# print(df[1:10][["CIFNUMMER", "ACCOUNTKEY", "BRANCH_NBR"]])


## Sample display

# print(df.sample(frac=0.5))
#
# print(df.sample(axis = 1))

print(df[:10]['LAST_YEAR_AVERAGE_BALANCE'])

print(df[:10].LAST_YEAR_AVERAGE_BALANCE.max())
print(df[:10].LAST_YEAR_AVERAGE_BALANCE.min())



