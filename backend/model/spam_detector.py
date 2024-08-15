from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


class SpamDetector:
    def __init__(self):
        self.model = GaussianNB()

    def train(self, X_train, y_train):
        print('Start training...')
        self.model = self.model.fit(X_train, y_train)
        print('Training completed!')

    def evaluate(self, X_val, y_val):
        y_val_pred = self.model.predict(X_val)
        val_accuracy = accuracy_score(y_val, y_val_pred)
        print(f'Val accuracy: {val_accuracy}')
        return val_accuracy

    def save_model(self, file_path):
        import joblib
        joblib.dump(self.model, file_path)

    def load_model(self, file_path):
        import joblib
        self.model = joblib.load(file_path)
