"""Lab 7 starter code: SVM models."""
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def train_svm(X, y, kernel='rbf', C=1.0):
    raise NotImplementedError('TODO: implement this')

def choose_kernel(X, y):
    """Return 'linear' or 'rbf', whichever has the higher 5-fold CV accuracy."""
    raise NotImplementedError('TODO: implement this')

def margin_width(model):
    """For a linear SVC (fitted on raw features), return 2/||w||."""
    raise NotImplementedError('TODO: implement this')
