"""
Created on Mon Apr 27 23:21:05 2020

@author: zeronp
"""

import json 
import csv 
import os

file_name = 'Top_100_TikTok_Influencers.json'      #file to read from 
csv_file_name = 'Top_100_TikTok_Influencers.csv'   #file to be written to


dummy_file = file_name + '.bak' 
with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
    # Write given line to the dummy file
    write_obj.write('{"Info": [' + '\n')
    
    # Read lines from original file one by one and append them to the dummy file
    for line in read_obj:
        write_obj.write(line)
    write_obj.write("{ }]}")
# remove original file
os.remove(file_name)
# Rename dummy file as the original file
os.rename(dummy_file, file_name)
  
# Opening JSON file and loading the data 
# into the variable data 
with open(file_name) as json_file: 
    data = json.load(json_file) 
  
restaurants_data = data['Info'] 
  
# now we will open a file for writing 
data_file = open(csv_file_name, 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 

#header=['name','speciality','rating','delivery_time','pricing','offer','conditions']  
#csv_writer.writerow(header) 
for r in restaurants_data: 
      # Writing data of CSV file 
    csv_writer.writerow(r.values()) 
  
data_file.close() 