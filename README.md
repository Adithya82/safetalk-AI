SafeTalk AI

SafeTalk AI is a multilingual scam detection system that analyzes SMS, WhatsApp-style messages, and recorded call audio using TensorFlow and NLP. The system detects fraudulent or emotionally manipulative communication in real time and supports English, Hindi, and Telugu languages.


 Features

*  Scam detection for SMS and social media messages
*  Recorded audio call analysis
*  Multilingual NLP support
  * English
  * Hindi
  * Telugu
*  Real-time scam risk prediction
*  Android-ready TensorFlow Lite compatible model
*  Offline-friendly and privacy-focused

 Technologies Used

* Python
* TensorFlow / Keras
* NLP (Character-Level Text Processing)
* Streamlit
* SpeechRecognition
* Pandas
* NumPy

How It Works

-> Text Analysis

1. User pastes SMS or WhatsApp-style message
2. Text is preprocessed
3. TensorFlow model predicts scam probability
4. Risk level is displayed

-> Audio Analysis

1. User uploads recorded audio call
2. Speech is converted to text
3. NLP model analyzes transcript
4. Scam risk warning is generated


  Project Structure

SafeTalkAI/
│
├── data/
│   └── dataset.csv
│
├── model/
│   └── scam_multilingual.keras
│
├── train_model.py
├── app.py
└── README.md


  Installation

1. Clone Repository

git clone https://github.com/your-username/SafeTalkAI.git
cd SafeTalkAI

2. Create Virtual Environment

python -m venv myenv

3. Activate Environment

myenv\Scripts\activate

4. Install Dependencies

pip install tensorflow
pip install streamlit
pip install pandas
pip install numpy
pip install SpeechRecognition


  Train the Model

python train_model.py


  Run the Application

streamlit run app.py


  Supported Languages

| Language | Supported |
| -------- | --------- |
| English  | ✅         |
| Hindi    | ✅         |
| Telugu   | ✅         |


  Future Enhancements

* Android APK deployment
* TensorFlow Lite optimization
* Live microphone analysis
* Expanded multilingual support
* Advanced scam pattern detection

   Sample Scam Inputs
 English

Your account is blocked verify immediately

Hindi

आपका खाता बंद कर दिया गया है तुरंत सत्यापित करें


Telugu

మీ ఖాతా నిలిపివేయబడింది వెంటనే ధృవీకరించండి


 Author

Adithya

 License

This project is developed for educational and research purposes.
