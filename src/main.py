from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
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
      
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
