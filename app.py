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
CESTO_URI = load_image_as_base64(IMAGENS_DIR / "cesto.png")
PRODUCT_GRID_URI = load_image_as_base64(IMAGENS_DIR / "product_grid.jpg")

ICON_INTRO_URI = load_image_as_base64(IMAGENS_DIR / "icon_intro.png")
ICON_ANALYSIS_URI = load_image_as_base64(IMAGENS_DIR / "icon_analysis.png")
ICON_PREPROCESS_URI = load_image_as_base64(IMAGENS_DIR / "icon_preprocess.png")
ICON_GEOGRAPHY_URI = load_image_as_base64(IMAGENS_DIR / "icon_geography.png")
ICON_CLUSTERING_URI = load_image_as_base64(IMAGENS_DIR / "icon_clustering.png")
BRAND_ICON_URI = load_image_as_base64(IMAGENS_DIR / "brand_icon.png")

SYMBOL_URIS = [load_image_as_base64(IMAGENS_DIR / f"symbol_{i}.png") for i in range(1, 8)]
SLICES_URIS = [load_image_as_base64(IMAGENS_DIR / "slices_simbolos" / f"symbol_{i}.png") for i in range(1, 8)]
FAMILIES_URI = load_image_as_base64(IMAGENS_DIR / "families.png")
VEGETARIANS_URI = load_image_as_base64(IMAGENS_DIR / "vegetarians.png")
WELLNESS_URI = load_image_as_base64(IMAGENS_DIR / "wellness.png")
PROMOTERS_URI = load_image_as_base64(IMAGENS_DIR / "promoters.png")
TECHIES_URI = load_image_as_base64(IMAGENS_DIR / "techies.png")
LOYALISTS_URI = load_image_as_base64(IMAGENS_DIR / "loyalists.png")
ECONOMIZERS_URI = load_image_as_base64(IMAGENS_DIR / "economizers.png")
REGULARS_URI = load_image_as_base64(IMAGENS_DIR / "regulars.png")

st.set_page_config(page_title="Customer Segmentation Project", layout="wide", page_icon=str(Path(__file__).resolve().parent / "imagens" / "brand_icon.png"))

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
    background-color: #fafaf8 !important;
}
body {
    background-color: #fafaf8 !important;
    color: #1a1a1a;
}
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stMainContainer"], [data-testid="stAppViewBlockContainer"], main, .main, div.block-container {
    background: transparent !important;
    background-color: transparent !important;
    backdrop-filter: none !important;
}
section[role="main"] {
    padding-top: 0px !important;
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
    background: #ede8df !important;
    border-right: 1px solid rgba(0,0,0,0.06) !important;
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
    font-size: 16px !important;
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
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 1rem !important;
    padding-bottom: 8rem !important;
    background: transparent !important;
    background-color: transparent !important;
    box-shadow: none !important;
    max-width: 100% !important;
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
[data-testid="stArrowVegaLiteChart"],
[data-testid="stVegaLiteChart"],
[data-testid="stPlotlyChart"],
.stVegaLiteChart,
.stPlotlyChart,
div[class*="stVegaLiteChart"],
div[class*="stPlotlyChart"],
iframe[title="plotly"] {
    border: 1px solid rgba(111, 79, 53, 0.15) !important;
    border-radius: 16px !important;
    overflow: hidden !important;
    background: transparent !important;
    background-color: transparent !important;
    box-shadow: none !important;
    padding: 0px !important;
    margin-bottom: 16px !important;
}
[data-testid="stArrowVegaLiteChart"] svg,
[data-testid="stVegaLiteChart"] svg,
.stVegaLiteChart svg,
div[class*="stVegaLiteChart"] svg,
[data-testid="stArrowVegaLiteChart"] svg rect.background,
[data-testid="stVegaLiteChart"] svg rect.background,
.stVegaLiteChart svg rect.background,
div[class*="stVegaLiteChart"] svg rect.background,
[data-testid="stPlotlyChart"] .js-plotly-plot,
[data-testid="stPlotlyChart"] .plot-container,
[data-testid="stPlotlyChart"] .main-svg,
[data-testid="stPlotlyChart"] rect.bg,
[data-testid="stPlotlyChart"] rect.plotbg {
    fill: transparent !important;
    background: transparent !important;
    background-color: transparent !important;
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
    padding: 28px 36px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.015);
    margin-bottom: 20px;
    width: 100%;
    box-sizing: border-box;
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
    line-height: 1.8;
    text-align: justify;
    font-size: 16px;
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
[data-testid="stSidebar"] div[role="radiogroup"] label div[dir="ltr"],
[data-testid="stSidebar"] div[role="radiogroup"] label input[type="radio"],
[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label {
    background-color: transparent !important;
    color: #4a3f2f !important;
    border: none !important;
    padding: 10px 14px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    line-height: 1.5 !important;
    border-radius: 10px !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
    margin-bottom: 2px !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    color: #1a1208 !important;
    background-color: rgba(0,0,0,0.07) !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    color: #c94f38 !important;
    background-color: #f7e6e1 !important;
    font-weight: 700 !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p,
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) span {
    color: #c94f38 !important;
    font-weight: 700 !important;
}

/* SVG icons for sidebar radio */
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(1)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(1):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(2)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(2):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(3)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(3):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(4)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(4):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(5)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(5):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(6)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(6):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(7)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="m9 12 2 2 4-4"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(7):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="m9 12 2 2 4-4"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(8)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(8):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>');
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(9)::before {
    content: "";
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 12px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="rgba(74,63,47,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(9):has(input:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23c94f38" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>');
}

.communities-grid {
    display: grid;
    gap: 12px;
    grid-template-columns: repeat(8, 1fr);
    margin-top: 20px;
    margin-bottom: 32px;
}
@media (max-width: 1400px) {
    .communities-grid { grid-template-columns: repeat(4, 1fr); }
}
@media (max-width: 900px) {
    .communities-grid { grid-template-columns: repeat(2, 1fr); }
}
.community-card {
    background: #ffffff;
    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 14px;
    padding: 16px 16px 14px 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 320px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    cursor: pointer;
}
.community-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border-color: rgba(0,0,0,0.15);
}
.community-card-icon-container {
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
}
.community-card-icon { display: inline-block; }
.community-card-img {
    max-height: 200px;
    max-width: 100%;
    object-fit: contain;
}
.community-card-title {
    font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
    font-size: 14px;
    font-weight: 700;
    color: #111827;
    margin: 0 0 6px 0 !important;
}
.community-card-value {
    font-size: 28px;
    font-weight: 800;
    color: #000000;
    margin-bottom: 1px;
    line-height: 1;
}
.community-card-sub {
    font-size: 11px;
    color: #9ca3af;
    margin-bottom: 8px;
}
.community-card-desc {
    font-size: 12px;
    color: #6b7280;
    line-height: 1.5;
    flex-grow: 1;
    margin-bottom: 10px;
}
.community-card-arrow {
    align-self: flex-end;
    font-size: 18px;
    color: #9ca3af;
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


_page_labels = {
    "Overview":                    "Overview",
    "Data Analysis":               "**NB0** - Data Analysis",
    "Data Preprocessing":          "**NB1** - EDA & Preprocessing",
    "Data in Geography":           "**NB2** - Geographic Analysis",
    "NB3 Clustering":             "**NB3** - Clustering",
    "NB4 Characterisation":       "**NB4** - Cluster Characterisation",
    "Targeter Promotion":          "**NB5** - Association Rules",
    "Conclusion & Recommendations":"Conclusion & Recommendations",
    "Customer Simulator":          "Customer Simulator",
}

st.sidebar.markdown("<div style='font-size: 32px; font-weight: 800; color: #000000; margin-top: 15px; margin-bottom: 25px; font-family: \"Plus Jakarta Sans\", \"Inter\", sans-serif !important; letter-spacing: -0.03em; line-height: 1.1; padding-left: 14px;'>Costumer<br/>Segmentation</div>", unsafe_allow_html=True)
selected_page = st.sidebar.radio(
    label="Index",
    options=list(_page_labels.keys()),
    format_func=lambda x: _page_labels[x],
    key="sidebar_radio_selection",
    label_visibility="collapsed"
)

def render_footer():
    st.markdown(
        """
        <div style='margin-top: 24px; font-family:"Plus Jakarta Sans", "Inter", sans-serif;'>
          <hr style='border: 0; border-top: 1px solid rgba(0, 0, 0, 0.08); margin: 0 0 32px 0;' />
          <div style='width:100%; display:grid; grid-template-columns:repeat(4, 1fr); gap:24px; align-items:start;'>
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
          <div style='background-color: #000000; color: #ffffff; padding: 18px 32px; margin-top: 32px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; width: 100%; border-radius: 12px; box-sizing: border-box;'>
            <span>&copy; 2026 Customer Segmentation Project - Academic Use Only</span>
            <span style='color: #a3a3a3;'>Built for Machine Learning II</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Page conditional routing
if selected_page == "Overview":
    st.markdown(f"""
    <div style='display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 32px; margin-top: 0px; margin-bottom: 24px; font-family: "Plus Jakarta Sans", "Inter", sans-serif; width: 100%;'>
        <div style='flex: 1.5; min-width: 320px;'>
            <h1 style='font-size: clamp(2rem, 4vw, 3.2rem); font-weight: 800; color: #000000; line-height: 1.05; margin: 0 0 20px 0; letter-spacing: -0.04em;'>Understand every customer.<br/>Grow with purpose.</h1>
            <p style='font-size: 17px; color: #5f6368; line-height: 1.7; margin: 0; max-width: 520px;'>A machine learning project that segments 34,060 supermarket customers into 8 distinct communities — uncovering who they are, how they shop, and what drives their decisions.</p>
        </div>
        <div style='flex: none; display: flex; flex-direction: column; gap: 24px; white-space: nowrap; min-width: 150px;'>
            <div>
                <div style='font-size: clamp(2rem, 3.5vw, 3.2rem); font-weight: 800; color: #000000; line-height: 1;'>34,060</div>
                <div style='font-size: 14px; color: #5f6368; margin-top: 4px;'>customers analyzed</div>
            </div>
            <div>
                <div style='font-size: clamp(2rem, 3.5vw, 3.2rem); font-weight: 800; color: #000000; line-height: 1;'>8</div>
                <div style='font-size: 14px; color: #5f6368; margin-top: 4px;'>communities discovered</div>
            </div>
        </div>
        <div style='flex: 1; min-width: 250px; display: flex; justify-content: center; align-items: center;'>
            <img src='{CESTO_URI}' style='max-height: 380px; width: auto; max-width: 100%; object-fit: contain;' />
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Explore your communities →", key="btn_explore"):
        st.session_state.sidebar_radio_selection = "Customer Communities"
        st.rerun()

    # Mini Community Cards — Overview preview
    import pandas as _pd
    _seg = _pd.read_csv(BASE_DIR / "datasets" / "id_and_cluster.csv")
    _total = len(_seg)
    _counts = _seg.groupby(["cluster","cluster_name"]).size().reset_index(name="n")
    _counts["pct"] = (_counts["n"] / _total * 100).round(1)

    # cluster → URI mapping
    _cluster_images = {
        0: VEGETARIANS_URI,
        1: REGULARS_URI,
        2: WELLNESS_URI,
        3: PROMOTERS_URI,
        4: LOYALISTS_URI,
        5: FAMILIES_URI,
        6: ECONOMIZERS_URI,
        7: TECHIES_URI,
    }
    for _i, _row in _counts.iterrows():
        _c = _row["cluster"]
        if _c not in _cluster_images:
            _cluster_images[_c] = SLICES_URIS[_i % len(SLICES_URIS)]

    _cluster_descs = {
        0: "Full-price, promotion-resistant shoppers. Lead with curation and quality framing.",
        1: "Active but newer, deal-aware shoppers. Strong targets for loyalty program onboarding.",
        2: "Quiet, low-maintenance shoppers. Low friction and buy full price.",
        3: "The ultimate deal-seekers. Perfect for price-led campaign stacking.",
        4: "Highest LTV and tenure. Loyal for 13+ years. Reward and protect.",
        5: "Large households. Loyal without needing promotions. Target with bulk-buying bundles.",
        6: "Restrained, low-friction spenders. Value baseline pricing over deals.",
        7: "Small households buying high-value tech. Best electronics cross-sell audience.",
    }

    _cards_html = ""
    for _, _row in _counts.sort_values("cluster").iterrows():
        _c = int(_row["cluster"])
        _name = _row["cluster_name"]
        _pct = _row["pct"]
        _n = int(_row["n"])
        _img = _cluster_images.get(_c, "")
        _desc = _cluster_descs.get(_c, "")
        _cards_html += f"""
        <div class='ov-card'>
            <div class='ov-img-wrap'><img src='{_img}' /></div>
            <div style='margin-top:10px;'>
                <div class='ov-name'>{_name}</div>
                <div class='ov-pct'>{_pct}%</div>
                <div class='ov-sub'>{_n:,} customers</div>
                <div class='ov-desc'>{_desc}</div>
            </div>
            <div class='ov-arrow'>→</div>
        </div>"""

    import streamlit.components.v1 as _components
    _overview_cards_html = f"""
    <style>
      body {{ margin:0; padding:0; background:transparent; font-family:'Plus Jakarta Sans','Inter',sans-serif; }}
      .ov-grid {{
          display: flex;
          flex-wrap: nowrap;
          overflow-x: auto;
          gap: 12px;
          width: 100%;
          box-sizing: border-box;
          padding-bottom: 12px;
          scroll-behavior: smooth;
      }}
      .ov-grid::-webkit-scrollbar {{
          height: 6px;
      }}
      .ov-grid::-webkit-scrollbar-track {{
          background: #f3f4f6;
          border-radius: 99px;
      }}
      .ov-grid::-webkit-scrollbar-thumb {{
          background: #e5e7eb;
          border-radius: 99px;
      }}
      .ov-grid::-webkit-scrollbar-thumb:hover {{
          background: #d1d5db;
      }}
      .ov-card {{
          background:#fff;
          border:1px solid #e5e7eb;
          border-radius:14px;
          padding:16px 14px;
          display:flex;
          flex-direction:column;
          justify-content:space-between;
          min-height:510px;
          flex: 0 0 280px;
          box-sizing: border-box;
      }}
      .ov-img-wrap {{ height:320px; display:flex; align-items:center; justify-content:center; overflow:hidden; }}
      .ov-img-wrap img {{ max-height:320px; max-width:100%; object-fit:contain; }}
      .ov-name {{ font-size:18px; font-weight:700; color:#111827; margin-bottom:6px; }}
      .ov-pct {{ font-size:42px; font-weight:800; color:#111827; line-height:1; }}
      .ov-sub {{ font-size:14px; color:#9ca3af; margin-top:4px; margin-bottom:8px; }}
      .ov-desc {{ font-size:13px; color:#6b7280; line-height:1.5; }}
      .ov-arrow {{ font-size:18px; color:#9ca3af; margin-top:12px; }}
      .ov-header {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; }}
      .ov-header-title {{ font-size:16px; font-weight:700; color:#111827; }}
      .ov-header-link {{ font-size:13px; color:#6b7280; }}
    </style>
    <div class='ov-header'>
      <div class='ov-header-title'>Your 8 customer communities</div>
      <div class='ov-header-link'>View all communities →</div>
    </div>
    <div class='ov-grid'>
      {_cards_html}
    </div>"""
    _components.html(_overview_cards_html, height=720, scrolling=False)

    # Key Metrics Bar
    st.markdown("""
    <div style='display: grid; grid-template-columns: repeat(5, 1fr); gap: 0; border: 1px solid #e5e7eb; border-radius: 14px; overflow: hidden; margin-top: 24px; background: #ffffff; width: 100%; box-sizing: border-box;'>
        <div style='padding: 20px 24px; border-right: 1px solid #e5e7eb;'>
            <div style='font-size: 11px; font-weight: 600; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px;'>Total Revenue</div>
            <div style='font-size: 26px; font-weight: 800; color: #111827; line-height: 1;'>€835.6M</div>
            <div style='font-size: 12px; color: #6b7280; margin-top: 4px;'>lifetime customer value</div>
        </div>
        <div style='padding: 20px 24px; border-right: 1px solid #e5e7eb;'>
            <div style='font-size: 11px; font-weight: 600; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px;'>Avg. Lifetime Spend</div>
            <div style='font-size: 26px; font-weight: 800; color: #111827; line-height: 1;'>€26,100</div>
            <div style='font-size: 12px; color: #6b7280; margin-top: 4px;'>per customer</div>
        </div>
        <div style='padding: 20px 24px; border-right: 1px solid #e5e7eb;'>
            <div style='font-size: 11px; font-weight: 600; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px;'>Loyalty Card Rate</div>
            <div style='font-size: 26px; font-weight: 800; color: #111827; line-height: 1;'>60.4%</div>
            <div style='font-size: 12px; color: #6b7280; margin-top: 4px;'>of customers enrolled</div>
        </div>
        <div style='padding: 20px 24px; border-right: 1px solid #e5e7eb;'>
            <div style='font-size: 11px; font-weight: 600; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px;'>Avg. Tenure</div>
            <div style='font-size: 26px; font-weight: 800; color: #111827; line-height: 1;'>11.0 yrs</div>
            <div style='font-size: 12px; color: #6b7280; margin-top: 4px;'>customer relationship</div>
        </div>
        <div style='padding: 20px 24px;'>
            <div style='font-size: 11px; font-weight: 600; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px;'>Distinct Products</div>
            <div style='font-size: 26px; font-weight: 800; color: #111827; line-height: 1;'>146</div>
            <div style='font-size: 12px; color: #6b7280; margin-top: 4px;'>avg. per customer</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Project Presentation
    st.markdown("""
    <div style='margin-top: 32px; width: 100%; box-sizing: border-box;'>

      <!-- Section: Objective -->
      <div style='margin-bottom: 48px;'>
        <div style='font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #9ca3af; margin-bottom: 12px;'>Project Objective</div>
        <h2 style='font-size: 28px; font-weight: 800; color: #111827; margin: 0 0 16px 0; letter-spacing: -0.02em; line-height: 1.2;'>Why segment customers at all?</h2>
        <p style='font-size: 16px; color: #374151; line-height: 1.8; margin: 0 0 14px 0;'>
          Traditional retail analytics treat the customer base as a single, homogeneous mass — averaging out behaviors that are fundamentally different from one another. This project challenges that assumption. The central objective of this work is to apply unsupervised machine learning to a real-world supermarket dataset and discover whether meaningful, stable, and actionable customer groups exist within the data.
        </p>
        <p style='font-size: 16px; color: #374151; line-height: 1.8; margin: 0;'>
          Rather than relying on intuition or demographic proxies, this analysis is driven entirely by observed behavior — spending patterns across product categories, promotional sensitivity, household composition, loyalty card usage, shopping frequency, and geographic footprint. The goal is to surface communities that are genuinely distinct and that carry real implications for marketing, product, and retention strategy.
        </p>
      </div>

      <!-- Divider -->
      <div style='border-top: 1px solid #e5e7eb; margin-bottom: 48px;'></div>

      <!-- Section: Scope -->
      <div style='margin-bottom: 48px;'>
        <div style='font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #9ca3af; margin-bottom: 12px;'>Scope & Dataset</div>
        <h2 style='font-size: 28px; font-weight: 800; color: #111827; margin: 0 0 16px 0; letter-spacing: -0.02em; line-height: 1.2;'>What data was used?</h2>
        <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 20px;'>
          <div style='background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px 22px;'>
            <div style='font-size: 32px; font-weight: 800; color: #111827; line-height: 1;'>34,060</div>
            <div style='font-size: 13px; color: #6b7280; margin-top: 4px;'>unique customers</div>
          </div>
          <div style='background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px 22px;'>
            <div style='font-size: 32px; font-weight: 800; color: #111827; line-height: 1;'>39</div>
            <div style='font-size: 13px; color: #6b7280; margin-top: 4px;'>behavioral & demographic features</div>
          </div>
          <div style='background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px 22px;'>
            <div style='font-size: 32px; font-weight: 800; color: #111827; line-height: 1;'>11 yrs</div>
            <div style='font-size: 13px; color: #6b7280; margin-top: 4px;'>average customer tenure</div>
          </div>
        </div>
        <p style='font-size: 16px; color: #374151; line-height: 1.8; margin: 0 0 14px 0;'>
          The dataset covers two linked tables: <strong>customer_info</strong>, containing demographic attributes, geographic coordinates, loyalty flag, and lifetime spend broken down by 10 product categories; and <strong>customer_basket</strong>, containing transaction-level purchase logs used for association rule mining.
        </p>
        <p style='font-size: 16px; color: #374151; line-height: 1.8; margin: 0;'>
          Prior to modelling, the data required substantial cleaning — removal of negative spend values introduced by return corrections, filtering of future-dated transactions, and outlier capping at the 99th percentile to prevent extreme spenders from distorting cluster centroids. Feature engineering added tenure (years since first transaction), annual spend rates, total children, a technology spend aggregate, and cyclical encodings of typical shopping hour.
        </p>
      </div>

      <!-- Divider -->
      <div style='border-top: 1px solid #e5e7eb; margin-bottom: 48px;'></div>

      <!-- Section: Methodology -->
      <div style='margin-bottom: 48px;'>
        <div style='font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #9ca3af; margin-bottom: 12px;'>Methodology</div>
        <h2 style='font-size: 28px; font-weight: 800; color: #111827; margin: 0 0 16px 0; letter-spacing: -0.02em; line-height: 1.2;'>How were the communities found?</h2>
        <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;'>
          <div style='border-left: 3px solid #111827; padding-left: 16px;'>
            <div style='font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 6px;'>1 — Exploratory Analysis</div>
            <div style='font-size: 13px; color: #6b7280; line-height: 1.6;'>Distribution checks, missing value mapping, spend category breakdowns, and geographic density analysis across the customer base.</div>
          </div>
          <div style='border-left: 3px solid #111827; padding-left: 16px;'>
            <div style='font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 6px;'>2 — Preprocessing</div>
            <div style='font-size: 13px; color: #6b7280; line-height: 1.6;'>Outlier capping, negative value correction, feature engineering of annual rates, tenure, and technology spend. StandardScaler normalization before clustering.</div>
          </div>
          <div style='border-left: 3px solid #111827; padding-left: 16px;'>
            <div style='font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 6px;'>3 — K-Means Clustering</div>
            <div style='font-size: 13px; color: #6b7280; line-height: 1.6;'>K=8 selected via the Elbow Method and Silhouette Score analysis. Multiple random seeds tested for centroid stability. Final model validated against key behavioral axes.</div>
          </div>
          <div style='border-left: 3px solid #111827; padding-left: 16px;'>
            <div style='font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 6px;'>4 — Association Rules</div>
            <div style='font-size: 13px; color: #6b7280; line-height: 1.6;'>Apriori algorithm applied per cluster to customer basket data, extracting high-confidence cross-sell rules for targeted campaign design.</div>
          </div>
        </div>
      </div>

      <!-- Divider -->
      <div style='border-top: 1px solid #e5e7eb; margin-bottom: 48px;'></div>

      <!-- Section: Navigate -->
      <div style='margin-bottom: 48px;'>
        <div style='font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #9ca3af; margin-bottom: 12px;'>How to use this dashboard</div>
        <h2 style='font-size: 28px; font-weight: 800; color: #111827; margin: 0 0 16px 0; letter-spacing: -0.02em; line-height: 1.2;'>Navigate the findings</h2>
        <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;'>
          <div style='background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px 22px;'>
            <div style='font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 6px;'>Data Analysis</div>
            <div style='font-size: 13px; color: #6b7280; line-height: 1.6;'>Raw dataset exploration — spend distributions, category breakdowns, and customer demographic profiles.</div>
          </div>
          <div style='background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px 22px;'>
            <div style='font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 6px;'>Customer Communities</div>
            <div style='font-size: 13px; color: #6b7280; line-height: 1.6;'>The 8 discovered segments with full behavioral profiles, spend radars, and cluster-level KPIs.</div>
          </div>
          <div style='background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px 22px;'>
            <div style='font-size: 13px; font-weight: 700; color: #111827; margin-bottom: 6px;'>Opportunities & Simulator</div>
            <div style='font-size: 13px; color: #6b7280; line-height: 1.6;'>Cross-sell campaign rules per segment and a real-time simulator to classify hypothetical customers.</div>
          </div>
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Data Analysis":
    st.markdown("""
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>Data Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 0 — Data Analysis</div>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 14px 0;'>
        Before any modelling decisions are made, the raw <code>customer_info.csv</code> dataset is subjected to a thorough exploratory analysis. The dataset contains <strong>33,038 unique customers</strong> described across <strong>21 numerical variables</strong> and a set of categorical and identifier fields. This notebook's purpose is diagnostic: no cleaning or transformation is applied here — every finding is deferred to the preprocessing stage.
      </p>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 24px 0;'>
        The analysis checks for exact and logical duplicates (customers matched by name and birthdate), inspects missing value rates per feature, categorises all columns, and produces distribution plots and boxplots for every numerical variable. A skewness table is computed to quantify the degree of asymmetry in each spending feature.
      </p>

      <div style='display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:28px;'>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:28px; font-weight:800; color:#c94f38; line-height:1;'>33,038</div>
          <div style='font-size:13px; color:#7a6454; margin-top:4px;'>unique customers in raw dataset</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:28px; font-weight:800; color:#c94f38; line-height:1;'>21</div>
          <div style='font-size:13px; color:#7a6454; margin-top:4px;'>numerical variables identified</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:28px; font-weight:800; color:#c94f38; line-height:1;'>30%</div>
          <div style='font-size:13px; color:#7a6454; margin-top:4px;'>missing value threshold for feature exclusion</div>
        </div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Missing value strategy</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Features with more than 30% missing values were flagged as too sparse to impute reliably. The inspection confirmed that missing values are concentrated in a limited group of behavioural and spend variables, supporting imputation over row-dropping — the customer base does not need to be reduced.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Education level as a proxy feature</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Customer names contain academic prefixes — BSc., MSc., PhD. — across all 33,038 unique names. These prefixes are flagged as an education-level proxy and earmarked for feature engineering in Notebook 1. Surname repetition alone was found to be too common to be a useful household signal; it was not carried into the modelling feature set.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Impossible values detected</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'><code>percentage_of_products_bought_promotion</code> was found to contain values outside the valid [0, 1] range — both below 0.0 and above 1.0 — indicating data entry errors. These are flagged here and corrected in preprocessing. Spending variables show strong right-skew, confirming that a small group of customers spends disproportionately more than the majority.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:8px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Duplicate check</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'>No exact duplicate rows were found. A logical duplicate check (matching on customer name AND birthdate) was also performed. A surname-only proximity test was also run but produced too many false positives due to common surnames. The conclusion is that the dataset does not contain systematic duplicate records requiring removal.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    customer_info = pd.read_csv(BASE_DIR / "datasets" / "customer_info.csv")

    # Chart 1: Missing values per feature
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Missing values per feature (%)</div>
</div>
""", unsafe_allow_html=True)
    missing_pct = (customer_info.isnull().mean() * 100).reset_index()
    missing_pct.columns = ["feature", "missing_pct"]
    missing_pct = missing_pct.sort_values("missing_pct", ascending=False)
    missing_pct = missing_pct[missing_pct["missing_pct"] > 0]
    base_missing = alt.Chart(missing_pct).mark_bar(color="#111827", cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
        y=alt.Y("feature:N", sort="-x", title="Feature"),
        x=alt.X("missing_pct:Q", title="Missing (%)"),
        tooltip=["feature", alt.Tooltip("missing_pct:Q", format=".2f", title="Missing %")]
    ).properties(height=max(200, len(missing_pct) * 22))
    threshold_line = alt.Chart(pd.DataFrame({"threshold": [30]})).mark_rule(color="#ef4444", strokeDash=[6, 3], strokeWidth=2).encode(
        x="threshold:Q"
    )
    st.altair_chart((base_missing + threshold_line), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The 30% threshold (red dashed line) was chosen as the boundary above which imputation is judged unreliable: reconstructing more than three out of ten values for a given feature would introduce more noise than signal into the dataset. Features below this threshold retain sufficient observed data to support KNN imputation, which leverages the similarity structure of the customer base. The chart confirms that missing values are concentrated in a small number of behavioural variables, and that no feature exceeds the threshold by a large margin, making row-dropping unnecessary. The majority of the 33,038 customers remain usable across all features.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 2: Distribution of key numerical features
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Distribution of key numerical features</div>
</div>
""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:8px;'>Lifetime spend: Groceries</div>", unsafe_allow_html=True)
    c2.markdown("<div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:8px;'>Lifetime spend: Electronics</div>", unsafe_allow_html=True)
    c3.markdown("<div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:8px;'>Total distinct products</div>", unsafe_allow_html=True)

    hist_groceries = alt.Chart(customer_info.dropna(subset=["lifetime_spend_groceries"])).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("lifetime_spend_groceries:Q", bin=alt.Bin(maxbins=30), title="Groceries spend"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=280)
    hist_electronics = alt.Chart(customer_info.dropna(subset=["lifetime_spend_electronics"])).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("lifetime_spend_electronics:Q", bin=alt.Bin(maxbins=30), title="Electronics spend"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=280)
    hist_products = alt.Chart(customer_info.dropna(subset=["lifetime_total_distinct_products"])).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("lifetime_total_distinct_products:Q", bin=alt.Bin(maxbins=30), title="Distinct products"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=280)
    c1.altair_chart(hist_groceries, use_container_width=True)
    c2.altair_chart(hist_electronics, use_container_width=True)
    c3.altair_chart(hist_products, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>All three distributions exhibit pronounced right-skew: the mass of customers clusters near the lower end of the scale, with a progressively thinner tail extending toward high-spending or high-variety individuals. This asymmetry has two direct implications for modelling. First, standard Euclidean distance in clustering is sensitive to scale differences, meaning that a small group of high-spending customers could disproportionately pull cluster centroids if the data are not scaled. Second, the long tail is precisely where the consensus outlier separation strategy intervenes: rather than capping values, the most extreme multivariate observations are separated into a dedicated outlier dataset before the clustering model is fitted, preserving the shape of the majority distribution while removing undue influence from the periphery.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 3: Promotion ratio distribution
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Promotion ratio distribution (valid range only)</div>
</div>
""", unsafe_allow_html=True)
    promo_valid = customer_info[
        (customer_info["percentage_of_products_bought_promotion"] >= 0) &
        (customer_info["percentage_of_products_bought_promotion"] <= 1)
    ].copy()
    promo_hist = alt.Chart(promo_valid).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("percentage_of_products_bought_promotion:Q", bin=alt.Bin(maxbins=30), title="Proportion of products bought on promotion"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=300)
    st.altair_chart(promo_hist, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The raw dataset contains entries for <code>percentage_of_products_bought_promotion</code> that fall outside the physically valid interval [0, 1], including both negative values and values exceeding 1.0. These are impossible by definition: a proportion cannot be negative or greater than unity, confirming data entry errors rather than extreme but valid behaviour. The chart above is restricted to the valid range only. Within [0, 1], the distribution is roughly bimodal: a concentration of customers near 0.4 to 0.6 suggests a moderately promotion-responsive majority, while a second mass near 1.0 identifies a distinct group of near-exclusively promotional buyers. This heterogeneity in promotional sensitivity later becomes one of the most discriminating variables in the clustering model, most clearly visible in the Promoters segment.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 4: Gender distribution
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Gender distribution</div>
</div>
""", unsafe_allow_html=True)
    gender_counts = customer_info["customer_gender"].value_counts().reset_index()
    gender_counts.columns = ["customer_gender", "count"]
    gender_bar = alt.Chart(gender_counts).mark_bar(color="#374151", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("customer_gender:N", title="Gender"),
        y=alt.Y("count:Q", title="Number of customers"),
        tooltip=["customer_gender", alt.Tooltip("count:Q", title="Customers", format=",")]
    ).properties(height=300)
    st.altair_chart(gender_bar, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The gender distribution across the customer base is approximately balanced between male and female customers, with no category representing an extreme minority. This near-parity is relevant for segmentation methodology: a heavily skewed gender distribution would risk producing segments that reflect gender composition artefacts rather than genuine behavioural differences. The approximate balance observed here supports the interpretation that the eight clusters recovered by the model reflect spending behaviour and lifestyle patterns rather than demographic overrepresentation of one group. Gender is retained as a profiling variable for segment characterisation but is not included in the clustering distance matrix.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 5: Skewness table
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Skewness of spend variables</div>
</div>
""", unsafe_allow_html=True)
    spend_cols_skew = [c for c in customer_info.columns if c.startswith("lifetime_spend_")]
    skew_df = customer_info[spend_cols_skew].skew().reset_index()
    skew_df.columns = ["Feature", "Skewness"]
    skew_df["Feature"] = skew_df["Feature"].str.replace("lifetime_spend_", "", regex=False).str.replace("_", " ").str.title()
    skew_df = skew_df.sort_values("Skewness", ascending=False)
    skew_df["Skewness"] = skew_df["Skewness"].round(2)
    st.dataframe(skew_df.reset_index(drop=True), use_container_width=True, hide_index=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>All spend categories exhibit positive skewness, confirming that the right-tailed pattern observed in the histograms above is not isolated to groceries and electronics but is systematic across the entire spend feature space. High positive skewness (values substantially above 1.0) indicates that a small number of customers account for a disproportionate share of category-level spending. This has two direct consequences for preprocessing: first, lifetime spend values are converted to annual rates by dividing by tenure, to reduce the contribution of long-tenure customers to the skew; second, the consensus outlier separation rule is applied before clustering to set aside the most extreme multivariate observations. Skewness alone does not justify removing observations, but it confirms the need for careful outlier treatment before distance-based clustering is applied.</p>
</div>
""", unsafe_allow_html=True)

    # Chart: Numeric boxplots (from NB0)
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Numerical variable distributions — boxplots</div>
</div>
""", unsafe_allow_html=True)
    nb00_boxplot_path = IMAGENS_DIR / "charts" / "numeric_boxplots.png"
    if nb00_boxplot_path.exists():
        st.image(str(nb00_boxplot_path), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The boxplots confirm the systematic right-skew identified in the histograms: every numerical variable shows a compact interquartile box close to the lower end of its range and a long upper whisker or visible outlier cloud extending far to the right. Median values across spending categories are low relative to the scale maximum, meaning that the majority of customers spend modestly while a thin tail of high-value customers accounts for most of the category-level variance. Variables such as total lifetime spend and electronics show particularly extreme upper outliers, reinforcing the need for the consensus outlier separation step prior to scaling. Age and tenure, by contrast, are more symmetric but still show a modest right tail in tenure, consistent with a customer base accumulated over multiple years of varying acquisition rates. These shapes collectively justify the MinMaxScaler choice over standard z-score normalisation: min-max compression bounds all features to [0, 1] while preserving the relative magnitude ordering within each variable, which is important when inter-feature comparisons are made in UMAP visualisations.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding:24px; border-radius:16px; background:#f9fafb; border:1px solid #e5e7eb; margin-top:12px;'>
          <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 0 — Conclusions</div>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 10px 0;'>"The raw customer data contains missing values, skewed spending variables, identifier columns, date fields and several variables that require type conversion before modelling. These findings motivate the preprocessing notebook, where invalid values are handled, categorical variables are encoded and outliers are addressed."</p>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 10px 0;'>"The distribution plots confirm that spending variables are highly skewed. This supports two later decisions: separating the most atypical customers before fitting the clustering model, and leaving scaling as a modelling choice."</p>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>"The missing value inspection shows that the dataset is usable without dropping large parts of the customer base." No cleaning is applied in this notebook — all transformations are deferred to NB1.</p>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Data Preprocessing":
    st.markdown("""
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>Data Preprocessing</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 1 — Data Preprocessing</div>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 24px 0;'>
        This notebook applies all transformations identified during the exploratory analysis. The goal is to produce a clean, analysis-ready dataset without losing customers unnecessarily. Every decision is justified by domain logic or statistical evidence — no arbitrary removals are made.
      </p>

      <!-- Stage 1: Data Cleaning & Missing Values Treatment -->
      <div style='border-top:1px solid #e5e7eb; padding-top:24px; margin-bottom:20px;'>
        <div style='font-size:18px; font-weight:700; color:#111827; margin-bottom:10px;'>1. Data Cleaning & Missing Values Treatment</div>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 16px 0;'>
          Data cleaning and missing value treatment are crucial initial steps to prevent downstream model bias and mathematical distance calculation errors. In this phase, logical inconsistencies are corrected, raw types are structured, and missing entries are addressed using custom domain logic and KNN imputation.
        </p>
      </div>

      <div style='display:grid; grid-template-columns:repeat(2,1fr); gap:16px; margin-bottom:28px;'>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Future years → NaN</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Future transaction years exceeding 2024 are logical errors. They are set to NaN rather than dropping the customer row.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Invalid promotion → NaN</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Promotion ratios outside the valid [0, 1] range are set to NaN, as they represent invalid measurements.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Zero-imputation for counts</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Missing values in kids_home, teens_home, and number_complaints are filled with 0, assuming lack of entry implies zero count.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Loyalty indicator flag</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Instead of discarding the 38% missing loyalty card numbers, we engineer a binary flag (1 if card exists, 0 otherwise).</div>
        </div>
      </div>

      <div style='margin-bottom:28px;'>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 12px 0;'>
          <strong>Negative Value Analysis:</strong> We scan all numerical columns for values below zero. While negative values in <code>longitude</code> are logically valid (since Lisbon is located west of the Greenwich meridian), negative values in <code>percentage_of_products_bought_promotion</code> represent a logical error and are set to NaN.
        </p>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 12px 0;'>
          <strong>Data Type Coercion:</strong> Mixed types in object columns are coerced. For instance, <code>customer_birthdate</code> is parsed to <code>datetime64</code> to compute age, and counts like <code>kids_home</code> and <code>number_complaints</code> are cast to nullable integers to handle noise.
        </p>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>
          <strong>KNN Imputation:</strong> Remaining missing values in variables such as typical hour, age, and spend categories are handled using a K-Nearest Neighbors (KNN) model with $k=5$. Imputation is only executed after outliers are separated to ensure that extreme multivariate observations do not bias the imputations of the regular customer base.
        </p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    customer_info_pre = pd.read_csv(BASE_DIR / "datasets" / "customer_info.csv")
    info_unscaled = pd.read_csv(BASE_DIR / "datasets" / "info_clustering_unscaled.csv")
    outlier_df = pd.read_csv(BASE_DIR / "datasets" / "outlier_dataset.csv")

    current_year = 2024
    # Calculate counts of anomalies on raw data
    future_years = customer_info_pre[customer_info_pre["year_first_transaction"] > current_year]
    future_year_count = len(future_years)
    invalid_promo = customer_info_pre[(customer_info_pre["percentage_of_products_bought_promotion"] < 0) | (customer_info_pre["percentage_of_products_bought_promotion"] > 1)]
    invalid_promo_count = len(invalid_promo)

    # 1. Anomalies Chart
    anomalies_df = pd.DataFrame({
        "Anomaly Type": ["Future transaction years (>2024)", "Invalid promotion ratio (<0 or >1)"],
        "Count": [future_year_count, invalid_promo_count]
    })
    
    st.markdown("""
<div style='margin-top:10px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Data cleaning anomalies detected in raw dataset</div>
</div>
""", unsafe_allow_html=True)

    anomalies_chart = alt.Chart(anomalies_df).mark_bar(color="#c94f38", cornerRadiusTopRight=6, cornerRadiusBottomRight=6).encode(
        y=alt.Y("Anomaly Type:N", title="Anomaly Type"),
        x=alt.X("Count:Q", title="Number of Records"),
        tooltip=["Anomaly Type", "Count"]
    ).properties(height=140)
    st.altair_chart(anomalies_chart, use_container_width=True)

    # Raw missing values bar chart
    raw_missing = customer_info_pre.isna().sum().reset_index(name="missing_count")
    raw_missing.columns = ["Column", "Missing Count"]
    raw_missing["Missing %"] = (raw_missing["Missing Count"] / len(customer_info_pre)) * 100
    raw_missing = raw_missing[raw_missing["Missing Count"] > 0].sort_values("Missing %", ascending=False)
    
    st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Missing values percentage by feature before imputation (raw dataset)</div>
</div>
""", unsafe_allow_html=True)

    missing_chart = alt.Chart(raw_missing).mark_bar(color="#c94f38", cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
        y=alt.Y("Column:N", sort="-x", title="Feature"),
        x=alt.X("Missing %:Q", title="Missing Percentage (%)"),
        tooltip=["Column", alt.Tooltip("Missing Count:Q", format=","), alt.Tooltip("Missing %:Q", format=".2f")]
    ).properties(height=280)
    st.altair_chart(missing_chart, use_container_width=True)

    # 2. Visual Heatmap of Missing Values (Plotly Heatmap with custom palette)
    df_missing_sample = customer_info_pre.sample(min(2500, len(customer_info_pre)), random_state=42).sort_index()
    null_matrix = df_missing_sample.isnull().astype(int)
    missing_cols = null_matrix.sum()[null_matrix.sum() > 0].index.tolist()
    
    if missing_cols:
        null_matrix_filtered = null_matrix[missing_cols]
        clean_cols = [col.replace("_", " ").title() for col in missing_cols]
        
        import plotly.graph_objects as go
        fig_heat = go.Figure(data=go.Heatmap(
            z=null_matrix_filtered.values,
            x=clean_cols,
            colorscale=[[0, '#fff8f2'], [1, '#c94f38']],
            showscale=False,
            ygaps=0,
            xgaps=0
        ))
        fig_heat.update_layout(
            margin=dict(l=40, r=40, t=15, b=40),
            height=280,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis={'title': "Features with Missing Values", 'tickangle': 45},
            yaxis={'title': "Customers (Sample of 2,500)", 'showticklabels': False}
        )
        
        st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Visual map of missing values distribution (raw dataset sample)</div>
</div>
""", unsafe_allow_html=True)
        st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("""
<div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The data cleaning shows specific logical errors (such as future transaction years and negative promotion percentages) that were successfully resolved. The missing value map confirms that <code>loyalty_card_number</code> contains the largest volume of missing values (approx 38%). Instead of removing these records or imputing card numbers, we engineer a binary loyalty indicator. Features like spend categories (meat, fish, vegetables) and typical hour have less than 3% missing rates. These are cleanly handled later by KNN Imputation (k=5) inside the regular base, preserving customer rows without losing significant volume.</p>
</div>
""", unsafe_allow_html=True)

    # Stage 2: Aggregation Feature Engineering
    st.markdown("""
      <!-- Stage 2: Aggregation Feature Engineering -->
      <div style='border-top:1px solid #e5e7eb; padding-top:24px; margin-bottom:20px;'>
        <div style='font-size:18px; font-weight:700; color:#111827; margin-bottom:10px;'>2. Aggregation Feature Engineering</div>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 16px 0;'>
          Before outlier separation and final transformation, we create broader demographic and loyalty features by parsing raw identifiers and dates:
        </p>
      </div>

      <div style='display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:28px;'>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Age calculation</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Age is calculated dynamically relative to the 2024 temporal baseline. Implausible ages (under 16 or over 100) are set to NaN.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Education level proxy</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Academic titles (BSc., MSc., PhD.) are extracted from names as a proxy for education level (years of study), and names are cleaned.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Gender binary mapping</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>The raw customer_gender text field (male/female) is mapped to a binary indicator (is_male: 1 for male, 0 for female).</div>
        </div>
      </div>
    """, unsafe_allow_html=True)

    # Engineered categorical features summary (Gender, Loyalty, Education)
    gender_df = info_unscaled["customer_gender"].value_counts().reset_index()
    gender_df.columns = ["Gender", "Customers"]
    gender_df["Gender"] = gender_df["Gender"].astype(str).str.title()
    
    gender_chart = alt.Chart(gender_df).mark_bar(color="#8c6f53", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Gender:N", title="Gender"),
        y=alt.Y("Customers:Q", title="Customers"),
        tooltip=["Gender", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=220)

    loyalty_df = info_unscaled["customer_loyalty_flag"].value_counts().reset_index()
    loyalty_df.columns = ["Loyalty", "Customers"]
    loyalty_df["Loyalty"] = loyalty_df["Loyalty"].map({1: "Loyal", 0: "Non-Loyal"})
    
    loyalty_chart = alt.Chart(loyalty_df).mark_bar(color="#b77b45", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Loyalty:N", title="Loyalty Card Flag"),
        y=alt.Y("Customers:Q", title="Customers"),
        tooltip=["Loyalty", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=220)

    def get_edu_label(name):
        if pd.isna(name):
            return "High School (12y)"
        name = str(name).strip().lower()
        if name.startswith("bsc."):
            return "BSc (15y)"
        elif name.startswith("msc."):
            return "MSc (17y)"
        elif name.startswith("phd."):
            return "PhD (22y)"
        return "High School (12y)"

    edu_series = info_unscaled["customer_name"].apply(get_edu_label)
    edu_df = edu_series.value_counts().reset_index()
    edu_df.columns = ["Education", "Customers"]
    
    edu_chart = alt.Chart(edu_df).mark_bar(color="#c94f38", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Education:N", title="Education Level", sort=["High School (12y)", "BSc (15y)", "MSc (17y)", "PhD (22y)"]),
        y=alt.Y("Customers:Q", title="Customers"),
        tooltip=["Education", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=220)

    st.markdown("""
<div style='margin-top:10px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Distribution of engineered categorical features</div>
</div>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.altair_chart(gender_chart, use_container_width=True)
    with col2:
        st.altair_chart(loyalty_chart, use_container_width=True)
    with col3:
        st.altair_chart(edu_chart, use_container_width=True)

    # 3. Household distributions
    kids_df = info_unscaled["kids_home"].value_counts().reset_index()
    kids_df.columns = ["Kids", "Customers"]
    kids_chart = alt.Chart(kids_df).mark_bar(color="#b77b45", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Kids:N", title="Kids at Home"),
        y=alt.Y("Customers:Q", title="Customers"),
        tooltip=["Kids", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=220)

    teens_df = info_unscaled["teens_home"].value_counts().reset_index()
    teens_df.columns = ["Teens", "Customers"]
    teens_chart = alt.Chart(teens_df).mark_bar(color="#8c6f53", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Teens:N", title="Teens at Home"),
        y=alt.Y("Customers:Q", title="Customers"),
        tooltip=["Teens", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=220)

    complaints_df = info_unscaled["number_complaints"].value_counts().reset_index()
    complaints_df.columns = ["Complaints", "Customers"]
    complaints_chart = alt.Chart(complaints_df).mark_bar(color="#c94f38", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Complaints:N", title="Number of Complaints"),
        y=alt.Y("Customers:Q", title="Customers"),
        tooltip=["Complaints", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=220)

    st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Distribution of household and complaints variables (after zero-filling)</div>
</div>
""", unsafe_allow_html=True)

    col1_hh, col2_hh, col3_hh = st.columns(3)
    with col1_hh:
        st.altair_chart(kids_chart, use_container_width=True)
    with col2_hh:
        st.altair_chart(teens_chart, use_container_width=True)
    with col3_hh:
        st.altair_chart(complaints_chart, use_container_width=True)

    # Customer age distribution
    st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Engineered customer age distribution</div>
</div>
""", unsafe_allow_html=True)
    customer_info_pre["customer_birthdate"] = pd.to_datetime(customer_info_pre["customer_birthdate"], errors="coerce")
    customer_info_pre["customer_age"] = 2024 - customer_info_pre["customer_birthdate"].dt.year
    age_clean = customer_info_pre.dropna(subset=["customer_age"])
    age_hist = alt.Chart(age_clean).mark_bar(color="#b77b45", opacity=0.85).encode(
        x=alt.X("customer_age:Q", bin=alt.Bin(maxbins=25), title="Age (years)"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=280)
    st.altair_chart(age_hist, use_container_width=True)

    st.markdown("""
<div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The age distribution covers a wide spread (centering on 30 to 50 years). Using birthdates directly would introduce raw date formats that distance calculations cannot interpret. Calculating age dynamically relative to the 2024 temporal baseline resolves this. The categorical summaries also confirm that gender is almost evenly split, loyalty is map-encoded for 62% of customers, and name parsing successfully identifies academic prefixes (BSc, MSc, PhD) as education level proxies. Zero-filling kids, teens and complaints handles the missing values under the assumption that missing counts represent zero counts.</p>
</div>
""", unsafe_allow_html=True)

    # Stage 3: Outlier Separation — The Consensus Rule
    st.markdown("""
      <!-- Stage 3: Outlier Separation -->
      <div style='border-top:1px solid #e5e7eb; padding-top:24px; margin-bottom:20px;'>
        <div style='font-size:18px; font-weight:700; color:#111827; margin-bottom:10px;'>3. Outlier Separation — The Consensus Rule</div>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 16px 0;'>
          Rather than capping or removing outliers based on a single method, a <strong>conservative consensus rule</strong> is applied: a customer is set aside only when simultaneously flagged as an outlier by all three of the following methods:
        </p>
      </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:12px;'>
          <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:10px; padding:14px 16px; text-align:center;'>
            <div style='font-size:13px; font-weight:700; color:#c94f38;'>IQR</div>
            <div style='font-size:22px; font-weight:800; color:#c94f38; margin:4px 0;'>k = 2.0</div>
            <div style='font-size:12px; color:#7a6454;'>multiplier</div>
          </div>
          <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:10px; padding:14px 16px; text-align:center;'>
            <div style='font-size:13px; font-weight:700; color:#c94f38;'>DBSCAN</div>
            <div style='font-size:22px; font-weight:800; color:#c94f38; margin:4px 0;'>eps = 1.0</div>
            <div style='font-size:12px; color:#7a6454;'>neighbourhood radius</div>
          </div>
          <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:10px; padding:14px 16px; text-align:center;'>
            <div style='font-size:13px; font-weight:700; color:#c94f38;'>3rd method</div>
            <div style='font-size:22px; font-weight:800; color:#c94f38; margin:4px 0;'>&cap;</div>
            <div style='font-size:12px; color:#7a6454;'>all three must agree</div>
          </div>
        </div>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:14px 0;'>
          Customers flagged by all three methods are exported to <code>outlier_dataset.csv</code>. The regular base is then processed with KNN imputation. This approach ensures that only multivariate extremes are removed — customers with one extreme variable but otherwise normal behaviour are retained. Outliers are later <strong>reattached to their nearest cluster centroid</strong> after the model is fitted.
        </p>
    """, unsafe_allow_html=True)

    # Dataset split after consensus outlier separation
    st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Dataset split after consensus outlier separation</div>
</div>
""", unsafe_allow_html=True)
    split_df = pd.DataFrame({
        "Dataset": ["Regular base", "Outlier dataset"],
        "Customers": [len(info_unscaled), len(outlier_df)]
    })
    split_chart = alt.Chart(split_df).mark_bar(color="#b77b45", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Dataset:N", title=""),
        y=alt.Y("Customers:Q", title="Number of customers"),
        tooltip=["Dataset", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=280)
    st.altair_chart(split_chart, use_container_width=True)

    st.markdown("""
<div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The chart demonstrates the conservative nature of the consensus outlier rule: the overwhelming majority of customers remain in the regular base, with only 1,023 customers (approx. 3.1%) separated. This conservative threshold avoids over-excluding customers who are unusual on a single variable but unremarkable in the multivariate space. Outliers are reattached to their nearest cluster centroid after model fitting.</p>
</div>
""", unsafe_allow_html=True)

    # Stage 4: Transformation Feature Engineering & Export
    st.markdown("""
      <!-- Stage 4: Transformation Feature Engineering -->
      <div style='border-top:1px solid #e5e7eb; padding-top:24px; margin-bottom:20px;'>
        <div style='font-size:18px; font-weight:700; color:#111827; margin-bottom:10px;'>4. Transformation Feature Engineering & Export</div>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 16px 0;'>
          After outlier separation, we apply mathematical transformations to prepare our variables for modeling, ensuring distance metrics operate correctly across circular dimensions and spending volume:
        </p>
      </div>

      <div style='display:grid; grid-template-columns:repeat(2,1fr); gap:16px; margin-bottom:28px;'>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>tenure (years of relationship)</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Replaces raw year_first_transaction to represent lifecycle duration as an interpretable numerical span.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>typical_hour sin/cos</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Sine and cosine transformations map typical shopping hour to a unit circle, preserving adjacent hour distance.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Annual spend rates</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Normalizes total spend by relationship tenure, preventing long tenure from inflating relative spending profiles.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Technology spend</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.5;'>Aggregates electronics and videogames into a single feature, reducing dimensionality and representing total tech affinity.</div>
        </div>
      </div>
    """, unsafe_allow_html=True)

    # Typical hour cyclic encoding scatter plot
    st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Cyclic typical shopping hour scatter plot</div>
</div>
""", unsafe_allow_html=True)
    hour_scatter = alt.Chart(info_unscaled.sample(min(5000, len(info_unscaled)), random_state=42)).mark_circle(color="#c94f38", opacity=0.4, size=15).encode(
        x=alt.X("typical_hour_sin:Q", title="sin(hour)", scale=alt.Scale(domain=[-1.1, 1.1])),
        y=alt.Y("typical_hour_cos:Q", title="cos(hour)", scale=alt.Scale(domain=[-1.1, 1.1])),
        tooltip=["typical_hour_sin", "typical_hour_cos"]
    ).properties(height=340)
    st.altair_chart(hour_scatter, use_container_width=True)

    st.markdown("""
<div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Using raw hours directly (0 to 23) introduces a boundary error where 23:00 and 00:00 appear maximally distant (difference of 23). The cyclic encoding resolves this by plotting them on a circle, ensuring hour 23 and hour 0 are correctly recognized as adjacent.</p>
</div>
""", unsafe_allow_html=True)

    # Spend boxplots after preprocessing
    st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Annual spend per category after preprocessing</div>
</div>
""", unsafe_allow_html=True)
    annual_cols = ["annual_spend_groceries", "annual_spend_electronics", "annual_spend_vegetables", "annual_spend_meat", "annual_spend_fish", "annual_spend_hygiene"]
    spend_melt = info_unscaled[annual_cols].melt(var_name="category", value_name="annual_spend")
    spend_melt["category"] = spend_melt["category"].str.replace("annual_spend_", "", regex=False).str.replace("_", " ").str.title()
    spend_melt = spend_melt.dropna(subset=["annual_spend"])
    box_chart_pre = alt.Chart(spend_melt).mark_boxplot(color="#8c6f53", outliers={"size": 4, "opacity": 0.2}).encode(
        x=alt.X("category:N", title="Category"),
        y=alt.Y("annual_spend:Q", title="Annual spend"),
        tooltip=["category"]
    ).properties(height=360)
    st.altair_chart(box_chart_pre, use_container_width=True)

    st.markdown("""
<div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Right-skew persists after preprocessing as expected. The goal of outlier separation is to remove extreme multivariate records, not all natural variation. The wide spend spread across categories indicates meaningful heterogeneity inside the customer base, which KMeans will utilize to identify segments.</p>
</div>
""", unsafe_allow_html=True)

    # Stage 5: Correlation heatmaps
    st.markdown("""
      <!-- Stage 5: Correlation Heatmaps -->
      <div style='border-top:1px solid #e5e7eb; padding-top:24px; margin-bottom:20px;'>
        <div style='font-size:18px; font-weight:700; color:#111827; margin-bottom:10px;'>5. Feature Correlation Matrix</div>
        <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 16px 0;'>
          Highly redundant features can distort distance metrics by double-weighting similar signals. We inspect the correlation matrix to ensure no features exceed a collinearity threshold of 0.7.
        </p>
      </div>
    """, unsafe_allow_html=True)

    corr_features = [
        "annual_spend_groceries", "annual_spend_electronics", "annual_spend_vegetables",
        "annual_spend_meat", "annual_spend_fish", "annual_spend_hygiene",
        "annual_spend_videogames", "percentage_of_products_bought_promotion",
        "tenure", "total_children"
    ]
    corr_matrix = info_unscaled[corr_features].corr()
    corr_labels = [f.replace("annual_spend_", "").replace("_", " ").title() for f in corr_features]
    corr_fig = px.imshow(
        corr_matrix.values,
        x=corr_labels,
        y=corr_labels,
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        text_auto=".2f"
    )
    corr_fig.update_layout(margin=dict(l=60, r=20, t=60, b=60), height=500, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(corr_fig, use_container_width=True)

    st.markdown("""
<div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Most spend categories correlate weakly, confirming they carry distinct signals. The strongest positive correlation is between meat and fish (0.42), well below the 0.7 feature-exclusion threshold. Promotional sensitivity shows near-zero correlation with spend categories, supporting its use as an independent clustering variable.</p>
</div>
""", unsafe_allow_html=True)

    # Full correlation heatmap from raw data
    st.markdown("""
<div style='margin-top:20px; margin-bottom:12px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Full correlation heatmap (raw features)</div>
</div>
""", unsafe_allow_html=True)
    corr_chart_path = IMAGENS_DIR / "charts" / "correlation_heatmap.png"
    if corr_chart_path.exists():
        st.image(str(corr_chart_path), use_container_width=True)
        
    st.markdown("""
<div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The full-feature correlation heatmap covers all variables in the raw dataset. It validates that spending variables are relatively independent, and that demographic age/tenure do not share a strong linear association, preventing redundancy in model features.</p>
</div>
""", unsafe_allow_html=True)

    # Why export unscaled card
    st.markdown("""
      <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:20px 24px; margin-top:16px; margin-bottom:32px;'>
        <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:6px;'>Why export unscaled?</div>
        <div style='font-size:16px; color:#7a6454; line-height:1.8;'>The final dataset is exported <strong>without scaling</strong>. Scaling is treated as a modelling choice — MinMaxScaler and RobustScaler are both evaluated in Notebook 3 against each other. Keeping the export unscaled ensures that the same raw dataset can be tested against any scaling strategy without re-running preprocessing.</div>
      </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='padding:24px; border-radius:16px; background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); margin-top:12px;'>
          <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#7a6454; margin-bottom:10px;'>Notebook 1 — Conclusions</div>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 10px 0;'>"Before imputing missing values, the most atypical customers are separated into an outlier dataset. The rule is conservative: a customer is only kept aside when it is simultaneously flagged by three methods."</p>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 10px 0;'>"After the conservative outlier separation, the regular customer base still contains natural variation, but the most extreme observations are kept aside. This reduces the risk that a small number of atypical customers dominate the clustering distances."</p>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>"In the final exported dataset, <code>year_first_transaction</code> is replaced by <code>tenure</code>, and <code>typical_hour</code> is replaced by its cyclic components. Some high values remain visible in the boxplots after preprocessing. This is expected because lifetime spending variables are naturally skewed."</p>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Data in Geography":
    st.markdown("""
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>Data In Geography</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 2 — Geographic Analysis</div>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 14px 0;'>
        Geographic data is available for a significant portion of the customer base in the form of latitude and longitude coordinates. This notebook investigates whether the spatial distribution of customers reveals behavioural patterns beyond what the demographic and spend variables capture. Crucially, <strong>geography is intentionally excluded from the clustering distance</strong> — including it would risk creating geographic groups rather than behavioural segments.
      </p>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 24px 0;'>
        The analysis uses four complementary visualisations: a scatter plot of coordinates, an interactive Plotly scatter mapbox, a Folium map with MarkerCluster, and a hexbin density map. The hotspot is identified programmatically using a coordinate grid (bins=50) — not visually — to ensure the finding is data-driven and reproducible.
      </p>

      <div style='display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:28px;'>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Hotspot location</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.6;'>Dense concentration near <strong>Cidade Universitária</strong> and <strong>Entrecampos</strong> in Lisbon. Consistent with a younger urban population around university and transport infrastructure.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Dominant age group</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.6;'>The <strong>25–34</strong> age band dominates the hotspot profile. Hotspot median age is significantly lower than the rest of the customer base.</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#c94f38; margin-bottom:4px;'>Hotspot radius</div>
          <div style='font-size:14px; color:#7a6454; line-height:1.6;'><strong>0.006 decimal degrees</strong> — defined programmatically via grid-based density analysis, not by visual inspection of the map.</div>
        </div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Behavioural differences: hotspot vs. rest of base</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'>The hotspot shows a distinct behavioural profile even before clustering labels are applied. The strongest differences are in <strong>age, product diversity, number of complaints, store visits, total spend, and promotion usage</strong>. Hotspot customers are younger, more active, and more variety-seeking — consistent with a younger urban population, though the data does not confirm student status directly.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Why geography is excluded from clustering</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Including geographic coordinates in the clustering distance would create spatially-defined groups — customers near each other in space would be forced into the same cluster regardless of their spending behaviour. The objective is to discover <em>behavioural</em> communities, not geographic ones. Geography is kept as a profiling tool: after clusters are fitted, the geographic distribution of each cluster is inspected as a validation and characterisation layer.</div>
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
    scatter_map.update_layout(margin=dict(l=0, r=0, t=0, b=0), coloraxis_colorbar=dict(title="Promo %"), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
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
    density_map.update_layout(margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
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
    st.altair_chart(compare_chart, use_container_width=True)

    # Chart: Age distribution hotspot vs outside
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Age distribution: hotspot vs. rest of base</div>
</div>
""", unsafe_allow_html=True)
    customer_info_geo = pd.read_csv(BASE_DIR / "datasets" / "customer_info.csv")
    customer_info_geo = customer_info_geo.dropna(subset=["latitude", "longitude"]).copy()
    customer_info_geo["customer_birthdate"] = pd.to_datetime(customer_info_geo["customer_birthdate"], errors="coerce")
    customer_info_geo["customer_age"] = 2024 - customer_info_geo["customer_birthdate"].dt.year
    customer_info_geo["lat_bin"] = (customer_info_geo["latitude"] * 20).round(0) / 20
    customer_info_geo["lon_bin"] = (customer_info_geo["longitude"] * 20).round(0) / 20
    geo_grid = customer_info_geo.groupby(["lat_bin", "lon_bin"]).size().reset_index(name="count")
    geo_hotspot = geo_grid.sort_values("count", ascending=False).head(1).iloc[0]
    customer_info_geo["geo_group"] = "Rest of base"
    customer_info_geo.loc[
        (customer_info_geo.lat_bin == geo_hotspot.lat_bin) & (customer_info_geo.lon_bin == geo_hotspot.lon_bin),
        "geo_group"
    ] = "Hotspot"
    age_geo_clean = customer_info_geo.dropna(subset=["customer_age"])
    age_hotspot_chart = alt.Chart(age_geo_clean).mark_bar(opacity=0.6).encode(
        x=alt.X("customer_age:Q", bin=alt.Bin(maxbins=25), title="Age (years)"),
        y=alt.Y("count():Q", stack=None, title="Customers"),
        color=alt.Color("geo_group:N", scale=alt.Scale(domain=["Hotspot", "Rest of base"], range=["#111827", "#9ca3af"]), title="Group"),
        tooltip=["geo_group", alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=320)
    st.altair_chart(age_hotspot_chart, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The overlaid age histograms reveal a pronounced difference in age composition between the hotspot and the rest of the customer base. The hotspot skews clearly toward the 25 to 34 age band, while the broader base has a flatter distribution extending through the 40 to 55 range. This age gap is the most statistically robust finding of the geographic analysis: it corroborates the hypothesis that the dense area near Cidade Universitaria and Entrecampos attracts a younger urban population, consistent with proximity to university infrastructure and high-density residential areas. The finding is treated as an interpretive insight rather than an actionable segment boundary, because geography is deliberately excluded from the clustering distance. The age skew observed in the hotspot does not define a segment; rather, it adds spatial context to the behavioural profiles that the clustering model identifies independently.</p>
</div>
""", unsafe_allow_html=True)

    # Chart: Static scatter (NB2)
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Static geographic scatter — all customers (raw coordinates)</div>
</div>
""", unsafe_allow_html=True)
    geo_raw_path = IMAGENS_DIR / "charts" / "geo_scatter_raw.png"
    if geo_raw_path.exists():
        st.image(str(geo_raw_path), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>This static scatter plot represents every customer as a point at their recorded latitude and longitude coordinates, plotted without any segmentation labels. The visualisation reveals that the customer base is heavily concentrated in a narrow geographic band consistent with the Lisbon Metropolitan Area, with a pronounced density peak in the central zone. The clustering of points is not uniform: a high-density region emerges in the centre-north quadrant of the scatter, corresponding to the urban core identified in the interactive maps above. Surrounding this core, points become progressively sparser and more dispersed, consistent with suburban and commuter-belt customers. This raw spatial pattern is the starting point for the geographic analysis: the identification of the hotspot bounding box, the density map, and the behavioural comparisons are all derived from the concentration visible here. The static format makes the overall geographic footprint clear without the visual clutter of colour-coded segments, which are overlaid in the clustering-era scatter produced later in Notebook 4.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding:24px; border-radius:16px; background:#f9fafb; border:1px solid #e5e7eb; margin-top:12px;'>
          <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 2 — Conclusions</div>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 10px 0;'>"The hotspot shows a distinct behavioural profile even before using any clustering labels. The strongest differences are age, product diversity, number of complaints, store visits, total spend and promotion usage. This suggests that the dense area is not only a map artefact; it also corresponds to a younger, more active customer profile."</p>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>"Age is the strongest signal supporting the area near the university hypothesis. At this stage, it should not be treated as one of the final customer segments because geography is not part of the clustering distance. However, it is useful as a geographic profiling insight."</p>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "NB3 Clustering":
    st.markdown("""
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>NB3 - Clustering</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 3 — Clustering</div>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 14px 0;'>
        This notebook contains the full model selection process. No single diagnostic drives the final choice: instead, six candidate feature sets, two scalers, and five values of k (6 to 10) are evaluated simultaneously using silhouette scores, elbow curves, Ward dendrograms, and dimensionality reduction projections. Every decision is documented and every alternative is tested before being accepted or rejected.
      </p>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 14px 0;'>
        The dataset entering this notebook is <code>info_clustering_unscaled.csv</code> — 32,015 customers after the consensus outlier separation carried out in NB1. Each record is described by 11 features: the 10 non-groceries lifetime spend columns plus <code>percentage_of_products_bought_promotion</code>. Groceries are deliberately excluded from the clustering distance because they act as a near-universal baseline with low discriminating power; they are retained for profiling in NB4.
      </p>

      <div style='display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:28px;'>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Algorithm</div>
          <div style='font-size:22px; font-weight:800; color:#c94f38;'>K-Means</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>K selected</div>
          <div style='font-size:22px; font-weight:800; color:#c94f38;'>8</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Scaler</div>
          <div style='font-size:22px; font-weight:800; color:#c94f38;'>MinMax</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Feature set</div>
          <div style='font-size:16px; font-weight:800; color:#c94f38; line-height:1.2;'>spend + promo<br/>no groceries</div>
        </div>
      </div>

      <div style='display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-bottom:28px;'>
        <div>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:12px;'>Model selection decisions</div>
          <div style='display:flex; flex-direction:column; gap:10px;'>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Why K=8?</div>
              <div style='font-size:15px; color:#6b7280; margin-top:3px;'>Values between 6 and 10 were compared across multiple feature spaces and scalers using the Elbow Method, Silhouette Score, Ward dendrogram (cut height=6.4), and R² grid. K=8 was selected as the configuration that balances geometric separation with business interpretability.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Why exclude groceries from clustering distance?</div>
              <div style='font-size:15px; color:#6b7280; margin-top:3px;'>Most customers spend heavily on groceries regardless of segment. Including it dominated the distance calculation, masking more differentiating categories. Groceries are kept for profiling — not for clustering.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Why MinMaxScaler over RobustScaler?</div>
              <div style='font-size:15px; color:#6b7280; margin-top:3px;'>Both scalers were tested. MinMaxScaler produced slightly stronger and more stable silhouette scores across the k range tested, and was preferred after side-by-side UMAP comparison.</div>
            </div>
          </div>
        </div>
        <div>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:12px;'>Alternatives tested & rejected</div>
          <div style='display:flex; flex-direction:column; gap:10px;'>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>DBSCAN — rejected</div>
              <div style='font-size:15px; color:#6b7280; margin-top:3px;'>"Strongest silhouettes are obtained when most customers are classified as noise." DBSCAN did not recover the richer eight-segment structure obtained with K-Means and was ruled out as the final model.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Petfood alternative — rejected</div>
              <div style='font-size:15px; color:#6b7280; margin-top:3px;'>A model adding <code>lifetime_spend_petfood</code> and separating electronics from videogames was tested. "Overall structure is slightly less clean than the current model." Petfood is kept as a profiling insight only.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>SOM & hierarchical Ward — benchmarked</div>
              <div style='font-size:15px; color:#6b7280; margin-top:3px;'>A 12×12 SOM (1,000 iterations) and a Centroid Ward macro (20 micro-K-Means → Ward into 8 macro segments) were run as benchmarks. K-Means was confirmed as the strongest and most interpretable model.</div>
            </div>
          </div>
        </div>
      </div>

      <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 20px; margin-bottom:28px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:8px;'>Naming rationale (Notebook 4)</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Business names are assigned only after the modelling stage is complete. A name is only confirmed when the same pattern appears consistently across <strong>at least three views</strong>: the spend deviation table, the radar plot, the spend profile heatmap, and the demographic/behavioural profile. "The final name of each segment is chosen only when the same pattern appears in more than one view."</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ---- NB3 Charts ----
    st.markdown("""
<div style='margin-top:48px; margin-bottom:6px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:6px;'>Notebook 3 — Clustering process</div>
  <div style='font-size:20px; font-weight:800; color:#111827; margin-bottom:4px;'>Model selection: charts from the clustering notebook</div>
</div>
""", unsafe_allow_html=True)

    # Scaler comparison
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Scaler comparison — silhouette score vs k (MinMax vs Robust)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "scaler_comparison.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Both MinMaxScaler and RobustScaler were tested across the full range of k values from 2 to 11 using the same feature set and KMeans initialisation. MinMaxScaler consistently produces higher silhouette scores at k=8 and shows a cleaner elbow in the curve. RobustScaler, designed to be resistant to outliers via median/IQR centering, performs worse here because the outlier separation step carried out in Notebook 1 already removed the most extreme observations — leaving the remaining distribution compact enough that robust centering offers no additional benefit. The advantage of MinMaxScaler is that it maps each feature to [0, 1], preserving relative spread within each variable while equalising their contribution to the Euclidean distance. This behaviour is appropriate for the spend feature set, where individual categories span very different absolute ranges but each contributes meaningful behavioural signal at any scale.</p>
</div>
""", unsafe_allow_html=True)

    # Elbow + silhouette
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Elbow curve and silhouette score vs k</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "elbow_silhouette.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The left panel shows the within-cluster sum of squares (inertia) as a function of k. The curve bends most sharply between k=3 and k=6, after which the rate of decrease slows considerably. The "elbow" is not pronounced at a single value but rather forms a gradual plateau from k=7 onward, which is consistent with datasets that contain many overlapping clusters of similar size. The right panel plots the average silhouette score, which measures how well each customer fits its own cluster relative to the nearest alternative. The silhouette peaks locally near k=4 and k=8, with k=8 providing the best balance between geometric separation and the number of actionable segments. The silhouette score at k=8 (0.249) is modest in absolute terms — typical for real-world retail datasets where customer behaviours overlap naturally — but is the best achievable value given the intrinsic structure of the feature space. Neither criterion alone is decisive; k=8 was selected because it is supported simultaneously by the silhouette plateau, the Ward dendrogram cut, and the business interpretability of the resulting segments.</p>
</div>
""", unsafe_allow_html=True)

    # Ward dendrogram
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Ward dendrogram — 3,000 customer subsample (cut height = 6.4)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "ward_dendrogram.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The Ward dendrogram merges clusters bottom-up by minimising the within-cluster sum of squares at each step, producing the same objective as KMeans but from a hierarchical perspective. A random subsample of 3,000 customers is used because computing full linkage on 32,015 observations is computationally prohibitive in a single session. The red dashed line marks the cut height of 6.4, which is the value at which the dendrogram is split to yield 8 macro-groups. This cut was chosen because the vertical segment lengths (representing merge costs) are substantially longer below this point, indicating that the 8 groups at this level are meaningfully separated from one another. Cutting higher would merge communities with genuinely different spend profiles; cutting lower would produce groups too small or too similar to be actionable. The dendrogram independently confirms k=8 as the natural partition depth, providing hierarchical validation for the flat KMeans solution.</p>
</div>
""", unsafe_allow_html=True)

    # Alternative dendrograms
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Alternative linkage methods — complete, average, single (500 customer subsample)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "alt_dendrograms.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Three alternative linkage strategies are shown for comparison: complete linkage (maximum pairwise distance), average linkage (mean pairwise distance), and single linkage (minimum pairwise distance). Complete linkage tends to produce compact, equally-sized clusters and is robust to outliers, but generates a complex dendrogram structure that is harder to cut cleanly. Average linkage is a compromise that balances compactness and sensitivity, but also results in a complex tree at this sample size. Single linkage, the most sensitive to noise, exhibits the chaining effect — long strands of incremental merges — which produces very unbalanced trees and is inappropriate for well-separated segment identification. The Ward linkage used in the final model produces the cleanest tree structure with the most interpretable cut point, which is why it was selected as the primary hierarchical validation tool. The alternative dendrograms are included here to document that the Ward method was not adopted arbitrarily but compared against standard alternatives.</p>
</div>
""", unsafe_allow_html=True)

    # Silhouette grid
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Silhouette score grid — feature sets vs number of clusters (k=6 to 10)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "silhouette_grid.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The grid evaluates six candidate feature sets against five values of k (6 through 10), with each cell reporting the average silhouette score on a green-yellow-red scale where green represents better separation. The feature set "spend + promo no groceries" — which corresponds to the 10 non-groceries lifetime spend columns plus the promotional sensitivity variable — produces the best or near-best silhouette score at k=8 across multiple feature set variants. Removing groceries consistently improves scores because groceries acts as a near-universal baseline: most customers buy groceries at moderate levels regardless of their broader spending profile, and its inclusion compresses inter-cluster distances without adding discriminative information. The grid also confirms that k=8 is the optimal choice within the range tested: scores do not improve meaningfully at k=9 or k=10, while the segment interpretability would decrease with more clusters. This systematic grid replaces the informal "try one configuration" approach and provides reproducible justification for the final feature set and k selection.</p>
</div>
""", unsafe_allow_html=True)

    # Silhouette blades
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Silhouette blades — KMeans k=8 (final model)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "silhouette_blades.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The silhouette blade plot shows the individual silhouette coefficient for every customer in the dataset, grouped by cluster and sorted in descending order. Each "blade" (filled horizontal bar) represents one cluster: a wide, tall blade extending well to the right of the global average line (red dashed) indicates a compact, well-separated cluster. A blade with a large negative portion (extending left of zero) indicates customers that may fit a neighbouring cluster better than their assigned one. In the final k=8 model, all clusters show predominantly positive silhouette values, with the global average around 0.249. Some clusters are narrower and taller, indicating tighter internal cohesion; others are wider and shorter, reflecting a naturally more dispersed population. The absence of large negative "valleys" across all clusters confirms that the KMeans solution does not force clearly misclassified customers into wrong segments — a critical quality check for retail segmentation, where a customer appearing in the wrong community would receive inappropriate campaign messaging.</p>
</div>
""", unsafe_allow_html=True)

    # PCA projection
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>PCA projection — 2D embedding of cluster assignments</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "pca_projection.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Principal Component Analysis reduces the 11-dimensional feature space to its two highest-variance directions, projecting each customer to a 2D point coloured by cluster assignment. PC1 and PC2 together explain the percentage of total variance noted in the axis labels. The PCA projection is the most conservative dimensionality reduction: it is a linear transformation and therefore cannot "unfold" non-linear manifold structure. Where clusters appear well-separated along the principal axes, the separation is genuine and would be detectable by any linear classifier. Where clusters overlap in this view, the separation may still be real in higher dimensions — it is simply not visible in the two principal directions. The Techies and Loyalists clusters tend to separate along the technology-spend axis that dominates PC1, while the Promoters cluster separates along the promotional-sensitivity axis visible in PC2. Some overlapping between adjacent clusters (Wellness, Regulars, Economizers) is expected given their moderate spending profiles; these are the communities whose naming decisions required the most supporting evidence from multiple chart types.</p>
</div>
""", unsafe_allow_html=True)

    # UMAP projection
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>UMAP projection — non-linear 2D embedding (n=3,000 subsample)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "umap_projection.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>UMAP (Uniform Manifold Approximation and Projection) is a non-linear dimensionality reduction method that preserves local neighbourhood structure more faithfully than PCA. Points that are close together in the 11-dimensional feature space remain close in the 2D embedding; the global distances between clusters are less interpretable but the within-cluster density and local boundaries are meaningful. In the UMAP projection, the clusters that are most behaviourally distinct — Techies, Promoters, Vegetarians — appear as more isolated and compact islands, confirming that the KMeans solution has identified genuinely separable groups. Clusters that overlap substantially in the UMAP (Regulars, Economizers, Wellness) share the most feature space in reality: they occupy the moderate-spend, moderate-promo region of the customer population, and their differentiation relies on subtle but consistent deviations visible in the spend profile and radar charts. UMAP was used as a validation tool at multiple stages of model selection, including to compare MinMaxScaler versus RobustScaler configurations, and the scaler that produced more structured UMAP topology was preferred.</p>
</div>
""", unsafe_allow_html=True)

    # t-SNE projection
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>t-SNE projection — stochastic 2D embedding (n=3,000 subsample)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "tsne_projection.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>t-SNE (t-distributed Stochastic Neighbour Embedding) is a probabilistic dimensionality reduction technique optimised for visualising high-dimensional cluster structure. Unlike PCA, t-SNE does not preserve global distances: the spacing between well-separated clusters in the t-SNE plot is not proportional to their actual feature-space distance. What it does preserve is local density: points within each cluster remain tightly grouped, and nearby clusters in the original space tend to appear adjacent. The t-SNE projection is included here as a third independent visual check alongside PCA and UMAP. Concordance across all three projections — that the same clusters appear compact and distinct in each — provides strong evidence that the KMeans partition is not an artefact of any single visualisation method. The perplexity parameter was set to 40 (a value appropriate for datasets of this size), and a subsample of 3,000 customers was used to make the computation tractable. Colour mapping is identical to the PCA and UMAP panels to facilitate direct comparison.</p>
</div>
""", unsafe_allow_html=True)

    # Z-score behavioural heatmap
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Standardised behavioural z-score heatmap — all features by cluster</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "zscore_heatmap.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Each cell shows the z-score deviation of a cluster's mean from the global dataset mean for that feature: red indicates above-average, blue below-average. Z-scores standardise across features with different scales, enabling direct comparison of how strongly each cluster deviates from baseline on each dimension. The heatmap makes naming decisions transparent: Techies show strong positive z-scores for electronics, technology, and videogames; Vegetarians for vegetables and non-alcoholic drinks; Promoters for the promotional sensitivity variable. Economizers and Wellness show uniformly near-zero or slightly negative z-scores, reflecting their moderate, below-average positioning across most categories — which explains why they are the most challenging segments to characterise from a single variable and require the full multivariate profile. Loyalists show above-average scores across multiple spend categories simultaneously, consistent with their status as the highest-lifetime-value segment. This heatmap was one of the primary tools used to validate cluster names before they were finalised.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding:24px; border-radius:16px; background:#f9fafb; border:1px solid #e5e7eb; margin-top:32px;'>
          <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 3 — Conclusions</div>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 10px 0;'>The final model is KMeans with k=8, MinMaxScaler, and the feature set "spend + promo no groceries" (11 features). This configuration was selected after systematically testing six feature sets, two scalers, and five k values using silhouette scores, elbow curves, Ward dendrogram, and three dimensionality reduction projections. No single diagnostic was decisive; k=8 was selected because it is consistently supported across all evaluation tools simultaneously.</p>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0 0 10px 0;'>DBSCAN was rejected because it classified most customers as noise and did not produce a rich multi-segment structure. The petfood alternative feature set produced a slightly less clean UMAP structure and was not adopted. SOM and hierarchical centroid Ward were run as benchmarks and confirmed KMeans as the best-performing model in terms of silhouette score and segment interpretability.</p>
          <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The z-score heatmap and three 2D projections (PCA, UMAP, t-SNE) serve as independent geometric validators: concordance across all three confirms that the eight-segment structure is not an artefact of any single visualisation method. The characterisation of each segment is carried out in Notebook 4.</p>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "NB4 Characterisation":
    cluster_id_map = {0: "Vegetarians", 1: "Regulars", 2: "Wellness", 3: "Promoters", 4: "Loyalists", 5: "Families", 6: "Economizers", 7: "Techies"}

    st.markdown("""
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>NB4 - Cluster Characterisation</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 4 — Cluster Characterisation</div>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 14px 0;'>
        Notebook 4 takes the cluster assignments produced by the KMeans model in NB3 and applies a systematic characterisation process to each of the eight communities. The goal is twofold: first, to understand what distinguishes each cluster from the rest of the customer base across spend, behaviour, and demographic dimensions; second, to assign interpretable business names that are grounded in the data rather than imposed a priori.
      </p>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 14px 0;'>
        The naming protocol is strict: a name is only confirmed when the same pattern appears consistently in at least three independent views — the spend profile heatmap, the z-score deviation table, the radar chart, and the demographic/behavioural profile. No segment is named from a single chart. This multi-view requirement prevents overfitting a name to a visual artefact and ensures that the label reflects a genuine and stable behavioural pattern.
      </p>
      <div style='display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:28px;'>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Segments named</div>
          <div style='font-size:22px; font-weight:800; color:#c94f38;'>8</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Chart views used</div>
          <div style='font-size:22px; font-weight:800; color:#c94f38;'>7</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Customers profiled</div>
          <div style='font-size:22px; font-weight:800; color:#c94f38;'>32,015</div>
        </div>
        <div style='background:#f7e6e1; border:1px solid rgba(201, 79, 56, 0.25); border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#7a6454; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Min views to name</div>
          <div style='font-size:22px; font-weight:800; color:#c94f38;'>3</div>
        </div>
      </div>
      <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 20px; margin-bottom:28px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:8px;'>Naming protocol</div>
        <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Business names are assigned only after the modelling stage is complete. A name is only confirmed when the same pattern appears consistently across at least three views: the spend deviation table, the radar plot, the spend profile heatmap, and the demographic/behavioural profile. "The final name of each segment is chosen only when the same pattern appears in more than one view." This prevents confirmation bias and ensures that names reflect stable, data-grounded patterns rather than single-chart impressions.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Cluster sizes
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Customer count per community</div>
</div>
""", unsafe_allow_html=True)
    id_cluster_df = pd.read_csv(BASE_DIR / "datasets" / "id_and_cluster.csv")
    cluster_counts = id_cluster_df.groupby("cluster_name").size().reset_index(name="customers")
    cluster_counts = cluster_counts.sort_values("customers", ascending=False)
    cluster_size_chart = alt.Chart(cluster_counts).mark_bar(color="#374151", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("cluster_name:N", sort="-y", title="Segment"),
        y=alt.Y("customers:Q", title="Number of customers"),
        tooltip=["cluster_name", alt.Tooltip("customers:Q", format=",")]
    ).properties(height=320)
    st.altair_chart(cluster_size_chart, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The distribution of customers across the eight communities is free from pathological size imbalance. No single community dominates the dataset and no community is too small to be actionable. This balance is a direct consequence of the outlier separation step in NB1: removing multivariate extremes before clustering produces a more homogeneous input space in which K-Means converges to more evenly populated centroids. The two largest segments (Regulars and Economizers) are also the most behaviourally moderate, which is consistent with a retail customer base where the majority of customers have unremarkable spending patterns. The three smallest segments (Techies, Promoters, Families) are the most behaviourally distinctive — their smaller size reflects how rare those specific patterns are in the population, not a modelling failure. Segment sizes inform campaign prioritisation: larger segments offer higher absolute reach, while smaller but more homogeneous segments offer higher targeting precision.</p>
</div>
""", unsafe_allow_html=True)

    # Interactive spend heatmap
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Normalised spend profile per cluster — interactive heatmap</div>
</div>
""", unsafe_allow_html=True)
    seg_spend_df = pd.read_csv(BASE_DIR / "datasets" / "segment_spend_profile.csv")
    spend_heat_cols = [c for c in seg_spend_df.columns if c.startswith("lifetime_spend_")]
    seg_spend_df["cluster"] = pd.to_numeric(seg_spend_df["cluster"], errors="coerce")
    seg_spend_df = seg_spend_df.dropna(subset=["cluster"])
    seg_spend_df = seg_spend_df.sort_values("cluster")
    seg_spend_df["segment_name"] = seg_spend_df["cluster"].astype(int).map(cluster_id_map)
    spend_matrix = seg_spend_df[spend_heat_cols].values.astype(float)
    col_min = spend_matrix.min(axis=0); col_max = spend_matrix.max(axis=0)
    col_range = col_max - col_min; col_range[col_range == 0] = 1
    spend_matrix_norm = (spend_matrix - col_min) / col_range
    spend_col_labels = [c.replace("lifetime_spend_", "").replace("_", " ").title() for c in spend_heat_cols]
    spend_heat_fig = px.imshow(spend_matrix_norm, x=spend_col_labels, y=seg_spend_df["segment_name"].tolist(),
        color_continuous_scale="Blues", zmin=0, zmax=1, text_auto=".2f")
    spend_heat_fig.update_layout(margin=dict(l=80, r=20, t=60, b=80), height=420, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(spend_heat_fig, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Each cell is normalised to [0, 1] across segments per column, so the darkest cell identifies the highest-spending segment in that category. Techies concentrate spending in electronics, videogames, and technology. Vegetarians over-index in vegetables and non-alcoholic drinks. Families show elevated spend across groceries and hygiene. Groceries show similar shading across nearly all segments, confirming that its exclusion from the clustering distance was correct — it adds little discriminative power. Alcohol and petfood show very low values across all segments, confirming their niche status in the customer base. Hover over any cell to see the normalised score; compare columns to identify which category most cleanly separates one segment from the rest.</p>
</div>
""", unsafe_allow_html=True)

    # Interactive behavioural heatmap
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Normalised behavioural profile per cluster — interactive heatmap</div>
</div>
""", unsafe_allow_html=True)
    info_unscaled_comm = pd.read_csv(BASE_DIR / "datasets" / "info_clustering_unscaled.csv")
    customer_segments_comm = pd.read_csv(BASE_DIR / "datasets" / "customer_segments.csv")
    merged_comm = info_unscaled_comm.merge(customer_segments_comm, on="customer_id", how="inner")
    behav_features = ["percentage_of_products_bought_promotion", "tenure", "total_children", "number_complaints"]
    behav_by_cluster = merged_comm.groupby("cluster")[behav_features].mean().reset_index()
    behav_by_cluster["segment_name"] = behav_by_cluster["cluster"].map(cluster_id_map)
    behav_by_cluster = behav_by_cluster.sort_values("cluster")
    behav_matrix = behav_by_cluster[behav_features].values.astype(float)
    b_min = behav_matrix.min(axis=0); b_max = behav_matrix.max(axis=0)
    b_range = b_max - b_min; b_range[b_range == 0] = 1
    behav_matrix_norm = (behav_matrix - b_min) / b_range
    behav_heat_fig = px.imshow(behav_matrix_norm, x=["Promo sensitivity", "Tenure (years)", "Total children", "Avg complaints"],
        y=behav_by_cluster["segment_name"].tolist(), color_continuous_scale="Blues", zmin=0, zmax=1,
        text_auto=".2f")
    behav_heat_fig.update_layout(margin=dict(l=80, r=20, t=60, b=80), height=420, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(behav_heat_fig, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Promotional sensitivity varies strongly across segments: Promoters register the maximum value on this dimension, confirming that their defining trait is price-driven purchasing. Tenure separates long-term customers (Loyalists, Vegetarians) from newer cohorts (Regulars), supporting differentiated retention versus acquisition strategies. Total children most strongly characterises the Families segment — the highest value on this axis was one of the primary naming criteria. Complaints vary modestly across segments; where elevated, they reflect higher transaction frequency rather than systematic dissatisfaction. Together, these four dimensions provide a multi-axis profile that is more actionable for campaign design than spend data alone.</p>
</div>
""", unsafe_allow_html=True)

    # Community cards
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
        cluster_images = {0:VEGETARIANS_URI,1:REGULARS_URI,2:WELLNESS_URI,3:PROMOTERS_URI,4:LOYALISTS_URI,5:FAMILIES_URI,6:ECONOMIZERS_URI,7:TECHIES_URI}
        st.markdown("<div style='font-size:20px; font-weight:700; color:#111827; margin-top:40px; margin-bottom:4px;'>Your 8 customer communities</div>", unsafe_allow_html=True)
        cards_list_html = []
        for idx, row in seg_summary.iterrows():
            c_id = int(row['cluster']); share = row['share_%']; custs = int(row['customers'])
            meta = seg_meta_grid.get(c_id, {"name": f"Cluster {c_id}", "desc": "No description.", "icon_idx": 0})
            img_uri = cluster_images.get(c_id, SLICES_URIS[c_id % len(SLICES_URIS)])
            cards_list_html.append(f"<div class='community-card'><div class='community-card-icon-container'><img src='{img_uri}' class='community-card-img' /></div><div><h3 class='community-card-title'>{meta['name']}</h3><div class='community-card-value'>{share:.1f}%</div><div class='community-card-sub'>{custs:,} customers</div><div class='community-card-desc'>{meta['desc']}</div></div><div class='community-card-arrow'>→</div></div>")
        st.markdown(f"<div class='communities-grid'>{''.join(cards_list_html)}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading segment summary: {e}")

    st.markdown("""
<div style='margin-top:48px; margin-bottom:6px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:6px;'>Notebook 4 — Segment profiling charts</div>
  <div style='font-size:20px; font-weight:800; color:#111827; margin-bottom:4px;'>Deep-dive characterisation — all charts from NB4</div>
</div>
""", unsafe_allow_html=True)

    # Spend profile heatmap (NB4 version)
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Spend profile heatmap — average lifetime spend per cluster (€)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "spend_heatmap.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The spend profile heatmap shows raw average lifetime spend in euros per cluster-category pair, with colour normalised across clusters per column so that the darkest cell identifies the highest-spending segment in each category. Cell annotations show the actual euro values. Techies stand out strongly in electronics, technology, and videogames — confirming they are the technology-oriented segment and making them the priority audience for any cross-sell campaign targeting premium devices. Vegetarians dominate vegetables and non-alcoholic drinks, consistent with a health- and diet-conscious profile. Families show elevated spend across groceries and hygiene, reflecting large household purchasing patterns. Loyalists rank highly across multiple categories simultaneously, consistent with a long-tenure, broad-basket profile. Economizers show consistently low raw spend values across all categories, reflecting a restrained purchasing style — importantly, this is not driven by promotion sensitivity (their promo usage is near the median), but by genuinely lower absolute spending levels. This raw-values version of the heatmap complements the normalised plotly version shown above by revealing the actual scale differences between clusters, which the normalised view compresses.</p>
</div>
""", unsafe_allow_html=True)

    # Behavioural + demographic heatmap (NB4)
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Behavioural and demographic profile heatmap — z-scores by cluster</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "behavioural_heatmap.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>This heatmap captures non-spend dimensions: customer age, tenure as a customer, number of children at home, number of teenagers at home, number of complaints, stores visited, and promotional sensitivity. Z-scores allow direct comparison across variables with different units and scales. Families show the strongest positive deviation on the children and teens dimensions, which is the primary naming driver for this segment. Loyalists score highest on tenure, consistent with their long-standing relationship with the retailer. Promoters show by far the strongest positive z-score on promotional sensitivity (percentage of products bought on promotion), confirming that this is their defining and differentiating characteristic. Regulars and Economizers have relatively flat profiles across behavioural dimensions, which contributes to their lower distinctiveness in the z-score space — their differentiation comes from the spend profile rather than demographic or behavioural attributes. Complaints vary modestly across segments; no cluster is systematically dissatisfied, reducing the risk that any identified community represents a cohort at high churn risk due to service quality alone.</p>
</div>
""", unsafe_allow_html=True)

    # Individual radar profiles
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Individual radar profiles — all 8 clusters (9-axis spider chart)</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "radar_individual.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Each panel shows a single cluster's average profile across nine axes: electronics, vegetables, meat, fish, technology, petfood, videogames, hygiene, and promotional sensitivity. Values are normalised to [0, 1] relative to the dataset maximum for each axis, so the shape of each radar reflects relative spend intensity rather than absolute euros. Techies (C7) present a highly asymmetric shape with large extensions along electronics and technology and a very small promotional sensitivity arm, confirming they are full-price technology buyers. Vegetarians (C0) show a large extension along the vegetables axis with a near-zero promotional arm, consistent with quality-driven, full-price vegetable purchasers. Promoters (C3) show a large promotional sensitivity arm but a relatively flat spend profile across product categories, confirming that what defines this segment is how they buy rather than what they buy. Families (C5) show elevated hygiene and meat arms. Loyalists (C4) present a broadly extended shape across multiple arms, reflecting their high-basket, broad-category purchasing. The individual view makes segment-specific patterns clear without the visual complexity of the overlaid comparison.</p>
</div>
""", unsafe_allow_html=True)

    # Combined radar
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Combined radar — all 8 clusters overlaid</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "radar_combined.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The combined radar overlays all eight cluster profiles in a single chart, enabling direct visual comparison of where each community stands relative to every other on the same axis. The chart reveals the concentration of most profiles near the centre for the majority of axes — confirming that most spending categories are at moderate or low levels for most customers — while a small number of clusters extend significantly outward on specific axes. This visual concentration pattern is the radar equivalent of the z-score heatmap's near-zero cells for moderate segments. The axes where clear separation occurs (electronics for Techies, vegetables for Vegetarians, promotional sensitivity for Promoters) are precisely the axes that carry the highest discriminative power in the clustering distance. The combined radar is particularly useful for campaign planning: any axis where the target segment extends furthest from the centre while others remain near the origin represents an opportunity for category-specific messaging with minimal audience overlap risk.</p>
</div>
""", unsafe_allow_html=True)

    # Feature barplots
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Average spend per category by cluster — grouped bar charts</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "feature_barplots.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Each panel shows one product category, with bars coloured by cluster and the y-axis representing the average lifetime spend in euros. This view complements the heatmap by making absolute scale differences explicit: the electronics panel, for example, reveals that Techies spend roughly twice the next-highest cluster on electronics, while the vegetables panel shows a moderate but consistent advantage for Vegetarians. The fish panel shows that Wellness customers have a notably elevated fish spend relative to other moderate-spending segments, an insight that would be invisible in a normalised view but visible here because the absolute difference is meaningful. The petfood panel confirms that the petfood feature, while excluded from the clustering distance, does differentiate one cluster (Families) in the profiling stage. The videogames panel shows that Techies dominate this category, while most other segments spend near zero — making videogames the most concentrated single-segment category in the dataset and therefore the most targeted cross-sell opportunity available from any campaign built on these segments.</p>
</div>
""", unsafe_allow_html=True)

    # Boxplot grid
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Key variable distributions by cluster — boxplot grid</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "boxplot_grid.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The boxplot grid shows the within-cluster distribution of four key variables: total lifetime spend, promotional purchase ratio, customer age, and tenure. Unlike mean-based heatmaps, boxplots expose the spread and skew within each cluster — information that is essential for assessing how targeted a campaign can realistically be. The total spend panel reveals that Loyalists have the highest median spend and also the widest interquartile range, meaning that this segment contains both very high and moderately high spenders. Promoters show a very narrow promotional sensitivity distribution clustered near 1.0, confirming that their defining characteristic is consistent, not occasional, promotion usage. The age panel reveals that Regulars and Techies skew younger while Loyalists and Families are older on average. Tenure follows a similar pattern: Loyalists have the longest tenure and the narrowest spread, while Regulars and Economizers are newer customers with wider tenure distributions, consistent with a more recently acquired and more heterogeneous cohort. These within-cluster distributions inform the confidence level with which each segment can be targeted: narrow distributions mean higher message precision; wide distributions mean a broader or tiered communication strategy is more appropriate.</p>
</div>
""", unsafe_allow_html=True)

    # Geographic scatter by cluster (NB4)
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Geographic distribution by cluster — static scatter</div>
</div>
""", unsafe_allow_html=True)
    _p = IMAGENS_DIR / "charts" / "geo_scatter.png"
    if _p.exists(): st.image(str(_p), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>The geographic scatter overlays all eight cluster labels on the latitude-longitude coordinate space, using the same colour palette as the radar and heatmap charts. Because geography was deliberately excluded from the clustering distance, any spatial pattern visible here is an emergent property of the behavioural segmentation rather than a modelling artefact. The chart reveals that clusters are not randomly mixed across space: Techies and Loyalists show a higher concentration in the central urban zone, consistent with the younger and higher-income urban customer profile identified in the geographic analysis notebook. Families are more evenly distributed across the suburban periphery, consistent with lower population density in residential areas outside the city centre. Promoters appear throughout the map with no strong geographic concentration, suggesting that price-sensitivity is a behavioural trait not constrained to a particular residential area. This geographic overlay is used as a final profiling validation step: if a cluster appeared concentrated exclusively in a single neighbourhood, that would raise a flag that geography had leaked into the segmentation through a correlated variable. The relatively mixed spatial distribution across clusters confirms that the model is capturing behavioural rather than geographic patterns.</p>
</div>
""", unsafe_allow_html=True)

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
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>Targeter Promotion</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 5 — Association Rules</div>
      <p style='font-size:18px; color:#374151; line-height:1.9; margin:0 0 14px 0;'>
        Association rule mining is applied as a <strong>post-segmentation interpretation tool</strong> — it does not change the cluster assignments in any way. The Apriori algorithm is run independently on the basket transaction data for each of the 8 segments, revealing which product combinations are statistically more likely to co-occur within each community.
      </p>

      <div style='display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:28px;'>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Min Support</div>
          <div style='font-size:26px; font-weight:800; color:#111827;'>1%</div>
          <div style='font-size:12px; color:#6b7280; margin-top:2px;'>intentionally low (per-segment)</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Min Confidence</div>
          <div style='font-size:26px; font-weight:800; color:#111827;'>20%</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Min Lift</div>
          <div style='font-size:26px; font-weight:800; color:#111827;'>1.2</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Robustness split</div>
          <div style='font-size:26px; font-weight:800; color:#111827;'>80/20</div>
          <div style='font-size:12px; color:#6b7280; margin-top:2px;'>train/test, seed=42</div>
        </div>
      </div>

      <div style='display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-bottom:24px;'>
        <div style='border-left:3px solid #111827; padding-left:20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Why support is set at 1%</div>
          <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Rules are mined per segment — each sub-population has far fewer transactions than the full dataset. A 1% support threshold ensures enough rules are discovered while still requiring meaningful co-occurrence frequency within each community.</div>
        </div>
        <div style='border-left:3px solid #111827; padding-left:20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Lift-derived campaign discounts</div>
          <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Suggested campaign discounts are not fixed — they are derived from the lift value of each rule. A higher lift means a stronger-than-random co-purchase signal, which justifies a larger promotional incentive. This ties the commercial decision directly to statistical evidence.</div>
        </div>
        <div style='border-left:3px solid #111827; padding-left:20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Excluded recommendations: Vegetarians (cluster 0)</div>
          <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Chicken, meat, and fish are excluded from recommendations for cluster 0 (Vegetarians). The Apriori rules initially suggested these items, but they contradict the segment's defining behavioural trait. Notebook 4 confirms that this segment's identity is plant-based — the exclusion ensures campaign coherence.</div>
        </div>
        <div style='border-left:3px solid #111827; padding-left:20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Robustness validation</div>
          <div style='font-size:16px; color:#6b7280; line-height:1.8;'>Each segment's rules are validated on an 80/20 train/test split. Segments with many matched rules and low mean lift difference between train and test have stable co-purchase patterns. Segments with few matched rules should be interpreted with caution.</div>
        </div>
      </div>
    </div>
    <div style='height:1px; background:#e5e7eb; margin-bottom:24px;'></div>
    """, unsafe_allow_html=True)

    # Chart 1: Top rules by lift per segment (grouped horizontal bar)
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Association rules by lift per segment</div>
</div>
""", unsafe_allow_html=True)
    rules_df = pd.read_csv(BASE_DIR / "datasets" / "segment_campaign_rules.csv")
    rules_df["rule_label"] = rules_df["if_buys"] + " -> " + rules_df["promote"]
    lift_chart = alt.Chart(rules_df).mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
        y=alt.Y("rule_label:N", sort="-x", title="Rule (if buys -> promote)"),
        x=alt.X("lift:Q", title="Lift"),
        color=alt.Color("segment:N", title="Segment"),
        tooltip=["segment", "if_buys", "promote", alt.Tooltip("confidence:Q", format=".2f", title="Confidence"), alt.Tooltip("lift:Q", format=".2f", title="Lift")]
    ).properties(height=520)
    st.altair_chart(lift_chart, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Lift measures how much more likely two products are to be purchased together compared to what would be expected if they were purchased independently. A lift of 1.0 indicates no association beyond chance; a lift of 1.2 indicates that the joint purchase is 20% more likely than random co-occurrence; values above 2.0 represent strong non-random co-purchase patterns. The chart reveals that the strongest lift values are concentrated in a small number of rules: vegetable-combination rules for produce-focused segments (Regulars, Promoters) and technology cross-sell rules (Techies, Economizers). These high-lift rules are the primary candidates for campaign deployment because they represent the strongest statistical evidence that promoting item B to a customer who bought item A will generate a genuine incremental purchase rather than recovering a purchase that would have occurred anyway. Lower-lift rules remain valid but justify smaller promotional incentives.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 2: Confidence vs lift scatter
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Confidence vs. lift across all segments</div>
</div>
""", unsafe_allow_html=True)
    scatter_fig = px.scatter(
        rules_df,
        x="confidence",
        y="lift",
        color="segment",
        hover_data={"if_buys": True, "promote": True, "segment": True, "confidence": ":.2f", "lift": ":.2f"},
        labels={"confidence": "Confidence", "lift": "Lift", "segment": "Segment"}
    )
    scatter_fig.update_traces(marker=dict(size=10))
    scatter_fig.update_layout(margin=dict(l=40, r=20, t=60, b=60), height=420, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(scatter_fig, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>Confidence and lift are complementary metrics that together characterise the commercial quality of an association rule. Confidence measures the conditional probability that a customer who buys the antecedent will also buy the consequent; lift adjusts this probability for the base rate of the consequent across all transactions. Rules positioned in the upper-right quadrant of this scatter plot (high confidence and high lift) represent the strongest candidates for campaign deployment: they are both reliable (customers who trigger the rule frequently also complete the recommended purchase) and non-trivial (the co-purchase is substantially more likely than random). Rules with high confidence but modest lift may reflect a consequent that is purchased frequently regardless of the antecedent, diminishing the causal interpretation of the rule. Rules with high lift but low confidence identify genuine but infrequent co-purchase patterns that may be better suited to targeted micro-campaigns than broad promotional rollouts.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div style='height:1px; background:#e5e7eb; margin-bottom:24px;'></div>", unsafe_allow_html=True)

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
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>Conclusion & Recommendations</h2>
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
    <div style='margin-top: 0px; margin-bottom: 24px;'>
        <h2 style='font-size: 56px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.03em;'>Customer Simulator</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>Simulate a customer's spending and complaints behavior to classify them into their most likely K-Means segment. The simulator uses the overall averages from the dataset to compute a normalized Euclidean distance to each segment centroid, assigning the simulated customer to the nearest community in real-time.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-bottom:28px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>How to Play</div>
      <p style='font-size:16px; color:#374151; line-height:1.9; margin:0;'>
        A virtual customer arrives with a pre-loaded basket. Add items you think they would buy, then checkout.
        After checkout, guess which of the eight customer segments they belong to based on their purchases.
        Score a point for every correct identification. Can you beat the algorithm?
      </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Data ─────────────────────────────────────────────────────────────
    _SHOP_EMOJI = {
        "airpods":"🎧","almonds":"🥜","antioxydant juice":"🧃","asparagus":"🌿",
        "avocado":"🥑","babies food":"👶","bacon":"🥓","barbecue sauce":"🍖",
        "beer":"🍺","black beer":"🍺","black tea":"🫖","blueberries":"🫐",
        "bluetooth headphones":"🎧","body spray":"✨","bramble":"🌿","brownies":"🍫",
        "burger sauce":"🍔","burgers":"🍔","butter":"🧈","cake":"🎂",
        "candy bars":"🍬","canned_tuna":"🐟","carrots":"🥕","cat food":"🐈",
        "catfish":"🐟","cauliflower":"🥦","cereals":"🥣","champagne":"🥂",
        "chicken":"🍗","chili":"🌶","chocolate":"🍫","chocolate bread":"🍫",
        "chutney":"🫙","cider":"🍺","cologne":"🧴","cookies":"🍪",
        "cooking oil":"🫙","corn":"🌽","cottage cheese":"🧀","cotton buds":"🪥",
        "cream":"🥛","deodorant":"💨","dessert wine":"🍷","dog food":"🐕",
        "eggplant":"🍆","eggs":"🥚","energy bar":"⚡","energy drink":"⚡",
        "escalope":"🥩","extra dark chocolate":"🍫","final fantasy XIX":"🎮",
        "final fantasy XX":"🎮","final fantasy XXII":"🎮","flax seed":"🌾",
        "french fries":"🍟","french wine":"🍷","fresh bread":"🍞","fresh tuna":"🐟",
        "fromage blanc":"🧀","frozen smoothie":"🥤","frozen vegetables":"🥦",
        "gadget for tiktok streaming":"📱","gluten free bar":"💪","grated cheese":"🧀",
        "green beans":"🫘","green grapes":"🍇","green tea":"🍵","ground beef":"🥩",
        "gums":"🫧","half-life 2":"🎮","half-life: alyx":"🎮","ham":"🥩",
        "hand protein bar":"💪","herb & pepper":"🌿","honey":"🍯","hot dogs":"🌭",
        "iMac":"🖥","iPad":"📱","iphone 10":"📱","ketchup":"🍅","laptop":"💻",
        "light cream":"🥛","light mayo":"🫙","low fat yogurt":"🍦",
        "mashed potato":"🥔","mayonnaise":"🫙","meatballs":"🍖",
        "megaman zero":"🤖","megaman zero 2":"🤖","megaman zero 3":"🤖",
        "megaman zero 4":"🤖","melons":"🍈","metroid fusion":"🎮","metroid prime":"🎮",
        "milk":"🥛","minecraft":"⛏","mineral water":"💧","mint":"🌿",
        "mint green tea":"🍵","muffins":"🧁","mushroom cream sauce":"🍄",
        "napkins":"🧻","nonfat milk":"🥛","oatmeal":"🌾","oil":"🫙","olive oil":"🫙",
        "pancakes":"🥞","parmesan cheese":"🧀","pasta":"🍝","pepper":"🫑",
        "pet food":"🐾","phone car charger":"🔌","phone charger":"🔌","pickles":"🥒",
        "pokemon scarlet":"🎮","pokemon shield":"🎮","pokemon sword":"🎮",
        "pokemon violet":"🎮","portal":"🎮","portal 2":"🎮","protein bar":"💪",
        "ratchet & clank":"🎮","ratchet & clank 2":"🎮","ratchet & clank 3":"🎮",
        "razor":"🪒","red wine":"🍷","rice":"🍚","ring light":"💡","salad":"🥗",
        "salmon":"🐟","salt":"🧂","samsung galaxy 10":"📱","sandwich":"🥪",
        "seabass":"🐟","shallot":"🧅","shampoo":"🧴","shower gel":"🚿",
        "shrimp":"🦐","soda":"🥤","soup":"🍲","spaghetti":"🍝",
        "sparkling water":"💧","spinach":"🥬","strawberries":"🍓",
        "strong cheese":"🧀","tea":"☕","toilet paper":"🧻","tomato juice":"🧃",
        "tomato sauce":"🍅","tomatoes":"🍅","tooth brush":"🪥","toothpaste":"🦷",
        "trout":"🐟","turkey":"🦃","vacuum cleaner":"🧹","vegetables mix":"🥦",
        "water spray":"💦","white wine":"🍾","whole weat flour":"🌾",
        "whole wheat pasta":"🍝","whole wheat rice":"🍚","yams":"🍠",
        "yogurt cake":"🍰","zucchini":"🥒",
    }
    _SHOP_PRICES = {
        "airpods":49.99,"almonds":3.99,"antioxydant juice":2.99,"asparagus":2.49,
        "avocado":1.99,"babies food":3.99,"bacon":4.99,"barbecue sauce":2.49,
        "beer":1.99,"black beer":2.49,"black tea":2.29,"blueberries":2.99,
        "bluetooth headphones":39.99,"body spray":6.99,"bramble":1.79,"brownies":3.49,
        "burger sauce":1.99,"burgers":5.99,"butter":2.79,"cake":4.99,
        "candy bars":1.99,"canned_tuna":2.49,"carrots":1.29,"cat food":4.99,
        "catfish":7.99,"cauliflower":1.99,"cereals":3.49,"champagne":24.99,
        "chicken":6.99,"chili":2.29,"chocolate":2.49,"chocolate bread":2.99,
        "chutney":2.99,"cider":2.49,"cologne":19.99,"cookies":2.49,
        "cooking oil":3.99,"corn":1.29,"cottage cheese":2.99,"cotton buds":1.99,
        "cream":1.99,"deodorant":4.49,"dessert wine":12.99,"dog food":5.99,
        "eggplant":1.49,"eggs":2.99,"energy bar":1.99,"energy drink":1.99,
        "escalope":8.99,"extra dark chocolate":3.49,"final fantasy XIX":59.99,
        "final fantasy XX":59.99,"final fantasy XXII":59.99,"flax seed":3.49,
        "french fries":2.99,"french wine":14.99,"fresh bread":2.29,"fresh tuna":9.99,
        "fromage blanc":2.29,"frozen smoothie":3.49,"frozen vegetables":2.99,
        "gadget for tiktok streaming":29.99,"gluten free bar":2.49,"grated cheese":3.49,
        "green beans":1.99,"green grapes":2.49,"green tea":2.49,"ground beef":7.99,
        "gums":1.49,"half-life 2":14.99,"half-life: alyx":39.99,"ham":4.99,
        "hand protein bar":2.99,"herb & pepper":1.99,"honey":4.49,"hot dogs":3.49,
        "iMac":1299.99,"iPad":399.99,"iphone 10":799.99,"ketchup":1.99,
        "laptop":899.99,"light cream":1.79,"light mayo":1.99,"low fat yogurt":1.99,
        "mashed potato":1.99,"mayonnaise":2.29,"meatballs":5.99,
        "megaman zero":19.99,"megaman zero 2":19.99,"megaman zero 3":19.99,
        "megaman zero 4":19.99,"melons":2.99,"metroid fusion":19.99,"metroid prime":19.99,
        "milk":1.49,"minecraft":19.99,"mineral water":0.99,"mint":0.99,
        "mint green tea":2.79,"muffins":2.99,"mushroom cream sauce":3.49,
        "napkins":1.99,"nonfat milk":1.49,"oatmeal":2.49,"oil":3.49,"olive oil":5.99,
        "pancakes":2.99,"parmesan cheese":4.49,"pasta":1.99,"pepper":1.29,
        "pet food":5.49,"phone car charger":19.99,"phone charger":19.99,"pickles":2.29,
        "pokemon scarlet":59.99,"pokemon shield":59.99,"pokemon sword":59.99,
        "pokemon violet":59.99,"portal":9.99,"portal 2":9.99,"protein bar":2.99,
        "ratchet & clank":19.99,"ratchet & clank 2":19.99,"ratchet & clank 3":19.99,
        "razor":4.99,"red wine":8.99,"rice":1.99,"ring light":24.99,"salad":1.99,
        "salmon":8.99,"salt":0.99,"samsung galaxy 10":399.99,"sandwich":3.49,
        "seabass":9.99,"shallot":0.99,"shampoo":5.99,"shower gel":3.99,"shrimp":9.99,
        "soda":1.29,"soup":3.49,"spaghetti":1.99,"sparkling water":1.29,
        "spinach":1.79,"strawberries":2.99,"strong cheese":4.49,"tea":2.29,
        "toilet paper":3.99,"tomato juice":1.99,"tomato sauce":1.99,"tomatoes":1.99,
        "tooth brush":2.99,"toothpaste":3.49,"trout":7.99,"turkey":7.99,
        "vacuum cleaner":89.99,"vegetables mix":2.49,"water spray":2.99,
        "white wine":9.99,"whole weat flour":2.49,"whole wheat pasta":2.29,
        "whole wheat rice":2.49,"yams":2.49,"yogurt cake":3.49,"zucchini":1.29,
    }
    _SHOP_CATEGORIES = {
        "🥦 Produce":["asparagus","avocado","blueberries","bramble","carrots","cauliflower",
            "corn","eggplant","frozen vegetables","green beans","green grapes",
            "herb & pepper","melons","mint","pepper","salad","shallot","spinach",
            "strawberries","tomatoes","vegetables mix","yams","zucchini"],
        "🥛 Dairy":["butter","cottage cheese","cream","fromage blanc","grated cheese",
            "light cream","low fat yogurt","milk","nonfat milk","parmesan cheese","strong cheese"],
        "🍞 Bakery":["cake","cereals","chocolate bread","cookies","fresh bread","muffins",
            "oatmeal","pancakes","whole weat flour","whole wheat pasta","whole wheat rice","yogurt cake"],
        "🍗 Meat & Fish":["bacon","burgers","catfish","chicken","escalope","fresh tuna",
            "ground beef","ham","hot dogs","meatballs","salmon","sandwich","seabass",
            "shrimp","trout","turkey","canned_tuna"],
        "🍷 Drinks":["antioxydant juice","beer","black beer","black tea","champagne","cider",
            "dessert wine","energy drink","french wine","frozen smoothie","green tea",
            "mineral water","mint green tea","red wine","soda","sparkling water","tea",
            "tomato juice","white wine"],
        "🥫 Pantry":["almonds","barbecue sauce","brownies","candy bars","chili","chocolate",
            "chutney","cooking oil","energy bar","extra dark chocolate","flax seed",
            "french fries","gluten free bar","hand protein bar","honey","ketchup",
            "light mayo","mashed potato","mayonnaise","mushroom cream sauce","oil","olive oil",
            "pasta","pickles","protein bar","rice","salt","soup","spaghetti","tomato sauce"],
        "🧴 Hygiene":["body spray","cologne","cotton buds","deodorant","gums","napkins",
            "razor","shampoo","shower gel","toilet paper","tooth brush","toothpaste","water spray"],
        "🐾 Pet & Baby":["babies food","cat food","dog food","pet food"],
        "📱 Electronics":["airpods","bluetooth headphones","gadget for tiktok streaming",
            "iMac","iPad","iphone 10","laptop","phone car charger","phone charger",
            "ring light","samsung galaxy 10","vacuum cleaner"],
        "🎮 Games":["final fantasy XIX","final fantasy XX","final fantasy XXII",
            "half-life 2","half-life: alyx","megaman zero","megaman zero 2",
            "megaman zero 3","megaman zero 4","metroid fusion","metroid prime","minecraft",
            "pokemon scarlet","pokemon shield","pokemon sword","pokemon violet",
            "portal","portal 2","ratchet & clank","ratchet & clank 2","ratchet & clank 3"],
    }
    _SHOP_SEGMENTS = {
        "👨‍👩‍👧 Families": {
            "desc": "Bread, eggs, cereals, butter, tea",
            "top": ["eggs","cereals","fresh bread","butter","bacon","tea","honey",
                    "sandwich","oatmeal","milk","black tea","chocolate bread","salt",
                    "oil","whole weat flour","cooking oil"],
        },
        "🧴 Techies": {
            "desc": "Shower gel, deodorant, shampoo, protein bars",
            "top": ["shower gel","tooth brush","deodorant","shampoo","toothpaste",
                    "razor","cotton buds","body spray","antioxydant juice","energy bar",
                    "protein bar","toilet paper","almonds","gluten free bar",
                    "nonfat milk","green tea","low fat yogurt"],
        },
        "🥦 Vegetarians": {
            "desc": "Dog food, babies food, pasta, chicken",
            "top": ["napkins","dog food","babies food","cooking oil","pet food","chicken",
                    "cat food","rice","spaghetti","pasta","meatballs","milk",
                    "toilet paper","fresh bread","cereals","soup","tomato sauce",
                    "mayonnaise","eggs","ketchup"],
        },
        "🎮 Regulars": {
            "desc": "Airpods, headphones, games, ring light",
            "top": ["final fantasy XX","ratchet & clank 3","metroid fusion",
                    "final fantasy XIX","ring light","bluetooth headphones",
                    "final fantasy XXII","phone car charger","airpods","pokemon sword",
                    "gadget for tiktok streaming","vacuum cleaner","pokemon shield",
                    "energy drink","iPad","ratchet & clank","portal 2","minecraft","portal"],
        },
        "🏷 Promoters": {
            "desc": "Tomatoes, carrots, spinach, fruits, laptop",
            "top": ["tomatoes","carrots","spinach","eggplant","laptop","strawberries",
                    "salad","corn","green beans","green grapes","asparagus","avocado",
                    "blueberries","cauliflower","frozen vegetables"],
        },
        "💰 Economizers": {
            "desc": "Spinach, tomatoes, carrots, avocado, berries",
            "top": ["spinach","tomatoes","carrots","avocado","strawberries","green beans",
                    "salad","green grapes","corn","zucchini","asparagus","blueberries",
                    "mineral water","cauliflower","mashed potato","eggplant"],
        },
        "⭐ Loyalists": {
            "desc": "Champagne, beer, french wine, iMac, pasta",
            "top": ["phone car charger","iMac","whole wheat pasta","flax seed",
                    "megaman zero 4","champagne","beer","mushroom cream sauce",
                    "half-life 2","final fantasy XIX","french wine","french fries",
                    "pickles","green beans","light mayo","melons","gums","turkey"],
        },
        "🧘 Wellness": {
            "desc": "Red wine, salmon, gaming, cologne, yams",
            "top": ["red wine","bramble","yams","black beer","portal","seabass",
                    "ratchet & clank 3","pokemon sword","megaman zero","cologne",
                    "ratchet & clank 2","ratchet & clank","cottage cheese","half-life 2",
                    "french fries","portal 2","metroid prime","salmon","samsung galaxy 10"],
        },
    }
    _SHOP_NAMES = ["Alice","Bruno","Carla","David","Eva","Fábio","Gina","Hugo",
                   "Inês","João","Lara","Miguel","Nuno","Olga","Pedro","Rita"]
    _SHOP_ALL_PRODUCTS = sorted(_SHOP_PRICES.keys())

    # ── Session state helpers ─────────────────────────────────────────────
    def _shop_init():
        defaults = {
            "shop_cart": {},
            "shop_true_seg": "",
            "shop_customer_name": "",
            "shop_checked_out": False,
            "shop_guessed": False,
            "shop_guess_result": None,
            "shop_score": 0,
            "shop_rounds": 0,
            "shop_round_started": False,
        }
        for k, v in defaults.items():
            if k not in st.session_state:
                st.session_state[k] = v

    def _shop_new_round():
        import random as _rnd
        seg = _rnd.choice(list(_SHOP_SEGMENTS.keys()))
        pool = list(_SHOP_SEGMENTS[seg]["top"])
        _rnd.shuffle(pool)
        n = _rnd.randint(5, 9)
        basket = pool[:min(n, len(pool))]
        cart = {}
        for item in basket:
            cart[item] = cart.get(item, 0) + 1
        st.session_state.shop_cart = cart
        st.session_state.shop_true_seg = seg
        st.session_state.shop_customer_name = _rnd.choice(_SHOP_NAMES)
        st.session_state.shop_checked_out = False
        st.session_state.shop_guessed = False
        st.session_state.shop_guess_result = None
        st.session_state.shop_round_started = True

    def _shop_add(product):
        st.session_state.shop_cart[product] = st.session_state.shop_cart.get(product, 0) + 1

    def _shop_remove(product):
        if product in st.session_state.shop_cart:
            if st.session_state.shop_cart[product] > 1:
                st.session_state.shop_cart[product] -= 1
            else:
                del st.session_state.shop_cart[product]

    def _shop_total():
        return sum(_SHOP_PRICES.get(p, 0) * q for p, q in st.session_state.shop_cart.items())

    _shop_init()

    # ── Scoreboard ───────────────────────────────────────────────────────
    _sc1, _sc2, _sc3 = st.columns(3)
    _sc1.metric("Score", st.session_state.shop_score)
    _sc2.metric("Rounds", st.session_state.shop_rounds)
    _shop_acc = (
        f"{round(st.session_state.shop_score / st.session_state.shop_rounds * 100)}%"
        if st.session_state.shop_rounds else "—"
    )
    _sc3.metric("Accuracy", _shop_acc)
    st.divider()

    # ── First start ──────────────────────────────────────────────────────
    if not st.session_state.shop_round_started:
        if st.button("▶ Start — first customer", use_container_width=True, type="primary", key="shop_start_btn"):
            _shop_new_round()
            st.rerun()
        st.stop()

    # ── Customer banner ──────────────────────────────────────────────────
    if not st.session_state.shop_checked_out:
        st.info(
            f"**Customer: {st.session_state.shop_customer_name}** — basket loaded. "
            "Add more items if you like, then checkout."
        )
    else:
        st.info(
            f"**Customer: {st.session_state.shop_customer_name}** checked out — "
            "which segment do they belong to?"
        )

    # ── Layout: shop | cart ──────────────────────────────────────────────
    _shop_col, _cart_col = st.columns([2, 1])

    with _shop_col:
        st.subheader("🏪 Products")
        _cs, _cc = st.columns([2, 1])
        _search = _cs.text_input("Search", placeholder="Search…", label_visibility="collapsed", key="shop_search")
        _cat_filter = _cc.selectbox(
            "Category", ["All"] + list(_SHOP_CATEGORIES.keys()),
            label_visibility="collapsed", key="shop_cat_filter"
        )
        _filtered = _SHOP_ALL_PRODUCTS
        if _cat_filter != "All":
            _filtered = [p for p in _filtered if p in _SHOP_CATEGORIES[_cat_filter]]
        if _search:
            _filtered = [p for p in _filtered if _search.lower() in p.lower()]

        _grid_cols = st.columns(4)
        for _i, _product in enumerate(_filtered):
            with _grid_cols[_i % 4]:
                _qty = st.session_state.shop_cart.get(_product, 0)
                _badge = f" ×{_qty}" if _qty else ""
                _label = f"{_SHOP_EMOJI.get(_product,'🛒')} {_product.title()}{_badge}\n€{_SHOP_PRICES[_product]:.2f}"
                if st.button(_label, key=f"shop_add_{_product}",
                             disabled=st.session_state.shop_checked_out,
                             use_container_width=True):
                    _shop_add(_product)
                    st.rerun()

    with _cart_col:
        st.subheader("🧺 Cart")
        if not st.session_state.shop_cart:
            st.caption("Cart is empty")
        else:
            for _product, _qty in list(st.session_state.shop_cart.items()):
                _ca, _cb, _cc2 = st.columns([3, 2, 1])
                _ca.write(f"{_SHOP_EMOJI.get(_product,'🛒')} {_product.title()}")
                _cb.write(f"×{_qty}  **€{_SHOP_PRICES[_product]*_qty:.2f}**")
                if not st.session_state.shop_checked_out:
                    if _cc2.button("✕", key=f"shop_rm_{_product}"):
                        _shop_remove(_product)
                        st.rerun()
            st.write(f"**Total: €{_shop_total():.2f}**")

        st.divider()

        if not st.session_state.shop_checked_out:
            if st.session_state.shop_cart:
                if st.button("💳 Checkout", use_container_width=True, type="primary", key="shop_checkout_btn"):
                    st.session_state.shop_checked_out = True
                    st.rerun()
        else:
            if not st.session_state.shop_guessed:
                st.write("**Which segment?**")
                for _seg_name, _seg_data in _SHOP_SEGMENTS.items():
                    if st.button(
                        f"{_seg_name}\n*{_seg_data['desc']}*",
                        key=f"shop_guess_{_seg_name}",
                        use_container_width=True
                    ):
                        _correct = _seg_name == st.session_state.shop_true_seg
                        st.session_state.shop_guessed = True
                        st.session_state.shop_guess_result = _correct
                        st.session_state.shop_rounds += 1
                        if _correct:
                            st.session_state.shop_score += 1
                        st.rerun()
            else:
                _true = st.session_state.shop_true_seg
                _info = _SHOP_SEGMENTS[_true]
                if st.session_state.shop_guess_result:
                    st.success(f"✅ **{_true}**\n\n*{_info['desc']}*")
                else:
                    st.error(f"❌ It was **{_true}**\n\n*{_info['desc']}*")
                if st.button("▶ Next customer", use_container_width=True, type="primary", key="shop_next_btn"):
                    _shop_new_round()
                    st.rerun()

    render_footer()
