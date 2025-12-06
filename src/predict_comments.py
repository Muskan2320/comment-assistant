import pandas as pd
import joblib
import argparse
import os

MODEL_PATH = "../models/comment_clf.joblib"

REPLY_TEMPLATES = {
    "praise": "Thank you so much for your kind words! We’re glad you enjoyed it 😊",
    "support": "We really appreciate your support – it keeps us motivated to create more!",
    "constructive_criticism": (
        "Thank you for the honest feedback. We’ll review this and keep improving. "
        "If you have more suggestions, we’d love to hear them."
    ),
    "hate": "Your feedback has been noted. We encourage respectful conversations in this space.",
    "threat": (
        "We take your message seriously. Please note that harmful or threatening content "
        "goes against our community guidelines."
    ),
    "emotional": "Thank you for sharing how this made you feel. We’re glad it resonated with you 💙",
    "spam": "This comment appears to be unrelated to the post. It may be removed as spam.",
    "question_suggestion": (
        "Great question/suggestion! We’ll definitely consider covering this in a future post."
    ),
}

def load_model():
    return joblib.load(MODEL_PATH)

def predict_and_save(input_path: str, output_path: str):
    model = load_model()
    df = pd.read_csv(input_path)

    if "comment" not in df.columns:
        raise ValueError("Input CSV must have a 'comment' column.")

    df["predicted_label"] = model.predict(df["comment"].astype(str))
    df["suggested_reply"] = df["predicted_label"].map(
        lambda lbl: REPLY_TEMPLATES.get(lbl, "Thank you for your comment!")
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved predictions to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to CSV with a 'comment' column")
    parser.add_argument("--output", default="../data/comments_categorized.csv")
    args = parser.parse_args()

    predict_and_save(args.input, args.output)
