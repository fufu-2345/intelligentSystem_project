import streamlit as st

st.title("Ensemble model")
st.write("This is model created with 3 models")
st.write("KNN, SVM, Decision tree and ensemble them together.")
st.write("for prediction this model using Random forest(hard voting)")
st.write("")
st.write("while train the model I train one by one model and dump into .sav file")
st.write("then load all of them and ensemble them into one model")
st.write("")
st.write("")

####################################
####################################
###### explan feature dataset
st.title("Dataset")
st.write("source dataset: https://www.kaggle.com/datasets/kevinarvai/clinvar-conflicting")
st.write("this dataset has 65188 rows and 46 columns and contain NaN values null values")
st.write("to clean the data I drop all the rows that contain NaN values null values and not important columns") 
st.write("after that I got 65188 rows and 11 columns or 5 columns depend on the models")
st.write("")
st.write("but some columns contain string values so I encode them into numerical values")
st.write("and scale the data using StandardScaler for improve data to be more performance training")
st.write("after that I dump LabelEncoder and scaler into .pkl file for use in website")
st.write("if I don't dump them, the next time I scale or use LabelEncoder")
st.write("the results might be different, leading to prediction errors.")
st.write("")
st.write("for more detail about the dataset cleaning")
st.write("I use scaler for 'POS', 'AF_ESP', 'AF_EXAC', 'AF_TGP' columns")
st.write("and LabelEncoder for 'CHROM', 'REF', 'ALT', 'CLNVC', 'ORIGIN', 'Allele', 'IMPACT' columns")
st.write("")
st.write("")

####################################
####################################

st.title("1.KNN")
st.write("k=15")
st.write("")

st.title("2.SVM")
st.write("kernel='poly', degree=3, C=2.005")
st.write("")

st.title("3.decision tree")
st.write("max_depth=15, min_samples_split=10, criterion=entropy")


