import streamlit as st
import pickle
import pandas as pd

# with open('model_lg.pkl', 'rb') as model:
#     model = pickle.load(model)

def run():
  
    with st.form('bank_form'):

        #Age
        age = st.number_input('Age: ', min_value = 18, max_value = 100, value = 30, help = 'Isi usia user')

        #Marital
        marital = st.selectbox('Marital : ', ('married', 'single marital', 'divorce'), index = 0)

        #Education
        education = st.selectbox('Education : ', ('primary', 'secondary', 'tertiary', 'unknown'), index = 0)

        #Balance
        balance = st.number_input('Balance: ', min_value = 0, value = 0, help = 'Isi usia user')

        #Loan
        loan = st.selectbox('Loan : ', ('yes', 'no'), index = 0)

        #Housing Loan
        housing = st.selectbox('Housing Loan : ', ('yes', 'no'), index = 0)

        #Contact
        contact = st.selectbox('Communication type : ', ('cellular', 'telephone', 'unknown'), index = 0)
        
        #Duration
        duration = st.number_input('Last contact duration: ', min_value = 0, value = 0, help = 'Isi usia user')

        #Campaign
        campaign = st.number_input('Number of marketing team contact: ', min_value = 0, value = 0, help = 'Isi usia user')

        #Previous
        previous = st.number_input('Number of marketing team contact before: ', min_value = 0, value = 0, help = 'Isi usia user')

        #Outcome
        outcome = st.selectbox('Outcome of the previous marketing campaign: ', ('failure', 'nonexistent', 'unknown', 'success'), index = 0)

        st.markdown('---')

        #High Skill Job
        job_high_skill = st.selectbox('High Skill Job : ', (1, 0), index = 1)

        #High Skill Job
        job_low_skill = st.selectbox('Low Skill Job : ', (1, 0), index = 1)
        
        #High Skill Job
        job_no_skill = st.selectbox('No Skill Job : ', (1, 0), index = 1)

        #Submit button
        submitted = st.form_submit_button('Predict')
    
    #Data Inference
    data_inf = {
        'age' : age,
        'marital' : marital,
        'education' : education,
        'balance' : balance,
        'housing' : housing,
        'loan' : loan,
        'contact' : contact,
        'duration' : duration,
        'campaign' : campaign,
        'previous' : previous,
        'outcome' : outcome,
        'job_high_skill' : job_high_skill,
        'job_low_skill' : job_low_skill,
        'job_no_skill' : job_no_skill
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)
    
    st.write('### Has the client subscribed a term deposit?')

    if submitted:
        # Prediction using saved models
        y_pred_inf = model.predict(data_inf)

        # Convert prediction results to text
        result = "Subscribed" if int(y_pred_inf) == 1 else "Not Subscribed"

        # Show Results
        st.write(result)

if __name__ == '__main__':
    run()