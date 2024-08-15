import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Read the data
DATASET_PATH = '/content/2cls_spam_text_cls.csv'
df = pd.read_csv(DATASET_PATH)

messages = df['Message'].values.tolist()
labels = df['Category'].values.tolist()

le = LabelEncoder()
y = le.fit_transform(labels)
print(f'Classes: {le.classes_}')
print(f'Encoded labels: {y}')