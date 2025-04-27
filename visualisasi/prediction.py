import streamlit as st
import pickle
import pandas as pd

# Load model
with open('best_random_forest_model_ian.pkl', 'rb') as file:
    best_model = pickle.load(file)

def run():
    # Load dataset
    df = pd.read_csv("DatosPrueba_clean.csv")

    # Map state abbreviations to full names
    us_state_names = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
        'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'DC': 'District of Columbia',
        'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois',
        'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
        'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
        'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
        'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
        'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon',
        'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
        'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia',
        'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
    }

    df['state_full'] = df['state'].map(us_state_names)
    state_list = df['state_full'].dropna().unique().tolist()
    state_list.sort()
    category_map = {cat.replace('_', ' ').title(): cat for cat in df['category'].dropna().unique()}
    category_list = sorted(category_map.keys())

    st.title("🔍 Fraud Prediction Form")

    with st.form("fraud_form"):
        trans_hour = st.number_input('Transaction Hour (0-23):', min_value=0, max_value=23, value=0, help = 'Input transaction hour')
        amt = st.number_input('Transaction Amount ($):', min_value=0.0, value=0.0, step=1.0, help = 'Input transaction amount')
        age = st.number_input('Customer Age:', min_value=0, max_value=120, value=0, help = 'Input user age')
        category_label = st.selectbox('Transaction Category:', category_list, help = 'Input transaction category')
        state_full = st.selectbox('Customer State:', state_list, help = 'Input user state')

        submitted = st.form_submit_button('Predict')

    # Reverse maps
    reverse_state_map = {v: k for k, v in us_state_names.items()}
    state = reverse_state_map.get(state_full)
    category = category_map.get(category_label)

    # Inference DataFrame
    data_inf = pd.DataFrame([{
        'trans_hour': trans_hour,
        'amt': amt,
        'age': age,
        'category_label': category,
        'state_full': state
    }])

    st.write("### 🔎 Input Summary")
    st.dataframe(data_inf)

    if submitted:
        prediction_result = best_model.predict(data_inf)[0]
        result = "🟥 Fraud Detected!" if prediction_result == 1 else "✅ Legitimate Transaction"

        st.subheader("Prediction Result")
        st.success(result) if prediction_result == 0 else st.error(result)

if __name__ == '__main__':
    run()