from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def _precision(confusion_matrix, label=1):
    return confusion_matrix[label, label] / confusion_matrix[:, label].sum()

def _recall(confusion_matrix, label=1): # true positive rate
    return confusion_matrix[label, label] / confusion_matrix[label, :].sum()

def _fpr(confusion_matrix, label=1): # false positive rate
    return confusion_matrix[1-label, label] / confusion_matrix[1-label, :].sum()

def _accuracy(confusion_matrix, label=1):
    return (confusion_matrix[label, label] + confusion_matrix[1-label, 1-label]) / confusion_matrix.sum()

def _f_measure(confusion_matrix, label=1):
    return 2 / (1 / _precision(confusion_matrix, label) + 1 / _recall(confusion_matrix, label))


def evaluate_performance(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(cm)
    
    print('Precision:', round(_precision(cm), 3))
    print('Recall:', round(_recall(cm), 3))
    print('False Positive Rate:', round(_fpr(cm), 3))
    print('F_measure:', round(_f_measure(cm), 3))
    print('Accuracy:', round(_accuracy(cm), 3))

def plot_accuracy(history):
    # Plot training accuracy values
    plt.plot(history.history['accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.show()

def plot_loss(history):
    # Plot training loss values
    plt.plot(history.history['loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.show()
