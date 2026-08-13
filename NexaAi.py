import os
import json
import streamlit as st

# Page Setup
st.set_page_config(
    page_title="NexGen | AI Assistant",
    page_icon="🎓",
    layout="wide"
)

# Load Knowledge Base
KNOWLEDGE_PATH = os.path.join(os.path.dirname(__file__), 'knowledge.json')
@st.cache_data
def load_knowledge():
    try:
        with open(KNOWLEDGE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

KNOWLEDGE_BASE = load_knowledge()

# Retrieve API Key from Streamlit Secrets or Environment
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

gemini_client = None
if api_key and api_key != "your_gemini_api_key_here":
    try:
        from google import genai
        gemini_client = genai.Client(api_key=api_key)
    except Exception as e:
        st.sidebar.warning(f"Gemini Init Warning: {e}")

SYSTEM_INSTRUCTION = f"""
You are "NexGenAI", the official AI Admissions Counselor & Student Assistant for colleges
Use the following Knowledge Base to answer student questions concisely with markdown bullet points:
{json.dumps(KNOWLEDGE_BASE, indent=2)}
"""

def local_fallback_reply(query):
    q = query.lower()
    if any(k in q for k in ["program", "course", "degree", "cs", "mba"]):
        return "🎓 **Degree Programs:** B.S. Computer Science ($28,500/yr), B.S. Data Science & AI ($28,500/yr), Executive MBA ($34,000/yr)."
    if any(k in q for k in ["apply", "admission", "requirement", "deadline"]):
        return "📋 **Admissions:** High School GPA 3.0+, Transcripts, 1 Recommendation letter.\n⏳ **Deadlines:** Fall Early Action: Nov 1 | Fall Regular: Feb 15."
    if any(k in q for k in ["fee", "scholarship", "aid"]):
        return "💰 **Scholarships:** Apex Academic Excellence (Up to $15,000/yr), STEM Leadership Fund ($10,000/yr)."
    return "Welcome to **Apex Tech University**! How can I assist your educational journey today?"

# Sidebar
with st.sidebar:
    st.title("🎓 NexGenAI")
    st.caption("AI ASSISTENT")
    st.markdown("---")
    st.subheader("🏛️ Campus Overview")
    col1, col2 = st.columns(2)
    col1.metric("Students", "14,500+")
    col1.metric("Acceptance", "38%")
    col2.metric("Placement", "96%")
    col2.metric("Max Grant", "$15K/yr")

    st.markdown("---")
    st.subheader("📩 Request Info")
    with st.form("inquiry_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        prog = st.selectbox("Program", ["B.S. Computer Science", "B.S. Data Science & AI", "Executive MBA"])
        if st.form_submit_button("Submit Inquiry"):
            if name and email:
                st.success(f"Thank you {name}! Admissions will email you at {email}.")
            else:
                st.error("Please enter your name and email.")

# Main Interface
st.title("NexGen AI Assistant")
st.caption("Interactive Admissions Counselor powered by Google Gemini 3.6 Flash API")

# Quick Action Prompt Chips
st.markdown("**⚡ Quick Prompts:**")
chip_cols = st.columns(4)
preset_input = None
if chip_cols[0].button("📋 Admission Criteria"):
    preset_input = "What are the undergraduate admission requirements and deadlines?"
if chip_cols[1].button("💰 Scholarships & Fees"):
    preset_input = "Tell me about tuition fees and available scholarships."
if chip_cols[2].button("🎓 Computer Science"):
    preset_input = "What courses and careers are included in B.S. Computer Science?"
if chip_cols[3].button("🏠 Campus Life"):
    preset_input = "Tell me about housing, dorms, and campus organizations."

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to **NexGen**! 🎓\n\nI am NexGen AI. Ask me anything about our degree programs, admissions criteria, scholarships, or campus life!"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🤖" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"])

user_query = st.chat_input("Ask NexGen AI about courses, fees, admissions...") or preset_input

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_query)

    with st.chat_message("assistant", avatar="🤖"):
        if gemini_client:
            try:
                context = "".join([f"{'User' if m['role']=='user' else 'ApexAI'}: {m['content']}\n" for m in st.session_state.messages[-6:]])
                resp = gemini_client.interactions.create(
                    model="gemini-3.6-flash",
                    input=f"{SYSTEM_INSTRUCTION}\n\nHistory:\n{context}\nUser: {user_query}\nApexAI:"
                )
                bot_reply = resp.output_text or local_fallback_reply(user_query)
            except Exception:
                bot_reply = local_fallback_reply(user_query)
        else:
            bot_reply = local_fallback_reply(user_query)

        st.markdown(bot_reply)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
