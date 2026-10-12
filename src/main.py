import csv

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# 1. Load historical tickets
with open("data/tickets.csv", newline="") as file:
    reader = csv.DictReader(file)
    ticket_list = list(reader)

x = [ticket["description"] for ticket in ticket_list]
y = [ticket["category"] for ticket in ticket_list]


# 2. Split data for training and evaluation
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)


# 3. Train and evaluate the classifier
vectorizer = TfidfVectorizer()
model = MultinomialNB()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)
model_score = accuracy_score(y_test, y_pred)
generate_class_report = classification_report(y_test, y_pred)

# Evaluation is available when needed:
# print("Accuracy:", model_score)
# print(generate_class_report)


# 4. Prepare similarity search using all historical tickets
similarity_vectorizer = TfidfVectorizer()
similarity_search_train = similarity_vectorizer.fit_transform(x)


# 5. Get a new ticket description
similarity_search_desc = input("Enter a ticket description: ")

# Convert the description for classification
similarity_search_convert = vectorizer.transform([similarity_search_desc])
predicted_category = model.predict(similarity_search_convert)


# Convert the description for similarity search
similarity_search_value = similarity_vectorizer.transform([similarity_search_desc])

similarity_search_score = cosine_similarity(
    similarity_search_train, similarity_search_value
).flatten()

top_three = np.argsort(similarity_search_score)[::-1][:3]


# 6. Display the predicted category
print(f"Predicted category: {predicted_category[0]}")
print()


# 7. Display similar tickets that meet the threshold
found_match = False

for index in top_three:
    score = similarity_search_score[index] * 100

    if score < 30:
        break

    found_match = True
    matching_ticket = ticket_list[index]

    print("Description:", matching_ticket["description"])
    print("Category:", matching_ticket["category"])
    print("Resolution:", matching_ticket["resolution"])
    print(f"Similarity: {score:.2f}%")
    print()

if not found_match:
    print("No meaningful word match found.")
