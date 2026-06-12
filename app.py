import streamlit as st
import time
from dotenv import load_dotenv

load_dotenv()

# Page config 
st.set_page_config(
    page_title="InsightLens: Video Intelligence Agent",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS
st.markdown("""
<style>
/* ── Import fonts ── */

@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
                        
/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #090C14 !important;
    color: #E8EAF0 !important;
    font-family: 'Inter', sans-serif;
}

[data-testid="stAppViewContainer"] > .main {
    background: #090C14 !important;
    padding-bottom: 4rem;
}

/* Hide default streamlit chrome */
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
[data-testid="stDecoration"] { display: none !important; }

/* ── Header ── */
.mm-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.1rem 0 0.1rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 2.5rem;
}
.mm-logo-ring {
    width: 54px; height: 54px;
    border-radius: 50%;
    background: conic-gradient(from 200deg, #5B6EF5, #A259FF, #5B6EF5);
    display: flex; align-items: center; justify-content: center;
    font-size: 24px;
    box-shadow: 0 0 22px rgba(91,110,245,0.45);
    flex-shrink: 0;
}
.mm-wordmark {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 800;
    font-size: 2.4rem;
    letter-spacing: -0.5px;
    color: #FFFFFF;
}
.mm-wordmark span { color: #7B8FF7; font-weight: 700;}
.mm-tagline {
    font-size: 0.78rem;
    color: #6B7280;
    font-weight: 400;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-left: auto;
}

/* ── Section label ── */
.mm-section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #7B8FF7;
    margin-bottom: 0.6rem;
}

/* ── Input card ── */
.mm-input-card {
    background: #10131F;
    border: 1px solid rgba(123,143,247,0.18);
    border-radius: 16px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.4rem;
    transition: border-color 0.25s;
}
.mm-input-card:hover { border-color: rgba(123,143,247,0.38); }

/* Style Streamlit inputs to match */
[data-testid="stTextInput"] input,
[data-testid="stSelectbox"] select {
    background: #181C2E !important;
    border: 1px solid rgba(123,143,247,0.25) !important;
    border-radius: 10px !important;
    color: #E8EAF0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.92rem !important;
    padding: 0.55rem 0.9rem !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stSelectbox"] select:focus {
    border-color: #7B8FF7 !important;
    box-shadow: 0 0 0 2px rgba(123,143,247,0.18) !important;
    outline: none !important;
}
[data-testid="stTextInput"] label,
[data-testid="stSelectbox"] label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    color: #9CA3AF !important;
    letter-spacing: 0.02em !important;
}

/* ── Primary button ── */
.stButton > button {
    background: linear-gradient(135deg, #5B6EF5 0%, #A259FF 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.6rem 2rem !important;
    text-transform: uppercase !important;
    transition: opacity 0.2s, transform 0.15s !important;
    box-shadow: 0 4px 18px rgba(91,110,245,0.35) !important;
    width: 100% !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Progress / spinner ── */
[data-testid="stSpinner"] { color: #7B8FF7 !important; }
.stProgress > div > div {
    background: linear-gradient(90deg, #5B6EF5, #A259FF) !important;
    border-radius: 99px !important;
}

/* ── Result cards ── */
.mm-result-card {
    background: #10131F;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1.5rem 1.7rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}
.mm-result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    border-radius: 14px 14px 0 0;
}
.mm-result-card.accent-blue::before  { background: linear-gradient(90deg,#5B6EF5,#7B8FF7); }
.mm-result-card.accent-purple::before { background: linear-gradient(90deg,#A259FF,#7B8FF7); }
.mm-result-card.accent-green::before  { background: linear-gradient(90deg,#34D399,#7B8FF7); }
.mm-result-card.accent-amber::before  { background: linear-gradient(90deg,#FBBF24,#A259FF); }
.mm-result-card.accent-pink::before   { background: linear-gradient(90deg,#F472B6,#A259FF); }

.mm-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #6B7280;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.mm-card-title .icon { font-size: 0.95rem; }

.mm-title-display {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.3;
    letter-spacing: -0.3px;
}

.mm-body-text {
    font-family: 'Inter', sans-serif;
    font-size: 0.91rem;
    color: #C4C9D8;
    line-height: 1.75;
}

/* ── Transcript box ── */
.mm-transcript {
    background: #0C0F1A;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #8892B0;
    line-height: 1.8;
    max-height: 240px;
    overflow-y: auto;
}
.mm-transcript::-webkit-scrollbar { width: 4px; }
.mm-transcript::-webkit-scrollbar-track { background: transparent; }
.mm-transcript::-webkit-scrollbar-thumb {
    background: rgba(123,143,247,0.3);
    border-radius: 99px;
}

/* ── Chat ── */
.mm-chat-container {
    background: #10131F;
    border: 1px solid rgba(123,143,247,0.18);
    border-radius: 16px;
    padding: 1.5rem 1.7rem;
    margin-top: 1.4rem;
}
.mm-chat-header {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #7B8FF7;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.mm-chat-bubble-user {
    background: rgba(91,110,245,0.15);
    border: 1px solid rgba(91,110,245,0.25);
    border-radius: 12px 12px 4px 12px;
    padding: 0.75rem 1rem;
    margin: 0.5rem 0;
    font-size: 0.88rem;
    color: #C9D0F0;
    text-align: right;
}
.mm-chat-bubble-ai {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px 12px 12px 4px;
    padding: 0.75rem 1rem;
    margin: 0.5rem 0;
    font-size: 0.88rem;
    color: #C4C9D8;
    line-height: 1.7;
}
.mm-chat-bubble-ai .ai-tag {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7B8FF7;
    margin-bottom: 0.35rem;
    display: block;
}

/* ── Pipeline steps ── */
.mm-pipeline-step {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.55rem 0;
    font-size: 0.85rem;
    color: #6B7280;
    transition: color 0.3s;
}
.mm-pipeline-step.done { color: #34D399; }
.mm-pipeline-step.active { color: #7B8FF7; }
.mm-step-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: currentColor;
    flex-shrink: 0;
}
.mm-step-dot.pulse {
    animation: pulse 1s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.7); }
}

/* ── Metric chips ── */
.mm-chips {
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
    margin-top: 0.6rem;
}
.mm-chip {
    background: rgba(123,143,247,0.1);
    border: 1px solid rgba(123,143,247,0.22);
    border-radius: 99px;
    padding: 0.28rem 0.85rem;
    font-size: 0.74rem;
    font-weight: 500;
    color: #9BAAF5;
    font-family: 'Inter', sans-serif;
}

/* ── Divider ── */
.mm-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(123,143,247,0.2), transparent);
    margin: 2rem 0;
}

/* ── Empty state ── */
.mm-empty {
    text-align: center;
    padding: 4rem 2rem;
    color: #FFFFFF;;
}
.mm-empty .big-icon { font-size: 3rem; margin-bottom: 1rem; }
.mm-empty p { font-size: 0.88rem; max-width: 360px; margin: 0 auto; line-height: 1.7; }

/* Fix stChatInput and chat message styling */
[data-testid="stChatInput"] {
    background: #181C2E !important;
    border: 1px solid rgba(123,143,247,0.25) !important;
    border-radius: 12px !important;
}
[data-testid="stChatInput"] textarea {
    background: transparent !important;
    color: #E8EAF0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
}
[data-testid="stChatMessage"] {
    background: transparent !important;
}

/* Fix tabs */
[data-testid="stTabs"] [data-testid="stTab"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #7B8FF7 !important;
    border-bottom-color: #7B8FF7 !important;
}

/* Columns gap tweak */
[data-testid="stColumns"] { gap: 1.2rem; }
</style>
""", unsafe_allow_html=True)


# Session state
if "result" not in st.session_state:
    st.session_state.result = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "processing" not in st.session_state:
    st.session_state.processing = False


# Header
st.markdown("""
<div class="mm-header">
  <div class="mm-logo-ring">🎙️</div>
  <div>
    <div class="mm-wordmark">InsightLens:<span> AI-Powered Video Intelligence Agent with RAG</span></div>
  </div>
  <div class="mm-tagline">Video Intelligence System</div>
</div>
""", unsafe_allow_html=True)


# Input section
st.markdown('<div class="mm-section-label">Process a video or meeting</div>', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        source = st.text_input(
            "YouTube URL or local file path",
            placeholder="https://youtu.be/... or /path/to/recording.mp4",
            label_visibility="visible",
        )
    with col2:
        language = st.selectbox(
            "Language",
            ["english", "hinglish"],
            index=0,
        )

run_clicked = st.button("⚡  Analyse Now", use_container_width=False)


# Pipeline execution
def run_pipeline_ui(source: str, language: str):
    from helpers.audio_extractor import process_input
    from visionRag.speech_transcriber import transcribe_all
    from visionRag.meeting_summarizer import summarize, generate_title
    from visionRag.transcript_analyzer import extract_action_items, extract_key_decisions, extract_questions
    from visionRag.rag_pipeline import build_rag_chain

    steps = [
        ("📥", "Downloading & processing audio"),
        ("🎙️", "Transcribing speech"),
        ("✍️", "Generating title"),
        ("📋", "Summarising content"),
        ("✅", "Extracting action items"),
        ("🔑", "Identifying key decisions"),
        ("❓", "Surfacing open questions"),
        ("🔗", "Building RAG knowledge base"),
    ]

    st.markdown('<div class="mm-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="mm-section-label">Processing pipeline</div>', unsafe_allow_html=True)

    step_slots = []
    for icon, label in steps:
        slot = st.empty()
        step_slots.append((slot, icon, label))

    def render_steps(active_idx):
        for i, (slot, icon, label) in enumerate(step_slots):
            if i < active_idx:
                slot.markdown(
                    f'<div class="mm-pipeline-step done"><div class="mm-step-dot"></div>✓ {icon} {label}</div>',
                    unsafe_allow_html=True,
                )
            elif i == active_idx:
                slot.markdown(
                    f'<div class="mm-pipeline-step active"><div class="mm-step-dot pulse"></div>{icon} {label} …</div>',
                    unsafe_allow_html=True,
                )
            else:
                slot.markdown(
                    f'<div class="mm-pipeline-step"><div class="mm-step-dot"></div>{icon} {label}</div>',
                    unsafe_allow_html=True,
                )

    progress = st.progress(0)

    render_steps(0)
    chunks = process_input(source)
    progress.progress(12)

    render_steps(1)
    transcript = transcribe_all(chunks, language)
    progress.progress(28)

    render_steps(2)
    title = generate_title(transcript)
    progress.progress(40)

    render_steps(3)
    summary = summarize(transcript)
    progress.progress(55)

    render_steps(4)
    action_items = extract_action_items(transcript)
    progress.progress(67)

    render_steps(5)
    decisions = extract_key_decisions(transcript)
    progress.progress(78)

    render_steps(6)
    questions = extract_questions(transcript)
    progress.progress(88)

    render_steps(7)
    rag_chain = build_rag_chain(transcript)
    progress.progress(100)

    for slot, icon, label in step_slots:
        slot.markdown(
            f'<div class="mm-pipeline-step done"><div class="mm-step-dot"></div>✓ {icon} {label}</div>',
            unsafe_allow_html=True,
        )

    time.sleep(0.3)
    progress.empty()

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": decisions,
        "open_questions": questions,
        "rag_chain": rag_chain,
    }


if run_clicked:
    if not source.strip():
        st.warning("Paste a YouTube URL or file path to get started.")
    else:
        st.session_state.chat_history = []
        st.session_state.result = None
        try:
            st.session_state.result = run_pipeline_ui(source.strip(), language)
        except Exception as e:
            st.error(f"Pipeline failed: {e}")


# Results
if st.session_state.result:
    r = st.session_state.result

    st.markdown('<div class="mm-divider"></div>', unsafe_allow_html=True)

    # Title card
    st.markdown(f"""
    <div class="mm-result-card accent-blue">
      <div class="mm-card-title"><span class="icon">📌</span>Meeting title</div>
      <div class="mm-title-display">{r["title"]}</div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs for the 4 analysis sections
    tab_summary, tab_actions, tab_decisions, tab_questions, tab_transcript = st.tabs([
        "📋  Summary",
        "✅  Action Items",
        "🔑  Decisions",
        "❓  Questions",
        "🗒️  Transcript",
    ])

    with tab_summary:
        st.markdown(f"""
        <div class="mm-result-card accent-purple" style="margin-top:1rem">
          <div class="mm-card-title"><span class="icon">📋</span>Summary</div>
          <div class="mm-body-text">{r["summary"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with tab_actions:
        st.markdown(f"""
        <div class="mm-result-card accent-green" style="margin-top:1rem">
          <div class="mm-card-title"><span class="icon">✅</span>Action items</div>
          <div class="mm-body-text">{r["action_items"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with tab_decisions:
        st.markdown(f"""
        <div class="mm-result-card accent-amber" style="margin-top:1rem">
          <div class="mm-card-title"><span class="icon">🔑</span>Key decisions</div>
          <div class="mm-body-text">{r["key_decisions"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with tab_questions:
        st.markdown(f"""
        <div class="mm-result-card accent-pink" style="margin-top:1rem">
          <div class="mm-card-title"><span class="icon">❓</span>Open questions</div>
          <div class="mm-body-text">{r["open_questions"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with tab_transcript:
        st.markdown("""
        <div style="margin-top:1rem">
          <div class="mm-section-label">Raw transcript</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f'<div class="mm-transcript">{r["transcript"]}</div>', unsafe_allow_html=True)
        st.download_button(
            "⬇  Download full transcript",
            data=r["transcript"],
            file_name="transcript.txt",
            mime="text/plain",
            use_container_width=True,
        )

    # RAG Chat
    st.markdown('<div class="mm-divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="mm-chat-container">
      <div class="mm-chat-header">
        <span>💬</span> Chat with your meeting
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Render existing history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

    # Input
    if user_q := st.chat_input("Ask anything about this meeting…"):
        st.session_state.chat_history.append({"role": "user", "content": user_q})
        with st.chat_message("user"):
            st.markdown(user_q)

        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                from visionRag.rag_pipeline import ask_question
                answer = ask_question(r["rag_chain"], user_q)
            st.markdown(answer)
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

else:
    # Empty state
    if not run_clicked:
        st.markdown("""
        <div class="mm-empty">
          <div class="big-icon">🎙️</div>
          <p>Paste a YouTube link or a local file path above, pick a language, and hit <strong>Analyse Now</strong>. InsightLens will transcribe, summarise, and let you chat with your meeting.</p>
        </div>
        """, unsafe_allow_html=True)