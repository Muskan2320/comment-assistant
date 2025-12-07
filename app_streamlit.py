import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
import joblib
from predict_comments import REPLY_TEMPLATES

# Load Model
@st.cache_resource
def load_model():
    return joblib.load("models/comment_clf.joblib")

model = load_model()

st.title("Comment Categorization & Reply Assistant")
st.write("Paste a comment below or choose an example to test the model.")

# Example Comments for Testing
EXAMPLES = {
    "Praise": "This video is absolutely amazing!",
    "Support": "You're improving so much, keep going!",
    "Constructive Criticism": "Good work, but the ending needs refinement.",
    "Hate": "This is awful, I can't believe you posted this.",
    "Threat": "Post something like this again and you'll regret it.",
    "Emotional": "This really touched my heart and brought back memories.",
    "Spam": "Win free prizes! Click the link in my profile!",
    "Question/Suggestion": "Could you make a tutorial explaining this process?"
}

st.sidebar.title("Test Examples")
st.sidebar.write("Click any example to auto-fill the text box.")

# When user clicks an example
for label, example in EXAMPLES.items():
    if st.sidebar.button(label):
        st.session_state["example_text"] = example

# Default text area content
default_text = st.session_state.get("example_text", "")

user_input = st.text_area("Paste a comment:", value=default_text, height=120)

# Analyze Button
if st.button("Analyze"):
    if user_input.strip():
        label = model.predict([user_input])[0]
        st.markdown(f"**Predicted Category:** `{label}`")
        st.markdown("**Suggested Reply:**")
        st.write(REPLY_TEMPLATES.get(label, "Thank you for your comment!"))
    else:
        st.warning("Please enter a comment first.")

st.markdown("---")
st.caption("Built with scikit-learn + Streamlit")
