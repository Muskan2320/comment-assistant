# Comment Categorization & Reply Assistant Tool

## 📌 Overview
This project is a mini NLP-based system that analyzes user comments and classifies them into meaningful categories such as praise, hate, spam, constructive criticism, etc. It also suggests automated, empathetic replies for each category — helping brands and creators engage with their audience efficiently.

---

### 🚀 Live Demo
Try the deployed Streamlit application here:

🔗 **https://comment-assistant-dbfd3ahmkkzfzdarwnzcxj.streamlit.app/**

The app allows you to paste any user comment, instantly categorize it (praise, hate, support, spam, etc.), and view an auto-generated suggested reply.

---

## 🎯 Objectives
- Categorize user comments based on intent/emotion  
- Detect praise, support, constructive criticism, hate/abuse, threats, emotional messages, spam, and questions  
- Auto-generate suitable response templates  
- Provide an easy-to-use script (CSV → labeled CSV)  
- Offer a Streamlit UI for real-time predictions  

---

## 📂 Dataset
A custom dataset of **200+ labeled comments** was created, covering:

- Praise  
- Support  
- Constructive Criticism  
- Hate / Abuse  
- Threat  
- Emotional  
- Spam  
- Question/Suggestion  

File: `data/training_data.csv`

---

## 🧠 Model

### Preprocessing
- Text cleaning  
- Lemmatization  
- Tokenization  
- Lowercasing  

### Feature Extraction
- TF-IDF (1–2 grams)

### Classifier
- Linear SVM (high performance on text classification)

---

## 🚀 How to Run

### 1. Train the model
```bash
cd src
python train_model.py
```

### 2. Predict categories for new comments
```bash
python training_data.py --input ../data/test_comments.csv --output ../data/test_comments_categorized.csv
```

Output CSV contains:
- comment  
- predicted_label  
- suggested_reply  

---

## 💬 Reply Assistant
Each category has a predefined empathetic reply.  
Examples:

- **praise** → “Thank you so much for your kind words!”  
- **constructive criticism** → “Thank you for the honest feedback…”  
- **hate** → “Your feedback has been noted…”  
- **threat** → “We take your message seriously…”  
- **spam** → “This appears to be unrelated…”  

---

## 📊 Visualization
A category distribution chart is generated as:

```
data/category_distribution.png
```

---

## 🖥 Streamlit UI
Run:
```bash
streamlit run app_streamlit.py
```

Features:
- Enter a comment or select from examples
- See predicted category  
- Get auto-generated reply  

---

## 📦 Project Structure
```
comment-assistant/
├── data/
│   ├── test_comments.csv
│   ├── training_data.csv
├── models/
│   └── comment_clf.joblib
├── src/
│   ├── train_model.py
│   ├── predict_comments.py
│   └── utils.py
├── app_streamlit.py
├── README.md
```

---

## 📝 Example Output

Input:
```
This video is absolutely stunning!
```

Output:
```
praise → "Thank you so much for your kind words!"
```

---

## ✅ Summary
This project includes:
✔ 200+ labeled dataset  
✔ Preprocessing pipeline  
✔ SVM classifier  
✔ Category predictions  
✔ Auto reply system  
✔ CSV-based workflow  
✔ UI + visualization output in data  

---