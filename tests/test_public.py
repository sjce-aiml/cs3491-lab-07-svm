"""Public tests for Lab 07. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab07 as lab  # noqa: E402

from sklearn.datasets import make_blobs

def test_linear_svm_runs():
    X, y = make_blobs(100, centers=2, random_state=0)
    assert lab.train_svm(X, y, kernel="linear").score(X, y) > 0.9
