import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INITIAL_BG_PATH = BASE_DIR / "imagens" / "initial.png"
INITIAL_BG_URI = ""
if INITIAL_BG_PATH.exists():
    with open(INITIAL_BG_PATH, "rb") as img_file:
        data = base64.b64encode(img_file.read()).decode("utf-8")
        INITIAL_BG_URI = f"data:image/png;base64,{data}"

# Car image logic removed

st.set_page_config(page_title="Costumer Segmentation Project", layout="wide")

css = """
<style>
html {
    background-color: #f7f1ec !important;
}
body {
    background-color: transparent !important;
    color: #3b2720;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
      linear-gradient(180deg, rgba(247, 241, 236, 0.35), rgba(247, 241, 236, 0.55)),
      url('{INITIAL_BG_URI}') no-repeat center center;
    background-size: cover;
    filter: saturate(35%) contrast(98%);
    opacity: 0.9;
    z-index: -1;
    pointer-events: none;
}
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stMainContainer"], [data-testid="stAppViewBlockContainer"], main, .main, div.block-container {
    background: transparent !important;
    background-color: transparent !important;
    backdrop-filter: none !important;
}
section[role="main"] {
    padding-top: 90px !important;
}
header, header[role="banner"], div[data-testid="stToolbar"] {
    position: relative !important;
    width: 100% !important;
    z-index: 50 !important;
    background: rgba(255, 255, 255, 0.8) !important;
    backdrop-filter: blur(8px) !important;
    box-shadow: 0 1px 3px rgba(15,23,42,0.05) !important;
    border-bottom: 1px solid rgba(226, 232, 240, 0.8) !important;
}
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.92) !important;
    min-width: 340px;
    max-width: 420px;
    position: relative;
    border-right: 1px solid rgba(226, 232, 240, 0.8) !important;
    backdrop-filter: blur(14px);
}
button[title*="sidebar"], button[aria-label*="sidebar"] {
    background: #ffffff !important;
    color: #0f172a !important;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    border-radius: 999px !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04) !important;
    position: fixed !important;
    top: 22px !important;
    left: 24px !important;
    transform: none !important;
    z-index: 100;
    padding: 10px 14px !important;
}
button[title*="sidebar"]:hover, button[aria-label*="sidebar"]:hover {
    background: #f1f5f9 !important;
    border-color: #cbd5e1 !important;
}
.css-1d391kg {
    background-color: #f1f5f9;
}
.stButton>button {
    background-color: #ea580c !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: 600 !important;
    transition: background-color 0.2s ease, transform 0.1s ease !important;
}
.stButton>button:hover {
    background-color: #f97316 !important;
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
    color: #64748b;
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
    padding-top: 0 !important;
    background: transparent !important;
    background-color: transparent !important;
    box-shadow: none !important;
}
.stMarkdown, .stText, .css-1d391kg {
    color: #1e293b;
}
div[data-testid="stImage"] img {
    border-radius: 12px;
    filter: saturate(1.05) contrast(1.05);
}
div[data-testid="stImage"] {
    border: 1px solid rgba(226, 232, 240, 0.8);
    padding: 8px;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(8px);
}
div[role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.6) !important;
    padding: 12px 16px !important;
    border-radius: 12px !important;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    transition: all 0.2s ease !important;
}
div[role="radiogroup"] label:hover {
    background: rgba(255, 255, 255, 0.9) !important;
    border-color: #ea580c !important;
}
.page-shell {
    background: #ffffff !important;
    border: 1px solid rgba(163, 78, 35, 0.12);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.02);
    margin-bottom: 28px;
}
.page-title-box {
    display: block;
    width: 100%;
    background: #f8e6d5 !important;
    color: #3b2720 !important;
    border: 1px solid rgba(163, 78, 35, 0.18) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
    border-radius: 12px;
    padding: 16px 24px;
    box-sizing: border-box;
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 24px;
    letter-spacing: -0.02em;
}
.page-text {
    color: #334155;
    line-height: 1.75;
    text-align: justify;
    font-size: 16px;
}
.page-next {
    margin-top: 32px;
    display: flex;
    justify-content: flex-end;
}
.page-next button {
    background: #f8e6d5 !important;
    color: #3b2720 !important;
    border: none !important;
    padding: 14px 24px !important;
    border-radius: 18px !important;
    font-weight: 700;
}
.sidebar-item {
    margin-bottom: 14px;
}
.sidebar-item .sidebar-link {
    display: block;
    color: #3b2720;
    text-decoration: none;
    font-size: 18px;
    line-height: 1.5;
    transition: color 0.2s ease, transform 0.2s ease;
}
.sidebar-item .sidebar-link:hover {
    color: #ea580c;
    transform: translateX(2px);
}
.sidebar-item.active .sidebar-link {
    color: #ea580c !important;
    background: none !important;
    border: none !important;
    padding: 0 !important;
    font-weight: 800 !important;
    text-decoration: underline !important;
    text-underline-offset: 6px;
    text-decoration-thickness: 3px;
    pointer-events: none;
    cursor: default;
}
.sidebar-item.active .sidebar-link::before {
    content: "" !important;
    margin: 0 !important;
}
.section-anchor {
    display: block;
    position: relative;
    top: -90px;
    visibility: hidden;
}
</style>
""".replace('{INITIAL_BG_URI}', INITIAL_BG_URI)

st.markdown(css, unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <div style='padding: 12px 0 18px 0; font-family:Garamond,serif;'>
      <div style='font-size:36px; font-weight:800; color:#3f2d22; line-height:1.05; margin-bottom:18px;'>Customer Segmentation Project</div>
      <div style='font-size:16px; color:#5f4635; margin-bottom:18px;'>Section index</div>
      <div class='sidebar-item' data-section='introduction'><span class='sidebar-link'>Introduction</span></div>
      <div class='sidebar-item' data-section='data-analysis'><span class='sidebar-link'>Data analysis</span></div>
      <div class='sidebar-item' data-section='data-preprocessing'><span class='sidebar-link'>Data preprocessing</span></div>
      <div class='sidebar-item' data-section='data-in-geography'><span class='sidebar-link'>Data in geography</span></div>
      <div class='sidebar-item' data-section='customer-segmentation'><span class='sidebar-link'>Customer segmentation and clustering</span></div>
      <div class='sidebar-item' data-section='targeter-promotion'><span class='sidebar-link'>Targeter promotion</span></div>
      <div class='sidebar-item' data-section='conclusion'><span class='sidebar-link'>Conclusion and recommendations</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

js_script = """
<img src="x" onerror="(function() {
  const SECTION_IDS = ['introduction', 'data-analysis', 'data-preprocessing', 'data-in-geography', 'customer-segmentation', 'targeter-promotion', 'conclusion'];
  const activateLink = id => {
    document.querySelectorAll('.sidebar-item').forEach(item => item.classList.remove('active'));
    const target = document.querySelector(`.sidebar-item[data-section='${id}']`);
    if (target) target.classList.add('active');
  };

  let observer;
  const setupObserver = () => {
    if (observer) observer.disconnect();
    observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          activateLink(entry.target.id);
        }
      });
    }, {root: null, rootMargin: '-40% 0px -55% 0px', threshold: 0});

    SECTION_IDS.forEach(id => {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    });
  };

  const setupClickListeners = () => {
    const items = document.querySelectorAll('.sidebar-item');
    items.forEach(item => {
      const link = item.querySelector('.sidebar-link');
      if (link) {
        link.style.cursor = 'pointer';
        item.onclick = (e) => {
          e.preventDefault();
          const sectionId = item.getAttribute('data-section');
          const el = document.getElementById(sectionId);
          if (el) {
            el.scrollIntoView({ behavior: 'smooth' });
            activateLink(sectionId);
          }
        };
      }
    });
  };

  const runSetup = () => {
    const ready = SECTION_IDS.every(id => document.getElementById(id)) && document.querySelector('.sidebar-item');
    if (ready) {
      setupObserver();
      setupClickListeners();
      if (window.location.hash) {
        activateLink(window.location.hash.slice(1));
      }
    }
  };

  if (!window.hasSetupSidebarObserver) {
    window.hasSetupSidebarObserver = true;
    const mutObserver = new MutationObserver(() => {
      runSetup();
    });
    mutObserver.observe(document.body, { childList: true, subtree: true });
    runSetup();
  }
})()"/>
"""

def render_footer():
    st.markdown(
        """
        <div style='margin:48px auto 0; padding:24px; border-radius:16px; max-width:1080px; background:rgba(255,255,255,0.7); border:1px solid rgba(226,232,240,0.8); backdrop-filter:blur(10px); font-family:"Inter", sans-serif;'>
          <div style='display:grid; grid-template-columns:repeat(4, minmax(180px, 1fr)); gap:18px; align-items:start;'>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.15em; color:#64748b; margin-bottom:10px; font-weight:700;'>Navigation</div>
              <p style='color:#475569; margin:0; line-height:1.6; font-size:14px;'>Use the navigation bar on the left side of the screen.</p>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.15em; color:#64748b; margin-bottom:10px; font-weight:700;'>Work done by</div>
              <div style='display:grid; gap:10px;'>
                <a href='https://github.com/CarlotaMarto' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#0f172a; cursor:pointer; padding:10px 12px; border-radius:12px; background:rgba(255,255,255,0.8); border:1px solid rgba(226,232,240,0.5);'>
                  <img src='https://github.com/CarlotaMarto.png' alt='Carlota Marto GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px;'>Carlota Marto</div>
                    <div style='font-size:12px; color:#64748b;'>20241729</div>
                  </div>
                </a>
                <a href='https://github.com/Franciscaveigateixeira' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#0f172a; cursor:pointer; padding:10px 12px; border-radius:12px; background:rgba(255,255,255,0.8); border:1px solid rgba(226,232,240,0.5);'>
                  <img src='https://github.com/Franciscaveigateixeira.png' alt='Francisca Teixeira GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px;'>Francisca Teixeira</div>
                    <div style='font-size:12px; color:#64748b;'>20241702</div>
                  </div>
                </a>
                <a href='https://github.com/Gouveia316' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#0f172a; cursor:pointer; padding:10px 12px; border-radius:12px; background:rgba(255,255,255,0.8); border:1px solid rgba(226,232,240,0.5);'>
                  <img src='https://github.com/Gouveia316.png' alt='Pedro GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px;'>Pedro Gouveia</div>
                    <div style='font-size:12px; color:#64748b;'>20231657</div>
                  </div>
                </a>
              </div>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.15em; color:#64748b; margin-bottom:10px; font-weight:700;'>Teacher</div>
              <div style='font-weight:700; color:#0f172a; margin-bottom:6px; font-size:14px;'>Ivo Bernardo</div>
              <div style='color:#64748b; font-size:13px;'>Machine Learning II</div>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.15em; color:#64748b; margin-bottom:10px; font-weight:700;'>Note</div>
              <p style='color:#475569; line-height:1.6; margin:0; font-size:14px;'>This project is optimized for executive-level business intelligence and strategic decision making.</p>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='page-title-box'>Customer Segmentation Project</div>", unsafe_allow_html=True)
st.markdown("<a id='introduction' class='section-anchor'></a>", unsafe_allow_html=True)
st.markdown("<div class='page-title-box'>Introduction</div>", unsafe_allow_html=True)
st.markdown("""
<div class='page-shell'>
  <div class='page-text'>
    <p>This introduction presents the customer segmentation project overview, combining initial analysis, data cleaning, and geographic insights. The goal is to show how each step contributes to a cleaner dataset, a stronger customer profile, and useful business segmentation.</p>
    <p>The report brings together exploratory analysis, preprocessing, and geographic investigation, with clear charts and maps that highlight real customer patterns.</p>
    <p>The left navigation takes you directly to each section, while the content remains on a single continuous page.</p>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<a id='data-analysis' class='section-anchor'></a>", unsafe_allow_html=True)
st.markdown("<div class='page-title-box'>Data analysis</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>This section presents the initial dataset analysis, based on the notebooks. It focuses on customer attributes, purchase behavior, and data quality before any segmentation.</p>
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
""",
unsafe_allow_html=True)

st.markdown("<a id='data-preprocessing' class='section-anchor'></a>", unsafe_allow_html=True)
st.markdown("<div class='page-title-box'>Data preprocessing</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='page-shell'>
      <div class='page-text'>
        <p>This section describes the data cleaning and preparation process. It includes date corrections, negative value fixes, feature engineering, and outlier review.</p>
        <ul>
          <li>Future transaction years are set to <code>NaN</code> instead of dropping rows.</li>
          <li>Negative promotion percentage values are corrected and invalid identifiers are excluded.</li>
          <li>Customer names are processed to extract education-level titles while preserving privacy.</li>
          <li>Outliers and skewed spending patterns are inspected to prevent distortion in clustering.</li>
        </ul>
      </div>
    </div>
""",
unsafe_allow_html=True,
)

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
""",
unsafe_allow_html=True)

st.markdown("<a id='data-in-geography' class='section-anchor'></a>", unsafe_allow_html=True)
st.markdown("<div class='page-title-box'>Data In Geography</div>", unsafe_allow_html=True)
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
st.subheader("Customer density map")
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
""",
unsafe_allow_html=True)

st.markdown("<a id='customer-segmentation' class='section-anchor'></a>", unsafe_allow_html=True)
st.markdown("<div class='page-title-box'>Customer segmentation and clustering</div>", unsafe_allow_html=True)

st.markdown("<a id='targeter-promotion' class='section-anchor'></a>", unsafe_allow_html=True)
st.markdown("<div class='page-title-box'>Targeter promotion</div>", unsafe_allow_html=True)

st.markdown("<a id='conclusion' class='section-anchor'></a>", unsafe_allow_html=True)
st.markdown("<div class='page-title-box'>Conclusion and recommendations</div>", unsafe_allow_html=True)

render_footer()
st.markdown(js_script, unsafe_allow_html=True)
