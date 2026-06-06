import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="🎥",
    layout="centered"
)

# ── Theme Toggle ──────────────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

dark = st.session_state.dark_mode

# ── CSS ───────────────────────────────────────────────────
bg        = "#0E1117" if dark else "#F8F9FA"
card_bg   = "#1E2130" if dark else "#FFFFFF"
text      = "#FAFAFA" if dark else "#1A1A2E"
sub_text  = "#A0AEC0" if dark else "#6B7280"
accent    = "#FF4B4B"
border    = "#2D3748" if dark else "#E2E8F0"

st.markdown(f"""
<style>
    /* Page background */
    .stApp {{ background-color: {bg}; }}

    /* Hide default header */
    header[data-testid="stHeader"] {{ background: transparent; }}

    /* Hero card */
    .hero-card {{
        background: {card_bg};
        border: 1px solid {border};
        border-radius: 16px;
        padding: 2rem 2.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.15);
    }}

    /* Title */
    .hero-title {{
        font-size: 2.2rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 0.3rem;
    }}

    .hero-sub {{
        color: {sub_text};
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }}

    /* Input */
    .stTextInput > div > div > input {{
        background-color: {bg} !important;
        color: {text} !important;
        border: 1.5px solid {border} !important;
        border-radius: 10px !important;
        padding: 0.6rem 1rem !important;
        font-size: 15px !important;
    }}

    /* Button */
    .stButton > button {{
        background: {accent};
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.55rem 1.8rem;
        font-size: 15px;
        font-weight: 600;
        width: 100%;
        transition: opacity 0.2s;
    }}
    .stButton > button:hover {{ opacity: 0.85; }}

    /* Result card */
    .result-card {{
        background: {card_bg};
        border: 1px solid {border};
        border-radius: 16px;
        padding: 1.8rem 2rem;
        color: {text};
        line-height: 1.8;
        margin-top: 1rem;
    }}

    /* Footer */
    .footer {{
        text-align: center;
        padding: 1.5rem 0 0.5rem;
        color: {sub_text};
        font-size: 13px;
    }}
    .footer a {{
        color: {accent};
        text-decoration: none;
        font-weight: 500;
    }}
</style>
""", unsafe_allow_html=True)

# ── Header Row ────────────────────────────────────────────
col1, col2 = st.columns([8, 1])
with col1:
    st.markdown(f"<div class='hero-title'>🎥 YouTube Video Analyzer</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-sub'>Paste any YouTube link and get an instant AI-powered analysis.</div>", unsafe_allow_html=True)
with col2:
    st.button("🌙" if dark else "☀️", on_click=toggle_theme, help="Toggle theme")

# ── Agent ─────────────────────────────────────────────────
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# ── Input Card ────────────────────────────────────────────
#st.markdown(f"<div class='hero-card'>", unsafe_allow_html=True)
video_url = st.text_input("", placeholder="https://www.youtube.com/watch?v=...", label_visibility="collapsed")
analyze = st.button("🔍 Analyze Video")
st.markdown("</div>", unsafe_allow_html=True)

# ── Result ────────────────────────────────────────────────
if video_url and analyze:
    with st.spinner("Analyzing video..."):
        response = agent.run(f"Analyze this video: {video_url}")

    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.markdown("#### 📊 Analysis Report")
    st.markdown(response.content)
    st.markdown("</div>", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────
st.markdown(f"""
<footer style="
    text-align: center;
    padding: 15px;
    margin-top: 20px;
    border-top: 1px solid #ddd;
    color: #666;
    font-size: 14px;
">
    © 2026 YouTube Video Analyzer | Developed by Vivek Satish Patil
</footer>
""", unsafe_allow_html=True)