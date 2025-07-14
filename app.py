import streamlit as st
from groq import Groq
from streamlit_option_menu import option_menu
import os
from fpdf import FPDF
import time
import datetime
import json
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, List
import base64
import datetime
import time

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'health_history' not in st.session_state:
    st.session_state.health_history = []
if 'nutrition_plans' not in st.session_state:
    st.session_state.nutrition_plans = []
if 'tip_index' not in st.session_state:
    st.session_state.tip_index = 0
if 'last_tip_time' not in st.session_state:
    st.session_state.last_tip_time = time.time()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'health_history' not in st.session_state:
    st.session_state.health_history = []
if 'nutrition_plans' not in st.session_state:
    st.session_state.nutrition_plans = []
if 'tip_index' not in st.session_state:
    st.session_state.tip_index = 0
if 'last_tip_time' not in st.session_state:
    st.session_state.last_tip_time = time.time()
# ADD THIS BLOCK:
if 'health_data' not in st.session_state:
    st.session_state.health_data = {
        'dates': [],
        'weight': [],
        'systolic': [],
        'diastolic': [],
        'heart_rate': [],
        'glucose': []
    }



# Set page config
st.set_page_config(
    page_title="HealthSense AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Groq API
try:
    groq_api_key = st.secrets["groq_api_key"]
    client = Groq(api_key=groq_api_key)
except:
    st.error("⚠️ Groq API key not found. Please set up your API key in Streamlit secrets.")
    st.stop()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'health_history' not in st.session_state:
    st.session_state.health_history = []
if 'nutrition_plans' not in st.session_state:
    st.session_state.nutrition_plans = []
if 'tip_index' not in st.session_state:
    st.session_state.tip_index = 0
if 'last_tip_time' not in st.session_state:
    st.session_state.last_tip_time = time.time()

# Fixed CSS with better contrast and visibility
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styles - Fixed background issue */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-family: 'Inter', sans-serif;
    }

    /* Fix main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Enhanced Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white !important;
        border: none;
        padding: 12px 28px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        font-family: 'Inter', sans-serif;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #4ECDC4, #FF6B6B);
    }

    /* Enhanced Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.9) !important;
        border: 2px solid transparent !important;
        border-radius: 10px !important;
        padding: 10px !important;
        color: #333 !important;
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stNumberInput > div > div > input:focus {
        border-color: #4ECDC4 !important;
        box-shadow: 0 0 0 3px rgba(78, 205, 196, 0.1) !important;
    }

    /* Fix labels */
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label,
    .stNumberInput > label {
        color: white !important;
        font-weight: 500;
    }

    /* Chat Messages */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px !important;
        padding: 15px !important;
        margin: 10px 0 !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }

    /* Enhanced Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        color: white;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }

    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        transition: all 0.3s ease;
        color: white;
    }

    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    }

    /* Health Tips Container */
    .tip-container {
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 25px;
        border-radius: 20px;
        font-size: 18px;
        font-weight: 500;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        margin: 25px 0;
        animation: fadeIn 0.5s ease-in-out;
        font-family: 'Inter', sans-serif;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Title Styling */
    .main-title {
        color: white !important;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        font-family: 'Inter', sans-serif;
    }

    .section-title {
        color: white !important;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
        font-family: 'Inter', sans-serif;
    }

    /* Fix all text to be white */
    .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: white !important;
    }

    /* Stats Display */
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 30px 0;
        flex-wrap: wrap;
    }

    .stat-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        color: white;
        min-width: 150px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #4ECDC4;
    }

    .stat-label {
        font-size: 0.9rem;
        opacity: 0.8;
        margin-top: 5px;
    }

    /* Fix forms */
    .stForm {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Fix dataframe */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 10px;
    }

    /* Fix metrics */
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .stMetric > div {
        color: white !important;
    }

    /* Fix sidebar */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    /* Fix spinner */
    .stSpinner > div {
        border-color: #4ECDC4 !important;
    }

    /* Fix success/error messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px);
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }

        .tip-container {
            font-size: 16px;
            padding: 20px;
        }

        .feature-card {
            padding: 20px;
        }

        .stats-container {
            flex-direction: column;
            align-items: center;
        }
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Sidebar
with st.sidebar:
    # Logo with better styling
    st.markdown('<div style="text-align: center; margin-bottom: 30px;">', unsafe_allow_html=True)
    try:
        # You can replace this with your own image URL or local image
        st.image(r"C:\Users\hp\Desktop\Sehat-Connect-main - Copy - Copy\ChatGPT_removebg.png", use_container_width=True)
    except:
        st.markdown('<h2 style="color: white; text-align: center;">🩺 HealthSense AI</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced Navigation Menu
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Doctor Chat", "Nutrition", "Health Tracker", "Emergency", "About"],
        icons=["house-fill", "chat-dots-fill", "apple", "activity", "exclamation-triangle-fill", "info-circle-fill"],
        menu_icon="list",
        default_index=0,
        styles={
            "container": {"padding": "10px", "background-color": "rgba(255, 255, 255, 0.1)", "border-radius": "15px"},
            "icon": {"color": "#4ECDC4", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "padding": "10px 15px",
                "border-radius": "10px",
                "color": "white",
                "font-weight": "500",
                "--hover-color": "rgba(78, 205, 196, 0.2)"
            },
            "nav-link-selected": {
                "background": "linear-gradient(45deg, #FF6B6B, #4ECDC4)",
                "color": "white",
                "font-weight": "600"
            },
        }
    )

    if selected:
        st.session_state.page = selected

    # # Quick Stats in Sidebar
    # st.markdown("---")
    # st.markdown("### 📊 Quick Stats")
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.metric("Chats Today", len(st.session_state.get('messages', [])))
    # with col2:
    #     st.metric("Health Score", "87%")

# Helper Functions
def get_ai_response(prompt: str, system_role: str) -> str:
    """Enhanced AI response with error handling and loading state"""
    try:
        with st.spinner('🤖 AI is thinking...'):
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": prompt}
                ],
                model="llama3-70b-8192",
                temperature=0.7,
                max_tokens=1024
            )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"🚨 AI Response Error: {str(e)}")
        return "I apologize, but I'm having trouble connecting right now. Please try again in a moment."

def calculate_bmi(weight: float, height: float) -> tuple:
    """Calculate BMI and return category"""
    bmi = weight / ((height/100)**2)
    if bmi < 18.5:
        category = "Underweight"
        color = "#3498db"
    elif bmi < 25:
        category = "Normal"
        color = "#2ecc71"
    elif bmi < 30:
        category = "Overweight"
        color = "#f39c12"
    else:
        category = "Obese"
        color = "#e74c3c"
    return bmi, category, color

def get_nutrition_plan(age: int, weight: float, height: float, goal: str, duration: str, activity_level: str = "moderate") -> str:
    """Enhanced nutrition plan generation"""
    bmi, category, _ = calculate_bmi(weight, height)

    prompt = f"""
    Create a comprehensive nutrition and exercise plan for:
    - Age: {age} years old
    - Weight: {weight} kg
    - Height: {height} cm
    - BMI: {bmi:.1f} ({category})
    - Goal: {goal}
    - Duration: {duration}
    - Activity Level: {activity_level}

    Please include:
    1. Daily calorie requirements
    2. Macronutrient breakdown
    3. Sample meal plans for each day
    4. Exercise recommendations
    5. Hydration guidelines
    6. Progress tracking suggestions
    7. Important health tips

    Make it practical and easy to follow.
    """

    return get_ai_response(prompt, "You are a certified nutritionist and fitness expert with 10+ years of experience. Provide evidence-based, practical advice.")

def generate_enhanced_pdf(content: str, filename: str, user_info: dict = None):
    """Enhanced PDF generation with better formatting"""
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "HealthSense AI - Personalized Health Report", ln=True, align='C')
        pdf.ln(10)

        if user_info:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"Generated for: {user_info.get('name', 'User')}", ln=True)
            pdf.cell(0, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
            pdf.ln(5)

        pdf.set_font("Arial", size=10)

        # Split content into lines and add to PDF
        lines = content.split('\n')
        for line in lines:
            if line.strip():
                pdf.multi_cell(0, 8, line.encode('latin-1', 'replace').decode('latin-1'))
                pdf.ln(2)

        pdf.output(filename)
        return True
    except Exception as e:
        st.error(f"PDF Generation Error: {str(e)}")
        return False
    

# Page Functions
# ... (rest of your imports and initial setup) ...

# Page Functions
def home():
    """Enhanced Home Page with auto-refreshing tips and emoji icons."""
    st.markdown('<h1 class="main-title">🩺 Welcome to HealthSense AI</h1>', unsafe_allow_html=True)

    # Hero Section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>Your AI-Powered Health Companion ✨</h3>
            <p>Get personalized health advice, nutrition plans, and medical consultations powered by advanced AI technology.</p>
        </div>
        """, unsafe_allow_html=True)

    # Feature Cards
    st.markdown("### 🌟 Explore Our Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🤖 AI Doctor Chat</h4>
            <p>Get instant medical advice from our AI doctor available 24/7 💬</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🥗 Nutrition Planning</h4>
            <p>Personalized meal plans based on your goals and preferences 🥦</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Health Tracking</h4>
            <p>Monitor your health metrics and track your progress 📈</p>
        </div>
        """, unsafe_allow_html=True)

    # Health Tips with Auto-refresh (within a fragment)
    st.markdown("### 💡 Daily Health Tips")

    health_tips = [
        "💧 Stay hydrated: Drink at least 8 glasses of water daily",
        "🏃‍♂️ Exercise regularly: Aim for 150 minutes of moderate activity weekly",
        "🍎 Eat the rainbow: Include colorful fruits and vegetables in your diet",
        "😴 Prioritize sleep: Get 7-9 hours of quality sleep each night",
        "🧘‍♀️ Manage stress: Practice meditation or deep breathing exercises",
        "🚭 Avoid tobacco: Stay away from smoking and secondhand smoke",
        "☀️ Get vitamin D: Spend time outdoors for natural sunlight",
        "🦷 Maintain oral health: Brush and floss teeth regularly",
        "🩺 Regular check-ups: Schedule annual health screenings",
        "🧠 Keep learning: Challenge your brain with new activities"
    ]

    # Use a fragment for the auto-updating tip
    @st.experimental_fragment(run_every=datetime.timedelta(seconds=5))
    def tip_fragment():
        # This function will rerun every 5 seconds
        if 'tip_index' not in st.session_state:
            st.session_state.tip_index = 0
        
        # Manually increment the tip index
        st.session_state.tip_index = (st.session_state.tip_index + 1) % len(health_tips)

        st.markdown(
            f'<div class="tip-container">{health_tips[st.session_state.tip_index]}</div>',
            unsafe_allow_html=True
        )

        # Important: st.rerun() or time.sleep() are NOT needed here when using run_every
        # The fragment itself controls its re-execution.

    tip_fragment() # Call the fragment function

    # # Manual refresh button for the tip
    # col1, col2, col3 = st.columns([1, 1, 1])
    # with col2:
    #     if st.button("🔄 Next Tip", use_container_width=True, key="next_tip_button_manual"):
    #         # This button will trigger a rerun of the main script,
    #         # which will then call the fragment again, and the fragment
    #         # will update its state and content.
    #         # No explicit st.rerun() needed here as button press naturally reruns.
    #         st.session_state.tip_index = (st.session_state.tip_index + 1) % len(health_tips) # Update index immediately

    # IMPORTANT: Remove the unconditional st.rerun() from here
    # time.sleep(0.1)
    # st.rerun() # This line caused the full page refresh


def doctor_chat():
    """Enhanced Doctor Chat with better UI"""
    st.markdown('<h1 class="section-title">🩺 AI Doctor Consultation</h1>', unsafe_allow_html=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat interface
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown("### 💬 Chat with Dr. AI")
        st.markdown("Ask your health questions or describe your symptoms below:")
      
        # Display chat messages
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

    with col2:
        st.markdown("### 📋 Quick Symptoms")
        symptoms = [
            "Headache", "Fever", "Cough", "Fatigue",
            "Nausea", "Chest Pain", "Shortness of Breath", "Dizziness"
        ]

        for symptom in symptoms:
            if st.button(symptom, key=f"symptom_{symptom}", use_container_width=True):
                prompt = f"I'm experiencing {symptom.lower()}. Can you help me understand what might be causing this?"
                st.session_state.messages.append({"role": "user", "content": prompt})

                response = get_ai_response(
                    prompt,
                    "You are Dr. Rizwan , a helpful and knowledgeable AI doctor. Provide medical advice but always remind users to consult with healthcare professionals for serious concerns."
                )

                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

    # Chat input
    if prompt := st.chat_input("Describe your symptoms or ask a health question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Dr. AI is analyzing your symptoms..."):
                response = get_ai_response(
                    prompt,
                    "You are Dr. Rizwan, a helpful and knowledgeable AI doctor. Provide medical advice but always remind users to consult with healthcare professionals for serious concerns."
                )
                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

    # Chat actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    with col2:
        if st.button("💾 Save Conversation"):
            if st.session_state.messages:
                conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
                if generate_enhanced_pdf(conversation, "consultation_report.pdf"):
                    st.success("Conversation saved as PDF!")

    # with col3:
    #     if st.button("📱 Get Emergency Help"):
    #         st.session_state.page = "Emergency"
    #         st.rerun()

def nutrition():
    """Enhanced Nutrition Planning"""
    st.markdown('<h1 class="section-title">🥗 Personalized Nutrition Planner</h1>', unsafe_allow_html=True)

    # User Profile Form
    with st.form("nutrition_form"):
        st.markdown("### 👤 Personal Information")

        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="Enter your name")
            age = st.number_input("Age", min_value=1, max_value=120, value=30)
            weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
            height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)

        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            activity_level = st.selectbox("Activity Level", [
                "Sedentary (little/no exercise)",
                "Lightly active (light exercise 1-3 days/week)",
                "Moderately active (moderate exercise 3-5 days/week)",
                "Very active (hard exercise 6-7 days/week)",
                "Extremely active (physical job + exercise)"
            ])
            goal = st.selectbox("Primary Goal", [
                "lose weight", "gain weight", "maintain weight",
                "build muscle", "improve health", "increase energy"
            ])
            duration = st.selectbox("Plan Duration", ["1 week", "2 weeks", "1 month", "3 months"])

        # Additional preferences
        st.markdown("### 🍽️ Dietary Preferences")
        col1, col2 = st.columns(2)
        with col1:
            dietary_restrictions = st.multiselect("Dietary Restrictions", [
                "None", "Vegetarian", "Vegan", "Keto", "Paleo",
                "Gluten-free", "Dairy-free", "Nut-free"
            ])

        with col2:
            meals_per_day = st.selectbox("Meals per day", [3, 4, 5, 6])
            budget = st.selectbox("Budget Range", ["Low", "Medium", "High"])

        submitted = st.form_submit_button("🚀 Generate Nutrition Plan", use_container_width=True)

    if submitted:
        # Calculate BMI and display
        bmi, category, color = calculate_bmi(weight, height)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number" style="color: {color};">{bmi:.1f}</div>
                <div class="stat-label">BMI</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{category}</div>
                <div class="stat-label">Category</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            daily_calories = int(weight * 24 * (1.2 if activity_level.startswith("Sedentary") else 1.5))
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{daily_calories}</div>
                <div class="stat-label">Daily Calories</div>
            </div>
            """, unsafe_allow_html=True)

        # Generate nutrition plan
        with st.spinner("🍳 Creating your personalized nutrition plan..."):
            activity_simple = activity_level.split(" ")[0].lower()
            plan = get_nutrition_plan(age, weight, height, goal, duration, activity_simple)

            st.session_state.nutrition_plan = {
                'content': plan,
                'user_info': {
                    'name': name,
                    'age': age,
                    'weight': weight,
                    'height': height,
                    'bmi': bmi,
                    'goal': goal,
                    'duration': duration
                }
            }

        # Display plan
        st.markdown("### 📋 Your Personalized Nutrition Plan")
        st.markdown(plan)

        # Action buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📄 Download PDF Report", use_container_width=True):
                if generate_enhanced_pdf(plan, "nutrition_plan.pdf", st.session_state.nutrition_plan['user_info']):
                    with open("nutrition_plan.pdf", "rb") as f:
                        st.download_button(
                            "📥 Download Plan",
                            f,
                            file_name=f"nutrition_plan_{name}_{datetime.datetime.now().strftime('%Y%m%d')}.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

        with col2:
            if st.button("💾 Save to Profile", use_container_width=True):
                st.session_state.nutrition_plans.append(st.session_state.nutrition_plan)
                st.success("Plan saved to your profile!")

        with col3:
            if st.button("🔄 Generate New Plan", use_container_width=True):
                st.rerun()

def health_tracker():
    """Health Tracking Feature with data entry, display, and visualization."""
    st.markdown('<h1 class="section-title">📊 Health Tracker</h1>', unsafe_allow_html=True)

    

    st.markdown("### ➕ Add New Health Data")
    with st.form("health_data_form"):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("Date", datetime.date.today())
            weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=None)
            systolic = st.number_input("Systolic BP (mmHg)", min_value=50, max_value=250, value=None)
        with col2:
            heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=None)
            diastolic = st.number_input("Diastolic BP (mmHg)", min_value=30, max_value=150, value=None)
            glucose = st.number_input("Blood Glucose (mg/dL)", min_value=10, max_value=500, value=None)

        submitted = st.form_submit_button("Add Data", use_container_width=True)

        if submitted:
            # Check if at least one field other than date is filled
            if any(val is not None for val in [weight, systolic, diastolic, heart_rate, glucose]):
                st.session_state.health_data['dates'].append(date.strftime('%Y-%m-%d'))
                st.session_state.health_data['weight'].append(weight)
                st.session_state.health_data['systolic'].append(systolic)
                st.session_state.health_data['diastolic'].append(diastolic)
                st.session_state.health_data['heart_rate'].append(heart_rate)
                st.session_state.health_data['glucose'].append(glucose)
                st.success("Health data added successfully!")
            else:
                st.warning("Please enter at least one health metric to add data.")

    st.markdown("---")
    st.markdown("### 📋 Your Health History")

    if st.session_state.health_data['dates']:
        df = pd.DataFrame(st.session_state.health_data)
        df['dates'] = pd.to_datetime(df['dates']) # Convert to datetime for proper sorting
        df = df.sort_values(by='dates', ascending=False) # Sort by date descending
        st.dataframe(df, use_container_width=True)

        st.markdown("---")
        st.markdown("### 📈 Health Trends Visualization")

        # Convert dates to datetime objects for plotting
        df_for_plot = df.copy()
        df_for_plot['dates'] = pd.to_datetime(df_for_plot['dates'])

        # Weight Trend
        if not df_for_plot['weight'].dropna().empty:
            fig_weight = px.line(df_for_plot.dropna(subset=['weight']), x='dates', y='weight', title='Weight Trend', markers=True)
            fig_weight.update_layout(xaxis_title="Date", yaxis_title="Weight (kg)", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
            st.plotly_chart(fig_weight, use_container_width=True)
        else:
            st.info("No weight data to display trends.")

        # Blood Pressure Trend
        bp_data = df_for_plot.dropna(subset=['systolic', 'diastolic'])
        if not bp_data.empty:
            fig_bp = go.Figure()
            fig_bp.add_trace(go.Scatter(x=bp_data['dates'], y=bp_data['systolic'], mode='lines+markers', name='Systolic'))
            fig_bp.add_trace(go.Scatter(x=bp_data['dates'], y=bp_data['diastolic'], mode='lines+markers', name='Diastolic'))
            fig_bp.update_layout(title='Blood Pressure Trend', xaxis_title="Date", yaxis_title="BP (mmHg)", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
            st.plotly_chart(fig_bp, use_container_width=True)
        else:
            st.info("No blood pressure data to display trends.")

        # Heart Rate Trend
        if not df_for_plot['heart_rate'].dropna().empty:
            fig_hr = px.line(df_for_plot.dropna(subset=['heart_rate']), x='dates', y='heart_rate', title='Heart Rate Trend', markers=True)
            fig_hr.update_layout(xaxis_title="Date", yaxis_title="Heart Rate (bpm)", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
            st.plotly_chart(fig_hr, use_container_width=True)
        else:
            st.info("No heart rate data to display trends.")

        # Blood Glucose Trend
        if not df_for_plot['glucose'].dropna().empty:
            fig_glucose = px.line(df_for_plot.dropna(subset=['glucose']), x='dates', y='glucose', title='Blood Glucose Trend', markers=True)
            fig_glucose.update_layout(xaxis_title="Date", yaxis_title="Glucose (mg/dL)", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
            st.plotly_chart(fig_glucose, use_container_width=True)
        else:
            st.info("No blood glucose data to display trends.")

    else:
        st.info("No health data recorded yet. Add some data above to see your history and trends!")

    # Clear Health Data
    if st.button("🗑️ Clear All Health Data", use_container_width=True):
        st.session_state.health_data = {
            'dates': [],
            'weight': [],
            'systolic': [],
            'diastolic': [],
            'heart_rate': [],
            'glucose': []
        }
        st.success("All health data cleared.")
        st.rerun()

def emergency():
    """Emergency Page with critical information and actions"""
    st.markdown('<h1 class="section-title">🚨 Emergency Services</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card" style="background: rgba(231, 76, 60, 0.2); border-color: #e74c3c;">
        <h4 style="color: #e74c3c;">❗️ In Case of Medical Emergency, Act Fast!</h4>
        <p>This page provides quick access to emergency contacts and information. If you are experiencing a life-threatening emergency, call your local emergency number immediately.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📞 Emergency Contacts")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>🚑 Ambulance / Emergency Medical Services</h4>
            <p style="font-size: 24px; font-weight: bold; color: #FF6B6B;">Dial 1122</p>
            <p>For immediate medical assistance.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>🚓 Police / Law Enforcement</h4>
            <p style="font-size: 24px; font-weight: bold; color: #FF6B6B;">Dial 15</p>
            <p>For safety and security concerns.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🏥 Nearest Hospitals & Clinics")
    st.write("Please use a mapping service (like Google Maps) to find the nearest hospitals or clinics based on your current location.")
    st.link_button("📍 Find Hospitals Near Me (Google Maps)", "https://www.google.com/maps/search/hospitals+near+me")

    # st.markdown("### 💊 Poison Control Information")
    # st.write("If you suspect poisoning, call your local poison control center immediately.")
    # st.markdown("""
    # <div class="metric-card">
    #     <h4>Poison Control Center (General)</h4>
    #     <p style="font-size: 20px; font-weight: bold; color: #4ECDC4;">04122222</p>
    #     <p>Please check for your country's specific poison control number.</p>
    # </div>
    # """, unsafe_allow_html=True)

    # st.markdown("### 📋 Important Personal Emergency Information")
    # st.write("Consider filling out and keeping the following information readily accessible for emergencies:")

    # with st.expander("📝 My Emergency Contacts & Medical Info"):
    #     st.text_input("Emergency Contact Name", placeholder="e.g., Muhammad Rizwan")
    #     st.text_input("Emergency Contact Phone", placeholder="0413567890")
    #     st.text_area("Known Allergies", placeholder="e.g., Penicillin, Peanuts")
    #     st.text_area("Current Medications", placeholder="e.g., Insulin, Blood Pressure Meds")
    #     st.text_area("Pre-existing Conditions", placeholder="e.g., Diabetes, Asthma, Heart Disease")
    #     st.button("Save Emergency Info (Local)", help="This will save information locally in your browser session.")

    st.markdown("---")
    st.markdown("### 🆘 What to Do in an Emergency:")
    st.markdown("""
    1.  **Stay Calm:** Take a deep breath to help think clearly.
    2.  **Ensure Safety:** Assess if the area is safe for you and the person in distress.
    3.  **Call for Help:** Dial your local emergency number (e.g., 1122,15).
    4.  **Provide Information:** Clearly state your location, the nature of the emergency, and the condition of the person.
    5.  **Follow Instructions:** Listen carefully to the dispatcher's instructions.
    6.  **Administer First Aid (if trained):** If you are trained in first aid or CPR, provide assistance if safe to do so.
    7.  **Do Not Move:** Unless absolutely necessary for safety, do not move an injured person.
    8.  **Wait for Professionals:** Remain with the person until emergency services arrive.
    """)

def about():
    """About Page"""
    st.markdown('<h1 class="section-title">ℹ️ About HealthSense AI</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>Our Mission</h3>
        <p>HealthSense AI is dedicated to empowering individuals to take control of their health through personalized, accessible, and intelligent solutions. We believe that everyone deserves easy access to reliable health information and tools to live a healthier life.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🚀 Technology Used")
    st.markdown("""
    -   **Streamlit:** For building interactive web applications quickly.
    -   **Groq API:** Powers our intelligent AI Doctor and Nutrition Planner for fast and accurate responses.
    -   **Plotly:** For creating interactive and insightful health data visualizations.
    -   **FPDF:** For generating downloadable PDF reports of consultations and nutrition plans.
    -   **Python:** The core programming language.
    """)

    st.markdown("---")
    st.markdown("### 🔒 Privacy and Data Security")
    st.markdown("""
    We prioritize your privacy. All chat conversations and health data entered into HealthSense AI are handled with utmost care.
    -   **Local Session Storage:** Your health data and chat history are primarily stored in your browser's session and are not persistently stored on our servers unless explicitly saved or downloaded by you.
    -   **API Usage:** While AI models process your queries, no personal identifying information is stored or used for model training by default.
    -   **Confidentiality:** We are committed to maintaining the confidentiality of your health information.
    """)

    st.markdown("---")
    st.markdown("### 👩‍💻 Developed by")
    st.markdown("""
    HealthSense AI is a project developed by Muhammad Rizwan. Our goal is to leverage the power of AI to make healthcare support more accessible and user-friendly.

    Feel free to connect with us or contribute to the project!
    """)

    st.markdown("---")
    st.markdown("### Disclaimer")
    st.warning("""
    **Important Disclaimer:** HealthSense AI is an AI-powered tool designed to provide general health information, personalized nutrition suggestions, and facilitate health tracking. It is **NOT a substitute for professional medical advice, diagnosis, or treatment.** Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or used on this application.
    """)

# Main app logic
if st.session_state.page == "Home":
    home()
elif st.session_state.page == "Doctor Chat":
    doctor_chat()
elif st.session_state.page == "Nutrition":
    nutrition()
elif st.session_state.page == "Health Tracker":
    health_tracker()
elif st.session_state.page == "Emergency":
    emergency()
elif st.session_state.page == "About":
    about()
else:
    st.error("Page not found. Please select a valid page from the sidebar.")
    