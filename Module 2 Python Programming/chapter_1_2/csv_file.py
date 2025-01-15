import csv

with open ("Ai_Micro_Degree.csv" , mode="w",newline='') as csvfile:
    add_csv=csv.writer(csvfile)
    add_csv.writerow(['Name', 'Address', 'Trade'])
    add_csv.writerow(['Aadil', 'Hyderabad' 'AI'])
    add_csv.writerow(['Ramesh', 'mumai', 'AIPA'])
    add_csv.writerow(['Daya', 'pune', 'CSA'])
print("Csv Created Successfully")

with open("AI_Micro_Degree.csv", newline='') as csvfile:
    csv1=csv.reader(csvfile)
    for row in csv1:
        print(row)
