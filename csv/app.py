import csv

# with open("names.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Alice", 30, "New York"])
#     writer.writerow(["Gwaka", 40, "Tanzania"])


with open("names.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
