<div align="center">
  <img src="https://raw.githubusercontent.com/devtayyabsajjad/Sehat-Connect/refs/heads/main/logo-removebg--preview.png" alt="Sehat Connect Logo" width="500"/>
  
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
  </p>
</div>

<div align="center">
  <h3>🌟 Your Virtual Doctor & Nutritionist powered by AI 🌟</h3>
</div># HealthSense AI

![HealthSense AI Logo](ChatGPT_removebg.png)

HealthSense AI is an AI-powered web application built with Streamlit, designed to provide personalized health advice, nutrition planning, health tracking, and emergency information. It leverages the Groq API for intelligent responses and Plotly for interactive visualizations.

## Features
- **AI Doctor Chat**: Get instant medical advice from an AI-powered doctor.
- **Nutrition Planner**: Generate personalized meal and exercise plans based on user inputs (age, weight, height, goals, etc.).
- **Health Tracker**: Log and visualize health metrics like weight, blood pressure, heart rate, and blood glucose.
- **Emergency Services**: Quick access to emergency contacts and guidelines.
- **About**: Learn about the app, its technology, and privacy policies.

## Technologies Used
- **Streamlit**: For the web interface.
- **Groq API**: For AI-powered responses.
- **Plotly**: For interactive health data visualizations.
- **FPDF**: For generating PDF reports.
- **Pandas**: For data manipulation.
- **Python**: Core programming language.

## Prerequisites
- Python 3.8+
- A Groq API key (sign up at [x.ai](https://x.ai/api) to obtain one)
- Git installed on your system
- A GitHub account
- A Streamlit Community Cloud account

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/HealthSense-AI.git
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

4. **Set Up Secrets**:
   - Create a `secrets.toml` file in the project root with your Groq API key:
     ```toml
     [secrets]
     groq_api_key = "your-groq-api-key-here"
     ```

5. **Run the App Locally**:
   ```bash
   streamlit run app.py
   ```
   - Open your browser to `http://localhost:8501` to view the app.

## Deployment on Streamlit Community Cloud
1. **Push to GitHub**:
   - Ensure your project files (`app.py`, `requirements.txt`, `ChatGPT_removebg.png`, `README.md`, `.gitignore`) are committed and pushed to a GitHub repository.
   - Example commands:
     ```bash
     git add .
     git commit -m "Initial commit"
     git push origin main
     ```

2. **Deploy on Streamlit Cloud**:
   - Sign in to [Streamlit Community Cloud](https://streamlit.io/cloud) with your GitHub account.
   - Create a new app, select your `HealthSense-AI` repository, and specify `app.py` as the main file.
   - In **Advanced settings**, add your `secrets.toml` content:
     ```toml
     [secrets]
     groq_api_key = "your-groq-api-key-here"
     ```
   - Click **Deploy** and wait for the app to build. Access it via the provided URL.

## Usage
- Navigate using the sidebar menu to access different features.
- **Doctor Chat**: Ask health-related questions or select common symptoms for quick responses.
- **Nutrition Planner**: Input personal details to generate a personalized nutrition and exercise plan.
- **Health Tracker**: Log health metrics and view trends in interactive charts.
- **Emergency**: Access emergency contacts and guidelines.
- **About**: Learn about the app and its technology.

## Privacy and Data Security
- Health data and chat history are stored locally in the browser session.
- No personal data is stored on servers unless explicitly saved or downloaded as a PDF.
- The Groq API processes queries without storing personal identifying information.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## Disclaimer
HealthSense AI is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

## Developer
Developed by Muhammad Rizwan.

## 🚀 About The Project

Sehat Connect is a revolutionary virtual healthcare platform that brings the power of AI to personal health management. Our application combines cutting-edge GPT-4 technology with an intuitive interface to provide personalized medical advice and nutritional guidance.

### ✨ Key Features

- 🤖 AI-powered medical consultation
- 📊 BMI calculation and tracking
- 🥗 Personalized diet plans
- 🏋️‍♂️ Customized exercise routines
- 📝 Automated PDF report generation
- 💬 Interactive chat interface
- 📱 User-friendly design

## 🛠️ Built With

- ![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
- ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red?style=flat-square&logo=streamlit)
- ![OpenAI](https://img.shields.io/badge/GPT--4-API-green?style=flat-square&logo=openai)

## 👥 Meet Our Amazing Team



<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/asim-khan-baloch/"><img src="https://github.com/Asimbaloch.png" width="120px;" alt="Asim Khan"/><br /><sub><b>Asim Khan</b><br></sub></a><br />
      <a href="https://www.linkedin.com/in/asim-khan-baloch/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" width="100px"/></a>
      <a href="https://github.com/Asimbaloch"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" width="100px"/></a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/ahmad-fakhar-357742258/"><img src="https://github.com/Ahmad-Fakhar.png" width="120px;" alt="Ahmad Fakhar"/><br /><sub><b>Ahmad Fakhar</b><br></sub></a><br />
      <a href="https://www.linkedin.com/in/ahmad-fakhar-357742258/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" width="100px"/></a>
      <a href="https://github.com/Ahmad-Fakhar"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" width="100px"/></a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/muhammad-jawad-86507b201"><img src="https://github.com/mj-awad17.png" width="120px;" alt="Muhammad Jawad"/><br /><sub><b>Muhammad Jawad</b><br></sub></a><br />
      <a href="https://www.linkedin.com/in/muhammad-jawad-86507b201"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" width="100px"/></a>
      <a href="https://github.com/mj-awad17"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" width="100px"/></a>
    </td>
    <td align="center">
      <a href="http://www.linkedin.com/in/tayyab-sajjad-156ab2267"><img src="https://avatars.githubusercontent.com/u/124726671?v=4" width="120px;" alt="Tayyab Sajjiad"/><br /><sub><b>Tayyab Sajjiad</b><br></sub></a><br />
      <a href="http://www.linkedin.com/in/tayyab-sajjad-156ab2267"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" width="100px"/></a>
      <a href="https://github.com/devtayyabsajjad"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" width="100px"/></a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/"><img src="https://github.com/muhammadibrahim313.png" width="120px;" alt="Muhammad Ibrahim"/><sub><br><b>Muhammad Ibrahim</b><br></sub></a><br />
      <a href="https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" width="100px"/></a>
      <a href="https://github.com/muhammadibrahim313"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" width="100px"/></a>
    </td>
   <td align="center"> 
  <a href="https://www.linkedin.com/in/"><img src="https://media.licdn.com/dms/image/v2/D4E03AQFyK8SIQkAFpA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1688370356823?e=1735776000&v=beta&t=1Uo6GsirXGHBxUzxrjJ77x6xBB4uduHmV5uyDaRK5Nw" width="120px;" alt="Usama"/><sub><br><b>Muhammad Bilal</b><br></sub></a><br />
  <a href="https://www.linkedin.com/in/muhammad-bilal-a75782280/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" width="100px"/></a>
  <a href="https://github.com/bilal77511"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" width="100px"/></a>
</td>
</table>


## 📱 UI Interface

<div align="center">
  <img src="https://github.com/devtayyabsajjad/Sehat-Connect/blob/main/ss/Capture1.PNG?raw=true" width="400" />
  <img src="https://github.com/devtayyabsajjad/Sehat-Connect/blob/main/ss/Capture2.PNG?raw=true" width="400" />
  <img src="https://github.com/devtayyabsajjad/Sehat-Connect/blob/main/ss/Capture3.PNG?raw=true" width="400" />
</div>

## 🚀 Getting Started

1. Clone the repository
```bash
git clone  https://github.com/yourusername/sehat-connect.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the application
```bash
streamlit run app.py
```
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

<div align="center"> <p>Made with ❤️ by Team B-TAJI</p> <p>© 2024 Sehat Connect. All rights reserved.</p> </div> 
