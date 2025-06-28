import gradio as gr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Przykładowe dane treningowe
emails = [
    "Win a free iPhone now",
    "Important meeting tomorrow",
    "Congratulations, you won a lottery",
    "Please find attached the report",
    "Claim your free vacation today",
    "Let's schedule a call for project discussion"
]
labels = ["spam", "ham", "spam", "ham", "spam", "ham"]  # 'ham' = nie-spam

# Tworzenie modelu
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

# Funkcja klasyfikująca e-mail
def classify_email(email_text):
    X_test = vectorizer.transform([email_text])
    prediction = model.predict(X_test)
    return f"Email classified as: {prediction[0]}"

# Tworzenie interfejsu Gradio
interface = gr.Interface(
    fn=classify_email,
    inputs=gr.Textbox(lines=10, placeholder="Enter email content here..."),
    outputs="text",
    title="Email Spam Detector",
    description="Enter the email content to check if it is spam or not."
)

# Uruchomienie aplikacji
interface.launch()
