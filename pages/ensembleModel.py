import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import joblib

ensemblePath = '../models/ensemble_model 1.sav'
ensemble_model = joblib.load('./models/ensemble_model 1.sav')

st.title("ensembleModel.py")
st.write("this is ensembleModel.py")

scaler = joblib.load('./scaler/scaler_model.pkl')
labelEn = joblib.load('./scaler/label_encoders.pkl')

st.title("Input Form")
features = ['CHROM','POS','REF','ALT','AF_ESP','AF_EXAC','AF_TGP','CLNVC','ORIGIN','Allele','IMPACT']

def on_submit(CHROM, POS, REF, ALT, AF_ESP, AF_EXAC, AF_TGP, CLNVC, ORIGIN, Allele, IMPACT):
    data = pd.DataFrame([[CHROM, POS, REF, ALT, AF_ESP, AF_EXAC, AF_TGP, CLNVC, ORIGIN, Allele, IMPACT]],
                        columns=['CHROM', 'POS', 'REF', 'ALT', 'AF_ESP', 'AF_EXAC', 'AF_TGP', 'CLNVC', 'ORIGIN', 'Allele', 'IMPACT'])

    st.write("Original data:")
    st.write(data)
    
    #numeric_data = data.select_dtypes(include=['number'])

    #scaler.fit(numeric_data)
    #print(scaler.feature_names_in_)

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
    
    st.write("Data after scaling, encoding, and ensuring column alignment:")
    st.write(data)
    
    prediction = ensemble_model.predict(data)

    # เก็บผลการพยากรณ์ในตัวแปร
    prediction_result = prediction[0]  # รับค่าผลลัพธ์จากการพยากรณ์ (ค่าผลลัพธ์อาจจะเป็นตัวแปรหนึ่งค่าหรืออาเรย์)

    # แสดงผลการพยากรณ์
    st.write("Prediction Result:")
    st.write(prediction_result)
    
with st.form("input_form"):
    CHROM = st.text_input("CHROM", "1")
    POS = st.number_input("POS", value=1168180, step=1)
    REF = st.text_input("REF", "G")
    ALT = st.text_input("ALT", "C")
    AF_ESP = st.number_input("AF_ESP", value=0.0771)
    AF_EXAC = st.number_input("AF_EXAC", value=0.10020)
    AF_TGP = st.number_input("AF_TGP", value=0.1066)
    CLNDISDB = st.text_input("CLNDISDB", "MedGen:CN169374")
    CLNDISDBINCL = st.text_input("CLNDISDBINCL", "AA")
    CLNDN = st.text_input("CLNDN", "not_specified")
    CLNDNINCL = st.text_input("CLNDNINCL", "1.00081")
    CLNHGVS = st.text_input("CLNHGVS", "NC_000001.10:g.1168180G>C")
    CLNSIGINCL = st.text_input("CLNSIGINCL", "-2")
    CLNVC = st.text_input("CLNVC", "single_nucleotide_variant")
    CLNVI = st.text_input("CLNVI", "UniProtKB_(protein):Q96L58#VAR_059317")
    MC = st.text_input("MC", "SO:0001583|missense_variant")
    ORIGIN = st.text_input("ORIGIN", "1")
    SSR = st.text_input("SSR", "AR")
    ALLELE = st.text_input("Allele", "C")
    CONSEQUENCE = st.text_input("Consequence", "missense_variant")
    IMPACT = st.text_input("IMPACT", "MODERATE")
    SYMBOL = st.text_input("SYMBOL", "B3GALT6")
    FEATURE_TYPE = st.text_input("Feature_type", "Transcript")
    FEATURE = st.text_input("Feature", "NM_080605.3")
    BIOTYPE = st.text_input("BIOTYPE", "protein_coding")
    EXON = st.text_input("EXON", "1/1")
    INTRON = st.text_input("INTRON", "w")
    CDNA_POSITION = st.text_input("cDNA_position", "552")
    CDS_POSITION = st.text_input("CDS_position", "522")
    PROTEIN_POSITION = st.text_input("Protein_position", "174")
    AMINO_ACIDS = st.text_input("Amino_acids", "E/D")
    CODONS = st.text_input("Codons", "gaG/gaC")
    DISTANCE = st.number_input("DISTANCE", value=1, step=1)
    STRAND = st.text_input("STRAND", "753.159")
    BAM_EDIT = st.text_input("BAM_EDIT", "AC")
    SIFT = st.text_input("SIFT", "tolerated")
    POLYPHEN = st.text_input("PolyPhen", "benign")
    MOTIF_NAME = st.text_input("MOTIF_NAME", "K1")
    MOTIF_POS = st.text_input("MOTIF_POS", "431")
    HIGH_INF_POS = st.text_input("HIGH_INF_POS", "0.0183")
    MOTIF_SCORE_CHANGE = st.text_input("MOTIF_SCORE_CHANGE", "0.021")
    LOFTOOL = st.number_input("LoFtool", value=1.053)
    CADD_PHRED = st.number_input("CADD_PHRED", value=-0.208682)
    CADD_RAW = st.number_input("CADD_RAW", value=2.0)
    BLOSUM62 = st.number_input("BLOSUM62", value=2.0)

        
    submitted = st.form_submit_button("Submit")
        
    if submitted:
        on_submit(CHROM, POS, REF, ALT, AF_ESP, AF_EXAC, AF_TGP, CLNVC, ORIGIN, ALLELE, IMPACT)
            
