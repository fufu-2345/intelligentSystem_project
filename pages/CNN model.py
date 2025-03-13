import streamlit as st
import numpy as np
import joblib
from pydub import AudioSegment
import librosa
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

basePath = Path(__file__).parent.parent/"models"
model = joblib.load(basePath/"cnn2.sav")

N_MFCC = 128
SAMPLE_RATE = 48000
label_map = {'Amau Ako': 0, 'Fuwa Renge': 1, 'Izumimoto Eimi': 2, 'Hakari Atsuko': 3, 'Ichinose Asuna': 4, 'Asahina Pina': 5, 'Wanibuchi Akari': 6, 'Akashi Junko': 7, 'Akeshiro Rumi': 8, 'Aikiyo Fuuka': 9, 'Okusora Ayane': 10, 'Motomiya Chiaki': 11, 'Kozeki Ui': 12, 'Kayama Reijo': 13, 'Shirasu Azusa': 14, 'Murokasa Akane': 15, 'Nemugaki Fubuki': 16, 'Renkawa Cherino': 17, 'Rikuhachima Aru': 18, 'Kurimura Airi': 19, 'Tendou Alice': 20, 'Ushimaki Juri': 21, 'Tsukatsuki Rio': 22, 'Uzawa Reisa': 23}
def extract_features(file_path):
    
    y, sr = librosa.load(file_path, sr=SAMPLE_RATE)

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC) 
    features = mfcc.mean(axis=1)  # ใช้เฉพาะ MFCC
    
    return features


def predict_top_3_speakers(file_path):
    feature = extract_features(file_path)
    feature = feature.reshape(1, 128, 1, 1)
    prediction = model.predict(feature)

    top_3_indices = np.argsort(prediction[0])[::-1][:3]

    top_3_speakers = []
    for idx in top_3_indices:
        speaker_id = idx
        speaker_name = [name for name, id in label_map.items() if id == speaker_id][0]
        confidence = prediction[0][idx] * 100 
        top_3_speakers.append((speaker_name, confidence))

    return top_3_speakers

st.title("Speaker Prediction Model")
st.write("This model predicts the top 3 speakers based on the audio file.")

st.write("Dataset's source: https://bluearchive.wiki/wiki/Category:Characters_audio")
    
uploaded = st.file_uploader("Upload an MP3 file", type=["mp3"])

if uploaded is not None:
    audio = AudioSegment.from_mp3(uploaded)
    wav_file_path = "uploaded_audio.wav"
    audio.export(wav_file_path, format="wav")

    top_3_predicted_speakers = predict_top_3_speakers(wav_file_path)

    st.write("Top 3 Predicted Speakers:")
    for rank, (speaker, confidence) in enumerate(top_3_predicted_speakers, 1):
        st.write(f"Rank {rank}: {speaker} - Confidence: {confidence:.2f}%")

st.write("")
st.write("")
st.title("download audio file guide") 
st.write("1.choose the character you want")
st.image("imgs/1.png")
st.write("2.choose the voice line you want to download")
st.image("imgs/2.png")
st.write("3.click i button")
st.image("imgs/3.png")
st.write("4.click the download button")
st.image("imgs/4.png")