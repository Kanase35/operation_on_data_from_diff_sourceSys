# -*- coding: utf-8 -*-
"""Data_visualization_project_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nyN_rulIdqi92xb-ICT3j_2YDH67uyFf

# Usecase-1 Load all three csv datasets in Pandas Data frames and display first 5 records.
"""

from google.colab import files
data = files.upload()

ls

import numpy as np
import pandas as pd
import seaborn as sns

df_customers = pd.read_csv('customers.csv')
df_customers.head()

df_transactions = pd.read_csv('transactions.csv', header   = None)
df_transactions.head()

trans_index =  ['txnno','txndate','custno','amount','productno','spendby']
df_transactions = pd.read_csv('transactions.csv', names =  ['txnno','txndate','custno','amount','productno','spendby'])
df_transactions.head()

df_products = pd.read_csv('products.csv')
df_products.head()

"""# Usecase-2 Display only those customers from CSV_s1, who purchased more than 3 products"""

df1 = pd.merge(df_customers,df_transactions, left_on="'custno'", right_on ='custno')
df1

df2 = df1.groupby('custno').count()
df2

dff = df2[df2 > 3]
dff

df_final = df_customers.set_index("'custno'")
df_final.head()

df_final['product_purchased'] = dff['txnno']
df_final.head()

df_final = df_final[df_final['product_purchased'] > 3]
df_final.head()

df_final['product_purchased'].value_counts()

"""# Usecase-3 Display top 5 most demanded products from CSV_s1

"""

df_3 = pd.merge(df_products, df_transactions, left_on="'productno'" ,right_on = "productno")
df_3.head()

pd_group = df_3.groupby('productno').count()
pd_group.head()

df_products_final = df_products.set_index("'productno'")
df_products_final.head()

df_products_final['product_sell'] = pd_group['custno']
df_products_final.head(2)

df_products_final.sort_values(by = 'product_sell', ascending = False).head()

"""# Usecase-4 Display top 5 transactions amount from CSV_s1

"""

df_transactions.head()

df_main_transactions = df_transactions.set_index('txnno')
df_main_transactions.head()

df_main_transactions.sort_values(by = 'amount', ascending= False).head()

"""# Usecase-5 Display distinct professions from CSV_s1"""

df_customers["'profession'"].value_counts()

df_pro_main = df_customers.groupby("'profession'").count()
df_pro_main

"""# Usecase-6 Display highest age in CSV_s1 customer’s dataset

"""

df_customers.sort_values(by = "'age'", ascending= False).head()

df_customers["'age'"].max()

"""# Usecase-7 Display custno, gender, age, profession, contactno, productno, productName, txndate, spendby, amount from CSV_s1 for custno = 923


"""

print("Customers Columns: ", df_customers.columns)
print()
print("Tarnasctions Columns: ", df_transactions.columns)
print()
print("Products Columns: ", df_products.columns)

df_7 = pd.merge(df_products[["'productno'","'productName'"]], df_transactions, left_on = "'productno'", right_on='productno')
df_7.head()

df_8 = pd.merge(df_customers, df_7, left_on = "'custno'", right_on = 'custno')
df_8.head()

df_7_final = df_8[["'custno'","'gender'","'age'","'profession'","'contactNo'","'productno'","'productName'",'txndate','spendby','amount']]
df_7_final.head(10)

df_7_final[df_7_final["'custno'"] == 923]

"""# Usecase-8 Load all three PSV (pipe separated values) dataset in Pandas Data frames and display first 5 records.


"""

ls

psv_customers = pd.read_csv('customers.txt',header = None, delimiter= "|")
psv_customers.head()

psv_customers = pd.read_csv('customers.txt',header = None, delimiter= "|", names = ['custno','firstname','lastname','gender','age','profession','contactNo',
'emailId','city','state','isActive','createdDate','UpdatedDate'])
psv_customers.head()

psv_transactions = pd.read_csv('transactions.txt',header = None, delimiter= "|", names =['txnno','txndate','custno','amount','productno','spendby'] )
psv_transactions.head()

psv_products = pd.read_csv('products.txt', header = None, delimiter = "|", names = ['productno','productName','Description','isActive','createdDate','UpdatedDate'])
psv_products.head()

"""# Usecase-9 Load all three JSON datasets in Pandas Data frames and display first 5 records."""

ls

df_json_cust = pd.read_json('customers.json', lines = True)
df_json_cust.head()

df_json_tran = pd.read_json('transactions.json', lines = True)
df_json_tran.head()

df_json_products = pd.read_json('products.json', lines = True)
df_json_products.head()

"""# Usecase-10 Load all three XML datasets in Pandas Data frames and display first 5 records."""

ls

df_xml_customers = pd.read_xml('customers.xml')
df_xml_customers.head()

df_xml_transactions = pd.read_xml('transactions.xml')
df_xml_transactions.head()

df_xml_products = pd.read_xml('products.xml')
df_xml_products.head()
