import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import joblib
import os

from utils import preprocess

DATA_PATH = "../data/comments_labeled.csv"
MODEL_PATH = "../models/comment_clf.joblib"

def main():
    df = pd.read_csv(DATA_PATH)

    # Basic sanity checks
    df = df.dropna(subset=["comment", "label"])
    print("Dataset size:", len(df))
    print("Label distribution:\n", df["label"].value_counts())

    X = df["comment"].astype(str)
    y = df["label"].astype(str)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Pipeline: preprocessing + TF-IDF + SVM classifier
    text_clf = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    preprocessor=preprocess,
                    ngram_range=(1, 2),
                    min_df=2,
                    stop_words="english",
                ),
            ),
            ("clf", LinearSVC())
        ]
    )

    text_clf.fit(X_train, y_train)

    y_pred = text_clf.predict(X_test)
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    os.makedirs("../models", exist_ok=True)
    joblib.dump(text_clf, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")

    label_counts = df["label"].value_counts()
    label_counts.plot(kind="bar")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.title("Comment Category Distribution")
    plt.tight_layout()
    plt.savefig("../data/category_distribution.png")

if __name__ == "__main__":
    main()
