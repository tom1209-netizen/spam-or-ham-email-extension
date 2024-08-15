import numpy as np
import pickle
from backend.model.data_preprocessing import preprocess_text
from backend.model.feature_extraction import create_features


def load_dictionary(file_path):
    with open(file_path, 'rb') as f:
        dictionary = pickle.load(f)
    return dictionary


def load_label_encoder(file_path):
    with open(file_path, 'rb') as f:
        label_encoder = pickle.load(f)
    return label_encoder


def predict(text, model, dictionary, label_encoder):
    processed_text = preprocess_text(text)
    features = create_features(processed_text, dictionary)
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    prediction_cls = label_encoder.inverse_transform(prediction)[0]

    proba = model.predict_proba(features)[0]
    confidence = np.max(proba)
    return prediction_cls, confidence


# Test
if __name__ == "__main__":
    from model.spam_detector import SpamDetector

    spam_detector = SpamDetector()
    spam_detector.load_model('./saved_models/model.pkl')

    dictionary = load_dictionary('./saved_models/dictionary.pkl')

    le = load_label_encoder('./saved_models/label_encoder.pkl')

    test_input = 'I have great new offers. Get 20% off on your first purchase!'

    prediction_cls, confidence = predict(test_input, spam_detector.model, dictionary, le)
    print(f'Prediction: {prediction_cls}, confidence: {confidence}')