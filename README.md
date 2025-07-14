# HealthSense AI 🩺

![HealthSense AI Logo](ChatGPT_removebg.png)

**HealthSense AI** is an AI-powered web application built with Streamlit, designed to empower users with personalized health insights and tools. It provides intelligent health advice, nutrition planning, health metric tracking, and emergency resources, leveraging the Groq API for real-time AI responses and Plotly for interactive visualizations.

## 🌟 Features

- **AI Doctor Chat** 💬: Get instant medical advice from an AI-powered doctor, available 24/7. Describe symptoms or ask health-related questions for quick, reliable responses.
- **Nutrition Planner** 🥗: Generate customized meal and exercise plans based on your age, weight, height, activity level, and health goals.
- **Health Tracker** 📈: Log and visualize health metrics like weight, blood pressure, heart rate, and blood glucose with interactive charts.
- **Emergency Services** 🚨: Access critical emergency contacts and guidelines for quick action in urgent situations.
- **User-Friendly Interface**: Sleek, responsive design with a modern UI, powered by Streamlit and custom CSS.

## 🛠️ Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Groq API**: Powers AI-driven responses for doctor chat and nutrition planning.
- **Plotly**: Creates dynamic, interactive health data visualizations.
- **FPDF**: Generates downloadable PDF reports for consultations and nutrition plans.
- **Pandas**: Handles data management for health tracking.
- **Python**: The core programming language.

## 📋 Prerequisites

To run or deploy HealthSense AI, you need:
- Python 3.8 or higher
- A [Groq API key](https://x.ai/api) for AI functionality
- Git installed for version control
- A GitHub account for repository management
- A [Streamlit Community Cloud](https://streamlit.io/cloud) account for deployment

## 🚀 Installation

Follow these steps to set up HealthSense AI locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rizwan-muhammad-ai/HealthSense-AI.git
   cd HealthSense-AI
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` includes:
   ```
   streamlit
   groq
   streamlit-option-menu
   fpdf
   plotly
   pandas
   ```

4. **Set Up Secrets**:
   - Create a `secrets.toml` file in the project root:
     ```toml
     [secrets]
     groq_api_key = "your-groq-api-key-here"
     ```
   - Replace `"your-groq-api-key-here"` with your actual Groq API key.

5. **Run the App Locally**:
   ```bash
   streamlit run app.py
   ```
   - Open `http://localhost:8501` in your browser to view the app.

## ☁️ Deployment on Streamlit Community Cloud

To deploy HealthSense AI on Streamlit Community Cloud:

1. **Push to GitHub**:
   - Ensure your project files (`app.py`, `requirements.txt`, `README.md`, `ChatGPT_removebg.png`, `.gitignore`) are committed and pushed:
     ```bash
     git add .
     git commit -m "Update project files"
     git push origin main
     ```

2. **Create a Streamlit App**:
   - Sign in to [Streamlit Community Cloud](https://streamlit.io/cloud) with your GitHub account.
   - Click **New app**, select the `rizwan-muhammad-ai/HealthSense-AI` repository, and choose the `main` branch.
   - Set the main Python file to `app.py`.

3. **Add Secrets**:
   - In **Advanced settings**, add your `secrets.toml` content:
     ```toml
     [secrets]
     groq_api_key = "your-groq-api-key-here"
     ```

4. **Deploy**:
   - Click **Deploy**. Once complete, access your app at the provided URL (e.g., `https://<your-app-name>.streamlit.app`).

5. **Troubleshooting**:
   - Check deployment logs for errors (e.g., missing dependencies or image file).
   - Ensure `ChatGPT_removebg.png` is in the repository root and referenced correctly in `app.py`.

## 🖥️ Usage

- **Navigate**: Use the sidebar menu to access Home, Doctor Chat, Nutrition, Health Tracker, Emergency, and About pages.
- **Doctor Chat**: Ask health questions or select common symptoms for AI-driven advice.
- **Nutrition Planner**: Input personal details to generate tailored meal and exercise plans, downloadable as PDFs.
- **Health Tracker**: Log health metrics and view trends in interactive Plotly charts.
- **Emergency**: Find emergency contacts and guidelines for immediate action.

## 🔒 Privacy and Data Security

- **Local Storage**: Health data and chat history are stored in your browser's session, not on servers, unless saved or downloaded.
- **API Security**: The Groq API processes queries without storing personal data.
- **Confidentiality**: We prioritize your privacy and handle data with care.

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit (`git commit -m "Add your feature"`).
4. Push to your fork (`git push origin feature/your-feature`).
5. Create a pull request on GitHub.

## ⚠️ Disclaimer

HealthSense AI is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns. Use this app for informational purposes only.

## 👨‍💻 Developer

Developed by **Muhammad Rizwan**. Connect with me on [GitHub](https://github.com/rizwan-muhammad-ai) or reach out for feedback and collaboration.

## 📬 Contact

For questions or support, open an issue on GitHub or contact the developer at [your.email@example.com](mailto:your.email@example.com).

---
