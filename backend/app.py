from flask import Flask, request, jsonify
from model.spam_detector import SpamDetector
from utils import load_dictionary, load_label_encoder, predict
import os

app = Flask(__name__)

# Load the saved model
model_path = './saved_models/model.pkl'
dictionary_path = './saved_models/dictionary.pkl'
label_encoder_path = './saved_models/label_encoder.pkl'

spam_detector = SpamDetector()
spam_detector.load_model(model_path)
dictionary = load_dictionary(dictionary_path)
label_encoder = load_label_encoder(label_encoder_path)


@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    text = data.get('text', '')

    prediction_cls, confidence = predict(text, spam_detector.model, dictionary, label_encoder)

    return jsonify(
        {'prediction': prediction_cls, 'confidence': confidence},
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
