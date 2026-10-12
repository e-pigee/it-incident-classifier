from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import csv

vectorizer = TfidfVectorizer()
model = MultinomialNB()

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
    x, y, test_size=0.2, random_state=42, stratify=y
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)
model_score = accuracy_score(y_test, y_pred)
generate_class_report = classification_report(y_test, y_pred)
print(f"model score is {model_score}")
print(generate_class_report)