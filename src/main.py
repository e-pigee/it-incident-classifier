import csv

with open("data/tickets.csv") as file:
    reader = csv.DictReader(file)
    ticket_list = []
    for ticket in reader:
        ticket_list.append(ticket)
    print(ticket_list)

