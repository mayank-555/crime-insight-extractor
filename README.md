# 🚨 Crime Insight Extractor - AI Assessment (Redpluto Analytics)

An AI-powered tool to process police complaint call recordings and extract actionable crime insights. Built using Whisper for transcription, spaCy for NLP, and Streamlit for a simple interface.

---

## 🧠 Features

- 🎙️ Upload `.mp3` or `.wav` police call audio files
- 📝 Automatic transcription (via Whisper)
- 🌐 Auto-translation to English (if needed)
- 📊 Extraction of key information:
  - Complaint category (Robbery, Assault, Cybercrime, etc.)
  - Location, Time, Person involved (NER-based)
- 📦 JSON output + Streamlit UI display

---

## 📁 File Structure

```bash
crime-insight-extractor/
├── crime_insight_extractor.py      # Main Streamlit app
├── requirements.txt                # Python dependencies
├── .gitignore                      # To exclude venvs and outputs
├── call_112.mp3                    # Sample test audio
└── README.md                       # You are here 🚀
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/mayank-555/crime-insight-extractor.git
cd crime-insight-extractor
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the App
```bash
streamlit run crime_insight_extractor.py
```

---

## 📥 Sample Output
```json
{
    "Transcript (Original)": " Santa's the emergency. What are you reporting? Hi, I need somebody escorted out of my store right away. He's causing problems. Okay, Mike is he fighting with people? Yeah, he's fighting with somebody right now. Is it a physical fight or verbal? Verbal. What is the address we need to come out to? Holy shit. What is the address? Or a gun. He has a gun or a knife. Okay. Stay on the phone. What's the address? Okay, okay. Okay. The address is 1330. Help with say-o, Dave Sarah, Cho'Ga. Now what makes you think he has a gun or a knife? Just hold it out. Okay. But there's a difference. If there's a gun. Okay. Stay on the phone. Go, go, go, go. In the bathroom. Go. Okay. And so this guy... Oh my god, he shot somebody! Oh my god! Oh my god! Oh my god! Oh my god. Holy shit. Okay. Okay. Sam, are you safe? Yeah, we're in the bathroom. Walk in the bathroom. Okay. So this guy is a white, black Hispanic or Asian. White. How old does he look? How old? What? How old does he look? 40. 40. Is he tall, short, or medium for a man? Medium? Heavy, thinner, medium. Heavy, thinner, medium. Come on. Is he heavy? Is he heavy? Come on. He's wearing a giant sweater and a shark hat. A giant sweatshirt and an... What is it? Giant sweater and giant hat. And a giant hat. Not a shark, but a giant baseball cap? Yeah. Okay. Stay on the phone with me. Okay. I want to get a really good description. Listen, I've got units on the way out there right now. You're going to Pete's coffee at 1330, Alpha Sayode, Saratoga. Yes. And let me just update this just a second. You saw somebody get shot or you just heard him eat fire the gun. Okay. So you heard him fire the gun, but you don't know if anybody shot? Is somebody shot? Yes. Somebody shot. Okay. So the guy who shot, is it a male or a female? I don't know. Okay. Do we have any age or anything like that? I don't know. Okay. I can't go out there. I don't want you to. I don't want you to, but I've got units on their way. I want a good description of this guy so we catch him. Okay. So it's a white male adult. He's about 40 years old. He's got a medium height. And then his weight. Is he heavy, skinny, or medium? Medium. What color hair do you remember? Dark hair under his hat. Dark hair. Dark short hair. Did he come in a car? Do you remember? No, I don't know. Okay. The car has a sign inside the store. And it's a giant baseball cap and a giant sweatshirt, right? Oh, yeah. Okay. Lost the door. Please. Listen, we've got units in the area. I don't want anybody getting hurt. So if you're in a safe place, I want you to stay there, all right? Okay. Where are you at right now? We're in the back room. I'm in the back room, but he's gone. Okay. He left? He's gone, but somebody is shot. Okay. So the guy that's shot, is it male or female? Is it a guy or... Is it male or female that's shot? Male. Male. Male. How old does he look? 20, 30, 40? He's right here. Okay. Okay. How old is the... How old is the guy that's shot, Trevor? Oh, my God. Oh, my God. Okay. Can you... Can we shut the door? Okay. The police are there now. And what is your name, hun? My name is... Can you talk to the officers? Okay. Thank you for calling. Okay. Thank you so much. Bye.",
    "Translated Text": " Santa's the emergency. What are you reporting? Hi, I need somebody escorted out of my store right away. He's causing problems. Okay, Mike is he fighting with people? Yeah, he's fighting with somebody right now. Is it a physical fight or verbal? Verbal. What is the address we need to come out to? Holy shit. What is the address? Or a gun. He has a gun or a knife. Okay. Stay on the phone. What's the address? Okay, okay. Okay. The address is 1330. Help with say-o, Dave Sarah, Cho'Ga. Now what makes you think he has a gun or a knife? Just hold it out. Okay. But there's a difference. If there's a gun. Okay. Stay on the phone. Go, go, go, go. In the bathroom. Go. Okay. And so this guy... Oh my god, he shot somebody! Oh my god! Oh my god! Oh my god! Oh my god. Holy shit. Okay. Okay. Sam, are you safe? Yeah, we're in the bathroom. Walk in the bathroom. Okay. So this guy is a white, black Hispanic or Asian. White. How old does he look? How old? What? How old does he look? 40. 40. Is he tall, short, or medium for a man? Medium? Heavy, thinner, medium. Heavy, thinner, medium. Come on. Is he heavy? Is he heavy? Come on. He's wearing a giant sweater and a shark hat. A giant sweatshirt and an... What is it? Giant sweater and giant hat. And a giant hat. Not a shark, but a giant baseball cap? Yeah. Okay. Stay on the phone with me. Okay. I want to get a really good description. Listen, I've got units on the way out there right now. You're going to Pete's coffee at 1330, Alpha Sayode, Saratoga. Yes. And let me just update this just a second. You saw somebody get shot or you just heard him eat fire the gun. Okay. So you heard him fire the gun, but you don't know if anybody shot? Is somebody shot? Yes. Somebody shot. Okay. So the guy who shot, is it a male or a female? I don't know. Okay. Do we have any age or anything like that? I don't know. Okay. I can't go out there. I don't want you to. I don't want you to, but I've got units on their way. I want a good description of this guy so we catch him. Okay. So it's a white male adult. He's about 40 years old. He's got a medium height. And then his weight. Is he heavy, skinny, or medium? Medium. What color hair do you remember? Dark hair under his hat. Dark hair. Dark short hair. Did he come in a car? Do you remember? No, I don't know. Okay. The car has a sign inside the store. And it's a giant baseball cap and a giant sweatshirt, right? Oh, yeah. Okay. Lost the door. Please. Listen, we've got units in the area. I don't want anybody getting hurt. So if you're in a safe place, I want you to stay there, all right? Okay. Where are you at right now? We're in the back room. I'm in the back room, but he's gone. Okay. He left? He's gone, but somebody is shot. Okay. So the guy that's shot, is it male or female? Is it a guy or... Is it male or female that's shot? Male. Male. Male. How old does he look? 20, 30, 40? He's right here. Okay. Okay. How old is the... How old is the guy that's shot, Trevor? Oh, my God. Oh, my God. Okay. Can you... Can we shut the door? Okay. The police are there now. And what is your name, hun? My name is... Can you talk to the officers? Okay. Thank you for calling. Okay. Thank you so much. Bye.",
    "Complaint Category": "Assault",
    "Location": "Santa",
    "Time": "",
    "Person Involved": "Mike"
}
```

---

## 🛠️ Tech Stack

- Python 3.10
- Whisper (OpenAI) for transcription
- Google Translate API
- spaCy for NER
- Streamlit for UI

---

## 📌 Notes

- Make sure `ffmpeg` is installed and in PATH
- Use Python 3.10 for best compatibility
- Avoid pushing `venv/` or `.dll` files to GitHub

---

## 👤 Author
**Mayank Gupta**  
[GitHub](https://github.com/mayank-555) | [Email](mailto:mayankguptamm99@gmail.com)

---

## 📄 License
This project is part of a Redpluto Analytics AI/ML assessment and is for demonstration purposes only.
