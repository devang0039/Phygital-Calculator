import streamlit as st

# Page config
st.set_page_config(page_title="NeuMoney Calculator", layout="wide")

# Page header
st.title("NeuMoney Calculator")
st.subheader(
    "Fast, agent-friendly access to common home-loan and insurance calculators. "
    "External links open in a new tab — always confirm results on the provider site before advising customers."
)

st.markdown("---")

# Helper: simple tile with title + CTA only (no badge, no subtitle)
def calculator_tile(title, url, aria=None, emoji=""):
    aria_attr = f'aria-label="{aria}"' if aria else ""
    tile_html = f"""
    <a class="tile-link" href="{url}" target="_blank" rel="noopener noreferrer" {aria_attr}>
      <div class="tile" role="group">
        <div class="tile-body">
          <div class="tile-title">{emoji} {title}</div>
          <div class="tile-cta-row">
            <span class="cta">Open calculator</span>
          </div>
        </div>
      </div>
    </a>
    """
    st.markdown(tile_html, unsafe_allow_html=True)


# Clean, modern styles — tiles side-by-side and centered content
st.markdown(
    """
    <style>
    .stApp { padding: 14px 14px 36px 14px; font-family: Inter, Roboto, Arial, sans-serif; }

    /* Remove link default styles */
    .tile-link { text-decoration: none; color: inherit; display: block; }

    /* Tile card */
    .tile {
      background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
      border-radius: 14px;
      padding: 18px;
      box-shadow: 0 10px 30px rgba(14,20,40,0.06);
      transition: transform .12s ease, box-shadow .12s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      min-height: 120px;
    }
    .tile:hover { transform: translateY(-4px); box-shadow: 0 18px 44px rgba(14,20,40,0.09); }

    .tile-body { width:100%; display:flex; flex-direction:column; gap:12px; align-items:center; }

    .tile-title {
      font-size: 18px;
      font-weight: 700;
      line-height: 1.15;
      color: #0f1724;
      padding: 0 6px;
    }

    .tile-cta-row { width:100%; display:flex; justify-content:center; }
    .cta {
      background: #0F62FE;
      color: #ffffff;
      padding: 10px 18px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 14px;
      box-shadow: 0 8px 20px rgba(15,98,254,0.16);
    }
    .cta:active { transform: translateY(1px); }

    /* Grid: side-by-side tiles — 2 columns on tablet/desktop */
    .tile-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 12px; align-items:stretch; }
    @media (max-width: 720px) {
      .tile-grid { grid-template-columns: 1fr; }
      .tile { min-height: 100px; padding: 14px; }
    }

    /* Larger screens can show 2x2 visually balanced */
    @media (min-width: 1100px) {
      .tile-grid { grid-template-columns: repeat(2, 1fr); }
      .tile { min-height: 130px; }
    }

    /* Tighten header spacing */
    .stApp > header { margin-bottom: 6px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# External links
HOME_ELIGIBILITY = "https://www.bajajhousingfinance.in/calculators/home-loan-eligibility-calculator"
HOME_EMI = "https://www.bajajhousingfinance.in/calculators/home-loan-emi-calculator"
HOME_BALANCE_TRANSFER = "https://www.bajajhousingfinance.in/calculators/home-loan-balance-transfer-calculator"

SSIP = "https://www.tataaia.com/calculator/compound-interest-calculator.html"
SRP = "https://www.tataaia.com/calculator/term-insurance-calculator.html"

# ---------------------
# Home Loan section (2x2 grid)
# ---------------------
st.markdown("<div style='font-size:18px; font-weight:700; margin:8px 0 6px;'>🏠 Home Loan</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)

calculator_tile("Eligibility calculator", HOME_ELIGIBILITY, aria="Open Home Loan Eligibility Calculator — Bajaj Housing", emoji="🏷️")
calculator_tile("EMI Calculator", HOME_EMI, aria="Open Home Loan EMI Calculator — Bajaj Housing", emoji="📊")
calculator_tile("Home Loan Balance Transfer", HOME_BALANCE_TRANSFER, aria="Open Home Loan Balance Transfer Calculator — Bajaj Housing", emoji="🔁")
# optional placeholder removed — keep tiles to exact calculators

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------
# Insurance section (2x2 grid)
# ---------------------
st.markdown("<div style='font-size:18px; font-weight:700; margin:8px 0 6px;'>🛡️ Insurance</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)

calculator_tile("SSIP (Compound interest)", SSIP, aria="Open SSIP Compound Interest Calculator — Tata AIA", emoji="💰")
calculator_tile("SRP (Term Insurance Premium)", SRP, aria="Open Term Insurance Premium Calculator — Tata AIA", emoji="📝")
# if you later want more tiles, add here

st.markdown("</div>", unsafe_allow_html=True)
