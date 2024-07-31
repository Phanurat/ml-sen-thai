from pythainlp.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

# โหลดข้อมูลจากไฟล์ CSV
data = pd.read_csv('data/test.csv')
print(data.head())

# ฟังก์ชันการตัดคำ
def preprocess(text):
    return ' '.join(word_tokenize(text))

# การเตรียมข้อมูล
data['processed_text'] = data['text'].apply(preprocess)
X = data['processed_text']
y = data['label']

# การแบ่งชุดข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

