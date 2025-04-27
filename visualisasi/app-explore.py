import streamlit as st
import eda
import prediction
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Logo
st.sidebar.image('logo.svg', use_column_width=True)

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

    #Load data
    df = pd.read_csv('DatosPrueba_clean.csv')

    # Title of the application
    st.title("🛡️ Welcome to Fraudtotype")
    st.subheader("Application designed to prevent potential fraud activities")

    #Image
    # image = Image.open("fraud-detection-system.jpg")
    # st.image(image)

    st.markdown('---')

    # Sample column descriptions (you can adjust this based on the actual dataset)
    column_data = {
        'Column Name': ['Trans_date_trans_time', 'Cc_num', 'Merchant', 'Category', 'Amt', 
                        'First', 'Last', 'Gender', 'Street', 'City', 'State', 'Zip',
                        'Lat', 'Long', 'City_pop', 'Job', 'Dob', 'Trans_num', 'Unix_time',
                        'Merch_lat', 'Merch_long', 'Is_fraud'
                    ],
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
            'Fraudulent transaction indicator (1 = fraud, 0 = legitimate). This is the target variable for classification purposes'
        ]
    }

    # Create a DataFrame from the dictionary
    df_columns = pd.DataFrame(column_data)

    # Display the DataFrame in Streamlit
    st.title("📊 Dataset Column Descriptions")
    st.write("Below is the description of each column in the dataset:")

    # Display the table
    st.dataframe(df_columns)
    












elif st.session_state.selected_menu == "Exploratory Data Analysis":
    eda.run()
elif st.session_state.selected_menu == "Prediction":
    st.title("Documentation")