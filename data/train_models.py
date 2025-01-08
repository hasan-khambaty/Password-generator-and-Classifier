import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle

# Load the dataset
df = pd.read_csv('cleanpasswordlist.csv')

# Ensure the dataset has the expected columns
assert 'password' in df.columns and 'strength' in df.columns, "Dataset must have 'password' and 'strength' columns."

# Drop rows with missing values in the 'password' or 'strength' columns
df = df.dropna(subset=['password', 'strength'])

# Ensure the 'password' column contains strings and 'strength' is numeric
df['password'] = df['password'].astype(str)
df['strength'] = df['strength'].astype(int)

# Extract passwords and labels
X = df['password']
y = df['strength']  # Numeric values: 1 for weak, 2 for strong, etc.

# Convert passwords into numerical features using CountVectorizer
cv = CountVectorizer(analyzer='char', ngram_range=(1, 2))  # Character-level n-grams
X_transformed = cv.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Train a Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# Train a Logistic Regression model
logit_model = LogisticRegression(max_iter=1000)
logit_model.fit(X_train, y_train)

# Evaluate both models
print("Naive Bayes Model Report:")
print(classification_report(y_test, nb_model.predict(X_test)))

print("Logistic Regression Model Report:")
print(classification_report(y_test, logit_model.predict(X_test)))

# Save the models and vectorizer as .pkl files
with open('pswd_cv.pkl', 'wb') as file:
    pickle.dump(cv, file)

with open('nv_pswd_model.pkl', 'wb') as file:
    pickle.dump(nb_model, file)

with open('logit_pswd_model.pkl', 'wb') as file:
    pickle.dump(logit_model, file)

print("Models and vectorizer saved successfully!")
