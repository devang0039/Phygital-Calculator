import streamlit as st

# Page config
st.set_page_config(page_title="NeuMoney Calculator", layout="wide")

# Title + subheader
st.title("NeuMoney Calculator")
st.subheader(
    "Fast, agent-friendly access to common home-loan and insurance calculators. "
    "External links open in a new tab — always confirm results on the provider site before advising customers."
)

st.markdown("---")

# Helper to render a clickable tile
def calculator_tile(title, description, url, badge=None, aria=None):
    aria_attr = f'aria-label="{aria}"' if aria else ""
    tile_html = f"""
    <a class="tile-link" href="{url}" target="_blank" rel="noopener noreferrer" {aria_attr}>
      <div class="tile" role="group">
        <div class="tile-inner">
          <div class="tile-row">
            <div class="tile-texts">
              <h3>{title}</h3>
              <p class="desc">{description}</p>
            </div>
            <div class="tile-badge">{f'<span class="badge">{badge}</span>' if badge else ''}</div>
          </div>
          <div class="cta-row">
            <span class="cta">Open calculator</span>
          </div>
        </div>
      </div>
    </a>
    """
    st.markdown(tile_html, unsafe_allow_html=True)


# Mobile-first CSS
st.markdown(
    """
    <style>
    .stApp { padding: 12px 12px 30px 12px; font-family: Inter, Roboto, Arial, sans-serif; }

    .tile-link { text-decoration: none; color: inherit; display: block; }

    .tile {
      background: #ffffff;
      border-radius: 12px;
      padding: 12px;
      box-shadow: 0 8px 20px rgba(15,20,30,0.06);
      transition: transform .12s ease, box-shadow .12s ease;
      -webkit-tap-highlight-color: transparent;
    }
    .tile:active { transform: translateY(1px); }
    .tile:hover { box-shadow: 0 12px 30px rgba(15,20,30,0.08); }

    .tile-inner h3 { margin: 0 0 6px 0; font-size: 16px; line-height: 1.2; }
    .desc { margin: 0; color: #495057; font-size: 13.5px; opacity: 0.95; }

    .tile-row { display:flex; align-items:flex-start; gap:10px; justify-content:space-between; }
    .tile-texts { flex: 1 1 auto; padding-right: 8px; }
    .tile-badge { flex: 0 0 auto; display:flex; align-items:center; justify-content:flex-end; }

    .badge {
      background: #eef6ff;
      color: #0553d7;
      padding: 6px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 600;
      white-space: nowrap;
    }

    .cta-row { margin-top: 12px; display:flex; justify-content:flex-end; }
    .cta {
      display: inline-block;
      font-weight: 700;
      font-size: 14px;
      padding: 10px 14px;
      border-radius: 10px;
      background: #0F62FE;
      color: #ffffff;
      text-decoration: none;
      box-shadow: 0 6px 18px rgba(15,98,254,0.18);
      -webkit-tap-highlight-color: transparent;
    }

    @media (max-width: 420px) {
      .cta-row { justify-content: center; }
      .cta { display: block; width: 100%; text-align: center; padding: 12px; font-size: 15px; }
    }

    .tile-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 6px; }
    @media (max-width: 700px) {
      .tile-grid { grid-template-columns: 1fr; }
    }

    .section-title { margin: 8px 0 6px; font-size: 18px; font-weight: 700; }
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
# Section: Home Loan
# ---------------------
st.markdown("<div class='section-title'>🏠 Home Loan</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)

home_items = [
    {
        "title": "Eligibility calculator",
        "description": "Estimate whether a customer qualifies for a home loan based on income, obligations and tenure.",
        "url": HOME_ELIGIBILITY,
        "badge": "Bajaj Housing",
        "aria": "Open Home Loan Eligibility Calculator — Bajaj Housing",
    },
    {
        "title": "EMI Calculator",
        "description": "Calculate the monthly EMI for a specified loan amount, interest rate, and tenure.",
        "url": HOME_EMI,
        "badge": "Bajaj Housing",
        "aria": "Open Home Loan EMI Calculator — Bajaj Housing",
    },
    {
        "title": "Home Loan Balance Transfer",
        "description": "Compare savings from transferring your home loan to another lender.",
        "url": HOME_BALANCE_TRANSFER,
        "badge": "Bajaj Housing",
        "aria": "Open Home Loan Balance Transfer Calculator — Bajaj Housing",
    },
]

for it in home_items:
    calculator_tile(it['title'], it['description'], it['url'], badge=it['badge'], aria=it['aria'])

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------
# Section: Insurance
# ---------------------
st.markdown("<div class='section-title'>🛡️ Insurance</div>", unsafe_allow_html=True)
st.markdown("<div class='tile-grid'>", unsafe_allow_html=True)

ins_items = [
    {
        "title": "SSIP (Compound interest)",
        "description": "Estimate projected returns under a compounding savings plan (SSIP).",
        "url": SSIP,
        "badge": "Tata AIA",
        "aria": "Open SSIP Compound Interest Calculator — Tata AIA",
    },
    {
        "title": "SRP (Term Insurance Premium)",
        "description": "Estimate term insurance premium for desired cover, age and policy term.",
        "url": SRP,
        "badge": "Tata AIA",
        "aria": "Open Term Insurance Premium Calculator — Tata AIA",
    },
]

for it in ins_items:
    calculator_tile(it['title'], it['description'], it['url'], badge=it['badge'], aria=it['aria'])

st.markdown("</div>", unsafe_allow_html=True)
