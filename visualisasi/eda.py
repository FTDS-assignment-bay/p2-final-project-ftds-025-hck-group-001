import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():

    #Title
    st.title('Exploratory Data Analysis')
    
    #Load data
    st.write('### Data Loading')
    df = pd.read_csv('DatosPrueba_clean.csv')
    st.dataframe(df)

    # Fraud vs Non-Fraud Distribution (Bar Chart)
    st.subheader("📊 Fraud vs Non Fraud")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.countplot(x='is_fraud', data=df, palette="viridis", order=[0, 1], ax=ax1)
    ax1.set_title("Distribusi Fraud vs Non Fraud")
    ax1.set_xlabel("Distribusi")
    ax1.set_ylabel("Jumlah")
    ax1.set_xticklabels(['Non Fraud', 'Fraud'])
    st.pyplot(fig1)


if __name__ == '__main__':
    run()