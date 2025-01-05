import pickle

# Load the vectorizer and models
with open('pswd_cv.pkl', 'rb') as file:
    cv = pickle.load(file)

with open('nv_pswd_model.pkl', 'rb') as file:
    nb_model = pickle.load(file)

with open('logit_pswd_model.pkl', 'rb') as file:
    logit_model = pickle.load(file)


# Function to classify a new password
def classify_password(password):
    """Classify password strength using both models."""
    # Transform the password into features
    password_features = cv.transform([password])

    # Predict using both models
    nb_prediction = nb_model.predict(password_features)[0]
    logit_prediction = logit_model.predict(password_features)[0]

    return {
        "Naive Bayes Prediction (Strength)": nb_prediction,
        "Logistic Regression Prediction (Strength)": logit_prediction
    }


# Test with a new password
test_password = "P@ssw0rd123!"
results = classify_password(test_password)

print(f"Password: {test_password}")
print("Predictions:")
for model, prediction in results.items():
    print(f"{model}: {prediction}")
