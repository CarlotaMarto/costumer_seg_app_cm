import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGENS_DIR = BASE_DIR / "imagens"

def load_image_as_base64(path):
    if path.exists():
        with open(path, "rb") as img_file:
            data = base64.b64encode(img_file.read()).decode("utf-8")
            ext = path.suffix[1:].lower()
            if ext == "jpg":
                ext = "jpeg"
            return f"data:image/{ext};base64,{data}"
    return ""

INITIAL_BG_URI = load_image_as_base64(IMAGENS_DIR / "initial.png")
SEG_IMG_URI = load_image_as_base64(IMAGENS_DIR / "customer_segmentation_imagem.png")
GROCERY_BASKET_URI = load_image_as_base64(IMAGENS_DIR / "grocery_basket.jpg")
PRODUCT_GRID_URI = load_image_as_base64(IMAGENS_DIR / "product_grid.jpg")

ICON_INTRO_URI = load_image_as_base64(IMAGENS_DIR / "icon_intro.png")
ICON_ANALYSIS_URI = load_image_as_base64(IMAGENS_DIR / "icon_analysis.png")
ICON_PREPROCESS_URI = load_image_as_base64(IMAGENS_DIR / "icon_preprocess.png")
ICON_GEOGRAPHY_URI = load_image_as_base64(IMAGENS_DIR / "icon_geography.png")
ICON_CLUSTERING_URI = load_image_as_base64(IMAGENS_DIR / "icon_clustering.png")
BRAND_ICON_URI = load_image_as_base64(IMAGENS_DIR / "brand_icon.png")

SYMBOL_URIS = [load_image_as_base64(IMAGENS_DIR / f"symbol_{i}.png") for i in range(1, 8)]

st.set_page_config(page_title="Customer Segmentation Project", layout="wide")

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp, p, span, div, h1, h2, h3, h4, h5, h6, li, a, label, button, input {
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
}
h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, Cambria, "Times New Roman", Times, serif !important;
    font-weight: 700 !important;
}
html {
    background-color: #faf9f6 !important;
}
body {
    background-color: #faf9f6 !important;
    color: #1a1a1a;
}
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stMainContainer"], [data-testid="stAppViewBlockContainer"], main, .main, div.block-container {
    background: transparent !important;
    background-color: transparent !important;
    backdrop-filter: none !important;
}
section[role="main"] {
    padding-top: 60px !important;
}
header, header[role="banner"], div[data-testid="stToolbar"] {
    position: relative !important;
    width: 100% !important;
    z-index: 50 !important;
    background: rgba(255, 255, 255, 0.8) !important;
    backdrop-filter: blur(8px) !important;
    box-shadow: 0 1px 3px rgba(15,23,42,0.05) !important;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05) !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ea580c 0%, #f97316 100%) !important;
    min-width: 300px;
    max-width: 360px;
    position: relative;
    border-right: none !important;
}
button[title*="sidebar"], button[aria-label*="sidebar"], [data-testid="stSidebarCollapseButton"] {
    display: none !important;
}
.css-1d391kg {
    background-color: #f1f5f9;
}
.stButton>button {
    background-color: #000000 !important;
    color: white !important;
    border-radius: 999px !important;
    border: none !important;
    font-weight: 700 !important;
    padding: 10px 24px !important;
    transition: background-color 0.2s ease, transform 0.1s ease !important;
}
.stButton>button:hover {
    background-color: #1a1a1a !important;
    transform: translateY(-1px);
}
.st-bb {
    border-radius: 12px;
}
.stSidebarNav label {
    font-size: 14px;
    font-weight: 700;
    line-height: 1.3;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.7);
}
div[role="radiogroup"] label {
    font-size: 15px !important;
    font-weight: 600 !important;
    line-height: 1.3;
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: keep-all;
    letter-spacing: -0.01em;
}
.stAppViewContainer, .main > div, div.block-container {
    max-width: 100% !important;
    width: 100% !important;
}
div.block-container, [data-testid="stAppViewBlockContainer"] {
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    padding-top: 0 !important;
    background: transparent !important;
    background-color: transparent !important;
    box-shadow: none !important;
}
.stMarkdown, .stText, .css-1d391kg {
    color: #1a1a1a;
}
div[data-testid="stImage"] img {
    border-radius: 16px;
}
div[data-testid="stImage"] {
    border: 1px solid rgba(0, 0, 0, 0.05);
    padding: 8px;
    border-radius: 20px;
    background: #ffffff;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.01);
}
div[role="radiogroup"] label {
    background: #ffffff !important;
    padding: 12px 16px !important;
    border-radius: 12px !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    transition: all 0.2s ease !important;
}
div[role="radiogroup"] label:hover {
    background: #fcfbfa !important;
    border-color: #000000 !important;
}
.page-shell {
    background: #ffffff !important;
    border: 1px solid rgba(0, 0, 0, 0.05);
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.015);
    margin-bottom: 28px;
}
.page-title-box {
    display: block;
    width: 100%;
    background: transparent !important;
    color: #000000 !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    font-size: 28px;
    font-weight: 800;
    margin-top: 48px;
    margin-bottom: 24px;
    letter-spacing: -0.03em;
}
.page-text {
    color: #4a4a4a;
    line-height: 1.75;
    text-align: justify;
    font-size: 15px;
}
.page-next {
    margin-top: 32px;
    display: flex;
    justify-content: flex-end;
}
.page-next button {
    background: #ffffff !important;
    color: #000000 !important;
    border: 1px solid rgba(0, 0, 0, 0.08) !important;
    padding: 12px 24px !important;
    border-radius: 999px !important;
    font-weight: 700;
}

/* Sidebar Radio Navigation Override Styles */
[data-testid="stSidebar"] div[role="radiogroup"] {
    background-color: transparent !important;
    padding: 0 !important;
    gap: 0 !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label [role="presentation"],
[data-testid="stSidebar"] div[role="radiogroup"] label div[dir="ltr"] {
    display: none !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label {
    background-color: transparent !important;
    color: rgba(255, 255, 255, 0.8) !important;
    border: none !important;
    padding: 10px 16px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    line-height: 1.5 !important;
    border-radius: 12px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    margin-bottom: 6px !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    color: #ffffff !important;
    background-color: rgba(255, 255, 255, 0.1) !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input[type="radio"]:checked) {
    color: #ea580c !important;
    background-color: #ffffff !important;
    font-weight: 700 !important;
}

/* SVG icons for sidebar radio */
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(1)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(1):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(2)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(2):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(3)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(3):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(4)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(4):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(5)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(5):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(6)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(6):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(7)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="m9 12 2 2 4-4"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(7):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="m9 12 2 2 4-4"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(8)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(8):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>');
}

.communities-grid {
    display: grid;
    gap: 16px;
    grid-template-columns: repeat(7, 1fr);
    margin-top: 24px;
    margin-bottom: 32px;
}
@media (max-width: 1400px) {
    .communities-grid {
        grid-template-columns: repeat(4, 1fr);
    }
}
@media (max-width: 1000px) {
    .communities-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}
@media (max-width: 600px) {
    .communities-grid {
        grid-template-columns: 1fr;
    }
}

.community-card {
    background: #ffffff;
    border: 1px solid rgba(0, 0, 0, 0.05);
    border-radius: 16px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 360px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.015);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.community-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.03);
    border-color: rgba(0, 0, 0, 0.12);
}
.community-card-icon-container {
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
}
.community-card-icon {
    display: inline-block;
}
.community-card-title {
    font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
    font-size: 16px;
    font-weight: 700;
    margin: 0 0 12px 0 !important;
}
.community-card-value {
    font-size: 24px;
    font-weight: 800;
    color: #000000;
    margin-bottom: 2px;
}
.community-card-sub {
    font-size: 12px;
    color: #8c8c8c;
    margin-bottom: 12px;
}
.community-card-desc {
    font-size: 13px;
    color: #5f6368;
    line-height: 1.5;
    margin-bottom: 16px;
    flex-grow: 1;
}
.community-card-arrow {
    align-self: flex-end;
    font-size: 16px;
    font-weight: 700;
}

.metrics-row-grid {
    border-top: 1px solid rgba(0, 0, 0, 0.08);
    padding-top: 28px;
    margin-top: 40px;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 24px;
}
@media (max-width: 1000px) {
    .metrics-row-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .metrics-row-item {
        border-right: none !important;
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        padding-bottom: 16px;
    }
}
@media (max-width: 600px) {
    .metrics-row-grid {
        grid-template-columns: 1fr;
    }
}
/* Hide heading anchor/link icons */
.anchor-link, 
.header-anchor, 
[data-testid="stHeaderActionElements"],
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    display: none !important;
    visibility: hidden !important;
}

/* Restore Streamlit's native Material Icons */
.material-icons,
[class*="material-symbols"],
[data-testid="stIconMaterial"],
span[data-testid="stIconMaterial"] {
    font-family: 'Material Symbols Outlined', 'Material Symbols Rounded', 'Material Symbols Sharp', 'Material Icons' !important;
}
</style>
""".replace('{INITIAL_BG_URI}', INITIAL_BG_URI)

st.markdown(css, unsafe_allow_html=True)

SEGMENT_COLORS = {
    0: "#10b981",  # Vegetarians -> Emerald Green
    1: "#f97316",  # Regulars -> Orange
    2: "#0d9488",  # Wellness -> Teal
    3: "#ef4444",  # Promoters -> Red
    4: "#8b5cf6",  # Loyalists -> Purple
    5: "#3b82f6",  # Families -> Blue
    6: "#b45309",  # Economizers -> Amber/Brown
    7: "#ec4899"   # Techies -> Pink
}

st.sidebar.markdown(
    f"""
    <div style='padding: 12px 0 18px 0; font-family:"Plus Jakarta Sans", "Inter", sans-serif;'>
      <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 28px;'>
        <img src='{BRAND_ICON_URI}' style='width: 38px; height: 38px; object-fit: contain; border-radius: 8px;' />
        <div style='font-size: 22px; font-weight: 800; color: #ffffff; line-height: 1.1; font-family:"Playfair Display", serif;'>Customer Intelligence</div>
      </div>
      <div style='font-size:11px; text-transform:uppercase; letter-spacing:0.08em; color:rgba(255,255,255,0.7); margin-bottom:16px; font-weight:700;'>Section Index</div>
    </div>
    """,
    unsafe_allow_html=True,
)

selected_page = st.sidebar.radio(
    label="Index",
    options=[
        "Overview",
        "Data Analysis",
        "Data Preprocessing",
        "Data in Geography",
        "Customer Communities",
        "Targeter Promotion",
        "Conclusion & Recommendations",
        "Customer Simulator"
    ],
    key="sidebar_radio_selection",
    label_visibility="collapsed"
)

def render_footer():
    st.markdown(
        """
        <div style='margin-top: 60px; font-family:"Plus Jakarta Sans", "Inter", sans-serif;'>
          <hr style='border: 0; border-top: 1px solid rgba(0, 0, 0, 0.08); margin: 0 0 32px 0;' />
          <div style='max-width:1080px; margin: 0 auto; display:grid; grid-template-columns:repeat(4, minmax(180px, 1fr)); gap:24px; align-items:start;'>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.15em; color:#8c8c8c; margin-bottom:16px; font-weight:700;'>Navigation</div>
              <p style='color:#3b2720; margin:0; line-height:1.6; font-size:14px;'>Use the navigation bar on the left side of the screen.</p>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.15em; color:#8c8c8c; margin-bottom:16px; font-weight:700;'>Work done by</div>
              <div style='display:grid; gap:12px;'>
                <a href='https://github.com/CarlotaMarto' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#0f172a; cursor:pointer; padding:0;'>
                  <img src='https://github.com/CarlotaMarto.png' alt='Carlota Marto GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px; color:#3b2720;'>Carlota Marto</div>
                    <div style='font-size:12px; color:#8c8c8c;'>20241729</div>
                  </div>
                </a>
                <a href='https://github.com/Franciscaveigateixeira' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#0f172a; cursor:pointer; padding:0;'>
                  <img src='https://github.com/Franciscaveigateixeira.png' alt='Francisca Teixeira GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px; color:#3b2720;'>Francisca Teixeira</div>
                    <div style='font-size:12px; color:#8c8c8c;'>20241702</div>
                  </div>
                </a>
                <a href='https://github.com/Gouveia316' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#0f172a; cursor:pointer; padding:0;'>
                  <img src='https://github.com/Gouveia316.png' alt='Pedro GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px; color:#3b2720;'>Pedro Gouveia</div>
                    <div style='font-size:12px; color:#8c8c8c;'>20231657</div>
                  </div>
                </a>
              </div>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.15em; color:#8c8c8c; margin-bottom:16px; font-weight:700;'>Teacher</div>
              <div style='font-weight:700; color:#3b2720; margin-bottom:4px; font-size:14px;'>Ivo Bernardo</div>
              <div style='color:#8c8c8c; font-size:13px;'>Machine Learning II</div>
            </div>
            <div>
              <p style='color:#64748b; line-height:1.6; margin:0; font-size:14px; padding-top: 27px;'>This project is optimized for executive-level business intelligence and strategic decision making.</p>
            </div>
          </div>
          <div style='background-color: #000000; color: #ffffff; padding: 18px 32px; margin-top: 48px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; width: 100vw; position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; box-sizing: border-box;'>
            <span>&copy; 2026 Customer Segmentation Project - Academic Use Only</span>
            <span style='color: #a3a3a3;'>Built for Machine Learning II</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Page conditional routing
if selected_page == "Overview":
    # Render Mockup Top Banner
    st.markdown(f"""
    <div style='display: flex; justify-content: space-between; align-items: center; gap: 40px; margin-bottom: 48px; font-family: "Plus Jakarta Sans", "Inter", sans-serif;'>
        <div style='flex: 1.5;'>
            <h1 style='font-size: 48px; font-weight: 800; color: #000000; line-height: 1.1; margin: 0 0 24px 0; letter-spacing: -0.03em;'>Understand every customer. <br/>Grow with purpose.</h1>
            <p style='font-size: 16px; color: #5f6368; line-height: 1.6; margin: 0 0 32px 0; max-width: 540px;'>We turn data into human understanding so you can build stronger relationships, create relevant experiences and drive sustainable growth.</p>
        </div>
        <div style='flex: 0.8; display: flex; flex-direction: column; gap: 32px; padding-top: 12px;'>
            <div>
                <div style='font-size: 32px; font-weight: 800; color: #000000; line-height: 1;'>34,060</div>
                <div style='font-size: 13px; color: #5f6368; margin-top: 4px;'>customers analyzed</div>
            </div>
            <div>
                <div style='font-size: 32px; font-weight: 800; color: #000000; line-height: 1;'>7</div>
                <div style='font-size: 13px; color: #5f6368; margin-top: 4px;'>communities discovered</div>
            </div>
        </div>
        <div style='flex: 1.2; display: flex; justify-content: flex-end;'>
            <img src='{SEG_IMG_URI}' style='max-width: 100%; height: auto; border-radius: 16px; object-fit: contain;' />
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Explore your communities →", key="btn_explore"):
        st.session_state.sidebar_radio_selection = "Customer Communities"
        st.rerun()

    # Overview Section Header
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Overview</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>This introduction presents the customer segmentation project overview, combining initial analysis, data cleaning, and geographic insights. The goal is to show how each step contributes to a cleaner dataset, a stronger customer profile, and useful business segmentation.</p>
        <p>The report brings together exploratory analysis, preprocessing, and geographic investigation, with clear charts and maps that highlight real customer patterns.</p>
        <p>The left navigation takes you directly to each section, showing only the selected page.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Data Analysis":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Data Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='page-shell'>
      <div style='display: flex; gap: 32px; align-items: center;'>
        <div class='page-text' style='flex: 1.5;'>
          <p>This section presents the initial dataset analysis, based on the notebooks. It focuses on customer attributes, purchase behavior, and data quality before any segmentation.</p>
          <p>By analyzing spending categories, we can see that groceries represent the largest share of budget, followed by electronics and fresh produce. The visual analysis of grocery baskets highlights standard household stocking behavior.</p>
        </div>
        <div style='flex: 1; display: flex; justify-content: center;'>
          <img src='{GROCERY_BASKET_URI}' style='max-width: 100%; max-height: 180px; border-radius: 12px; border: 1px solid rgba(0, 0, 0, 0.05); box-shadow: 0 4px 12px rgba(0,0,0,0.01); object-fit: contain;' />
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    customer_info = pd.read_csv(BASE_DIR / "datasets" / "customer_info.csv")
    customer_basket = pd.read_csv(BASE_DIR / "datasets" / "customer_basket.csv")

    total_customers = len(customer_info)
    total_invoices = len(customer_basket)
    avg_promo = customer_info["percentage_of_products_bought_promotion"].mean() * 100
    median_products = customer_info["lifetime_total_distinct_products"].median()
    avg_groceries = customer_info["lifetime_spend_groceries"].mean()
    avg_electronics = customer_info["lifetime_spend_electronics"].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Customers", f"{total_customers:,}")
    col2.metric("Invoices", f"{total_invoices:,}")
    col3.metric("Median distinct products", f"{median_products:,}")
    col4.metric("Avg. promo share", f"{avg_promo:.1f}%")

    st.markdown("---")

    gender_counts = customer_info["customer_gender"].value_counts().reset_index()
    gender_counts.columns = ["customer_gender", "count"]
    gender_chart = alt.Chart(gender_counts).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color="#c2410c").encode(
        x=alt.X("customer_gender:N", title="Gender"),
        y=alt.Y("count:Q", title="Customers"),
        tooltip=["customer_gender", "count"]
    ).properties(height=320)

    promo_chart = alt.Chart(customer_info).mark_bar(color="#ea580c", opacity=0.8).encode(
        x=alt.X("percentage_of_products_bought_promotion:Q", bin=alt.Bin(maxbins=20), title="Promotion purchase ratio"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=320)

    spend_categories = customer_info[["lifetime_spend_groceries", "lifetime_spend_electronics", "lifetime_spend_vegetables", "lifetime_spend_nonalcohol_drinks"]].mean().reset_index()
    spend_categories.columns = ["category", "average_spend"]
    spend_categories["category"] = spend_categories["category"].str.replace("lifetime_spend_", "", regex=False).str.replace("_", " ")
    spend_chart = alt.Chart(spend_categories).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("category:N", title="Spend category", sort="-y"),
        y=alt.Y("average_spend:Q", title="Average spend"),
        color=alt.Color("category:N", legend=None, scale=alt.Scale(range=["#f97316", "#fb923c", "#f59e0b", "#facc15"])),
        tooltip=["category", alt.Tooltip("average_spend:Q", format=",.2f")]
    ).properties(height=360)

    st.subheader("Initial dataset profile")
    c1, c2 = st.columns(2)
    c1.subheader("Gender distribution")
    c1.altair_chart(gender_chart, width=520)
    c2.subheader("Promotion purchase ratio")
    c2.altair_chart(promo_chart, width=520)

    st.markdown("### Average spend per category")
    st.altair_chart(spend_chart, width=1080)

    st.markdown("""
        <div style='padding: 24px; border-radius: 16px; background: #fff4ed; border: 1px solid rgba(209,115,70,0.18);'>
          <h3 style='font-family:"Inter", sans-serif; color:#3b2720; margin-bottom:12px; font-weight:700; font-size:20px;'>Key insights from the initial dataset review</h3>
          <ul style='color:#5f4635; line-height:1.8; margin-left:18px; font-family:"Inter", sans-serif;'>
            <li>The dataset includes <strong>33,038 customers</strong> and <strong>100,000 purchase invoices</strong>, based on the raw customer profile and basket data.</li>
            <li>Gender balance is nearly even, which supports representative customer profiling.</li>
            <li>Average promotion-driven purchases are around <strong>32%</strong>, highlighting early signs of promotional sensitivity.</li>
            <li>Groceries are the largest spend category, followed by electronics, vegetables, and non-alcoholic drinks.</li>
            <li>This analysis is intentionally preliminary and reflects the data before applying any segmentation or clustering.</li>
          </ul>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Data Preprocessing":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Data Preprocessing</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='page-shell'>
      <div style='display: flex; gap: 32px; align-items: center;'>
        <div class='page-text' style='flex: 1.5;'>
          <p>This section describes the data cleaning and preparation process. It includes date corrections, negative value fixes, feature engineering, and outlier review.</p>
          <ul style='margin: 0; padding-left: 20px;'>
            <li style='margin-bottom: 8px;'>Future transaction years are set to <code>NaN</code> instead of dropping rows.</li>
            <li style='margin-bottom: 8px;'>Negative promotion percentage values are corrected and invalid identifiers are excluded.</li>
            <li style='margin-bottom: 8px;'>Customer names are processed to extract education-level titles while preserving privacy.</li>
            <li style='margin-bottom: 8px;'>Outliers and skewed spending patterns are inspected to prevent distortion in clustering.</li>
          </ul>
        </div>
        <div style='flex: 1; display: flex; justify-content: center;'>
          <img src='{PRODUCT_GRID_URI}' style='max-width: 100%; max-height: 180px; border-radius: 12px; border: 1px solid rgba(0, 0, 0, 0.05); box-shadow: 0 4px 12px rgba(0,0,0,0.01); object-fit: contain;' />
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    customer_info = pd.read_csv(BASE_DIR / "datasets" / "customer_info.csv")
    customer_info["customer_birthdate"] = pd.to_datetime(customer_info["customer_birthdate"], errors="coerce")
    customer_info["customer_age"] = 2024 - customer_info["customer_birthdate"].dt.year
    customer_info["promo_ratio"] = customer_info["percentage_of_products_bought_promotion"] * 100
    customer_clean = customer_info.dropna(subset=["customer_age", "promo_ratio"])

    age_chart = alt.Chart(customer_clean).mark_bar(color="#c2410c", opacity=0.85).encode(
        x=alt.X("customer_age:Q", bin=alt.Bin(maxbins=20), title="Age"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")],
    ).properties(height=320)

    promo_chart = alt.Chart(customer_clean).mark_bar(color="#ea580c", opacity=0.85).encode(
        x=alt.X("promo_ratio:Q", bin=alt.Bin(maxbins=20), title="Promotion ratio (%)"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")],
    ).properties(height=320)

    box_chart = alt.Chart(customer_clean).mark_boxplot().encode(
        y=alt.Y("lifetime_total_distinct_products:Q", title="Distinct products"),
        tooltip=[alt.Tooltip("lifetime_total_distinct_products:Q", title="Distinct products")],
    ).properties(height=320)

    st.subheader("Preprocessing visuals")
    c1, c2 = st.columns(2)
    c1.markdown("#### Age distribution")
    c1.altair_chart(age_chart, width=520)
    c2.markdown("#### Promotion purchase ratio")
    c2.altair_chart(promo_chart, width=520)

    st.markdown("### Distinct products after cleaning")
    st.altair_chart(box_chart, width=1080)

    st.markdown("""
        <div style='padding: 24px; border-radius: 16px; background: #fff4ed; border: 1px solid rgba(209,115,70,0.18);'>
          <h3 style='font-family:"Inter", sans-serif; color:#3b2720; margin-bottom:12px; font-weight:700; font-size:20px;'>Preprocessing conclusions</h3>
          <ul style='color:#5f4635; line-height:1.8; margin-left:18px; font-family:"Inter", sans-serif;'>
            <li>The data was cleaned while preserving the customer base, applying only logical corrections without abrupt removals.</li>
            <li>Spending and promotion variables remain skewed but are now consistent for modeling.</li>
            <li>Age and promotion fields were prepared to support segmentation and campaign analytics.</li>
            <li>The final dataset was exported unscaled for use in the next segmentation steps.</li>
          </ul>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Data in Geography":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Data In Geography</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class='page-shell'>
          <div class='page-text'>
            <p>This section shows how customers are distributed geographically and which areas have the highest purchase density. Before the maps, we describe the regional pattern to understand whether the customer base is concentrated in urban centers, campus areas, or high-activity commercial corridors.</p>
            <p>The geographic data reveals a core cluster of customers around the main urban axis and potential hotspots with stronger promotional purchase intensity and distinct product behavior. This explanation prepares the map reading and helps interpret density patterns and local behavior.</p>
          </div>
        </div>
    """, unsafe_allow_html=True)

    customer_info = pd.read_csv(BASE_DIR / "datasets" / "customer_info.csv")
    customer_info = customer_info.dropna(subset=["latitude", "longitude"]).copy()
    customer_info["promo_ratio"] = customer_info["percentage_of_products_bought_promotion"] * 100
    customer_info["size_spend"] = customer_info["lifetime_total_distinct_products"].fillna(0) / 50

    st.subheader("Customer geographic distribution")
    scatter_map = px.scatter_mapbox(
        customer_info,
        lat="latitude",
        lon="longitude",
        color="promo_ratio",
        size="size_spend",
        size_max=8,
        zoom=9,
        mapbox_style="open-street-map",
        color_continuous_scale="OrRd",
        hover_data={"customer_gender":True, "promo_ratio":True, "lifetime_total_distinct_products":True},
    )
    scatter_map.update_layout(margin=dict(l=0, r=0, t=0, b=0), coloraxis_colorbar=dict(title="Promo %"))
    st.plotly_chart(scatter_map, width=1080, config={"scrollZoom": True})

    st.subheader("Customer density map")
    density_map = px.density_mapbox(
        customer_info,
        lat="latitude",
        lon="longitude",
        radius=15,
        zoom=9,
        mapbox_style="open-street-map",
        color_continuous_scale="YlOrRd",
        hover_data={"promo_ratio":True},
    )
    density_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(density_map, width=1080, config={"scrollZoom": True})

    customer_info["lat_bin"] = (customer_info["latitude"] * 20).round(0) / 20
    customer_info["lon_bin"] = (customer_info["longitude"] * 20).round(0) / 20
    grid = customer_info.groupby(["lat_bin", "lon_bin"]).size().reset_index(name="count")
    hotspot = grid.sort_values("count", ascending=False).head(1).iloc[0]
    hotspot_customers = customer_info[(customer_info.lat_bin == hotspot.lat_bin) & (customer_info.lon_bin == hotspot.lon_bin)]
    outside_customers = customer_info[~((customer_info.lat_bin == hotspot.lat_bin) & (customer_info.lon_bin == hotspot.lon_bin))]
    hotspot_summary = pd.DataFrame({
        "metric": ["Promo ratio", "Distinct products", "Stores visited"],
        "Hotspot": [
            hotspot_customers["promo_ratio"].mean(),
            hotspot_customers["lifetime_total_distinct_products"].mean(),
            hotspot_customers["distinct_stores_visited"].mean(),
        ],
        "Outside": [
            outside_customers["promo_ratio"].mean(),
            outside_customers["lifetime_total_distinct_products"].mean(),
            outside_customers["distinct_stores_visited"].mean(),
        ],
    })
    hotspot_compare = hotspot_summary.melt(id_vars=["metric"], var_name="group", value_name="value")

    compare_chart = alt.Chart(hotspot_compare).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("metric:N", title="Metric"),
        y=alt.Y("value:Q", title="Value"),
        color=alt.Color("group:N", title="Group", scale=alt.Scale(range=["#c2410c", "#f97316"])),
        column=alt.Column("metric:N", header=alt.Header(labelAngle=0, labelAlign="left", title=""))
    ).properties(height=260)

    st.subheader("Hotspot profile vs outside")
    st.altair_chart(compare_chart, width=1080)

    st.markdown("""
        <div style='padding: 24px; border-radius: 16px; background: #fff4ed; border: 1px solid rgba(209,115,70,0.18);'>
          <h3 style='font-family:"Inter", sans-serif; color:#3b2720; margin-bottom:12px; font-weight:700; font-size:20px;'>Geography conclusions</h3>
          <ul style='color:#5f4635; line-height:1.8; margin-left:18px; font-family:"Inter", sans-serif;'>
            <li>The scatter map shows the customer base concentrated along the main urban corridor.</li>
            <li>The density map highlights a high-concentration cluster near a university area.</li>
            <li>Hotspot customers are more likely to make promotional purchases and visit more distinct stores.</li>
            <li>These geographic signals can support local segmentation and regional campaign decisions.</li>
          </ul>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Customer Communities":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Customer Communities</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>Using K-Means clustering, our customer base was segmented into 8 distinct customer communities. The grid below profiles the official business personas discovered during Notebook 4's characterization exercise. Use the cluster explorer dropdown below the grid to inspect spend distributions per category.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    try:
        seg_summary = pd.read_csv(BASE_DIR / "datasets" / "segment_summary.csv")
        seg_meta_grid = {
            0: {"name": "Vegetarians", "desc": "Full-price, promotion-resistant shoppers. Lead with curation/quality framing rather than discounts.", "icon_idx": 0},
            1: {"name": "Regulars", "desc": "Active but newer, deal-aware shoppers. Strong targets for onboarding to the loyalty program.", "icon_idx": 1},
            2: {"name": "Wellness", "desc": "Quiet, low-maintenance, and low-complaint shoppers. Exert low friction and buy full price.", "icon_idx": 2},
            3: {"name": "Promoters", "desc": "The ultimate deal-seekers (+145% promo share). Perfect for price-led campaign stacking.", "icon_idx": 3},
            4: {"name": "Loyalists", "desc": "Highest LTV, highest tenure (13.6 years), and highest loyalty flag adoption (76.8%). Reward and protect.", "icon_idx": 4},
            5: {"name": "Families", "desc": "Large households (avg. 5.41 kids). Loyal without needing promotions. Target with bulk-buying bundles.", "icon_idx": 5},
            6: {"name": "Economizers", "desc": "Restrained, low-friction spenders who buy at baseline. NOT deal-chasers; value baseline pricing.", "icon_idx": 6},
            7: {"name": "Techies", "desc": "Small households buying high-value tech. Cleanest electronics and audio cross-sell campaign audience.", "icon_idx": 7}
        }
        
        cards_list_html = []
        for idx, row in seg_summary.iterrows():
            c_id = int(row['cluster'])
            share = row['share_%']
            custs = int(row['customers'])
            meta = seg_meta_grid.get(c_id, {"name": f"Cluster {c_id}", "desc": "No description available.", "icon_idx": 0})
            card_color = SEGMENT_COLORS.get(c_id, "#ea580c")
            symbol_uri = SYMBOL_URIS[meta['icon_idx'] % len(SYMBOL_URIS)]
            
            card_html = f"""
            <div class='community-card'>
              <div class='community-card-icon-container'>
                <div class='community-card-icon' style='
                  width: 80px;
                  height: 80px;
                  background-color: {card_color};
                  -webkit-mask: url("{symbol_uri}") no-repeat center / contain;
                  mask: url("{symbol_uri}") no-repeat center / contain;
                '></div>
              </div>
              <div>
                <h3 class='community-card-title' style='color: {card_color};'>{meta['name']}</h3>
                <div class='community-card-value'>{share:.1f}%</div>
                <div class='community-card-sub'>{custs:,} customers</div>
                <div class='community-card-desc'>{meta['desc']}</div>
              </div>
              <div class='community-card-arrow' style='color: {card_color};'>→</div>
            </div>
            """
            cards_list_html.append(card_html)
            
        cards_html = f"<div class='communities-grid'>{''.join(cards_list_html)}</div>"
        st.markdown(cards_html, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading segment summary: {e}")

    metrics_html = """
    <div class='metrics-row-grid'>
      <div class='metrics-row-item' style='border-right: 1px solid rgba(0, 0, 0, 0.08); padding-right: 16px;'>
        <div style='font-size: 12px; color: #5f6368; margin-bottom: 8px;'>Revenue contribution</div>
        <div style='display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px;'>
          <span style='font-size: 24px; font-weight: 800; color: #000000;'>€2.48M</span>
          <span style='font-size: 12px; font-weight: 700; color: #10b981;'>↑ 18.7%</span>
        </div>
        <div style='font-size: 11px; color: #8c8c8c;'>vs Apr 1 - Apr 30</div>
      </div>
      <div class='metrics-row-item' style='border-right: 1px solid rgba(0, 0, 0, 0.08); padding-right: 16px; padding-left: 8px;'>
        <div style='font-size: 12px; color: #5f6368; margin-bottom: 8px;'>Avg. order value</div>
        <div style='display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px;'>
          <span style='font-size: 24px; font-weight: 800; color: #000000;'>€68.21</span>
          <span style='font-size: 12px; font-weight: 700; color: #10b981;'>↑ 8.3%</span>
        </div>
        <div style='font-size: 11px; color: #8c8c8c;'>vs Apr 1 - Apr 30</div>
      </div>
      <div class='metrics-row-item' style='border-right: 1px solid rgba(0, 0, 0, 0.08); padding-right: 16px; padding-left: 8px;'>
        <div style='font-size: 12px; color: #5f6368; margin-bottom: 8px;'>Repeat purchase rate</div>
        <div style='display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px;'>
          <span style='font-size: 24px; font-weight: 800; color: #000000;'>78%</span>
          <span style='font-size: 12px; font-weight: 700; color: #10b981;'>↑ 5.4%</span>
        </div>
        <div style='font-size: 11px; color: #8c8c8c;'>vs Apr 1 - Apr 30</div>
      </div>
      <div class='metrics-row-item' style='border-right: 1px solid rgba(0, 0, 0, 0.08); padding-right: 16px; padding-left: 8px;'>
        <div style='font-size: 12px; color: #5f6368; margin-bottom: 8px;'>Retention rate</div>
        <div style='display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px;'>
          <span style='font-size: 24px; font-weight: 800; color: #000000;'>2.73</span>
          <span style='font-size: 12px; font-weight: 700; color: #10b981;'>↑ 6.1%</span>
        </div>
        <div style='font-size: 11px; color: #8c8c8c;'>vs Apr 1 - Apr 30</div>
      </div>
      <div class='metrics-row-item' style='padding-left: 8px;'>
        <div style='font-size: 12px; color: #5f6368; margin-bottom: 8px;'>CLV (estimated)</div>
        <div style='display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px;'>
          <span style='font-size: 24px; font-weight: 800; color: #000000;'>€326</span>
          <span style='font-size: 12px; font-weight: 700; color: #10b981;'>↑ 11.8%</span>
        </div>
        <div style='font-size: 11px; color: #8c8c8c;'>vs Apr 1 - Apr 30</div>
      </div>
    </div>
    """
    st.markdown(metrics_html, unsafe_allow_html=True)

    st.markdown("<h3 style='margin-top: 48px; margin-bottom: 24px;'>Explore Clustered Data</h3>", unsafe_allow_html=True)

    try:
        seg_summary = pd.read_csv(BASE_DIR / "datasets" / "segment_summary.csv")
        seg_spend = pd.read_csv(BASE_DIR / "datasets" / "segment_spend_profile.csv")
        seg_complaints = pd.read_csv(BASE_DIR / "datasets" / "segment_complaints_profile.csv")
        
        cluster_options = {
            0: "Cluster 0: Vegetarians",
            1: "Cluster 1: Regulars",
            2: "Cluster 2: Wellness",
            3: "Cluster 3: Promoters",
            4: "Cluster 4: Loyalists",
            5: "Cluster 5: Families",
            6: "Cluster 6: Economizers",
            7: "Cluster 7: Techies"
        }
        
        selected_cluster = st.selectbox("Select cluster to inspect", options=list(cluster_options.keys()), format_func=lambda x: cluster_options[x])
        cluster_color = SEGMENT_COLORS.get(selected_cluster, "#ea580c")
        
        row_summary = seg_summary[pd.to_numeric(seg_summary['cluster'], errors='coerce') == selected_cluster]
        row_spend = seg_spend[pd.to_numeric(seg_spend['cluster'], errors='coerce') == selected_cluster]
        row_complaints = seg_complaints[pd.to_numeric(seg_complaints['cluster'], errors='coerce') == selected_cluster]
        
        if not row_summary.empty:
            cust_count = row_summary.iloc[0]['customers']
            cust_share = row_summary.iloc[0]['share_%']
            num_complaints = row_complaints.iloc[0]['avg_complaints'] if not row_complaints.empty else 0.0
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Customers in cluster", f"{cust_count:,}")
            c2.metric("Share of customer base", f"{cust_share:.1f}%")
            c3.metric("Average complaints", f"{num_complaints:.2f}")
            
            st.markdown("#### Average Spend per Product Category (€)")
            spend_cols = [c for c in row_spend.columns if c.startswith("lifetime_spend_")]
            spend_vals = [row_spend.iloc[0][col] for col in spend_cols]
            spend_labels = [col.replace("lifetime_spend_", "").replace("_", " ").title() for col in spend_cols]
            
            spend_df = pd.DataFrame({
                "Category": spend_labels,
                "Average Spend (€)": spend_vals
            })
            
            spend_chart_cluster = alt.Chart(spend_df).mark_bar(color=cluster_color, cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                x=alt.X("Category:N", sort="-y", title="Spend Category"),
                y=alt.Y("Average Spend (€):Q", title="Average Spend (€)"),
                tooltip=["Category", alt.Tooltip("Average Spend (€):Q", format=",.2f")]
            ).properties(height=300)
            
            st.altair_chart(spend_chart_cluster, use_container_width=True)
    except Exception as e:
        st.info("Dynamic cluster files not fully loaded. Displaying static mockup.")
    render_footer()

elif selected_page == "Targeter Promotion":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Targeter Promotion</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>Based on association rule mining (Apriori algorithm) applied to customer baskets, this section details the targeted cross-selling rules discovered for each segment. Select a segment below to display its campaign rules and simulate targeter actions.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    try:
        campaign_rules = pd.read_csv(BASE_DIR / "datasets" / "segment_campaign_rules.csv")
        unique_segments = campaign_rules['segment'].unique()
        
        # Segment label map to color rules by matching SEGMENT_COLORS keys
        segment_label_map = {
            "Vegetarians": 0, "Regulars": 1, "Wellness": 2, "Promoters": 3,
            "Loyalists": 4, "Families": 5, "Economizers": 6, "Techies": 7
        }
        
        selected_segment = st.selectbox("Select segment for campaigns", options=unique_segments)
        segment_color_idx = segment_label_map.get(selected_segment, 0)
        promo_color = SEGMENT_COLORS.get(segment_color_idx, "#ea580c")
        
        segment_rules = campaign_rules[campaign_rules['segment'] == selected_segment]
        
        st.markdown(f"#### Top Association Rules for {selected_segment}")
        
        for idx, rule in segment_rules.iterrows():
            if_buys = rule['if_buys']
            promote = rule['promote']
            conf = rule['confidence'] * 100
            lift = rule['lift']
            
            st.markdown(f"""
            <div style='background: #ffffff; border: 1px solid rgba(0,0,0,0.05); border-radius: 12px; padding: 18px; margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between;'>
              <div style='flex: 2;'>
                <div style='font-size: 11px; text-transform: uppercase; color: #8c8c8c; font-weight: 700; margin-bottom: 4px;'>Trigger purchase</div>
                <div style='font-size: 15px; font-weight: 700; color: #1a1a1a;'>If customer buys: <code style='font-size: 13px; background: rgba(0,0,0,0.04); padding: 3px 6px; border-radius: 6px;'>{if_buys}</code></div>
              </div>
              <div style='flex: 1.5; border-left: 1px solid rgba(0,0,0,0.08); padding-left: 20px;'>
                <div style='font-size: 11px; text-transform: uppercase; color: {promo_color}; font-weight: 700; margin-bottom: 4px;'>Targeted promotion</div>
                <div style='font-size: 16px; font-weight: 700; color: {promo_color};'>Promote: <strong>{promote.upper()}</strong></div>
              </div>
              <div style='flex: 1; border-left: 1px solid rgba(0,0,0,0.08); padding-left: 20px; text-align: center;'>
                <div style='font-size: 11px; text-transform: uppercase; color: #8c8c8c; font-weight: 700; margin-bottom: 4px;'>Confidence</div>
                <div style='font-size: 18px; font-weight: 800; color: #000000;'>{conf:.0f}%</div>
              </div>
              <div style='flex: 1; border-left: 1px solid rgba(0,0,0,0.08); padding-left: 20px; text-align: center;'>
                <div style='font-size: 11px; text-transform: uppercase; color: #8c8c8c; font-weight: 700; margin-bottom: 4px;'>Lift ratio</div>
                <div style='font-size: 18px; font-weight: 800; color: #10b981;'>{lift:.2f}x</div>
              </div>
            </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        st.info("No campaign rules CSV found. Add datasets/segment_campaign_rules.csv to enable targeter simulation.")
    render_footer()

elif selected_page == "Conclusion & Recommendations":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Conclusion & Recommendations</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>The Customer Intelligence dashboard successfully maps raw transactional behavior and customer attributes into actionable insights. By cleaning negative entries, correcting future transaction records, and mapping spatial density, we have built a stable dataset for business decisions.</p>
        <h3 style='margin-top: 24px; margin-bottom: 16px; font-family:"Playfair Display", serif;'>Strategic Actions</h3>
        <ul style='padding-left: 20px;'>
          <li style='margin-bottom: 12px;'><strong>Targeted Campaign Lift</strong>: Apply the association rules (e.g., salad cross-sell for Promo Shoppers, airpods for Technologists) directly in checkout systems to drive average order value.</li>
          <li style='margin-bottom: 12px;'><strong>Geographic Expansion</strong>: The university and urban corridor hotspots present immediate physical expansion opportunities for premium and student convenience stores.</li>
          <li style='margin-bottom: 12px;'><strong>Retention Programs</strong>: Build tailored communication lines focusing on vegetable-focused mature segments and premium wellness buyers, which show higher loyalty flag consistency.</li>
        </ul>
      </div>
    </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Customer Simulator":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Customer Simulator</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>Simulate a customer's spending and complaints behavior to classify them into their most likely K-Means segment. The simulator uses the overall averages from the dataset to compute a normalized Euclidean distance to each segment centroid, assigning the simulated customer to the nearest community in real-time.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    sim_left_col, sim_right_col = st.columns([1.2, 1.0])

    with sim_left_col:
        st.markdown("#### Customer Attributes")
        
        in_col1, in_col2 = st.columns(2)
        
        with in_col1:
            val_groceries = st.slider("Groceries Spend (€)", min_value=0, max_value=80000, value=15843, step=500)
            val_electronics = st.slider("Electronics Spend (€)", min_value=0, max_value=25000, value=2646, step=100)
            val_vegetables = st.slider("Vegetables Spend (€)", min_value=0, max_value=4000, value=730, step=50)
            val_nonalcohol = st.slider("Non-Alcoholic Drinks Spend (€)", min_value=0, max_value=2000, value=456, step=20)
            val_alcohol = st.slider("Alcoholic Drinks Spend (€)", min_value=0, max_value=4000, value=605, step=50)
            val_meat = st.slider("Meat Spend (€)", min_value=0, max_value=3000, value=709, step=50)
            
        with in_col2:
            val_fish = st.slider("Fish Spend (€)", min_value=0, max_value=3000, value=593, step=50)
            val_hygiene = st.slider("Hygiene Spend (€)", min_value=0, max_value=817, value=817, step=50)
            val_videogames = st.slider("Video Games Spend (€)", min_value=0, max_value=3000, value=358, step=20)
            val_petfood = st.slider("Pet Food Spend (€)", min_value=0, max_value=1500, value=333, step=10)
            val_technology = st.slider("Technology Spend (€)", min_value=0, max_value=25000, value=3004, step=100)
            val_complaints = st.slider("Number of Complaints", min_value=0, max_value=7, value=1, step=1)

    user_spends = {
        "lifetime_spend_groceries": val_groceries,
        "lifetime_spend_electronics": val_electronics,
        "lifetime_spend_vegetables": val_vegetables,
        "lifetime_spend_nonalcohol_drinks": val_nonalcohol,
        "lifetime_spend_alcohol_drinks": val_alcohol,
        "lifetime_spend_meat": val_meat,
        "lifetime_spend_fish": val_fish,
        "lifetime_spend_hygiene": val_hygiene,
        "lifetime_spend_videogames": val_videogames,
        "lifetime_spend_petfood": val_petfood,
        "lifetime_spend_technology": val_technology
    }

    try:
        df_spend_sim = pd.read_csv(BASE_DIR / "datasets" / "segment_spend_profile.csv")
        df_comp_sim = pd.read_csv(BASE_DIR / "datasets" / "segment_complaints_profile.csv")
        
        overall_spend = df_spend_sim[df_spend_sim['cluster'] == 'OVERALL'].iloc[0]
        overall_complaints = (df_comp_sim['avg_complaints'] * df_comp_sim['customers']).sum() / df_comp_sim['customers'].sum()
        
        min_dist = float('inf')
        best_cluster = 0
        
        for c in range(8):
            c_spend = df_spend_sim[pd.to_numeric(df_spend_sim['cluster'], errors='coerce') == c].iloc[0]
            c_comp = df_comp_sim[pd.to_numeric(df_comp_sim['cluster'], errors='coerce') == c].iloc[0]
            
            dist_sq = 0.0
            
            for col_name in user_spends.keys():
                mu_overall = float(overall_spend[col_name])
                mu_cluster = float(c_spend[col_name])
                u_val = float(user_spends[col_name])
                if mu_overall > 0:
                    dist_sq += ((u_val - mu_cluster) / mu_overall) ** 2
                    
            u_comp = float(val_complaints)
            mu_c_comp = float(c_comp['avg_complaints'])
            if overall_complaints > 0:
                dist_sq += ((u_comp - mu_c_comp) / overall_complaints) ** 2
                
            dist = dist_sq ** 0.5
            if dist < min_dist:
                min_dist = dist
                best_cluster = c
                
        seg_meta_sim = {
            0: {"name": "Vegetarians", "desc": "Full-price, promotion-resistant shoppers. Lead with curation/quality framing rather than discounts.", "icon_idx": 0},
            1: {"name": "Regulars", "desc": "Active but newer, deal-aware shoppers. Strong targets for onboarding to the loyalty program.", "icon_idx": 1},
            2: {"name": "Wellness", "desc": "Quiet, low-maintenance, and low-complaint shoppers. Exert low friction and buy full price.", "icon_idx": 2},
            3: {"name": "Promoters", "desc": "The ultimate deal-seekers (+145% promo share). Perfect for price-led campaign stacking.", "icon_idx": 3},
            4: {"name": "Loyalists", "desc": "Highest LTV, highest tenure (13.6 years), and highest loyalty flag adoption (76.8%). Reward and protect.", "icon_idx": 4},
            5: {"name": "Families", "desc": "Large households (avg. 5.41 kids). Loyal without needing promotions. Target with bulk-buying bundles.", "icon_idx": 5},
            6: {"name": "Economizers", "desc": "Restrained, low-friction spenders who buy at baseline. NOT deal-chasers; value baseline pricing.", "icon_idx": 6},
            7: {"name": "Techies", "desc": "Small households buying high-value tech. Cleanest electronics and audio cross-sell campaign audience.", "icon_idx": 7}
        }
        
        meta_info = seg_meta_sim.get(best_cluster)
        active_color = SEGMENT_COLORS.get(best_cluster, "#ea580c")
        symbol_uri_sim = SYMBOL_URIS[meta_info['icon_idx'] % len(SYMBOL_URIS)]
        
        seg_sum_sim = pd.read_csv(BASE_DIR / "datasets" / "segment_summary.csv")
        row_sum_sim = seg_sum_sim[pd.to_numeric(seg_sum_sim['cluster'], errors='coerce') == best_cluster]
        share_val = row_sum_sim.iloc[0]['share_%'] if not row_sum_sim.empty else 0.0
        custs_val = int(row_sum_sim.iloc[0]['customers']) if not row_sum_sim.empty else 0
        
        # Inject custom styling dynamically to style slider tracks & handles to match classified segment's theme color
        st.markdown(
            f"""
            <style>
            div[data-testid="stSlider"] div[role="slider"] {{
                background-color: {active_color} !important;
            }}
            div[data-testid="stSlider"] div[data-baseweb="slider"] > div > div > div {{
                background-color: {active_color} !important;
            }}
            div[data-testid="stSlider"] div[role="slider"]:focus, 
            div[data-testid="stSlider"] div[role="slider"]:hover {{
                box-shadow: 0px 0px 0px 8px {active_color}33 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        with sim_right_col:
            st.markdown("#### Classified Segment")
            
            result_card_html = f"""
            <div class='community-card' style='min-height: auto; margin-bottom: 24px; border-color: {active_color}33;'>
              <div style='display: flex; gap: 20px; align-items: center;'>
                <div class='community-card-icon-container' style='height: 80px; margin-bottom: 0;'>
                  <div class='community-card-icon' style='
                    width: 70px;
                    height: 70px;
                    background-color: {active_color};
                    -webkit-mask: url("{symbol_uri_sim}") no-repeat center / contain;
                    mask: url("{symbol_uri_sim}") no-repeat center / contain;
                  '></div>
                </div>
                <div>
                  <div style='font-size: 11px; text-transform: uppercase; color: {active_color}; font-weight: 700; margin-bottom: 4px;'>Assigned Community</div>
                  <h3 class='community-card-title' style='font-size: 20px; color: {active_color}; margin-bottom: 4px !important;'>{meta_info['name']}</h3>
                  <div style='font-size: 14px; font-weight: 700; color: #000000;'>Cluster {best_cluster} • {share_val:.1f}% Share ({custs_val:,} customers)</div>
                </div>
              </div>
              <div style='font-size: 13px; color: #5f6368; line-height: 1.5; margin-top: 14px;'>{meta_info['desc']}</div>
            </div>
            """
            st.markdown(result_card_html, unsafe_allow_html=True)
            
            st.markdown("#### Spends Comparison: Simulated vs. Centroid")
            
            best_c_spend = df_spend_sim[pd.to_numeric(df_spend_sim['cluster'], errors='coerce') == best_cluster].iloc[0]
            spend_cols = [c for c in df_spend_sim.columns if c.startswith("lifetime_spend_")]
            
            comparison_rows = []
            for col in spend_cols:
                cat_label = col.replace("lifetime_spend_", "").replace("_", " ").title()
                comparison_rows.append({
                    "Category": cat_label,
                    "Group": "Simulated Customer",
                    "Spend (€)": float(user_spends[col])
                })
                comparison_rows.append({
                    "Category": cat_label,
                    "Group": f"{meta_info['name']} Average",
                    "Spend (€)": float(best_c_spend[col])
                })
                
            comp_df = pd.DataFrame(comparison_rows)
            
            comp_chart = alt.Chart(comp_df).mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4).encode(
                x=alt.X("Category:N", sort="-y", title="Spend Category"),
                y=alt.Y("Spend (€):Q", title="Average Spend (€)"),
                color=alt.Color("Group:N", scale=alt.Scale(range=[active_color, f"{active_color}88"]), title=""),
                xOffset="Group:N"
            ).properties(height=320)
            
            st.altair_chart(comp_chart, use_container_width=True)
            
    except Exception as e:
        st.error(f"Error executing simulator: {e}")
    render_footer()
