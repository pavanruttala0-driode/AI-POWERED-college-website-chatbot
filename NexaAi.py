import os
import json
import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="NexaAI College Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #777;
        margin-bottom: 25px;
    }

    .feature-card {
        padding: 18px;
        border-radius: 16px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 12px;
        background: rgba(128,128,128,0.05);
    }

    .feature-title {
        font-size: 18px;
        font-weight: 700;
    }

    .small-text {
        font-size: 14px;
        color: #777;
    }

    .college-box {
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(128,128,128,0.3);
        background: rgba(128,128,128,0.06);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD KNOWLEDGE BASE
# =========================================================

KNOWLEDGE_PATH = os.path.join(
    os.path.dirname(__file__),
    "knowledge.json"
)


@st.cache_data
def load_knowledge():
    try:
        with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return {}


KNOWLEDGE_BASE = load_knowledge()

# =========================================================
# GEMINI API
# =========================================================

api_key = None

try:
    api_key = st.secrets.get("GEMINI_API_KEY")
except Exception:
    api_key = None

if not api_key:
    api_key = os.environ.get("GEMINI_API_KEY")


gemini_client = None

if api_key and api_key != "your_gemini_api_key_here":
    try:
        from google import genai

        gemini_client = genai.Client(api_key=api_key)

    except Exception as e:
        st.sidebar.error(
            "Gemini SDK could not be initialized."
        )
else:
    gemini_client = None


# =========================================================
# SYSTEM INSTRUCTION
# =========================================================

SYSTEM_INSTRUCTION = """
You are NexaAI College Assistant, an intelligent AI assistant
designed to help students, parents and visitors understand
college-related information.

Your job is NOT limited to one specific college.

You can answer questions about:

1. College information
2. Courses and degree programs
3. Departments
4. Admissions
5. Eligibility
6. Application process
7. Fees
8. Scholarships
9. Hostel facilities
10. Campus facilities
11. Transportation
12. Student life
13. Clubs and activities
14. Placements
15. Internships
16. Career opportunities
17. Exams
18. Timetables
19. College notices
20. General college guidance
21. Comparing colleges
22. Choosing a suitable college
23. Engineering branches
24. Career guidance

IMPORTANT RULES:

- Be helpful, friendly and professional.
- Use simple language.
- Prefer short paragraphs and bullet points.
- If the user gives a college name, focus on that college.
- If the user asks about another college, answer about that college.
- Do not pretend that you have verified information if you have not.
- Never invent fees, placement percentages, rankings, faculty names,
  admission deadlines or contact details.
- If exact information is unavailable, clearly say that the information
  needs to be verified from the official college source.
- Do not claim that information is live/current unless it is provided
  by the application or verified source.
- If the user asks a general educational question, answer it normally.
- If the user asks for a college comparison, organize the answer clearly.
- If the question is unclear, ask a short clarification question.
- Maintain conversation context.

You are called:

NexaAI College Assistant
"""


# =========================================================
# LOCAL FALLBACK
# =========================================================

def local_fallback_reply(query):

    q = query.lower().strip()

    if any(
        word in q
        for word in [
            "admission",
            "apply",
            "application",
            "eligibility",
            "requirement"
        ]
    ):
        return """
### 📝 Admissions

I can help you with:

- Admission eligibility
- Application process
- Required documents
- Entrance examinations
- Important admission information

Please provide the **college name** and course/branch you are interested in.
"""

    if any(
        word in q
        for word in [
            "course",
            "courses",
            "branch",
            "degree",
            "program",
            "department"
        ]
    ):
        return """
### 🎓 Courses & Departments

I can help you find information about:

- B.Tech / Engineering
- Computer Science
- Electronics & Communication
- Electrical Engineering
- Mechanical Engineering
- Civil Engineering
- MBA
- MCA
- Other degree programs

Please tell me the **college name** for college-specific information.
"""

    if any(
        word in q
        for word in [
            "fee",
            "fees",
            "tuition",
            "scholarship"
        ]
    ):
        return """
### 💰 Fees & Scholarships

I can help you understand:

- Tuition fees
- Hostel fees
- Scholarship opportunities
- Financial assistance
- Government scholarship options

For exact amounts, please provide the college name and course.
"""

    if any(
        word in q
        for word in [
            "hostel",
            "campus",
            "facility",
            "facilities",
            "library",
            "canteen"
        ]
    ):
        return """
### 🏫 Campus & Facilities

I can help you with information about:

- Hostel
- Library
- Laboratories
- Canteen
- Sports
- Transportation
- Campus facilities
- Student activities

Tell me the college name to get college-specific information.
"""

    if any(
        word in q
        for word in [
            "placement",
            "placements",
            "job",
            "jobs",
            "internship",
            "career"
        ]
    ):
        return """
### 💼 Placements & Careers

I can help you understand:

- Placement process
- Internship opportunities
- Recruiters
- Career options
- Branch-wise career paths
- Skills required for jobs

For college-specific placement statistics, the official college placement
information should be verified.
"""

    return """
### 👋 Welcome to NexaAI College Assistant!

I can help you with:

🎓 **Courses & Departments**  
📝 **Admissions & Eligibility**  
💰 **Fees & Scholarships**  
🏫 **Hostel & Campus Facilities**  
💼 **Placements & Internships**  
📚 **Exams & Student Information**  
🔎 **College Comparisons**  
🚀 **Career Guidance**

Try asking:

> "Tell me about B.Tech CSE"

or

> "What are the admission requirements for XYZ College?"

or

> "Compare two engineering colleges."
"""


# =========================================================
# GEMINI RESPONSE
# =========================================================

def get_gemini_response(user_query):

    if not gemini_client:
        return local_fallback_reply(user_query)

    try:

        knowledge_context = ""

        if KNOWLEDGE_BASE:
            knowledge_context = f"""
LOCAL KNOWLEDGE BASE:

{json.dumps(
    KNOWLEDGE_BASE,
    indent=2,
    ensure_ascii=False
)}
"""

        history = ""

        for message in st.session_state.messages[-10:]:
            role = message["role"]

            if role == "user":
                history += f"User: {message['content']}\n"

            elif role == "assistant":
                history += f"NexaAI: {message['content']}\n"

        prompt = f"""
{SYSTEM_INSTRUCTION}

{knowledge_context}

CONVERSATION HISTORY:
{history}

CURRENT USER QUESTION:
{user_query}

Answer the user now.

Remember:
- Do not invent unknown college facts.
- If a college name is provided, answer specifically about that college.
- If exact information is unavailable, say so.
- Use Markdown.
- Keep the answer useful and easy to understand.
"""

        response = gemini_client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        if response and response.text:
            return response.text.strip()

        return local_fallback_reply(user_query)

    except Exception as e:

        return f"""
⚠️ **I couldn't connect to the AI service right now.**

Please check your Gemini API configuration.

If the problem continues, verify that your Streamlit Secret is:

`GEMINI_API_KEY`

**Technical message:** `{str(e)}`
"""


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🎓 NexaAI")

    st.caption("COLLEGE ASSISTANT")

    st.markdown("---")

    st.subheader("🏫 What I Can Help With")

    st.markdown("""
    - 🎓 Courses & Departments
    - 📝 Admissions
    - 💰 Fees & Scholarships
    - 🏠 Hostel & Facilities
    - 💼 Placements
    - 🚀 Internships
    - 📚 Exams & Academics
    - 🔎 College Comparison
    - 🎯 Career Guidance
    """)

    st.markdown("---")

    st.subheader("💡 Tip")

    st.info(
        "For college-specific answers, include the college name "
        "in your question."
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "Welcome to **NexaAI College Assistant**! 🎓\n\n"
                "Ask me about colleges, courses, admissions, fees, "
                "placements, campus facilities or career guidance."
            }
        ]

        st.rerun()


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🎓 NexaAI College Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your AI-powered assistant for college information, admissions, '
    'courses, careers and student guidance.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# COLLEGE INPUT
# =========================================================

st.markdown(
    '<div class="college-box">',
    unsafe_allow_html=True
)

st.markdown("### 🏫 Select / Enter College")

college_name = st.text_input(
    "College Name",
    placeholder="Example: ABC Engineering College",
    label_visibility="collapsed"
)

st.caption(
    "Optional: Enter a college name to make your questions more specific."
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# QUICK ACTIONS
# =========================================================

st.markdown("### ⚡ Quick Questions")

col1, col2, col3, col4 = st.columns(4)

preset_input = None

with col1:
    if st.button(
        "🎓 Courses",
        use_container_width=True
    ):
        preset_input = "What courses and departments are available?"

with col2:
    if st.button(
        "📝 Admissions",
        use_container_width=True
    ):
        preset_input = "What are the admission requirements and process?"

with col3:
    if st.button(
        "💼 Placements",
        use_container_width=True
    ):
        preset_input = "Tell me about placements and career opportunities."

with col4:
    if st.button(
        "🏠 Facilities",
        use_container_width=True
    ):
        preset_input = "What facilities and campus services are available?"


# =========================================================
# CHAT INITIALIZATION
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            """
# 👋 Welcome to NexaAI!

I am your **AI-powered College Assistant**.

I can help you with:

- 🎓 Courses & departments
- 📝 Admissions & eligibility
- 💰 Fees & scholarships
- 🏫 Campus & hostel
- 💼 Placements & internships
- 📚 Academic information
- 🔎 College comparisons
- 🚀 Career guidance

**Example:**  
`Tell me about CSE in engineering colleges`

You can also enter a college name above for a more focused conversation.
"""
        }
    ]


# =========================================================
# DISPLAY CHAT
# =========================================================

for message in st.session_state.messages:

    if message["role"] == "assistant":

        with st.chat_message(
            "assistant",
            avatar="🎓"
        ):
            st.markdown(message["content"])

    else:

        with st.chat_message(
            "user",
            avatar="👤"
        ):
            st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

user_query = st.chat_input(
    "Ask NexaAI about colleges, courses, admissions..."
)

if preset_input:
    user_query = preset_input


# =========================================================
# PROCESS USER QUESTION
# =========================================================

if user_query:

    # Add college context if provided
    final_query = user_query

    if college_name.strip():

        final_query = f"""
College selected by the user:

{college_name.strip()}

User question:

{user_query}
"""

    # Add user message to UI
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    with st.chat_message(
        "user",
        avatar="👤"
    ):
        st.markdown(user_query)

    # Generate response
    with st.chat_message(
        "assistant",
        avatar="🎓"
    ):

        with st.spinner("NexaAI is thinking... 🤖"):

            bot_reply = get_gemini_response(
                final_query
            )

        st.markdown(bot_reply)

    # Save response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )
