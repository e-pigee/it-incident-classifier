from sklearn.feature_extraction.text import TfidfVectorizer
import csv

vectorizer = TfidfVectorizer()

with open("data/tickets.csv") as file:
    reader = csv.DictReader(file)
    ticket_list = []
    x = []
    y = []
    
    for ticket in reader:
        ticket_list.append(ticket)
        x.append(ticket["description"])
        y.append(ticket["category"])
        
            # print(ticket_list)

    print("Descriptions:", len(x))
    print("Categories:", len(y))
    print("First description:", x[0])
    print("First category:", y[0])

x_tfidf = vectorizer.fit_transform(x)
x_token = vectorizer.get_feature_names_out()