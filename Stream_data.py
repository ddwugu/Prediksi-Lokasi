import pickle
import streamlit as st

try:
    # Load the model
    LokasiKM = pickle.load(open('Pred_lokasi.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading the model: {e}")

# Web Title
st.title('Pertamina Field Jambi')

# User Inputs
Titik_1_PSI = st.text_input('Input Pressure di titik 1 (PSI)')
Titik_2_PSI = st.text_input('Input Pressure di titik 2 (PSI)')

# Prediction Code
suspect_loct = ''

# Prediction Button
if st.button('Prediksi Lokasi'):
    try:
        prediksi_lokasi = LokasiKM.predict([[float(Titik_1_PSI), float(Titik_2_PSI)]])
        if prediksi_lokasi[0] == 0:
            suspect_loct = 'Pipa Aman'
        elif prediksi_lokasi[0] == 26.8:
            suspect_loct = 'Tidak Terdapat Fluida yang Mengalir'
        else:
            suspect_loct = f'Terjadi di titik {prediksi_lokasi[0]} KM'
        st.success(suspect_loct)
    except Exception as e:
        st.error(f"Error predicting location: {e}")
