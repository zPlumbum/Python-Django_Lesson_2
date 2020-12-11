import csv


with open('data-398-2018-08-30.csv', 'r', encoding='cp1251') as file:
    reader = csv.DictReader(file)
    # for row in reader:
    #     print(row['Name'], row['RouteNumbers'])

print(reader)