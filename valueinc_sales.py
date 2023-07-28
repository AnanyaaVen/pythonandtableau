#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:17:06 2023

@author: ananyaavengurlekar
"""

import pandas as pd 

# file_name = pd.read_csv('file.csv') <---- format of read_csv 

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data 
data.info()


#wokring with calculations 

#Defining variables 

CostPerItem = 11.73 
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical operations on Tableau 

ProfitperItem = 21.11 - 11.73 
ProfitperItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitperItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem

#Cost per transaction Column Calculation 

#Cost per transaction = CostPerItem * NumberofItemsPurchases 
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased 

#adding a new column to a data frame 

data['CostPerTransaction'] = CostPerTransaction 

#Sales per Transaction 

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost 

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/ Cost 

data['Markup'] =  ( data['SalesPerTransaction'] - data['CostPerTransaction'] )/ data ['CostPerTransaction']

data['Markup'] =  ( data['ProfitPerTransaction'] / data['CostPerTransaction'] ) 
                   
#Rounding Marking 

roundmarkup = round(data['Markup'], 2) 

data['Markup'] = round(data['Markup'], 2) 

#combining data fields 

my_name = 'Ananyaa' + 'Vengurlekar'
my_date = 'Day'+'-'+'Month'+'-'+'Year' 

my_date = data['Day']+'-'

#checking columns data type 
print(data['Day'].dtype)

#Change column types 

day = data['Day'] .astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year 

data['date'] = my_date

#using iloc to view specific columns/rows 

data.iloc[0] #views the row with index = 0 
data.iloc[0:3] #first 3 rows 
data.iloc[-5:] #last 5 rows

data.head(5) #first 5 rows 

data.iloc[:,2] #brings in all rows from the 2nd column 

data.iloc[4,2] #brings in 4th row, 2nd column 

#using spilt to spilt the client keywords 
#new var = column.str.spilt('sep', expand = Trie) 

split_col = data['ClientKeywords'].str.split(',' , expand = True) 

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase 

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files 

#bringing in a new dataset 

seasons = pd.read_csv('value_inc_seasons.csv', sep=';') 

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns 
# df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1) 

#Export in CSV

data.to_csv('ValueInc_Cleaned.csv', index = False) 



























































































