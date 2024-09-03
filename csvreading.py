import csv
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print("Header:", header)
    for row in csv_reader:
        print(row)
