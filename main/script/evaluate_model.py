import pandas as pd
import joblib
from sklearn.metrics import classification_report, accuracy_score
from pythainlp.tokenize import word_tokenize
import os

# ฟังก์ชันสำหรับการตัดคำในภาษาไทย
def tokenize(text):
    return ' '.join(word_tokenize(text))

# กำหนดเส้นทางไฟล์
base_path = os.path.dirname(__file__)
test_data_path = os.path.join(base_path, '../data/test_data.csv')

# 1. โหลดข้อมูลทดสอบ
test_data = pd.read_csv(test_data_path)

# 2. โหลดโมเดลและเวกเตอร์ที่บันทึกไว้
model = joblib.load(os.path.join(base_path, '../model/model.pkl'))
vectorizer = joblib.load(os.path.join(base_path, '../model/vectorizer.pkl'))

# 3. ตัดคำและแปลงข้อความเป็นตัวเลข
test_data['text'] = test_data['text'].apply(tokenize)
X_test_vectors = vectorizer.transform(test_data['text'])
y_test = test_data['label']

# 4. ทำนายและประเมินผล
y_pred = model.predict(X_test_vectors)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print('Classification Report:')
print(classification_report(y_test, y_pred))
