import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from roadmap_prompt import learning_roadmap_prompt

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Check API key
if not api_key:
    st.error("🚫 API Key not found. Please check your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
     
    system_instruction="You're a Roadmap generator for Tools, Technology, and Programming languages."
)

# Page config
st.set_page_config(page_title=" AI Roadmap Generator", layout="centered")

# --- 🎨 CSS Styling ---
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background-color: #f0f2f5 !important;
            color: #2e3b4e !important;
        }

        .title {
            text-align: center;
            font-size: 36px;
            color: #1a237e;
            font-weight: bold;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #636e72;
            margin-bottom: 20px;
        }

        .input-area {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        }

        .stTextInput > div > input,
        .stNumberInput > div > input {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        .stButton > button {
            background-color: #e74c3c !important;
            color: white !important;
            font-weight: bold;
            padding: 0.75em 1.5em;
            border: none;
            border-radius: 8px;
        }

        .stButton > button:hover {
            background-color: #c0392b !important;
        }

        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# --- 🧠 Header Section ---
st.markdown('<div class="title">🚀 AI Powered Roadmap Generator 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Craft a personalized learning journey with AI</div>', unsafe_allow_html=True)


col1, col2 = st.columns([2, 1])
with col1:
    topic = st.text_input("🔍 Topic You Want to Learn", placeholder="e.g., Machine Learning, Flutter, Rust...")
with col2:
    num_days = st.number_input("🗓️ Duration (in days)", min_value=7, max_value=180, value=28, step=1)

st.markdown('</div>', unsafe_allow_html=True)

# --- 🛠️ Generate Button ---
generate = st.button("✨ Create My Roadmap")

# --- 📋 Output Section ---
if generate and topic.strip() != "":
    with st.spinner("🔧 Generating your roadmap..."):
        full_prompt = learning_roadmap_prompt.format(topic=topic, num_days=num_days)
        response = model.generate_content(full_prompt)
        output = response.text

        st.markdown("---")
        st.markdown("### 🧭 Your Personalized Learning Roadmap")
        st.markdown(f"#### Topic: **{topic}** | Duration: **{num_days} days**")
        st.markdown(output, unsafe_allow_html=True)

# --- 👣 Footer ---
st.markdown("<div style='text-align:center; color: grey; font-size: 14px;'>Made with ❤️ by Isha | Powered by Gemini Pro</div>", unsafe_allow_html=True)
