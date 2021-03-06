import csv
from faker import Faker
from collections import defaultdict

def anonymize ():
    faker =Faker()
    names = defaultdict(faker.name)
    emails = defaultdict(faker.email)
    citys = defaultdict(faker.city)
    with open("original_data.csv", newline='') as Lucky:
        with open("anonymized.csv", 'w',newline='') as Brady:
            reader = csv.DictReader(Lucky)
            writer = csv.DictWriter(Brady,reader.fieldnames,delimiter=','
            writer.writeheader()
        for row in reader:
            row[' name'] names [row[' name']]
            row[' email']=emails[row['email']]
            row[' city']=citys[row[' city']]
            writer.writerow(row)
if _name_=='_ main_'
    anonymize()