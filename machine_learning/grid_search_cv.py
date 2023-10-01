# -*- coding: utf-8 -*-
"""Grid_Search_CV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oUZcRA12Q44LuHHapQut1DhOvvumhSM-
"""

from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pandas as pd


model_params = {
    "svm": {
        "model": svm.SVC(gamma="auto"),
        "params": {"C": [1, 10, 20], "kernel": ["rbf", "linear"]},
    },
    "random_forest": {
        "model": RandomForestClassifier(),
        "params": {"n_estimators": [1, 5, 10]},
    },
    "logistic_regression": {
        "model": LogisticRegression(solver="liblinear", multi_class="auto"),
        "params": {"C": [1, 5, 10]},
    },
}



iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["flower"] = iris.target
df["flower"] = df["flower"].apply(lambda x: iris.target_names[x])
df[47:150]

scores = []

for model_name, mp in model_params.items():
    clf = GridSearchCV(mp["model"], mp["params"], cv=5, return_train_score=False)
    clf.fit(iris.data, iris.target)
    scores.append(
        {
            "model": model_name,
            "best_scores": clf.best_score_,
            "best_params": clf.best_params_,
        }
    )
df = pd.DataFrame(scores, columns=["model", "best_scores", "best_params"])
df
