import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('penyakit_jantung.sav','rb'))

#judul web
st.title('memprediksi penyakit jantung')

col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input('Umur')
with col2:
    sex = st.number_input('Jenis Kelamin')
with col3:
    cp = st.number_input('Jenis Nyeri Dada')
with col4:
    trestbps = st.number_input('Tekanan Darah')
with col1:
    chol = st.number_input('Kolestrol')
with col2:
    fbs = st.number_input('Gula Darah')
with col3:
    restecg = st.number_input('Hasil Elektrokadriografi')
with col4:
    thalach = st.number_input('Detak Jantung Maksimum')
with col1:
    exang = st.number_input('Induksi Angina')
with col2:
    oldpeak = st.number_input('ST Depression')
with col3:
    slope = st.number_input('Slope')
with col4:
    ca = st.number_input('NIlai Ca')
with col1:
    thal = st.number_input('Nilai Thal')

# code for prediction
heart_diagnosis =''

# membuat tombol prediksi
if st.button('Hasil Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if (heart_prediction[0]==1):
        heart_diagnosis = 'Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Tidak Terkena Penyakit Jantung'
st.success(heart_diagnosis)
                     