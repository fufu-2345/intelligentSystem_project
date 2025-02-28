import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import joblib

ensemblePath = '../models/ensemble_model 1.sav'

st.title("ensembleModel.py")
st.write("this is ensembleModel.py")

scaler = joblib.load('./scaler/scaler_model.pkl')
labelEn = joblib.load('./scaler/label_encoder_model.pkl')

st.title("Input Form")
features = ['CHROM','POS','REF','ALT','AF_ESP','AF_EXAC','AF_TGP','CLNVC','ORIGIN','CLASS','Allele','IMPACT']


def on_submit():
    data = pd.DataFrame([[
        chrom, pos, ref, alt, af_esp, af_exac, af_tgp, clnvc, origin, consequence, allele, impact
    ]], columns=features)

    st.write("Original data:")
    st.write(data)

    # ใช้ scaler ที่โหลดมาเพื่อแปลงข้อมูล
    data['POS'] = scaler.transform(data[['POS']])
    data['AF_ESP'] = scaler.transform(data[['AF_ESP']])
    data['AF_EXAC'] = scaler.transform(data[['AF_EXAC']])
    data['AF_TGP'] = scaler.transform(data[['AF_TGP']])



    # แสดงผลข้อมูลหลังจากแปลง
    st.write("Data after scaling and encoding:")
    st.write(data)
    
with st.form("input_form"):
    chrom = st.text_input("CHROM", "1")
    pos = st.number_input("POS", value=1168180, step=1)
    ref = st.text_input("REF", "G")
    alt = st.text_input("ALT", "C")
    af_esp = st.number_input("AF_ESP", value=0.0771)
    af_exac = st.number_input("AF_EXAC", value=0.10020)
    af_tgp = st.number_input("AF_TGP", value=0.1066)
    clndisdb = st.text_input("CLNDISDB", "MedGen:CN169374")
    clndisbinc = st.text_input("CLNDISDBINCL", "AA")
    clndn = st.text_input("CLNDN", "not_specified")
    clndnincl = st.text_input("CLNDNINCL", "1.00081")
    clnhgvs = st.text_input("CLNHGVS", "NC_000001.10:g.1168180G>C")
    clnsigincl = st.text_input("CLNSIGINCL", "-2")
    clnvc = st.text_input("CLNVC", "single_nucleotide_variant")
    clnvi = st.text_input("CLNVI", "UniProtKB_(protein):Q96L58#VAR_059317")
    mc = st.text_input("MC", "SO:0001583|missense_variant")
    origin = st.text_input("ORIGIN", "1")
    ssr = st.text_input("SSR", "AR")
    allele = st.text_input("Allele", "C")
    consequence = st.text_input("Consequence", "missense_variant")
    impact = st.text_input("IMPACT", "MODERATE")
    symbol = st.text_input("SYMBOL", "B3GALT6")
    feature_type = st.text_input("Feature_type", "Transcript")
    feature = st.text_input("Feature", "NM_080605.3")
    biotype = st.text_input("BIOTYPE", "protein_coding")
    exon = st.text_input("EXON", "1/1")
    intron = st.text_input("INTRON", "w")
    cdna_position = st.text_input("cDNA_position", "552")
    cds_position = st.text_input("CDS_position", "522")
    protein_position = st.text_input("Protein_position", "174")
    amino_acids = st.text_input("Amino_acids", "E/D")
    codons = st.text_input("Codons", "gaG/gaC")
    distance = st.number_input("DISTANCE", value=1, step=1)
    strand = st.text_input("STRAND", "753.159")
    bam_edit = st.text_input("BAM_EDIT", "AC")
    sift = st.text_input("SIFT", "tolerated")
    polyphen = st.text_input("PolyPhen", "benign")
    motif_name = st.text_input("MOTIF_NAME", "K1")
    motif_pos = st.text_input("MOTIF_POS", "431")
    high_inf_pos = st.text_input("HIGH_INF_POS", "0.0183")
    motif_score_change = st.text_input("MOTIF_SCORE_CHANGE", "0.021")
    loftool = st.number_input("LoFtool", value=1.053)
    cadd_phred = st.number_input("CADD_PHRED", value=-0.208682)
    cadd_raw = st.number_input("CADD_RAW", value=2.0)
    blosum62 = st.number_input("BLOSUM62", value=2.0)
        
    submitted = st.form_submit_button("Submit")
        
    if submitted:
        on_submit()
            
