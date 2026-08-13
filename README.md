# 🎓 AI-Powered College Website Chatbot

An AI-powered chatbot designed to help students, parents, applicants, faculty, and visitors quickly find information about a college.

The chatbot uses the **Google Gemini API** to understand natural-language questions and provide intelligent responses through a user-friendly Streamlit interface.

---

## 🚀 Project Overview

College websites contain a large amount of information about admissions, courses, fees, scholarships, departments, facilities, placements, examinations, and campus services.

Instead of searching through multiple pages, users can simply ask the chatbot a question and receive an AI-generated response.

### Example

**User:**

> What courses does the college offer?

**Chatbot:**

> The college offers various undergraduate and postgraduate programs. You can ask me about a specific course or department for more information.

---

## 🎯 Problem Statement

Students and visitors often spend a lot of time searching college websites for specific information.

The chatbot provides a simple conversational solution that allows users to ask questions naturally and get quick responses.

---

## 💡 Proposed Solution

The **AI-Powered College Website Chatbot** provides a conversational interface powered by the **Google Gemini API**.

Users can ask questions about the college, and the chatbot processes the question and generates an appropriate response.

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

* Fee information
* Scholarship information
* Financial assistance questions

### 🏫 Campus Facilities

* Library
* Laboratories
* Hostel
* Canteen
* Transportation
* Other campus facilities

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
* **Google Gemini API** — Artificial intelligence and natural-language processing
* **HTML/CSS** — User interface design

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Streamlit Web App │
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
                  │     Gemini API      │
                  │    AI Processing    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   AI Generated      │
                  │      Response       │
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
└── README.md
```

### File Description

| File               | Description                        |
| ------------------ | ---------------------------------- |
| `NexaAI.py`        | Main Streamlit chatbot application |
| `requirements.txt` | Required Python libraries          |
| `README.md`        | Project documentation              |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Powered-College-Website-Chatbot
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API

Add your Gemini API key according to your application's configuration.

For Streamlit deployment, use the application's **Secrets** settings to store the API key securely.

### 4. Run the Application

```bash
streamlit run NexaAI.py
```

The chatbot will open in your web browser.

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

## 🧠 How the Chatbot Works

1. The user enters a question.
2. The Streamlit application receives the question.
3. The question is sent to the Gemini API.
4. Gemini processes the user's request.
5. The AI generates a response.
6. The response is displayed in the chatbot interface.
7. Previous messages are maintained during the conversation.

---

## 🏆 Hackathon Impact

### Problem

Students, parents, and visitors often need to search through multiple college website pages to find specific information.

### Solution

An AI-powered chatbot that allows users to ask questions naturally and receive instant responses using Google Gemini.

### Benefits

* ⚡ Faster access to information
* 🤖 24/7 AI assistance
* 🎓 Better student experience
* 🔎 Easier information discovery
* 💬 Natural-language interaction
* ⏱️ Reduced search time

---

## 👥 Target Users

* 👨‍🎓 Students
* 👩‍🎓 Prospective students
* 👨‍👩‍👧 Parents
* 👨‍🏫 Faculty
* 🧑‍💼 College staff
* 🌐 Website visitors

---

## 🚀 Future Enhancements

* 🔎 College website knowledge-base integration
* 📄 PDF and document question answering
* 🧠 Retrieval-Augmented Generation (RAG)
* 🗃️ College database integration
* 🌐 Multiple language support
* 🎤 Voice input
* 🔊 Voice responses
* 📱 Mobile-friendly interface
* 📊 Admin dashboard
* 📰 College announcements
* 📅 Event and academic-calendar integration
* 🔗 Links to relevant college website pages

---

## 🔐 Security

The Gemini API key should **not be publicly exposed** in the source code or GitHub repository.

For deployment, configure the API key using **Streamlit Secrets**.

---

## 📜 License

This project is developed for educational and hackathon purposes.

---

## 👨‍💻 Project Information

**Project Name:** AI-Powered College Website Chatbot

**AI Technology:** Google Gemini API

**Frontend:** Streamlit

**Programming Language:** Python

**Project Type:** AI / Education / Chatbot

**Purpose:** Intelligent college information and student assistance

**Version:** 1.0

---

## ⭐ Conclusion

The **AI-Powered College Website Chatbot** combines **Python, Streamlit, and Google Gemini AI** to provide an intelligent and user-friendly college information assistant.

Users can ask questions naturally instead of manually searching through multiple college website pages, making access to educational information faster, simpler, and more interactive.
