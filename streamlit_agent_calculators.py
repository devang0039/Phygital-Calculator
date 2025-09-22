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

# --- Styles ---
css = """
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
  mar
