from sklearn.metrics import accuracy_score


def evaluate_model(model, X_test, y_test):
    y_test_pred = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    print(f'Test accuracy: {test_accuracy}')
    return test_accuracy