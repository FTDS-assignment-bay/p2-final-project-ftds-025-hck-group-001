import streamlit as st
import eda
import prediction

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
getting_started_button = st.sidebar.button("Exploratory Data Analysis")
documentation_button = st.sidebar.button("Prediction")

if home_button:
    st.session_state.selected_menu = "Home"
elif getting_started_button:
    st.session_state.selected_menu = "Exploratory Data Analysis"
elif documentation_button:
    st.session_state.selected_menu = "Prediction"

#Content
if st.session_state.selected_menu == "Home":
    st.title("Welcome to the Home Page")
elif st.session_state.selected_menu == "Exploratory Data Analysis":
    eda.run()
elif st.session_state.selected_menu == "Prediction":
    st.title("Documentation")