import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# =========================================================
# CONFIG
# =========================================================

load_dotenv()

st.set_page_config(
    page_title="NexaAI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_KEY = os.getenv("OPENAI_API_KEY")

if API_KEY:
    client = OpenAI(api_key=API_KEY)
else:
    client = None


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ---------- Global ---------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.10), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(14,165,233,0.10), transparent 25%),
        #f8fafc;
}

/* ---------- Hide Streamlit UI ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.88);
    border-right: 1px solid #e2e8f0;
}

/* ---------- Brand ---------- */

.brand {
    font-size: 30px;
    font-weight: 800;
    letter-spacing: -1px;
}

.brand-icon {
    display: inline-flex;
    width: 42px;
    height: 42px;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: linear-gradient(135deg,#6366f1,#06b6d4);
    color: white;
    margin-right: 8px;
    box-shadow: 0 8px 25px rgba(99,102,241,0.25);
}

.tagline {
    color: #64748b;
    font-size: 14px;
    margin-top: -4px;
}

/* ---------- Hero ---------- */

.hero {
    text-align: center;
    padding: 55px 20px 25px 20px;
}

.hero-icon {
    font-size: 55px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-top: 8px;
}

.hero-subtitle {
    color: #64748b;
    font-size: 18px;
    margin-top: 5px;
}

/* ---------- Feature cards ---------- */

.feature-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 20px;
    height: 125px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
    transition: 0.2s;
}

.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(15,23,42,0.09);
}

.feature-icon {
    font-size: 25px;
}

.feature-title {
    font-weight: 700;
    margin-top: 8px;
}

.feature-text {
    color: #64748b;
    font-size: 13px;
}

/* ---------- Chat messages ---------- */

[data-testid="stChatMessage"] {
    border-radius: 18px;
    margin-bottom: 12px;
}

/* ---------- Input ---------- */

[data-testid="stChatInput"] {
    border-radius: 18px;
}

/* ---------- Buttons ---------- */

.stButton > button {
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    background: white;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #6366f1;
    color: #4f46e5;
}

/* ---------- Footer ---------- */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <span class="brand-icon">✦</span>
        NexaAI
    </div>
    <div class="tagline">
        Ask naturally. Get intelligent answers.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    if st.button("＋  New Chat", use_container_width=True):

        st.session_state.messages = []
        st.rerun()

    st.markdown("### 🕘 Recent Chats")

    if st.session_state.chat_history:

        for chat in st.session_state.chat_history[-5:]:
            st.caption("• " + chat)

    else:
        st.caption("Your conversations will appear here.")

    st.divider()

    st.markdown("### ⚙️ Settings")

    dark_mode = st.toggle("🌙 Dark mode")

    st.divider()

    st.caption("NexaAI v1.0")
    st.caption("AI-powered conversational assistant")


# =========================================================
# TOP BAR
# =========================================================

top1, top2 = st.columns([8, 1])

with top1:
    st.markdown(
        "**✦ NexaAI**  ·  Intelligent AI Assistant"
    )

with top2:
    st.markdown("🔒")


# =========================================================
# WELCOME SCREEN
# =========================================================

if not st.session_state.messages:

    st.markdown("""
    <div class="hero">

        <div class="hero-icon">✦</div>

        <div class="hero-title">
            What can I help you with?
        </div>

        <div class="hero-subtitle">
            Ask questions, learn concepts, generate ideas,
            or find information.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">Ask Anything</div>
            <div class="feature-text">
                Get clear answers to your questions.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Try: Explain AI",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "Explain artificial intelligence in simple words."
            )

    with c2:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Learn</div>
            <div class="feature-text">
                Understand difficult topics easily.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Try: Teach me Python",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "Teach me Python programming from the beginning."
            )

    with c3:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Create</div>
            <div class="feature-text">
                Generate ideas, plans and content.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Try: Give me an idea",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "Give me an innovative project idea."
            )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar="👤" if message["role"] == "user" else "✦"
    ):
        st.markdown(message["content"])


# =========================================================
# USER INPUT
# =========================================================

question = st.chat_input(
    "Ask NexaAI anything..."
)


if "pending_question" in st.session_state:

    question = st.session_state.pending_question

    del st.session_state.pending_question


# =========================================================
# AI RESPONSE
# =========================================================

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(question)

    with st.chat_message("assistant", avatar="✦"):

        if not client:

            answer = """
### ⚠️ AI service not connected

Please add your API key to the `.env` file:

`OPENAI_API_KEY=your_api_key_here`

Then restart the application.
"""

            st.markdown(answer)

        else:

            try:

                with st.spinner("Thinking..."):

                    response = client.chat.completions.create(

                        model="gpt-4o-mini",

                        messages=[
                            {
                                "role": "system",
                                "content": """
You are NexaAI, a helpful, intelligent,
friendly and accurate AI assistant.

Give clear and useful answers.

Use simple language when possible.

For complex questions, organize the
answer using headings and bullet points.

Never intentionally provide false information.
"""
                            }
                        ] +
                        st.session_state.messages,

                        temperature=0.4
                    )

                answer = response.choices[0].message.content

                st.markdown(answer)

                st.caption("✦ Generated by NexaAI")

            except Exception as e:

                answer = (
                    "Sorry, I couldn't process that request. "
                    "Please check your API configuration."
                )

                st.error(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.session_state.chat_history.append(
        question[:45]
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    ✦ NexaAI &nbsp; • &nbsp;
    Ask Naturally. Get Intelligent Answers.
</div>
""", unsafe_allow_html=True)
