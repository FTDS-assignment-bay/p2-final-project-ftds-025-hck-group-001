# app.py
import streamlit as st
import eda
import prediction
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Logo
st.sidebar.image('logo.png', use_container_width=True)

# CSS
st.markdown("""
    <style>
        .stButton > button {
            background-color: #5B4E65; 
            color: #FFF !important;
            border: none;
            padding: 10px 24px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            width: 100%;
            transition: background-color 0.3s ease, color 0.3s ease;

        }
        .stButton > button:hover {
            background-color: #4C1973;
        }

        .stRadio > button[aria-checked="true"] {
            background-color: #4C1973 !important;
            color: #FFF !important;
        }

        .stRadio > button[aria-checked="false"] {
            background-color: #5B4E65;
        }
            
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Pilih Menu")

# Session state
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = "Home"

# Buttons
home_button = st.sidebar.button("Home")
prediction_button = st.sidebar.button("Prediction")

if home_button:
    st.session_state.selected_menu = "Home"
elif prediction_button:
    st.session_state.selected_menu = "Prediction"

# Content
if st.session_state.selected_menu == "Home":
    df = pd.read_csv('DatosPrueba_clean.csv')

    st.title("🛡️ Welcome to Fraudtotype")
    st.subheader("Application designed to prevent potential fraud activities")

    # image
    image = Image.open('fraud-detection.png')
    st.image(image, caption='', use_container_width=True)

    st.markdown('---')

    # Section 1: Project Introduction
    st.markdown("### 📌 Project Introduction")
    st.write("""
    Fraudtotype is a smart application designed to analyze and predict potential fraud activities. By combining transaction pattern analysis with machine learning technology, Fraudtotype helps businesses identify suspicious behavior before it causes significant losses.
    """)

    # Section 2: Objective
    st.markdown("### 🎯 Objective")
    st.write("""
    The main objective is to build a reliable fraud detection model using historical credit card transaction data. 
    By identifying fraud patterns, we aim to reduce losses and protect customers.
    """)

    # Section 3: Dataset
    column_data = {
        'Column Name': ['Trans_date_trans_time', 'Cc_num', 'Merchant', 'Category', 'Amt', 
                        'First', 'Last', 'Gender', 'Street', 'City', 'State', 'Zip',
                        'Lat', 'Long', 'City_pop', 'Job', 'Dob', 'Trans_num', 'Unix_time',
                        'Merch_lat', 'Merch_long', 'Is_fraud'],
        'Description': [
            'Timestamp of the transaction (date and time)',
            'Unique customer identification number',
            'The merchant involved in the transaction',
            'Transaction type (e.g., personal, childcare)',
            'Transaction amount',
            'User first name',
            'User last name',
            'User gender',
            'User street address',
            'User city of residence',
            'User state of residence',
            'User zip code',
            'Latitude of User location',
            'Longitude of User location',
            'Population of the User city',
            'User job title',
            'User date of birth',
            'Unique transaction identifier',
            'Transaction timestamp (Unix format)',
            'Merchant location (latitude)',
            'Merchant location (longitude)',
            'Fraudulent transaction indicator'
        ]
    }
    df_columns = pd.DataFrame(column_data)
    st.markdown("### 📊 Dataset Descriptions")
    st.write("Below is the description of each column in the dataset:")
    st.dataframe(df_columns)

    # Section 4: Tools and Libraries
    st.markdown("### 🛠️ Tools and Libraries")
    st.write("""
    - Python: For data preprocessing, modeling, and deployment
    - Pandas: For data manipulation and analysis
    - Numpy: For numerical operations and array handling
    - Matplotlib & Seaborn: For data visualization
    - Scikit-learn: Pipeline RandomForestClassifier, LogisticRegression, GridSearchCV
    - GridSearchCV: For hyperparameter tuning
    - Pickle : For model saving
    """)

    # Section 4: Modeling Algorithms
    st.markdown("### 🧠 Models Used")
    st.write("""
    We experimented with several classification models:
    - Logistic Regression
    - Random Forest Classifier
    - GridSearchCV for hyperparameter tuning
    - Target Encoding for categorical features
    - Undersampling to address class imbalance
    """)

    # Section 5: Model Performance
    st.markdown("### 🎯 Evaluation Results")
    st.write("""
    Based on classification reports and cross-validation:
    - Recall: 98%
    - Hyperparameter tuning using `GridSearchCV`
    - Final model chosen: `Random Forest Classifier with Hyperparameter Tuning`
    """)

elif st.session_state.selected_menu == "Prediction":
    prediction.run()
