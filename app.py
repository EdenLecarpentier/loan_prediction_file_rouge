
import streamlit as st




st.title("""
# Co2 Building
""")


st.selectbox('Gender : ',(
            'Male' , 'Female' ))

st.selectbox('Married : ',(
            'Yes' , 'No' ))

st.selectbox('Education : ',(
            'Graduate' , 'Not graduate' ))

st.selectbox('self_employed : ',(
            'Yes' , 'No' ))

st.selectbox('Credit hsitory : ',(
            '1.0' , '0' ))

st.number_input("Applicant's Monthly Income(€)")

st.number_input("Co-Applicant's Monthly Income(€)")

st.number_input('Loan Amount', value=0)

st.selectbox('Loan Duration : ',(
            '1 Month' , '2 Month', '3 Month' , '4 Month', '5 Month' , '6 Month', '7 Month' , '8 Month', '9 Month' , '10 Month' , '11 Month' , '12 Month' ))
