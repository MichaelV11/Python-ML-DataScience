import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Leer el PDF y extraer texto
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

# Preprocesamiento de texto
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)

# Ejemplo de categorización de informes
# Supongamos que tenemos informes clasificados en dos categorías: "positivo" y "negativo"
# y tenemos un diccionario con la ruta de cada PDF y su categoría correspondiente
pdf_files = {"path/to/positive_report.pdf": "positive",
             "path/to/negative_report.pdf": "negative"}

# Recopilar datos y etiquetas
data = []
labels = []
for pdf_path, label in pdf_files.items():
    text = extract_text_from_pdf(pdf_path)
    preprocessed_text = preprocess_text(text)
    data.append(preprocessed_text)
    labels.append(label)

# Vectorización de texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data)

# División de datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Entrenamiento del modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Predicción y evaluación del modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
