import pandas as pd
import re
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report,confusion_matrix
import joblib
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')
print(classification_report(y_test , y_pred))

ps=PorterStemmer()
stop_words=set(stopwords.words('english'))

model=LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf,y_train)

RISK_WORDS=["urgent","transfer","otp","bank","kyc","help","hospital","account","block","verify","send","rs","₹","gift"]
def predict_message(message):
    cleaned=clean_text(message)
    vec=vectorizer.transform([cleaned])
    ml_pred=model.predict(vec)[0]
    score=sum(word in cleaned for word in RISK_WORDS)
    if score>=2:
        return 1
    return ml_pred

# Load dataset
data = pd.read_csv("D:\safetalkAI\data\spam.csv", encoding='latin-1')[['v1', 'v2']]
data.columns = ['label', 'message']

# Preprocess text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words=[ps.stem(word) for word in text.split() if word not in stop_words]
    return " ".join(words)

data['message'] = data['message'].apply(clean_text)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2, random_state=42)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=3000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, "model/scam_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
print("Model and vectorizer saved successfully!")