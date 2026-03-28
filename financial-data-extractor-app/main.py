### Boilerplate code
import streamlit as st
import pandas as pd
from data_extractor_app import extract_data

st.title("Financial Data Extractor")

paragraph = st.text_area("Enter financial paragraph:")

if st.button("Extract"):
    if paragraph:
        extracted_data = extract_data(paragraph)
        ## Creating a dataframe-table
        data = {
            'Measure': ['Revenue', 'EPS'],
            'Estimated (amount in $)': [extracted_data['revenue_expected'], extracted_data['eps_expected']],
            'Actual (amount in $)': [extracted_data['revenue_actual'], extracted_data['eps_actual']]
        }
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("Please enter a paragraph to extract data from.")