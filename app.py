import streamlit as st
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import speech_recognition as sr

# Load model and vectorizer
model = joblib.load("model/scam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(page_title="SafeTalk AI", page_icon="🧠", layout="centered")
st.title("🧠 SafeTalk AI: Scam Message & Call Detection System")
st.markdown("Detect suspicious or emotionally manipulative messages in real time.")

# --- Helper Functions ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def predict_message(message):
    cleaned = clean_text(message)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    return prediction

# --- Tabs ---
tab1, tab2 = st.tabs(["💬 Text Message", "🎙️ Voice Message"])

with tab1:
    msg = st.text_area("Enter the message text:")
    if st.button("Analyze Message"):
        if msg.strip():
            result = predict_message(msg)
            if result == 1:
                st.error("⚠️ This message may be fraudulent!")
            else:
                st.success("✅ This message seems safe.")
        else:
            st.warning("Please enter some text.")

with tab2:
    audio_file = st.file_uploader("Upload a voice message (WAV format)", type=["wav"])
    if audio_file is not None:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            with open("uploaded_audio.wav","wb") as f:
                f.write(audio_file.getbuffer())
            st.info("audio file saved as uploaded_audio.wav")
            try:
                text = recognizer.recognize_google(audio)
                st.write("**Transcribed Message:**", text)
                result = predict_message(text)
                if result == 1:
                    st.error("⚠️ Scam detected from voice message!")
                else:
                    st.success("✅ Voice message seems safe.")
            except Exception as e:
                st.warning("Couldn't process the audio. Please try again.")
