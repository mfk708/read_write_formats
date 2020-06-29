# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:36:24 2020

@author: moham
"""
##reading and writing data with different formats
import pandas as pd
df = pd.read_csv('survey_results_public.csv', index_col='Respondent') 
pd.set_option('display.max_columns', 85)
df.shape
filt = (df['Country']=='India')
india_df = df.loc[filt]
india_df.head()
#now let's export this to csv format.
india_df.to_csv('modified.csv') #saves the dataframe as csv in the same location.
#in csv data is seperated with comma, now if the data is tab-seperated, here is how to save it properly:
india_df.to_csv('modified.tsv', sep= '\t') #saves the data as tsv in which data is seperated by tabs.
#if we want to work with excel, we need to pip install some packages
pip install xlwt openpyxl xlrd #install packages needed to work with excel files.
india_df.to_excel('modified.xlsx') #saves file in excel format
test = pd.read_excel('modified.xlsx', index_col='Respondent') #read data from the excel file(.xlsx)
test.head()
#JSON format-default in json format is dictionary.
india_df.to_json('modified.json') #json default is dictionary format. To change it to look more readable:
india_df.to_json('modified.json', orient='records', lines=True)#saves in json format, with records separated in lines.
test = pd.read_json('modified.json', orient='records', lines=True) #reads the json file and assigns it to test.
#SQL database
#need to install packages to work with SQL database.
pip install 
