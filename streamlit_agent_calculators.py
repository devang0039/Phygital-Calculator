import streamlit as st

st.set_page_config(page_title="NeuMoney Calculator", layout="wide")

# Header
header_html = (
    "<div style='text-align:center;margin-bottom:18px'>"
    "<h1 style='margin:0;font-size:26px'>NeuMoney Calculator</h1>"
    "<p style='color:#555;margin-top:8px;font-size:14px'>"
    "Fast, agent-friendly access to common home-loan and insurance calculators. "
    "External links open in a new tab — always confirm results on the provider site before advising customers."
    "</p></div>"
)
st.markdown(header_html, unsafe_allow_html=True)

# CSS (force CTA colour + clean style)
st.markdown(
    """
    <style>
    body, .stApp { font-family: Inter, Roboto, Arial, sans-serif; background:#f9fafc; color:#0f1724; }
    .section-title { font-size:18px; font-weight:700; margin:18px 0 10px; }
    .tile-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:14px; margin-bottom:18px; }
    @media (max-width:720px) { .tile-grid { grid-template-columns:1fr; } }
    .tile-link { text-decoration:none; color:inherit; }
    .tile {
      background:#fff; border-radius:12px; padding:20px; text-align:center; min-height:120px;
      display:flex; flex-direction:column; justify-content:center; gap:10px;
      box-shadow:0 6px 18px rgba(15,20,30,0.08);
    }
    .tile:hover { transform:translateY(-3px); box-shadow:0 12px 32px rgba(15,20,30,0.1); }
    .tile-icon { font-size:26px; }
    .tile-title { font-size:16px; font-weight:600; }
    .tile-cta {
      display:inline-block;
      background-color:#0F62FE !important;
      color:#ffffff !important;
      padding:8px 14px;
      border-radius:999px;
      font-weight:600;
      font-size:13px;
      box-shadow:0 6px 14px rgba(15,98,254,0.18);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Tile helper
def calculator_tile(title, url, emoji):
    html = f"""
    <a class='tile-link' href='{url}' target='_blank' rel='noopener noreferrer'>
      <div class='tile'>
        <div class='tile-icon'>{emoji}</div>
        <div class='tile-title'>{title}</div>
        <div class='tile-cta'>Open calculator</div>
      </div>
    </a>
    """
    st.markdown(html, unsafe_allow_html=True)

# Links
HOME_ELIGIBILITY = "https://www.bajajhousingfinance.in/calculators/home-loan-eligibility-calculator"
HOME_EMI = "https://www.bajajhousingfinance.in/calculators/home-loan-emi-calculator"
HOME_BALANCE_TRANSFER = "https://www.bajajhousingfinance.in/calculators/home-loan-balance-transfer-calculator"
SSIP = "https://www.tataaia.com/calculator/compound-interest-calculator.html"
SRP = "https://www.tataaia.com/calculator/term-insurance-calculator.html"

# Sections
st.markdown("<div class='section-title'>🏠 Home Loan</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)
calculator_tile("Eligibility calculator", HOME_ELIGIBILITY, "📋")
calculator_tile("EMI Calculator", HOME_EMI, "💳")
calculator_tile("Home Loan Balance Transfer", HOME_BALANCE_TRANSFER, "🔄")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🛡️ Insurance</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)
calculator_tile("SSIP", SSIP, "💰")
calculator_tile("SRP", SRP, "📝")
st.markdown("</div>", unsafe_allow_html=True)

# --- Hide Streamlit default UI elements (top bar, menu, footer) ---
st.markdown(
    """
    <style>
    /* Hide the entire top header (with 3 dots menu) */
    header {visibility: hidden;}

    /* Hide the three-dots menu if header still renders */
    #MainMenu {visibility: hidden;}

    /* Hide the Streamlit footer */
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

