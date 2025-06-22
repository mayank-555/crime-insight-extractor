# crime_insight_extractor.py

import os
import whisper
import json
import streamlit as st
from googletrans import Translator
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load Whisper model
model = whisper.load_model("base")  # Use 'small' or 'medium' for better accuracy

# Translation
translator = Translator()

def transcribe_and_translate(audio_path):
    # Transcription
    result = model.transcribe(audio_path)
    original_text = result["text"]

    # Detect language
    detected_lang = translator.detect(original_text).lang
    translated_text = original_text

    if detected_lang != 'en':
        translated_text = translator.translate(original_text, dest='en').text

    return original_text, translated_text

def extract_info(text):
    doc = nlp(text)
    location = ""
    time = ""
    person = ""
    
    for ent in doc.ents:
        if ent.label_ == "GPE" and not location:
            location = ent.text
        elif ent.label_ == "TIME" and not time:
            time = ent.text
        elif ent.label_ == "PERSON" and not person:
            person = ent.text

    category = classify_complaint(text)

    return {
        "Complaint Category": category,
        "Location": location,
        "Time": time,
        "Person Involved": person
    }

def classify_complaint(text):
    text = text.lower()
    if "robbery" in text or "stolen" in text:
        return "Robbery"
    elif "assault" in text or "hit" in text:
        return "Assault"
    elif "cyber" in text or "online" in text:
        return "Cybercrime"
    else:
        return "Other"

# Streamlit UI
st.title("🔍 Police Complaint Insight Extractor")

uploaded_file = st.file_uploader("Upload a police call audio (.mp3/.wav)", type=["mp3", "wav"])

if uploaded_file is not None:
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("Processing audio, please wait...")

    original, translated = transcribe_and_translate("temp_audio.mp3")
    info = extract_info(translated)

    result = {
        "Transcript (Original)": original,
        "Translated Text": translated,
        **info
    }

    st.subheader("📝 Extracted Insights")
    st.json(result)

    # Save to JSON (optional)
    with open("output.json", "w") as outfile:
        json.dump(result, outfile, indent=4)

    st.success("✅ Completed and saved result as output.json")
