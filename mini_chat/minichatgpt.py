import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Leer el contenido del archivo de texto
with open("entrenamiento.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Preprocesamiento: Tokenización de oraciones y palabras, lematización y eliminación de stopwords
sentences = sent_tokenize(texto)
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.isalpha()]
    # Reducir la eliminación de palabras para mantener más contexto
    tokens = [word for word in tokens if word not in stop_words or word in ["what", "who", "when", "where", "how", "why"]]
    return " ".join(tokens)

preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]

# Crear un vectorizador TF-IDF con mejores parámetros
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
vectorized_sentences = vectorizer.fit_transform(preprocessed_sentences)

def find_most_relevant_sentence(question, threshold=0.1):
    preprocessed_question = preprocess_text(question)
    vectorized_question = vectorizer.transform([preprocessed_question])
    similarities = cosine_similarity(vectorized_sentences, vectorized_question)
    
    most_relevant_index = similarities.argmax()
    highest_similarity = similarities.max()
    
    if highest_similarity < threshold:
        return "I'm not sure, can you rephrase?"
    
    return sentences[most_relevant_index]

# Bucle principal de interacción con el usuario
def main():
    while True:
        question = input("Hello, I am MiniGpt. How can I assist you? ")
        if question.lower() == "exit":
            break
        
        most_relevant_sentence = find_most_relevant_sentence(question)
        print("Response:", most_relevant_sentence)

# Ejecutar el bucle principal
if __name__ == "__main__":
    main()
