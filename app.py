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
    min-width: 260px;
    max-width: 300px;
    position: relative;
    border-right: 1px solid rgba(0,0,0,0.06) !important;
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
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 0 !important;
    padding-bottom: 1rem !important;
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
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input[type="radio"]:checked) {
    color: #1a1208 !important;
    background-color: rgba(0,0,0,0.1) !important;
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(1):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>');
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(2):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>');
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(3):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>');
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(4):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>');
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(5):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>');
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(6):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>');
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(7):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="m9 12 2 2 4-4"/></svg>');
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
[data-testid="stSidebar"] div[role="radiogroup"] label:nth-of-type(8):has(input[type="radio"]:checked)::before {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%231a1208" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>');
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
    # Render Mockup Top Banner
    st.markdown(f"""
    <div style='display: flex; align-items: center; gap: 48px; margin-top: -48px; margin-bottom: 16px; font-family: "Plus Jakarta Sans", "Inter", sans-serif;'>
        <div style='flex: 1;'>
            <h1 style='font-size: 96px; font-weight: 800; color: #000000; line-height: 1.0; margin: 0 0 20px 0; letter-spacing: -0.04em;'>Understand every customer.<br/>Grow with purpose.</h1>
            <p style='font-size: 17px; color: #5f6368; line-height: 1.7; margin: 0; max-width: 520px;'>A machine learning project that segments 34,060 supermarket customers into 8 distinct communities — uncovering who they are, how they shop, and what drives their decisions.</p>
        </div>
        <div style='flex: none; display: flex; flex-direction: column; gap: 28px; white-space: nowrap;'>
            <div>
                <div style='font-size: 52px; font-weight: 800; color: #000000; line-height: 1;'>34,060</div>
                <div style='font-size: 14px; color: #5f6368; margin-top: 4px;'>customers analyzed</div>
            </div>
            <div>
                <div style='font-size: 52px; font-weight: 800; color: #000000; line-height: 1;'>8</div>
                <div style='font-size: 14px; color: #5f6368; margin-top: 4px;'>communities discovered</div>
            </div>
        </div>
        <img src='{CESTO_URI}' style='height: 700px; width: auto; object-fit: contain; flex: none;' />
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
      .ov-grid {{ display:grid; grid-template-columns:repeat(8,1fr); gap:10px; width:100%; box-sizing:border-box; }}
      .ov-card {{ background:#fff; border:1px solid #e5e7eb; border-radius:14px; padding:16px 14px;
                  display:flex; flex-direction:column; justify-content:space-between; min-height:510px; }}
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
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Data Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 00 — Data Analysis</div>
      <p style='font-size:16px; color:#374151; line-height:1.8; margin:0 0 14px 0;'>
        Before any modelling decisions are made, the raw <code>customer_info.csv</code> dataset is subjected to a thorough exploratory analysis. The dataset contains <strong>33,038 unique customers</strong> described across <strong>21 numerical variables</strong> and a set of categorical and identifier fields. This notebook's purpose is diagnostic: no cleaning or transformation is applied here — every finding is deferred to the preprocessing stage.
      </p>
      <p style='font-size:16px; color:#374151; line-height:1.8; margin:0 0 24px 0;'>
        The analysis checks for exact and logical duplicates (customers matched by name and birthdate), inspects missing value rates per feature, categorises all columns, and produces distribution plots and boxplots for every numerical variable. A skewness table is computed to quantify the degree of asymmetry in each spending feature.
      </p>

      <div style='display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:28px;'>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:18px 20px;'>
          <div style='font-size:28px; font-weight:800; color:#111827; line-height:1;'>33,038</div>
          <div style='font-size:13px; color:#6b7280; margin-top:4px;'>unique customers in raw dataset</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:18px 20px;'>
          <div style='font-size:28px; font-weight:800; color:#111827; line-height:1;'>21</div>
          <div style='font-size:13px; color:#6b7280; margin-top:4px;'>numerical variables identified</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:18px 20px;'>
          <div style='font-size:28px; font-weight:800; color:#111827; line-height:1;'>30%</div>
          <div style='font-size:13px; color:#6b7280; margin-top:4px;'>missing value threshold for feature exclusion</div>
        </div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Missing value strategy</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Features with more than 30% missing values were flagged as too sparse to impute reliably. The inspection confirmed that missing values are concentrated in a limited group of behavioural and spend variables, supporting imputation over row-dropping — the customer base does not need to be reduced.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Education level as a proxy feature</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Customer names contain academic prefixes — BSc., MSc., PhD. — across all 33,038 unique names. These prefixes are flagged as an education-level proxy and earmarked for feature engineering in Notebook 1. Surname repetition alone was found to be too common to be a useful household signal; it was not carried into the modelling feature set.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Impossible values detected</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'><code>percentage_of_products_bought_promotion</code> was found to contain values outside the valid [0, 1] range — both below 0.0 and above 1.0 — indicating data entry errors. These are flagged here and corrected in preprocessing. Spending variables show strong right-skew, confirming that a small group of customers spends disproportionately more than the majority.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:8px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Duplicate check</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'>No exact duplicate rows were found. A logical duplicate check (matching on customer name AND birthdate) was also performed. A surname-only proximity test was also run but produced too many false positives due to common surnames. The conclusion is that the dataset does not contain systematic duplicate records requiring removal.</div>
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
    ).properties(height=max(200, len(missing_pct) * 22), title="Missing values per feature (%)")
    threshold_line = alt.Chart(pd.DataFrame({"threshold": [30]})).mark_rule(color="#ef4444", strokeDash=[6, 3], strokeWidth=2).encode(
        x="threshold:Q"
    )
    st.altair_chart((base_missing + threshold_line), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The 30% threshold (red dashed line) was chosen as the boundary above which imputation is judged unreliable: reconstructing more than three out of ten values for a given feature would introduce more noise than signal into the dataset. Features below this threshold retain sufficient observed data to support KNN imputation, which leverages the similarity structure of the customer base. The chart confirms that missing values are concentrated in a small number of behavioural variables, and that no feature exceeds the threshold by a large margin, making row-dropping unnecessary. The majority of the 33,038 customers remain usable across all features.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 2: Distribution of key numerical features
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Distribution of key numerical features</div>
</div>
""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    hist_groceries = alt.Chart(customer_info.dropna(subset=["lifetime_spend_groceries"])).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("lifetime_spend_groceries:Q", bin=alt.Bin(maxbins=30), title="Groceries spend"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(title="Lifetime spend: Groceries", height=280)
    hist_electronics = alt.Chart(customer_info.dropna(subset=["lifetime_spend_electronics"])).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("lifetime_spend_electronics:Q", bin=alt.Bin(maxbins=30), title="Electronics spend"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(title="Lifetime spend: Electronics", height=280)
    hist_products = alt.Chart(customer_info.dropna(subset=["lifetime_total_distinct_products"])).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("lifetime_total_distinct_products:Q", bin=alt.Bin(maxbins=30), title="Distinct products"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(title="Total distinct products", height=280)
    c1.altair_chart(hist_groceries, use_container_width=True)
    c2.altair_chart(hist_electronics, use_container_width=True)
    c3.altair_chart(hist_products, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>All three distributions exhibit pronounced right-skew: the mass of customers clusters near the lower end of the scale, with a progressively thinner tail extending toward high-spending or high-variety individuals. This asymmetry has two direct implications for modelling. First, standard Euclidean distance in clustering is sensitive to scale differences, meaning that a small group of high-spending customers could disproportionately pull cluster centroids if the data are not scaled. Second, the long tail is precisely where the consensus outlier separation strategy intervenes: rather than capping values, the most extreme multivariate observations are separated into a dedicated outlier dataset before the clustering model is fitted, preserving the shape of the majority distribution while removing undue influence from the periphery.</p>
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
    ).properties(height=300, title="Promotion ratio distribution (filtered to [0, 1])")
    st.altair_chart(promo_hist, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The raw dataset contains entries for <code>percentage_of_products_bought_promotion</code> that fall outside the physically valid interval [0, 1], including both negative values and values exceeding 1.0. These are impossible by definition: a proportion cannot be negative or greater than unity, confirming data entry errors rather than extreme but valid behaviour. The chart above is restricted to the valid range only. Within [0, 1], the distribution is roughly bimodal: a concentration of customers near 0.4 to 0.6 suggests a moderately promotion-responsive majority, while a second mass near 1.0 identifies a distinct group of near-exclusively promotional buyers. This heterogeneity in promotional sensitivity later becomes one of the most discriminating variables in the clustering model, most clearly visible in the Promoters segment.</p>
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
    ).properties(height=300, title="Customer gender distribution")
    st.altair_chart(gender_bar, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The gender distribution across the customer base is approximately balanced between male and female customers, with no category representing an extreme minority. This near-parity is relevant for segmentation methodology: a heavily skewed gender distribution would risk producing segments that reflect gender composition artefacts rather than genuine behavioural differences. The approximate balance observed here supports the interpretation that the eight clusters recovered by the model reflect spending behaviour and lifestyle patterns rather than demographic overrepresentation of one group. Gender is retained as a profiling variable for segment characterisation but is not included in the clustering distance matrix.</p>
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
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>All spend categories exhibit positive skewness, confirming that the right-tailed pattern observed in the histograms above is not isolated to groceries and electronics but is systematic across the entire spend feature space. High positive skewness (values substantially above 1.0) indicates that a small number of customers account for a disproportionate share of category-level spending. This has two direct consequences for preprocessing: first, lifetime spend values are converted to annual rates by dividing by tenure, to reduce the contribution of long-tenure customers to the skew; second, the consensus outlier separation rule is applied before clustering to set aside the most extreme multivariate observations. Skewness alone does not justify removing observations, but it confirms the need for careful outlier treatment before distance-based clustering is applied.</p>
</div>
""", unsafe_allow_html=True)

    # Chart: Numeric boxplots (from NB00)
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
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The boxplots confirm the systematic right-skew identified in the histograms: every numerical variable shows a compact interquartile box close to the lower end of its range and a long upper whisker or visible outlier cloud extending far to the right. Median values across spending categories are low relative to the scale maximum, meaning that the majority of customers spend modestly while a thin tail of high-value customers accounts for most of the category-level variance. Variables such as total lifetime spend and electronics show particularly extreme upper outliers, reinforcing the need for the consensus outlier separation step prior to scaling. Age and tenure, by contrast, are more symmetric but still show a modest right tail in tenure, consistent with a customer base accumulated over multiple years of varying acquisition rates. These shapes collectively justify the MinMaxScaler choice over standard z-score normalisation: min-max compression bounds all features to [0, 1] while preserving the relative magnitude ordering within each variable, which is important when inter-feature comparisons are made in UMAP visualisations.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding:24px; border-radius:16px; background:#f9fafb; border:1px solid #e5e7eb; margin-top:12px;'>
          <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 00 — Conclusions</div>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0 0 10px 0;'>"The raw customer data contains missing values, skewed spending variables, identifier columns, date fields and several variables that require type conversion before modelling. These findings motivate the preprocessing notebook, where invalid values are handled, categorical variables are encoded and outliers are addressed."</p>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0 0 10px 0;'>"The distribution plots confirm that spending variables are highly skewed. This supports two later decisions: separating the most atypical customers before fitting the clustering model, and leaving scaling as a modelling choice."</p>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>"The missing value inspection shows that the dataset is usable without dropping large parts of the customer base." No cleaning is applied in this notebook — all transformations are deferred to NB01.</p>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

elif selected_page == "Data Preprocessing":
    st.markdown("""
    <div style='margin-top: 48px; margin-bottom: 24px;'>
        <h2 style='font-size: 28px; font-weight: 800; color: #000000; margin: 0; letter-spacing: -0.02em;'>Data Preprocessing</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 01 — Data Preprocessing</div>
      <p style='font-size:16px; color:#374151; line-height:1.8; margin:0 0 14px 0;'>
        This notebook applies all transformations identified during the exploratory analysis. The goal is to produce a clean, analysis-ready dataset without losing customers unnecessarily. Every decision is justified by domain logic or statistical evidence — no arbitrary removals are made.
      </p>

      <div style='display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-bottom:28px;'>
        <div>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:12px;'>Corrections applied</div>
          <div style='display:flex; flex-direction:column; gap:10px;'>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Future transaction years → NaN</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Values of <code>year_first_transaction</code> exceeding the current year are data entry errors. Set to NaN rather than dropping the entire customer row.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Invalid promotion ratio → NaN</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'><code>percentage_of_products_bought_promotion</code> values outside [0, 1] are nulled. These are physically impossible and cannot be imputed.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Zero-imputation for count columns</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'><code>kids_home</code>, <code>teens_home</code>, and <code>number_complaints</code> receive zero imputation. Domain logic: a missing count means the event was not recorded, which is equivalent to zero.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Longitude: negative values kept</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Negative longitudes are geographically valid for Portugal (west of the Greenwich meridian) and are not treated as errors.</div>
            </div>
          </div>
        </div>
        <div>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:12px;'>Feature engineering</div>
          <div style='display:flex; flex-direction:column; gap:10px;'>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>tenure (years since first transaction)</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Replaces <code>year_first_transaction</code> to avoid redundancy and make the feature directly interpretable as relationship length.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>typical_hour_sin / typical_hour_cos</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Cyclic transformation of <code>typical_hour</code> (max=24). Preserves the circular nature of time: 23:00 and 01:00 are adjacent, not distant.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Annual spend rates</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Lifetime spend divided by tenure to normalise for relationship length. A customer of 2 years and a customer of 15 years spending the same total are very different profiles.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>lifetime_spend_technology</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Aggregate of electronics + videogames spend, capturing total technology investment as a single signal.</div>
            </div>
          </div>
        </div>
      </div>

      <div style='border-top:1px solid #e5e7eb; padding-top:24px; margin-bottom:24px;'>
        <div style='font-size:14px; font-weight:700; color:#111827; margin-bottom:14px;'>Outlier separation — the consensus rule</div>
        <p style='font-size:14px; color:#374151; line-height:1.8; margin:0 0 12px 0;'>
          Rather than capping or removing outliers based on a single method, a <strong>conservative consensus rule</strong> is applied: a customer is set aside only when simultaneously flagged as an outlier by all three of the following methods:
        </p>
        <div style='display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:12px;'>
          <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px; text-align:center;'>
            <div style='font-size:13px; font-weight:700; color:#111827;'>IQR</div>
            <div style='font-size:22px; font-weight:800; color:#111827; margin:4px 0;'>k = 2.0</div>
            <div style='font-size:12px; color:#6b7280;'>multiplier</div>
          </div>
          <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px; text-align:center;'>
            <div style='font-size:13px; font-weight:700; color:#111827;'>DBSCAN</div>
            <div style='font-size:22px; font-weight:800; color:#111827; margin:4px 0;'>eps = 1.0</div>
            <div style='font-size:12px; color:#6b7280;'>neighbourhood radius</div>
          </div>
          <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px; text-align:center;'>
            <div style='font-size:13px; font-weight:700; color:#111827;'>3rd method</div>
            <div style='font-size:22px; font-weight:800; color:#111827; margin:4px 0;'>∩</div>
            <div style='font-size:12px; color:#6b7280;'>all three must agree</div>
          </div>
        </div>
        <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>
          Customers flagged by all three methods are exported to <code>outlier_dataset.csv</code>. The regular base is then processed with KNN imputation. This approach ensures that only multivariate extremes are removed — customers with one extreme variable but otherwise normal behaviour are retained. Outliers are later <strong>reattached to their nearest cluster centroid</strong> after the model is fitted.
        </p>
      </div>

      <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Why export unscaled?</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'>The final dataset is exported <strong>without scaling</strong>. Scaling is treated as a modelling choice — MinMaxScaler and RobustScaler are both evaluated in Notebook 3 against each other. Keeping the export unscaled ensures that the same raw dataset can be tested against any scaling strategy without re-running preprocessing.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    customer_info_pre = pd.read_csv(BASE_DIR / "datasets" / "customer_info.csv")
    info_unscaled = pd.read_csv(BASE_DIR / "datasets" / "info_clustering_unscaled.csv")
    outlier_df = pd.read_csv(BASE_DIR / "datasets" / "outlier_dataset.csv")

    # Chart 1: Age distribution
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Customer age distribution</div>
</div>
""", unsafe_allow_html=True)
    customer_info_pre["customer_birthdate"] = pd.to_datetime(customer_info_pre["customer_birthdate"], errors="coerce")
    customer_info_pre["customer_age"] = 2024 - customer_info_pre["customer_birthdate"].dt.year
    age_clean = customer_info_pre.dropna(subset=["customer_age"])
    age_hist = alt.Chart(age_clean).mark_bar(color="#374151", opacity=0.85).encode(
        x=alt.X("customer_age:Q", bin=alt.Bin(maxbins=25), title="Age (years)"),
        y=alt.Y("count():Q", title="Customers"),
        tooltip=[alt.Tooltip("count():Q", title="Customers")]
    ).properties(height=300, title="Customer age distribution")
    st.altair_chart(age_hist, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The age distribution spans a wide range, with the dominant band falling in the 30 to 50 year range. Rather than using the raw birthdate field directly as a feature, age is engineered as the difference between the reference year 2024 and the birth year extracted from the <code>customer_birthdate</code> timestamp column. This approach resolves two issues: the raw birthdate is a datetime string containing hours and minutes that carry no meaningful information for customer profiling, and storing birthdates directly would introduce a non-linear relationship with time that is harder to interpret in a distance-based model. The resulting <code>customer_age</code> integer is directly interpretable as years of age and is used as a profiling variable in segment characterisation, though it is not included in the clustering feature set to avoid confounding behavioural differences with demographic age effects.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 2: Cyclic hour encoding
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Cyclic encoding of typical shopping hour</div>
</div>
""", unsafe_allow_html=True)
    hour_scatter = alt.Chart(info_unscaled.sample(min(5000, len(info_unscaled)), random_state=42)).mark_circle(color="#374151", opacity=0.3, size=10).encode(
        x=alt.X("typical_hour_sin:Q", title="sin(hour)", scale=alt.Scale(domain=[-1.1, 1.1])),
        y=alt.Y("typical_hour_cos:Q", title="cos(hour)", scale=alt.Scale(domain=[-1.1, 1.1])),
        tooltip=["typical_hour_sin", "typical_hour_cos"]
    ).properties(height=380, title="Cyclic encoding of typical shopping hour")
    st.altair_chart(hour_scatter, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The raw <code>typical_hour</code> variable is an integer in [0, 23] representing the most common hour of shopping. Using this integer directly in a clustering distance metric creates a topological error: hour 23 and hour 0 are adjacent in real time but maximally distant numerically (a difference of 23). Sine and cosine encoding resolves this by mapping the circular hour dimension onto a two-dimensional unit circle, where every pair of adjacent hours is equally close regardless of where the boundary between days falls. The scatter plot above confirms that the encoding is correct: points form a circular arc pattern, and the density is distributed smoothly around the circle rather than clustering at the numerical extremes. Customers who shop at 23:00 and those who shop at 01:00 are now correctly represented as near-neighbours in feature space.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 3: Spend boxplots after preprocessing
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Annual spend per category after preprocessing</div>
</div>
""", unsafe_allow_html=True)
    annual_cols = ["annual_spend_groceries", "annual_spend_electronics", "annual_spend_vegetables", "annual_spend_meat", "annual_spend_fish", "annual_spend_hygiene"]
    spend_melt = info_unscaled[annual_cols].melt(var_name="category", value_name="annual_spend")
    spend_melt["category"] = spend_melt["category"].str.replace("annual_spend_", "", regex=False).str.replace("_", " ").str.title()
    spend_melt = spend_melt.dropna(subset=["annual_spend"])
    box_chart_pre = alt.Chart(spend_melt).mark_boxplot(color="#374151", outliers={"size": 4, "opacity": 0.2}).encode(
        x=alt.X("category:N", title="Category"),
        y=alt.Y("annual_spend:Q", title="Annual spend"),
        tooltip=["category"]
    ).properties(height=360, title="Annual spend per category after preprocessing")
    st.altair_chart(box_chart_pre, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The boxplots confirm that right-skew persists even after the preprocessing steps are applied. This is an expected and deliberate outcome: the objective of the outlier separation step is not to eliminate all distributional asymmetry but to remove only the most extreme multivariate observations that would distort cluster centroids. Remaining spread represents genuine natural variation in customer spending behaviour. The wide interquartile ranges across categories, particularly groceries, indicate that spending patterns are highly heterogeneous within the regular customer base, which is precisely the signal that the clustering model is designed to capture. Capping or transforming these values would suppress the very differences the segmentation aims to detect.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 4: Outlier dataset size vs regular base
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Dataset split after consensus outlier separation</div>
</div>
""", unsafe_allow_html=True)
    split_df = pd.DataFrame({
        "Dataset": ["Regular base", "Outlier dataset"],
        "Customers": [len(info_unscaled), len(outlier_df)]
    })
    split_chart = alt.Chart(split_df).mark_bar(color="#374151", cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X("Dataset:N", title=""),
        y=alt.Y("Customers:Q", title="Number of customers"),
        tooltip=["Dataset", alt.Tooltip("Customers:Q", format=",")]
    ).properties(height=300, title="Dataset split after consensus outlier separation")
    st.altair_chart(split_chart, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The chart demonstrates the conservative nature of the consensus outlier rule: the overwhelming majority of customers remain in the regular base, with only 1,023 customers (approximately 3.1% of the total) separated into the outlier dataset. This proportion is consistent with a rule that requires simultaneous agreement from three independent detection methods: univariate IQR with a generous multiplier of k = 2.0, DBSCAN density-based isolation with eps = 1.0, and a third method. A customer flagged by only one or two methods is retained in the regular base. This conservative threshold avoids the common error of over-excluding customers who are unusual on a single variable but otherwise unremarkable in the multivariate space. Separated outlier customers are not discarded; they are reassigned to their nearest cluster centroid after the model is fitted on the regular base.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 5: Correlation heatmap
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Feature correlation matrix</div>
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
        text_auto=".2f",
        title="Feature correlation matrix"
    )
    corr_fig.update_layout(margin=dict(l=60, r=20, t=60, b=60), height=500)
    st.plotly_chart(corr_fig, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The correlation matrix reveals that most spend categories are weakly or negligibly correlated with each other, confirming that they carry distinct information and justifying their separate inclusion in the feature set. The strongest positive correlations appear between meat and fish annual spend, and between electronics and videogames annual spend, both of which are expected given the shared product affinity within those pairs. No pair exceeds the 0.7 collinearity threshold that would typically motivate feature removal. The near-zero correlations between promotional sensitivity and spend categories confirm that promotion usage is an independent behavioural dimension rather than a proxy for spending volume, supporting its inclusion as a separate clustering variable. Total children shows negligible correlation with all spend categories, suggesting that household composition affects product category preferences in ways that are not linearly captured by spend levels alone.</p>
</div>
""", unsafe_allow_html=True)

    # Chart: Full correlation heatmap (NB01)
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Full-feature correlation heatmap — raw dataset</div>
</div>
""", unsafe_allow_html=True)
    corr_chart_path = IMAGENS_DIR / "charts" / "correlation_heatmap.png"
    if corr_chart_path.exists():
        st.image(str(corr_chart_path), use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The full-feature Pearson correlation matrix covers all numerical variables in the raw dataset. The lower triangle uses a diverging red-blue palette: red cells indicate negative correlation, blue cells positive correlation, and near-white cells negligible linear association. The strongest positive associations cluster within the spending feature group: meat and fish annual spend correlate moderately, as do electronics and videogames — pairs that reflect shared category affinity. Groceries correlates weakly with all other spend categories, consistent with its role as a near-universal baseline rather than a discriminating dimension. Promotional sensitivity shows near-zero correlation with all spend categories, confirming that it captures an independent behavioural dimension. The age and tenure features are weakly correlated, suggesting that long-standing customers are not necessarily older, and that acquisition cohort effects are not fully confounded with demographic age. No pair exceeds the 0.7 threshold that would constitute a collinearity problem requiring feature removal. These findings support including all spend categories in the clustering feature set while treating promotional sensitivity as a distinct axis.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding:24px; border-radius:16px; background:#f9fafb; border:1px solid #e5e7eb; margin-top:12px;'>
          <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 01 — Conclusions</div>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0 0 10px 0;'>"Before imputing missing values, the most atypical customers are separated into an outlier dataset. The rule is conservative: a customer is only kept aside when it is simultaneously flagged by three methods."</p>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0 0 10px 0;'>"After the conservative outlier separation, the regular customer base still contains natural variation, but the most extreme observations are kept aside. This reduces the risk that a small number of atypical customers dominate the clustering distances."</p>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>"In the final exported dataset, <code>year_first_transaction</code> is replaced by <code>tenure</code>, and <code>typical_hour</code> is replaced by its cyclic components. Some high values remain visible in the boxplots after preprocessing. This is expected because lifetime spending variables are naturally skewed."</p>
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
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 02 — Geographic Analysis</div>
      <p style='font-size:16px; color:#374151; line-height:1.8; margin:0 0 14px 0;'>
        Geographic data is available for a significant portion of the customer base in the form of latitude and longitude coordinates. This notebook investigates whether the spatial distribution of customers reveals behavioural patterns beyond what the demographic and spend variables capture. Crucially, <strong>geography is intentionally excluded from the clustering distance</strong> — including it would risk creating geographic groups rather than behavioural segments.
      </p>
      <p style='font-size:16px; color:#374151; line-height:1.8; margin:0 0 24px 0;'>
        The analysis uses four complementary visualisations: a scatter plot of coordinates, an interactive Plotly scatter mapbox, a Folium map with MarkerCluster, and a hexbin density map. The hotspot is identified programmatically using a coordinate grid (bins=50) — not visually — to ensure the finding is data-driven and reproducible.
      </p>

      <div style='display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:28px;'>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:4px;'>Hotspot location</div>
          <div style='font-size:14px; color:#6b7280; line-height:1.6;'>Dense concentration near <strong>Cidade Universitária</strong> and <strong>Entrecampos</strong> in Lisbon. Consistent with a younger urban population around university and transport infrastructure.</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:4px;'>Dominant age group</div>
          <div style='font-size:14px; color:#6b7280; line-height:1.6;'>The <strong>25–34</strong> age band dominates the hotspot profile. Hotspot median age is significantly lower than the rest of the customer base.</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:18px 20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:4px;'>Hotspot radius</div>
          <div style='font-size:14px; color:#6b7280; line-height:1.6;'><strong>0.006 decimal degrees</strong> — defined programmatically via grid-based density analysis, not by visual inspection of the map.</div>
        </div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px; margin-bottom:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Behavioural differences: hotspot vs. rest of base</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'>The hotspot shows a distinct behavioural profile even before clustering labels are applied. The strongest differences are in <strong>age, product diversity, number of complaints, store visits, total spend, and promotion usage</strong>. Hotspot customers are younger, more active, and more variety-seeking — consistent with a younger urban population, though the data does not confirm student status directly.</div>
      </div>

      <div style='border-left:3px solid #111827; padding-left:20px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Why geography is excluded from clustering</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Including geographic coordinates in the clustering distance would create spatially-defined groups — customers near each other in space would be forced into the same cluster regardless of their spending behaviour. The objective is to discover <em>behavioural</em> communities, not geographic ones. Geography is kept as a profiling tool: after clusters are fitted, the geographic distribution of each cluster is inspected as a validation and characterisation layer.</div>
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
    ).properties(height=320, title="Age distribution: hotspot vs. rest of base")
    st.altair_chart(age_hotspot_chart, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The overlaid age histograms reveal a pronounced difference in age composition between the hotspot and the rest of the customer base. The hotspot skews clearly toward the 25 to 34 age band, while the broader base has a flatter distribution extending through the 40 to 55 range. This age gap is the most statistically robust finding of the geographic analysis: it corroborates the hypothesis that the dense area near Cidade Universitaria and Entrecampos attracts a younger urban population, consistent with proximity to university infrastructure and high-density residential areas. The finding is treated as an interpretive insight rather than an actionable segment boundary, because geography is deliberately excluded from the clustering distance. The age skew observed in the hotspot does not define a segment; rather, it adds spatial context to the behavioural profiles that the clustering model identifies independently.</p>
</div>
""", unsafe_allow_html=True)

    # Chart: Static scatter (NB02)
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
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>This static scatter plot represents every customer as a point at their recorded latitude and longitude coordinates, plotted without any segmentation labels. The visualisation reveals that the customer base is heavily concentrated in a narrow geographic band consistent with the Lisbon Metropolitan Area, with a pronounced density peak in the central zone. The clustering of points is not uniform: a high-density region emerges in the centre-north quadrant of the scatter, corresponding to the urban core identified in the interactive maps above. Surrounding this core, points become progressively sparser and more dispersed, consistent with suburban and commuter-belt customers. This raw spatial pattern is the starting point for the geographic analysis: the identification of the hotspot bounding box, the density map, and the behavioural comparisons are all derived from the concentration visible here. The static format makes the overall geographic footprint clear without the visual clutter of colour-coded segments, which are overlaid in the clustering-era scatter produced later in Notebook 04.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding:24px; border-radius:16px; background:#f9fafb; border:1px solid #e5e7eb; margin-top:12px;'>
          <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 02 — Conclusions</div>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0 0 10px 0;'>"The hotspot shows a distinct behavioural profile even before using any clustering labels. The strongest differences are age, product diversity, number of complaints, store visits, total spend and promotion usage. This suggests that the dense area is not only a map artefact; it also corresponds to a younger, more active customer profile."</p>
          <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>"Age is the strongest signal supporting the area near the university hypothesis. At this stage, it should not be treated as one of the final customer segments because geography is not part of the clustering distance. However, it is useful as a geographic profiling insight."</p>
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
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebooks 03 & 04 — Clustering & Characterisation</div>
      <p style='font-size:16px; color:#374151; line-height:1.8; margin:0 0 14px 0;'>
        The modelling stage applies K-Means clustering to the preprocessed, unscaled customer dataset. The model selection process evaluates multiple candidate feature sets, two scalers, and a range of k values (6–10) simultaneously — no single diagnostic drives the final choice.
      </p>

      <div style='display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:28px;'>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Algorithm</div>
          <div style='font-size:22px; font-weight:800; color:#111827;'>K-Means</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>K selected</div>
          <div style='font-size:22px; font-weight:800; color:#111827;'>8</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Scaler</div>
          <div style='font-size:22px; font-weight:800; color:#111827;'>MinMax</div>
        </div>
        <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 18px; text-align:center;'>
          <div style='font-size:11px; font-weight:600; color:#9ca3af; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.08em;'>Feature set</div>
          <div style='font-size:16px; font-weight:800; color:#111827; line-height:1.2;'>spend + promo<br/>no groceries</div>
        </div>
      </div>

      <div style='display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-bottom:28px;'>
        <div>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:12px;'>Model selection decisions</div>
          <div style='display:flex; flex-direction:column; gap:10px;'>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Why K=8?</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Values between 6 and 10 were compared across multiple feature spaces and scalers using the Elbow Method, Silhouette Score, Ward dendrogram (cut height=6.4), and R² grid. K=8 was selected as the configuration that balances geometric separation with business interpretability.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Why exclude groceries from clustering distance?</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Most customers spend heavily on groceries regardless of segment. Including it dominated the distance calculation, masking more differentiating categories. Groceries are kept for profiling — not for clustering.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Why MinMaxScaler over RobustScaler?</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>Both scalers were tested. MinMaxScaler produced slightly stronger and more stable silhouette scores across the k range tested, and was preferred after side-by-side UMAP comparison.</div>
            </div>
          </div>
        </div>
        <div>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:12px;'>Alternatives tested & rejected</div>
          <div style='display:flex; flex-direction:column; gap:10px;'>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>DBSCAN — rejected</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>"Strongest silhouettes are obtained when most customers are classified as noise." DBSCAN did not recover the richer eight-segment structure obtained with K-Means and was ruled out as the final model.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>Petfood alternative — rejected</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>A model adding <code>lifetime_spend_petfood</code> and separating electronics from videogames was tested. "Overall structure is slightly less clean than the current model." Petfood is kept as a profiling insight only.</div>
            </div>
            <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:10px; padding:14px 16px;'>
              <div style='font-size:13px; font-weight:600; color:#111827;'>SOM & hierarchical Ward — benchmarked</div>
              <div style='font-size:13px; color:#6b7280; margin-top:3px;'>A 12×12 SOM (1,000 iterations) and a Centroid Ward macro (20 micro-K-Means → Ward into 8 macro segments) were run as benchmarks. K-Means was confirmed as the strongest and most interpretable model.</div>
            </div>
          </div>
        </div>
      </div>

      <div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:16px 20px; margin-bottom:28px;'>
        <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:8px;'>Naming rationale (Notebook 04)</div>
        <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Business names are assigned only after the modelling stage is complete. A name is only confirmed when the same pattern appears consistently across <strong>at least three views</strong>: the spend deviation table, the radar plot, the spend profile heatmap, and the demographic/behavioural profile. "The final name of each segment is chosen only when the same pattern appears in more than one view."</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Chart 1: Cluster sizes
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
    ).properties(height=320, title="Customer count per community")
    st.altair_chart(cluster_size_chart, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The distribution of customers across the eight communities demonstrates that the clustering solution is free from the pathological cluster size imbalance that often signals residual outlier structure or an inappropriate choice of k. No single community is excessively small relative to the others, and no community dominates the dataset to the point where it absorbs customers that would be better differentiated elsewhere. This balance is a consequence of the prior outlier separation step: by removing multivariate extremes before fitting the model, the K-Means algorithm operates on a more homogeneous space and converges to more evenly populated centroids. Segment sizes are subsequently used as weighting factors when prioritising campaign deployment: larger segments offer higher absolute reach, while smaller segments may offer higher precision for targeted promotions.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 2: Spend profile heatmap per cluster
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Normalised spend profile per cluster</div>
</div>
""", unsafe_allow_html=True)
    seg_spend_df = pd.read_csv(BASE_DIR / "datasets" / "segment_spend_profile.csv")
    spend_heat_cols = [c for c in seg_spend_df.columns if c.startswith("lifetime_spend_")]
    seg_spend_df["cluster"] = pd.to_numeric(seg_spend_df["cluster"], errors="coerce")
    seg_spend_df = seg_spend_df.dropna(subset=["cluster"])
    seg_spend_df = seg_spend_df.sort_values("cluster")
    cluster_id_map = {0: "Vegetarians", 1: "Regulars", 2: "Wellness", 3: "Promoters", 4: "Loyalists", 5: "Families", 6: "Economizers", 7: "Techies"}
    seg_spend_df["segment_name"] = seg_spend_df["cluster"].astype(int).map(cluster_id_map)
    spend_matrix = seg_spend_df[spend_heat_cols].values.astype(float)
    col_min = spend_matrix.min(axis=0)
    col_max = spend_matrix.max(axis=0)
    col_range = col_max - col_min
    col_range[col_range == 0] = 1
    spend_matrix_norm = (spend_matrix - col_min) / col_range
    spend_col_labels = [c.replace("lifetime_spend_", "").replace("_", " ").title() for c in spend_heat_cols]
    segment_labels = seg_spend_df["segment_name"].tolist()
    spend_heat_fig = px.imshow(
        spend_matrix_norm,
        x=spend_col_labels,
        y=segment_labels,
        color_continuous_scale="Blues",
        zmin=0, zmax=1,
        text_auto=".2f",
        title="Normalised spend profile per cluster"
    )
    spend_heat_fig.update_layout(margin=dict(l=80, r=20, t=60, b=80), height=420)
    st.plotly_chart(spend_heat_fig, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>Each cell represents the normalised mean lifetime spend for a given segment-category pair, scaled to [0, 1] across segments so that the darkest cell in each column identifies which community spends most in that category. The heatmap directly reveals the over-indexing patterns that motivated the naming decisions: the Techies segment concentrates spending in electronics, videogames, and technology; Vegetarians over-index in vegetables and non-alcoholic drinks; Families show elevated spend across groceries and hygiene products consistent with a large household. Categories where all segments show similar shading confirm that the corresponding spend dimension does not discriminate well between communities, which is why groceries were excluded from the clustering distance despite remaining a useful profiling variable. Cells with very low values across all segments highlight categories that are niche rather than universal, such as alcohol and petfood.</p>
</div>
""", unsafe_allow_html=True)

    # Chart 3: Behavioural profile heatmap per cluster
    st.markdown("""
<div style='margin-top:36px; margin-bottom:12px; border-top:1px solid #e5e7eb; padding-top:24px;'>
  <div style='font-size:13px; font-weight:700; color:#111827;'>Normalised behavioural profile per cluster</div>
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
    b_min = behav_matrix.min(axis=0)
    b_max = behav_matrix.max(axis=0)
    b_range = b_max - b_min
    b_range[b_range == 0] = 1
    behav_matrix_norm = (behav_matrix - b_min) / b_range
    behav_col_labels = ["Promo sensitivity", "Tenure (years)", "Total children", "Avg complaints"]
    behav_segment_labels = behav_by_cluster["segment_name"].tolist()
    behav_heat_fig = px.imshow(
        behav_matrix_norm,
        x=behav_col_labels,
        y=behav_segment_labels,
        color_continuous_scale="Blues",
        zmin=0, zmax=1,
        text_auto=".2f",
        title="Normalised behavioural profile per cluster"
    )
    behav_heat_fig.update_layout(margin=dict(l=80, r=20, t=60, b=80), height=420)
    st.plotly_chart(behav_heat_fig, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>The behavioural heatmap complements the spend profile by capturing dimensions that are not directly reflected in category spending. Promotional sensitivity varies strongly across segments: Promoters register the maximum value on this dimension, confirming that their defining trait is price-driven purchasing rather than category affinity. Tenure separates long-term customers (Loyalists, Vegetarians) from newer cohorts (Regulars), providing a basis for differentiated retention versus acquisition strategies. Total children most strongly characterises the Families segment, validating the naming decision and supporting the recommendation to target this group with bulk-buying and family-bundle promotions. Complaints vary across segments but tend to be low overall; where elevated, they may reflect higher engagement and transaction frequency rather than systematic dissatisfaction. Together, these four dimensions provide a multi-axis profile that is more actionable for campaign design than spend data alone.</p>
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
        
        # Image mapping per cluster: use named PNGs where available, slices for the rest
        cluster_images = {
            0: VEGETARIANS_URI,
            1: REGULARS_URI,
            2: WELLNESS_URI,
            3: PROMOTERS_URI,
            4: LOYALISTS_URI,
            5: FAMILIES_URI,
            6: ECONOMIZERS_URI,
            7: TECHIES_URI,
        }
        for i in range(len(SLICES_URIS)):
            c = [1,2,3,4,6,7][i] if i < 6 else i
            if c not in cluster_images:
                cluster_images[c] = SLICES_URIS[i % len(SLICES_URIS)]

        # Header row
        st.markdown("""
        <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;'>
            <div style='font-size:20px; font-weight:700; color:#111827;'>Your 8 customer communities</div>
        </div>
        """, unsafe_allow_html=True)

        cards_list_html = []
        for idx, row in seg_summary.iterrows():
            c_id = int(row['cluster'])
            share = row['share_%']
            custs = int(row['customers'])
            meta = seg_meta_grid.get(c_id, {"name": f"Cluster {c_id}", "desc": "No description available.", "icon_idx": 0})
            img_uri = cluster_images.get(c_id, SLICES_URIS[c_id % len(SLICES_URIS)])

            card_html = f"""
            <div class='community-card'>
              <div class='community-card-icon-container'>
                <img src='{img_uri}' class='community-card-img' />
              </div>
              <div>
                <h3 class='community-card-title'>{meta['name']}</h3>
                <div class='community-card-value'>{share:.1f}%</div>
                <div class='community-card-sub'>{custs:,} customers</div>
                <div class='community-card-desc'>{meta['desc']}</div>
              </div>
              <div class='community-card-arrow'>→</div>
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
    <div style='width:100%; box-sizing:border-box; margin-bottom:32px;'>
      <div style='font-size:11px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#9ca3af; margin-bottom:10px;'>Notebook 05 — Association Rules</div>
      <p style='font-size:16px; color:#374151; line-height:1.8; margin:0 0 14px 0;'>
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
          <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Rules are mined per segment — each sub-population has far fewer transactions than the full dataset. A 1% support threshold ensures enough rules are discovered while still requiring meaningful co-occurrence frequency within each community.</div>
        </div>
        <div style='border-left:3px solid #111827; padding-left:20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Lift-derived campaign discounts</div>
          <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Suggested campaign discounts are not fixed — they are derived from the lift value of each rule. A higher lift means a stronger-than-random co-purchase signal, which justifies a larger promotional incentive. This ties the commercial decision directly to statistical evidence.</div>
        </div>
        <div style='border-left:3px solid #111827; padding-left:20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Excluded recommendations: Vegetarians (cluster 0)</div>
          <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Chicken, meat, and fish are excluded from recommendations for cluster 0 (Vegetarians). The Apriori rules initially suggested these items, but they contradict the segment's defining behavioural trait. Notebook 4 confirms that this segment's identity is plant-based — the exclusion ensures campaign coherence.</div>
        </div>
        <div style='border-left:3px solid #111827; padding-left:20px;'>
          <div style='font-size:13px; font-weight:700; color:#111827; margin-bottom:6px;'>Robustness validation</div>
          <div style='font-size:14px; color:#6b7280; line-height:1.7;'>Each segment's rules are validated on an 80/20 train/test split. Segments with many matched rules and low mean lift difference between train and test have stable co-purchase patterns. Segments with few matched rules should be interpreted with caution.</div>
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
    ).properties(height=520, title="Association rules by lift per segment")
    st.altair_chart(lift_chart, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>Lift measures how much more likely two products are to be purchased together compared to what would be expected if they were purchased independently. A lift of 1.0 indicates no association beyond chance; a lift of 1.2 indicates that the joint purchase is 20% more likely than random co-occurrence; values above 2.0 represent strong non-random co-purchase patterns. The chart reveals that the strongest lift values are concentrated in a small number of rules: vegetable-combination rules for produce-focused segments (Regulars, Promoters) and technology cross-sell rules (Techies, Economizers). These high-lift rules are the primary candidates for campaign deployment because they represent the strongest statistical evidence that promoting item B to a customer who bought item A will generate a genuine incremental purchase rather than recovering a purchase that would have occurred anyway. Lower-lift rules remain valid but justify smaller promotional incentives.</p>
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
        title="Confidence vs. lift across all segments",
        labels={"confidence": "Confidence", "lift": "Lift", "segment": "Segment"}
    )
    scatter_fig.update_traces(marker=dict(size=10))
    scatter_fig.update_layout(margin=dict(l=40, r=20, t=60, b=60), height=420)
    st.plotly_chart(scatter_fig, use_container_width=True)
    st.markdown("""
<div style='background:#f9fafb; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin-top:8px; margin-bottom:32px;'>
  <div style='font-size:11px; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Interpretation</div>
  <p style='font-size:14px; color:#374151; line-height:1.8; margin:0;'>Confidence and lift are complementary metrics that together characterise the commercial quality of an association rule. Confidence measures the conditional probability that a customer who buys the antecedent will also buy the consequent; lift adjusts this probability for the base rate of the consequent across all transactions. Rules positioned in the upper-right quadrant of this scatter plot (high confidence and high lift) represent the strongest candidates for campaign deployment: they are both reliable (customers who trigger the rule frequently also complete the recommended purchase) and non-trivial (the co-purchase is substantially more likely than random). Rules with high confidence but modest lift may reflect a consequent that is purchased frequently regardless of the antecedent, diminishing the causal interpretation of the rule. Rules with high lift but low confidence identify genuine but infrequent co-purchase patterns that may be better suited to targeted micro-campaigns than broad promotional rollouts.</p>
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
