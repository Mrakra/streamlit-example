import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('telecom_customer_churn.csv')

df = load_data()

# Calculate total customers and churn
total_customers = len(df)
total_churn = df['Churn'].sum()

# Display total customers and churn
st.title('Churn Analysis')
st.write(f'Total Customers: {total_customers}')
st.write(f'Total Churn: {total_churn}')

# Customer ID input
customer_id = st.text_input('Enter Customer ID')

# Function to get churn prediction and reason
def predict_churn_and_reason(customer_id):
    if customer_id:
        customer_row = df[df['Customer ID'] == customer_id]
        if not customer_row.empty:
            churn_prediction = 'Yes' if customer_row['Churn'].iloc[0] == 'Yes' else 'No'
            churn_reason = customer_row['Churn Reason'].iloc[0]
            return churn_prediction, churn_reason
        else:
            return 'Customer ID not found', ''
    else:
        return '', ''

# Button to get churn prediction and reason
if st.button('Enter Customer ID'):
    churn_prediction, churn_reason = predict_churn_and_reason(customer_id)
    st.write(f'Customer ID: {customer_id}')
    st.write(f'Expected to Churn: {churn_prediction}')
    st.write(f'Reason for Churn: {churn_reason}')
