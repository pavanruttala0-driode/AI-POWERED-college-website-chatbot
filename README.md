# 🎓 AI-Powered College Website Chatbot

An AI-powered conversational chatbot designed to help students, parents, applicants, faculty, and visitors quickly access information about a college.

The chatbot uses the **Google Gemini API** to understand natural-language questions and provide intelligent, conversational responses through a user-friendly web interface.

---

## 🚀 Project Overview

College websites contain a large amount of information about admissions, courses, fees, scholarships, departments, facilities, placements, examinations, and campus services.

Finding specific information can sometimes require searching through multiple pages.

The **AI-Powered College Website Chatbot** provides a simple solution: users can ask questions naturally and receive instant AI-powered responses.

### Example

**User:**

> What courses does the college offer?

**Chatbot:**

> The college offers various undergraduate and postgraduate programs. You can ask me about a specific course or department for more details.

---

## 🎯 Problem Statement

Students and visitors often spend a lot of time searching through college websites to find specific information.

Common questions include:

* How do I apply for admission?
* What courses are available?
* What are the eligibility requirements?
* What is the fee structure?
* Are scholarships available?
* Does the college provide hostel facilities?
* What are the placement opportunities?

The chatbot aims to provide a faster and more convenient way to access this information.

---

## 💡 Proposed Solution

The chatbot provides an AI-powered conversational interface where users can ask college-related questions in natural language.

The **Gemini API** processes the user's question and generates an appropriate response.

---

## ✨ Features

### 🎓 Admissions

* Admission process
* Eligibility requirements
* Application information
* Required documents
* Admission FAQs

### 📚 Courses & Departments

* Available courses
* Departments
* Academic programs
* Course-related questions

### 💰 Fees & Scholarships

* Fee-related information
* Scholarship information
* Financial assistance questions

### 🏫 Campus Facilities

* Library
* Laboratories
* Hostel
* Canteen
* Transportation
* Campus facilities

### 💼 Placements

* Placement information
* Career opportunities
* Recruiters
* Training and placement questions

### 📝 Examinations

* Examination information
* Academic questions
* Semester-related information

### 📞 Contact & Location

* College contact information
* Department information
* Campus location
* Administrative information

---

## 🛠️ Technologies Used

* **Python** — Programming language
* **Streamlit** — Web application framework
* **Google Gemini API** — AI model and natural-language processing
* **python-dotenv** — Environment variable management
* **HTML/CSS** — User interface customization

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Streamlit Web App   │
                  │    Chat Interface   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Chatbot Processing │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │    Gemini API       │
                  │   AI Processing     │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Generated Answer   │
                  └──────────┬──────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      User       │
                    └─────────────────┘
```

---

## 📂 Project Structure

```text
AI-Powered-College-Website-Chatbot/
│
├── NexaAI.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> **Important:** Never upload your `.env` file or Gemini API key to GitHub.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Powered-College-Website-Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Never publish your real API key.

### 4. Run the Application

```bash
streamlit run NexaAI.py
```

The chatbot will open in your browser.

---

## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

For deployment, add your Gemini API key to the application's Secrets:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

The API key should not be included directly in the Python source code.

---

## 💬 Sample Questions

Users can ask questions such as:

```text
What courses does the college offer?

How can I apply for admission?

What is the eligibility for B.Tech?

What is the fee structure?

Are scholarships available?

Does the college provide hostel facilities?

What campus facilities are available?

What companies recruit students?

What are the placement opportunities?

Where is the college located?

How can I contact the admission office?
```

---

## 🔐 Security

The project uses environment variables and deployment secrets to protect the Gemini API key.

### Security practices

* API keys are stored outside the source code.
* `.env` should be included in `.gitignore`.
* API keys should never be committed to GitHub.
* Deployment secrets should be used for production deployment.

---

## 🚀 Future Enhancements

Future versions can include:

* 🔎 College website knowledge-base integration
* 📄 PDF/document question answering
* 🧠 Retrieval-Augmented Generation (RAG)
* 🗃️ College database integration
* 🌐 Multiple language support
* 🎤 Voice input
* 🔊 Voice responses
* 📱 Mobile-friendly design
* 📊 Admin dashboard
* 📰 College announcements
* 📅 Event and academic-calendar integration
* 🔗 Links to relevant college website pages

---

## 🏆 Hackathon Impact

### Problem

Students, parents, and visitors often need to search through multiple college website pages to find specific information.

### Solution

An AI-powered chatbot that allows users to ask questions naturally and receive instant responses using the **Google Gemini API**.

### Impact

* ⚡ Faster access to college information
* 🤖 24/7 AI assistance
* 🎓 Better student experience
* 🔎 Easier website navigation
* 💬 Natural-language interaction
* ⏱️ Reduced time spent searching for information

---

## 👥 Target Users

* 👨‍🎓 Students
* 👩‍🎓 Prospective students
* 👨‍👩‍👧 Parents
* 👨‍🏫 Faculty
* 🧑‍💼 College staff
* 🌐 Website visitors

---

## 🧠 AI Technology

This project uses the **Google Gemini API** as its AI engine.

Gemini enables the chatbot to:

* Understand natural-language questions
* Maintain conversational context
* Generate helpful responses
* Explain complex topics in simple language
* Assist users with college-related queries

---

## 📜 License

This project is developed for educational and hackathon purposes.

---

## 👨‍💻 Project Information

**Project Name:** AI-Powered College Website Chatbot

**AI Model:** Google Gemini

**Frontend:** Streamlit

**Programming Language:** Python

**Purpose:** AI-powered college information and student assistance

**Version:** 1.0

---

## ⭐ Conclusion

The **AI-Powered College Website Chatbot** combines **Python, Streamlit, and Google Gemini AI** to create an intelligent and user-friendly college information assistant.

Instead of manually searching through multiple pages, users can simply ask questions and interact with the college website through natural conversation.
