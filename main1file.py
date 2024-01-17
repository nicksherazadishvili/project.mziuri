from bs4 import BeautifulSoup
import requests
import csv
import os
import lxml

column_name = ['Downloads', 'Name', 'Lastest_realise', 'Create_date', 'File_size',]
csvfile = open('mod_data.csv', 'w', newline='') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)

