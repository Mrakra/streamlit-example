{
 "cells": [
  {
   "cell_type": "code",
   "id": "e4709edc-6715-4321-b7ea-1f31c05787e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "@st.cache\n",
    "def load_data():\n",
    "    return pd.read_csv('telecom_customer_churn.csv')\n",
    "\n",
    "df = load_data()\n",
    "\n",
    "total_customers = len(df)\n",
    "total_churn = df['Churn'].sum()\n",
    "\n",
    "\n",
    "st.title('Churn Analysis')\n",
    "st.write(f'Total Customers: {total_customers}')\n",
    "st.write(f'Total Churn: {total_churn}')\n",
    "\n",
    "\n",
    "customer_id = st.text_input('Enter Customer ID')\n",
    "\n",
    "\n",
    "def predict_churn_and_reason(customer_id):\n",
    "    if customer_id:\n",
    "        customer_row = df[df['Customer ID'] == customer_id]\n",
    "        if not customer_row.empty:\n",
    "            churn_prediction = 'Yes' if customer_row['Churn'].iloc[0] == 'Yes' else 'No'\n",
    "            churn_reason = customer_row['Churn Reason'].iloc[0]\n",
    "            return churn_prediction, churn_reason\n",
    "        else:\n",
    "            return 'Customer ID not found', ''\n",
    "    else:\n",
    "        return '', ''\n",
    "\n",
    "\n",
    "if st.button('Enter Customer ID'):\n",
    "    churn_prediction, churn_reason = predict_churn_and_reason(customer_id)\n",
    "    st.write(f'Customer ID: {customer_id}')\n",
    "    st.write(f'Expected to Churn: {churn_prediction}')\n",
    "    st.write(f'Reason for Churn: {churn_reason}')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
