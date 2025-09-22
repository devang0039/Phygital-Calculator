import streamlit as st

# Page config
st.set_page_config(page_title="NeuMoney Calculator", layout="wide")

# --- Header ---
st.markdown(
    """
    <div class="page-header">
      <h1>NeuMoney Calculator</h1>
      <p class="subhead">
        Fast, agent-friendly access to common home-loan and insurance calculators. 
        External links open in a new tab — always confirm results on the provider site before advising customers.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Helper for tiles ---
def calculator_tile(title, url, emoji=""):
    tile_html = f"""
    <a class="tile-link" href="{url}" target="_blank" rel="noopener noreferrer">
      <div class="tile">
        <div class="tile-icon">{emoji}</div>
        <div class="tile-title">{title}</div>
        <div class="tile-cta">Open calculator</div>
      </div>
    </a>
    """
    st.markdown(tile_html, unsafe_allow_html=True)

# --- Styles (inline, triple quotes opened and closed properly) ---
st.markdown(
    """
    <style>
    body, .stApp {
      font-family: Inter, Roboto, Arial, sans-serif;
      background: #f9fafc;
      color: #0f1724;
    }

    .page-header {
      text-align: center;
      margin-bottom: 24px;
    }
    .page-header h1 {
      font-size: 28px;
      font-weight: 700;
      margin: 0;
    }
    .page-header .subhead {
      font-size: 14px;
      color: #555;
      margin-top: 8px;
    }

    .section-title {
      font-size: 20px;
      font-weight: 700;
      margin: 20px 0 12px;
    }

    .tile-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin-bottom: 20px;
    }
    @media (max-width: 720px) {
      .tile-grid { grid-template-columns: 1fr; }
    }

    .tile-link { text-decoration: none; color: inherit; }
    .tile {
      background: #fff;
      border-radius: 14px;
      padding: 20px;
      text-align: center;
      box-shadow: 0 6px 18px rgba(15,20,30,0.08);
      transition: transform .12s ease, box-shadow .12s ease;
      min-height: 140px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 12px;
    }
    .tile:hover { transform: translateY(-3px); box-shadow: 0 12px 32px rgba(15,20,30,0.1); }

    .tile-icon { font-size: 28px; }
    .tile-title { font-size: 16px; font-weight: 600; }
    .tile-cta {
      display: inline-block;
      background: #0F62FE;
      color: #fff;
      padding: 8px 16px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 6px 14px rgba(15,98,254,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- External links ---
HOME_ELIGIBILITY = "https://www.bajajhousingfinance.in/calculators/home-loan-eligibility-calculator"
HOME_EMI = "https://www.bajajhousingfinance.in/calculators/home-loan-emi-calculator"
HOME_BALANCE_TRANSFER = "https://www.bajajhousingfinance.in/calculators/home-loan-balance-transfer-calculator"

SSIP = "https://www.tataaia.com/calculator/compound-interest-calculator.html"
SRP = "https://www.tataaia.com/calculator/term-insurance-calculator.html"

# --- Sections ---
st.markdown("<div class='section-title'>🏠 Home Loan</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)
calculator_tile("Eligibility calculator", HOME_ELIGIBILITY, emoji="📋")
calculator_tile("EMI Calculator", HOME_EMI, emoji="💳")
calculator_tile("Home Loan Balance Transfer", HOME_BALANCE_TRANSFER, emoji="🔄")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🛡️ Insurance</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)
calculator_tile("SSIP (Compound interest)", SSIP, emoji="💰")
calculator_tile("SRP (Term Insurance Premium)", SRP, emoji="📝")
st.markdown("</div>", unsafe_allow_html=True)
