import csv

def highees_score(csv_file):

    more_score = -1
    student_with_highes_score = None

    with open(csv_file, 'r') as file:
         reader = csv.reader(file)
         next(reader)

         for row in reader:
              
              name = row[2]
              score = int(row[3])

              if score > more_score:
                   more_score = score
                   student_with_highes_score = name
    return student_with_highes_score , more_score

csv_file = 'Sample.csv'
men,score = highees_score(csv_file)

if men:
     print(f"more {men} with {score}")
else :
     print("no data found")