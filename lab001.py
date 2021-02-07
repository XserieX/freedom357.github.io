"""
This script will Anonymize the data in original_data.csv file to Anonymized form in anonymized_data csv file
"""
import csv     #Brad  
from faker import Faker   #Luck
from collections import defaultdict   #Brad
  
def anonymize():   #Luck
	# Load the faker and its providers
	faker  = Faker()   #Brad

	# Create mappings of names &amp; emails to faked names &amp; emails.
	names  = defaultdict(faker.name) #Luck
	emails = defaultdict(faker.email)   #Brad

	with open("original_data.csv", newline='') as Lucky:   #Luck     
		with open("anonymized_data.csv", 'w', newline='') as Brady :   #Brad
		# Use the DictReader to easily extract fields
			 reader = csv.DictReader(Lucky)   #Luck
			 writer = csv.DictWriter(Brady, reader.fieldnames, delimiter=',')   #Brad
	        		writer.writeheader()   #Luck
	        		for row in reader:   #Brad
	            			row['name']  = names[row['name']]   #Luck
	            			row['email'] = emails[row['email']]   #Brad
	            			writer.writerow(row)   #Luck
 
if __name__ == '__main__':   #Brad
    anonymize()
