import streamlit as st
from stt_engine import transcribe_audio
from nlp_structuring import structure_medical_record
from utils import save_text

st.title("🎤 Voice-to-Text Medical Record Generator")

uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

if uploaded_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Transcribing audio... please wait.")
    text = transcribe_audio("temp_audio.wav")

    st.subheader("Raw Transcription")
    st.write(text)

    st.info("Structuring medical record...")
    record = structure_medical_record(text)

    st.subheader("Generated Medical Record")
    st.text(record)

    if st.button("Save Record"):
        save_text(record)
        st.success("Saved to outputs/generated_record.txt")


