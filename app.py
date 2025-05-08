import streamlit as st
from transformers import pipeline

# Load the summarization model from Hugging Face
@st.cache_resource
def load_model():
    summarizer = pipeline("summarization")
    return summarizer

# Initialize the model
model = load_model()

# Set the title of the app with custom styling
st.markdown(
    """
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #1E2A47;
        text-align: center;
        padding: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #4A90E2;
        text-align: center;
        margin-top: -10px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
    }
    .button:hover {
        background-color: #45a049;
    }
    .text-area {
        border: 2px solid #ddd;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        width: 100%;
        margin-bottom: 20px;
    }
    .summary-box {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #888;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app with styling
st.markdown('<div class="title">AI-Powered Text Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simplify your text with AI-driven summaries</div>', unsafe_allow_html=True)

# Input text area with custom styling
text_input = st.text_area("Enter the text to summarize:", height=200, key="input_text", label_visibility="collapsed", help="Paste the text you want to summarize.", max_chars=2000)

# Add a summary button with custom styling
if st.button("Summarize", key="summarize_button"):
    if text_input:
        # Summarize the input text
        summary = model(text_input, max_length=150, min_length=30, do_sample=False)
        
        # Display the summary inside a styled box
        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to summarize.", icon="⚠️")


