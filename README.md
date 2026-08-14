🎓 NexaAI College Assistant

NexaAI College Assistant is an AI-powered conversational assistant designed to help students, parents, and visitors get useful information about colleges, courses, admissions, fees, scholarships, campus facilities, placements, internships, and career opportunities.

The application is built with Streamlit and powered by the Google Gemini API.

✨ Features

- 🤖 AI-powered conversational chatbot
- 🏫 College-specific question support
- 🎓 Courses and department information
- 📝 Admission and eligibility guidance
- 💰 Fees and scholarship information
- 🏠 Hostel and campus facilities
- 💼 Placement and internship guidance
- 📚 Academic and examination-related assistance
- 🔎 College comparison and general college guidance
- 🚀 Career guidance
- 💬 Conversation context for follow-up questions
- ⚡ Quick-question buttons
- 📱 Responsive Streamlit interface
- 🔐 Secure Gemini API key configuration through Streamlit Secrets
- 📚 Optional local "knowledge.json" knowledge base

🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI Python SDK
- JSON Knowledge Base

📁 Project Structure

NexaAI-College-Assistant/
│
├── app.py
├── knowledge.json
├── requirements.txt
└── README.md

🚀 Getting Started

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

2. Install dependencies

pip install -r requirements.txt

Your "requirements.txt" should contain:

streamlit
google-genai

3. Configure Gemini API

Create a Gemini API key using Google AI Studio.

Do not put the API key directly inside "app.py" or upload it to GitHub.

For local development, configure the key using your environment or Streamlit secrets.

For Streamlit Cloud, add the following under App Settings → Secrets:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

4. Run the application

streamlit run app.py

The application will open in your browser.

☁️ Deploy on Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Select your GitHub repository.
4. Select "app.py" as the main file.
5. Deploy the application.
6. Open Settings → Secrets.
7. Add:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

8. Save the secret and reboot the application.

🔐 Security

Never commit your Gemini API key to GitHub.

❌ Don't do this:

api_key = "YOUR_REAL_API_KEY"

✅ Use Streamlit Secrets:

api_key = st.secrets.get("GEMINI_API_KEY")

If an API key is accidentally published, revoke it and create a new one.

💡 Example Questions

Users can ask:

What courses are available?

What are the admission requirements?

Tell me about B.Tech CSE.

What scholarships are available?

What facilities does the college provide?

Tell me about hostel facilities.

How do placements work?

What career opportunities are available after ECE?

Compare CSE and ECE.

What documents are required for admission?

For college-specific questions, users can enter the college name and then ask their question.

🧠 How It Works

User
  ↓
NexaAI College Assistant
  ↓
College / User Context
  ↓
Gemini AI
  ↓
AI-generated Response
  ↓
Student

The application combines the Gemini AI model with an optional local "knowledge.json" file to provide contextual answers.

⚠️ Information Accuracy

NexaAI should not be treated as an official source for time-sensitive information such as:

- Current admission deadlines
- Exact fees
- Current placement statistics
- Latest notices
- Official rankings
- Faculty changes

Users should verify important information through the respective college's official sources.

🔮 Future Enhancements

- 🌐 Live college website search
- 📰 Real-time college notices
- 📅 Admission deadline tracking
- 📍 College location and map integration
- 🔎 Advanced college discovery
- 📊 College comparison dashboard
- 📄 PDF/document-based college knowledge
- 🗣️ Voice-based interaction
- 🌍 Multilingual support
- 👨‍🎓 Personalized student dashboard

🎯 Project Goal

The goal of NexaAI College Assistant is to make college-related information easier to access through a simple conversational AI interface.

Instead of searching through multiple pages and documents, students can ask questions naturally and receive relevant guidance from one assistant.

👨‍💻 Project

Project Name: NexaAI College Assistant

Category: Artificial Intelligence / Education Technology

Built With: Python, Streamlit & Google Gemini API

---

⭐ If you find this project useful

Give the repository a ⭐ on GitHub!
