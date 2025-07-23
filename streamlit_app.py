import streamlit as st
import joblib
import numpy as np
import base64

model = joblib.load("stress_rf_model.pkl")

def set_bg_and_text(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        color: black !important;
        font-weight: bold !important;
    }}
    }}
    label, .stSlider span, .stSlider div {{
        color: black !important;
        font-weight: bold !important;
    }}
    section.main > div {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def coping_mechanism(level):
    if level == "LOW":
        return [
            "Tetap pertahankan rutinitas sehat",
            "Luangkan waktu istirahat",
            "Hindari overthinking"
        ]
    elif level == "MEDIUM":
        return [
            "Latihan pernapasan atau meditasi ringan",
            "Olahraga rutin",
            "Atur waktu belajar dan istirahat"
        ]
    else:
        return [
            "Konsultasi dengan psikolog",
            "Aktivitas fisik menyenangkan",
            "Kurangi tekanan sosial"
        ]

set_bg_and_text("static/bg.jpeg")

st.markdown("""
<h1 style='font-size:36px; font-weight:800; color:black;'>🧠 Stress Level Predictor</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); font-size:17px; line-height:1.6; color:black;'>
    <p><b>Silakan isi nilai dari setiap aspek berikut dengan skala 0 hingga 10:</b></p>
    <ul>
        <li><b>Financial Stress</b>: tekanan karena kondisi keuangan</li>
        <li><b>Peer Pressure</b>: tekanan dari lingkungan sosial atau teman</li>
        <li><b>Relationship Stress</b>: tekanan dari hubungan pribadi atau keluarga</li>
        <li><b>Sleep Quality</b>: kualitas tidur (semakin baik, nilai semakin tinggi)</li>
        <li><b>GPA</b>: nilai akademik kamu (semakin baik, nilai semakin tinggi)</li>
        <li><b>Exercise Frequency</b>: seberapa sering kamu olahraga (0 = tidak pernah)</li>
        <li><b>Cognitive Load</b>: seberapa berat beban mental atau tugasmu</li>
    </ul>
    <p>Nilai <b>0</b> berarti tidak ada tekanan sama sekali, dan <b>10</b> berarti tekanan sangat tinggi.<br>Isikan dengan jujur agar prediksi lebih akurat.</p>
</div>
""", unsafe_allow_html=True)

with st.form("stress_form"):
    with st.container():
        st.markdown("""
        <div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
            <h4 style='color:black;'>Financial Stress (0-10)</h4>
        </div>
        """, unsafe_allow_html=True)
        financial = st.number_input("", min_value=0.0, max_value=10.0, step=0.1, key="financial")
    with st.container():
        st.markdown("""
        <div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
            <h4 style='color:black;'>Peer Pressure (0-10)</h4>
        </div>
        """, unsafe_allow_html=True)
        peer = st.number_input("", min_value=0.0, max_value=10.0, step=0.1, key="peer")
    with st.container():
        st.markdown("""
        <div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
            <h4 style='color:black;'>Relationship Stress (0-10)</h4>
        </div>
        """, unsafe_allow_html=True)
        relationship = st.number_input("", min_value=0.0, max_value=10.0, step=0.1, key="relationship")
    with st.container():
        st.markdown("""
        <div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
            <h4 style='color:black;'>Sleep Quality (0-10)</h4>
        </div>
        """, unsafe_allow_html=True)
        sleep = st.number_input("", min_value=0.0, max_value=10.0, step=0.1, key="sleep")
    with st.container():
        st.markdown("""
        <div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
            <h4 style='color:black;'>GPA (0-10)</h4>
        </div>
        """, unsafe_allow_html=True)
        gpa = st.number_input("", min_value=0.0, max_value=10.0, step=0.1, key="gpa")
    with st.container():
        st.markdown("""
        <div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
            <h4 style='color:black;'>Exercise Frequency (0-10)</h4>
        </div>
        """, unsafe_allow_html=True)
        exercise = st.number_input("", min_value=0.0, max_value=10.0, step=0.1, key="exercise")
    with st.container():
        st.markdown("""
        <div style='background-color: #ffffffcc; padding: 1rem; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
            <h4 style='color:black;'>Cognitive Load (0-10)</h4>
        </div>
        """, unsafe_allow_html=True)
        cognitive = st.number_input("", min_value=0.0, max_value=10.0, step=0.1, key="cognitive")

    submitted = st.form_submit_button("Predict")

if submitted:
    data = [financial, peer, relationship, sleep, gpa, exercise, cognitive]
    total_stress = financial + peer + relationship + cognitive
    lifestyle = sleep + gpa + exercise
    features = np.array([data + [total_stress, lifestyle]])
    pred = model.predict(features)[0]

    level = "LOW" if pred == 0 else "MEDIUM" if pred == 1 else "HIGH"
    tips = coping_mechanism(level)

    st.markdown(f"""
<h2 style='font-size:28px; font-weight:700; color:black;'>Predicted Stress Level: {level}</h2>
""", unsafe_allow_html=True)
    st.markdown("""
<h3 style='font-size:22px; font-weight:600; color:black;'>💡 Coping Tips:</h3>
""", unsafe_allow_html=True)
    for tip in tips:
        st.markdown(f"- {tip}")
