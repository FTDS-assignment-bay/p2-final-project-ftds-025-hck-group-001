import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():

    #Title
    st.title('Bank Marketing Classification')

    #Image
    image = Image.open("bank_portugal.jpg")
    st.image(image)
    
    st.markdown('---')
    st.write('## Exploratory Data Analysis')

    #Load data
    st.write('### Data Loading')
    df = pd.read_csv('bank.csv', delimiter=';')
    st.dataframe(df)

    df = df.rename(columns = 
        {'poutcome' : 'outcome',
        'y' : 'subscribed'}
    )

    # Age Distribution
    st.write('### Age Distribution')
    fig = plt.figure(figsize=(12,5))
    sns.histplot(x=df['age'], bins=20, kde=True, color='blue')
    st.pyplot(fig)

    # Job Distribution
    st.write('### Job Distribution')
    fig = plt.figure(figsize=(12,10))
    sns.countplot(y=df['job'], order=df['job'].value_counts().index, hue=df['job'], palette="viridis")
    st.pyplot(fig)

    # Marital Distribution
    st.write('### Marital Distribution')
    fig = plt.figure(figsize=(12,10))
    sns.countplot(x=df['marital'], order=df['marital'].value_counts().index, hue=df['marital'], palette="viridis")
    st.pyplot(fig)

    # Education Distribution
    st.write('### Education Distribution')
    fig = plt.figure(figsize=(12,10))
    sns.countplot(x=df['education'], order=df['education'].value_counts().index, hue=df['education'], palette="viridis")
    st.pyplot(fig)

    # Loan or Housing Loan
    st.write('### Personal Loan Vs. Housing Loan')
    option = st.selectbox('Pilih column : ', ['loan', 'housing'])
    fig = plt.figure(figsize=(12,10))
    sns.countplot(data=df, x=option, palette="pastel")
    st.pyplot(fig)

    # Target Class Distribution
    st.write('### Target Class Distribution')
    fig = plt.figure(figsize=(12,10))
    sns.countplot(x=df['subscribed'], hue=df['subscribed'], palette="viridis")
    st.pyplot(fig)

if __name__ == '__main__':
    run()