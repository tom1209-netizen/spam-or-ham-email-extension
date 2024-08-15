import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from backend.model.spam_detector import SpamDetector
from backend.model.data_preprocessing import preprocess_text
from backend.model.feature_extraction import create_features
from backend.model.dictionary import create_dictionary
import pickle

# Load and prepare data
DATASET_PATH = './datasets/2cls_spam_text_cls.csv'
df = pd.read_csv(DATASET_PATH)

messages = df['Message'].values.tolist()
labels = df['Category'].values.tolist()

le = LabelEncoder()
y = le.fit_transform(labels)

# Preprocess messages
messages = [preprocess_text(message) for message in messages]

# Create dictionary and features
dictionary = create_dictionary(messages)

# Save the dictionary to a file
with open('../saved_models/dictionary.pkl', 'wb') as f:
    pickle.dump(dictionary, f)

# Save the LabelEncoder
with open('../saved_models/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

X = np.array([create_features(tokens, dictionary) for tokens in messages])

# Split data
VAL_SIZE = 0.2
TEST_SIZE = 0.125
SEED = 0

X_train, X_val, y_train, y_val = train_test_split(X, y,
                                                  test_size=VAL_SIZE,
                                                  shuffle=True,
                                                  random_state=SEED)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train,
                                                    test_size=TEST_SIZE,
                                                    shuffle=True,
                                                    random_state=SEED)

# Train model
spam_detector = SpamDetector()
spam_detector.train(X_train, y_train)

# Evaluate model
spam_detector.evaluate(X_val, y_val)

# Save the model
spam_detector.save_model('../saved_models/model.pkl')
