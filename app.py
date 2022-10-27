import streamlit as st
#from PIL import Image
import pickle

model = pickle.load(open('pickle_model/model_pkl.pickle', 'rb'))


def run():
    
    st.title("Prédiction de prêt bancaire")

    ## Account No
    account_no = st.text_input('Numéro du compte')

    ## Full Name
    fn = st.text_input('Nom / Prénom')

    ## For gender
    gen_display = ('Femme','Homme')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Genre",gen_options, format_func=lambda x: gen_display[x])

    ## No of dependets
    dep_display = ('Non','Un','Deux','Plus de deux')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dépendents",  dep_options, format_func=lambda x: dep_display[x])

    ## For edu
    edu_display = ('Non diplômé','Diplômé')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('Job','Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Endroit de résidence",prop_options, format_func=lambda x: prop_display[x])

    ## For Credit Score
    cred_display = ('0','1')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Historique de prêt",cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("Salaire mensuelle du demandeur",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Salaire mensuelle du codemandeur",value=0)

    ## Loan AMount
    loan_amt = st.number_input("Prix du prêt",value=0)

    ## loan duration
    dur_display = ['2 Mois','6 Mois','8 Mois','1 Année','16 Mois']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Durée du prêt",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Prédiction du prêt"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Bonjour: " + fn +" || "
                "Numéro de compte: "+account_no +' || '
                'Suite à nos calcul vous ne pouvez pas prétendre à un prêt bancaire.'
            )
        else:
            st.success(
                "Bonjour: " + fn +" || "
                "Numéro de compte "+account_no +' || '
                'Félécitations! Vous pouvez prétendre à un prêt bancaire !'
            )

run()

#cycler==0.10
#protobuf>=3.20.1
#kiwisolver>=1.0.1
#cachetools==5.2.0
#GitPython==3.1.29
#jsonschema==4.16.0
#Jinja2==3.1.2
#toolz==0.12.0
#gitdb==4.0.9
#urllib3==1.26.12
#decorator>=3.4.0
#MarkupSafe==2.1.1
#pyrsistent==0.18.1
#MarkupSafe==2.1.1
#click==8.0.0
