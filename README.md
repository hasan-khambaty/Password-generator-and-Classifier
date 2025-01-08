Password Strength Generator and Classifier

This project is a password strength generator and classifier that helps users generate strong passwords and evaluate the strength of existing passwords using machine learning models.

Features

Password Generator: Automatically generates strong passwords with customizable length and character sets.

Password Classifier: Classifies password strength as weak, moderate, or strong using a trained machine learning model.

User-Friendly Interface: Built using Streamlit for an interactive web-based experience.

Model Integration: Supports multiple classification models, including Logistic Regression, Decision Trees, and Random Forest.

Installation

Clone the repository:

git clone https://github.com/hasan-khambaty/Password-generator-and-Classifier

cd Password-generator-and-Classifier

Create a virtual environment (optional but recommended):

python3 -m venv venv

source venv/bin/activate

Install the required packages:

pip install streamlit

pip install joblib

Usage

Run the Streamlit application:

streamlit run app.py

Open the web app in your browser and:

Generate a strong password using the generator tool.

Test a password's strength using the classifier.

Project Structure

password-strength-classifier/

├── app.py                 # Main Streamlit web application

├── models/                # Trained models stored as .pkl files

├── data/                  # Datasets for training and testing


Model Training

To train a new model:

Prepare the dataset in the data/ folder.

Run the Jupyter notebooks in the notebooks/ directory for feature engineering and model training.

Export the trained model to the models/ folder using joblib.

Technologies Used

Python

Streamlit

Scikit-Learn

Pandas

Joblib

