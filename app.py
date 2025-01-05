import streamlit as st

import os.path

# ML package
import joblib

# Other packages
import random
import string


def password_gen(size):
    chars = string.digits + string.ascii_letters + string.punctuation
    gen_pass = "".join(random.choice(chars) for x in range(size))
    return gen_pass


def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

pswd_vectorizer = open("models/pswd_cv.pkl", "rb")
pswd_cv = joblib.load(pswd_vectorizer)

def get_key(val , my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

pass_label = {"weak": 0 , "medium": 1 , "strong": 2}

def main():
    """Password strength classifier"""
    st.title("Password Strength Classifier ML App")
    st.subheader("With Streamlit")

    activities = ["Classify Password", "Generate Password", "About"]

    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Classify Password":
        st.subheader("Classifying Password with ML")
        #password = st.text_input("Enter password", "Type here")  # < 0.54
        password = st.text_input("Enter password", type="password") #>= 0.54
        model_list = ["LR", "Naive Bayes"]
        model_choice = st.selectbox("Select ML", model_list)
        if st.button("Classify"):
            vect_pass = pswd_cv.transform([password]).toarray()
            if model_choice == "LR":
                predictor = load_model("models/logit_pswd_model.pkl")
                prediction = predictor.predict(vect_pass)
            elif model_choice == "Naive Bayes":
                predictor = load_model("models/nv_pswd_model.pkl")
                prediction = predictor.predict(vect_pass)

            final_predict = get_key(prediction , pass_label)
            st.info(final_predict)

    elif choice == "Generate Password":
        st.subheader("Generating password with ML")
        numb = st.number_input("Enter length of password", 8, 50)
        st.write(numb)
        if st.button("Generate"):
            custom_pass = password_gen(numb)
            st.write(custom_pass)
    else:
        st.subheader("About page")


if __name__ == '__main__':
    main()
