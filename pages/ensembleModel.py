import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from pathlib import Path
import joblib

basePath = Path(__file__).parent/"models"
ensemble_model = joblib.load(basePath/"ensemble_model1.sav")

st.title("ensembleModel.py")
st.write("this is ensembleMode l.py")

scaler = joblib.load('./scaler/scaler_model.pkl')
labelEn = joblib.load('./scaler/label_encoders.pkl')

st.title("Input Form")
features = ['CHROM','POS','REF','ALT','AF_ESP','AF_EXAC','AF_TGP','CLNVC','ORIGIN','Allele','IMPACT']

def on_submit(CHROM, POS, REF, ALT, AF_ESP, AF_EXAC, AF_TGP, CLNVC, ORIGIN, Allele, IMPACT):
    data = pd.DataFrame([[CHROM, POS, REF, ALT, AF_ESP, AF_EXAC, AF_TGP, CLNVC, ORIGIN, Allele, IMPACT]],
                        columns=['CHROM', 'POS', 'REF', 'ALT', 'AF_ESP', 'AF_EXAC', 'AF_TGP', 'CLNVC', 'ORIGIN', 'Allele', 'IMPACT'])

    st.write("Original data:")
    st.write(data)

    #streamlit run app.py
 
    columns_to_scale = ['POS', 'AF_ESP', 'AF_EXAC', 'AF_TGP']
    
    data[columns_to_scale] = scaler.transform(data[columns_to_scale].astype(float))

    for col in data.columns:
        if col in labelEn and col not in columns_to_scale:
            data[col] = labelEn[col].transform(data[col])
            
    st.write("Data after scaling and encoding:")
    st.write(data)
    
    required_columns = ['CHROM', 'POS', 'REF', 'ALT', 'AF_ESP', 'AF_EXAC', 'AF_TGP', 'CLNVC', 'ORIGIN', 'CLASS','Allele', 'IMPACT', ]
    for col in required_columns:
        if col not in data.columns:
            data[col] = 0 
            
    data = data[required_columns]
    
    prediction = ensemble_model.predict(data)

    prediction_result = prediction[0]

    st.write("**Prediction Result:**")
    if(prediction_result == 0):
        st.write("0 (The variant has consistent classifications)")
    else:
        st.write("1 (The variant has conflicting classifications)")
    
with st.form("input_form"):
    CHROM = st.text_input("CHROM", "1")
    POS = st.number_input("POS", value=1168180, step=1)
    REF = st.text_input("REF", "G")
    ALT = st.text_input("ALT", "C")
    AF_ESP = st.number_input("AF_ESP", value=0.0771)
    AF_EXAC = st.number_input("AF_EXAC", value=0.10020)
    AF_TGP = st.number_input("AF_TGP", value=0.1066)
    CLNVC = st.text_input("CLNVC", "single_nucleotide_variant")
    ORIGIN = st.text_input("ORIGIN", "1")
    ALLELE = st.text_input("Allele", "C")
    IMPACT = st.text_input("IMPACT", "MODERATE")

    st.write("Dataset's source: https://www.kaggle.com/datasets/kevinarvai/clinvar-conflicting")    
    
    submitted = st.form_submit_button("Submit")
        
    if submitted:
        on_submit(CHROM, POS, REF, ALT, AF_ESP, AF_EXAC, AF_TGP, CLNVC, ORIGIN, ALLELE, IMPACT)
            
