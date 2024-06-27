import csv

def average_score(csv_file):

    with open(csv_file, 'r') as file :

        reader = csv.reader(file)
        next(reader)

        average = 0

        for row in reader:

            salary = int(row[3])

            if row :
                average += salary

    print(average)

csv_file = 'Sample.csv'
average_score(csv_file)


