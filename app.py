import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="Costumer Segmentation Project", layout="wide")

css = """
<style>
body {
    background: radial-gradient(circle at top left, #ffe6d9 0%, #ffd2b2 35%, #f6b07e 100%);
    color: #3b2720;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
section[role="main"] {
    padding-top: 90px !important;
}
main, .main, div.block-container {
    padding-top: 90px !important;
}
header, header[role="banner"], div[data-testid="stToolbar"] {
    position: relative !important;
    width: 100% !important;
    z-index: 50 !important;
    background: #ffffff !important;
    box-shadow: 0 2px 25px rgba(0,0,0,0.08) !important;
}
[data-testid="stSidebar"] {
    background: #ffe8d5;
    min-width: 340px;
    max-width: 420px;
    position: relative;
    border-right: 1px solid rgba(205,93,57,0.18);
}
button[title*="sidebar"], button[aria-label*="sidebar"] {
    background: #ffe3d3 !important;
    color: #3b2720 !important;
    border: 1px solid rgba(205,93,57,0.28) !important;
    border-radius: 999px !important;
    box-shadow: 0 16px 30px -22px rgba(0, 0, 0, 0.24) !important;
    position: fixed !important;
    top: 22px !important;
    left: 24px !important;
    transform: none !important;
    z-index: 100;
    padding: 10px 14px !important;
}
button[title*="sidebar"]:hover, button[aria-label*="sidebar"]:hover {
    background: #ffd6b8 !important;
}
.css-1d391kg {
    background-color: #fff2e7;
}
.stButton>button {
    background-color: #e6513b;
    color: white;
    border-radius: 999px;
    border: none;
}
.st-bb {
    border-radius: 24px;
}
.stSidebarNav label,
div[role="radiogroup"] label {
    font-size: 32px;
    font-weight: 700;
    line-height: 1.3;
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: keep-all;
    letter-spacing: 0.01em;
}
.stSidebarNav label span {
    font-size: 32px;
}
.stAppViewContainer, .main > div, div.block-container {
    max-width: 100% !important;
    width: 100% !important;
}
div.block-container {
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 0 !important;
}
.stMarkdown, .stText, .css-1d391kg {
    color: #402b22;
}
div[data-testid="stImage"] img {
    border-radius: 28px;
    filter: saturate(1.12) contrast(1.08);
}
div[data-testid="stImage"] {
    border: 1px solid rgba(205,93,57,0.18);
    padding: 12px;
    border-radius: 28px;
    background: rgba(255, 245, 236, 0.95);
}
div[role="radiogroup"] label {
    background: rgba(255, 239, 227, 0.98);
    padding: 18px 16px;
    border-radius: 22px;
    border: 1px solid rgba(205,93,57,0.18);
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.sidebar.markdown(
    "<div style='padding: 8px 0 18px 0; font-family:Garamond,serif;'>"
    "<div style='font-size:48px; font-weight:800; color:#3f2d22; line-height:0.95; word-break: keep-all; overflow-wrap: normal;'>Costumer Segmentation<br>Project</div>"
    "</div>",
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "",
    [
        "Introduction",
        "Data analysis",
        "Data preprocessing",
        "Customer segmentation and clustering",
        "Targeter promotion",
        "Conclusion and recommendations",
    ],
    index=0,
)

st.sidebar.markdown("---")

def render_footer():
    st.markdown(
        """
        <div style='margin:48px auto 0; padding:22px; border-radius:28px; max-width:1080px; background:#fff9f5; border:1px solid rgba(111,79,53,0.12);'>
          <div style='display:grid; grid-template-columns:repeat(4, minmax(180px, 1fr)); gap:18px; align-items:start;'>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.24em; color:#7a6454; margin-bottom:10px;'>Navigation</div>
              <p style='color:#3f2d22; margin:0; line-height:1.6; font-size:14px;'>Use the navigation bar on the left side of the screen.</p>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.24em; color:#7a6454; margin-bottom:10px;'>Work done by</div>
              <div style='display:grid; gap:10px;'>
                <a href='https://github.com/CarlotaMarto' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#3f2d22; cursor:pointer; padding:10px 12px; border-radius:18px; background:rgba(255,255,255,0.75);'>
                  <img src='https://github.com/CarlotaMarto.png' alt='Carlota Marto GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px;'>Carlota Marto</div>
                    <div style='font-size:12px; color:#7a6454;'>20241729</div>
                  </div>
                </a>
                <a href='https://github.com/Franciscaveigateixeira' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#3f2d22; cursor:pointer; padding:10px 12px; border-radius:18px; background:rgba(255,255,255,0.75);'>
                  <img src='https://github.com/Franciscaveigateixeira.png' alt='Francisca Teixeira GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px;'>Francisca Teixeira</div>
                    <div style='font-size:12px; color:#7a6454;'>20241702</div>
                  </div>
                </a>
                <a href='https://github.com/Gouveia316' target='_blank' rel='noreferrer noopener' style='display:flex; gap:12px; align-items:center; text-decoration:none; color:#3f2d22; cursor:pointer; padding:10px 12px; border-radius:18px; background:rgba(255,255,255,0.75);'>
                  <img src='https://github.com/Gouveia316.png' alt='Pedro GitHub' style='width:36px; height:36px; border-radius:50%; object-fit:cover; flex-shrink:0;'/>
                  <div>
                    <div style='font-weight:700; font-size:14px;'>Pedro Gouveia</div>
                    <div style='font-size:12px; color:#7a6454;'>20231657</div>
                  </div>
                </a>
              </div>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.24em; color:#7a6454; margin-bottom:10px;'>Teacher</div>
              <div style='font-weight:700; color:#3f2d22; margin-bottom:6px; font-size:14px;'>Ivo Bernardo</div>
              <div style='color:#7a6454; font-size:13px;'>Machine Learning II</div>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:11px; letter-spacing:0.24em; color:#7a6454; margin-bottom:10px;'>Note</div>
              <p style='color:#3f2d22; line-height:1.6; margin:0; font-size:14px;'>This project is optimized for executive-level business intelligence and strategic decision making.</p>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if page == "Introduction":
    image_file = BASE_DIR / "initial.png"
    st.image(image_file, width=420)
    st.markdown("""
        <div style='font-family:Garamond,serif; color:#3b2720; font-size:46px; line-height:1.05; font-weight:700; margin-top:22px;'>
            Welcome to the customer segmentation project.
        </div>
        <div style='font-size:18px; color:#5f4635; max-width:720px; margin-top:16px; line-height:1.65;'>
            This dashboard brings together preprocessing and clustering workflows from the notebooks. It uses customer purchase, demographic and behavior data to build cleaner datasets, create rich customer features, and identify practical segments for marketing and loyalty strategy.
        </div>
        <div style='font-size:18px; color:#5f4635; max-width:720px; margin-top:16px; line-height:1.65;'>
            Explore how the data was prepared, how customer profiles were calculated, and how clustering produced seven actionable customer groups with distinct spend and loyalty patterns.
        </div>
        <div style='font-size:18px; color:#5f4635; max-width:720px; margin-top:16px; line-height:1.65;'>
            The analytics in this dashboard are designed to support targeted campaigns, optimized promotions, and stronger operational decisions.
        </div>
        <div style='margin-top:26px; max-width:720px; display:grid; row-gap:24px; color:#3b2720;'>
            <div style='padding:18px 20px; background:#fff6f1; border-radius:20px; border:1px solid rgba(205,93,57,0.14);'>
                <div style='font-size:36px; font-weight:700; line-height:1;'>7</div>
                <div style='font-size:14px; color:#7a6454; margin-top:8px;'>segments identified</div>
            </div>
            <div style='padding:18px 20px; background:#fff6f1; border-radius:20px; border:1px solid rgba(205,93,57,0.14);'>
                <div style='font-size:36px; font-weight:700; line-height:1;'>34,060</div>
                <div style='font-size:14px; color:#7a6454; margin-top:8px;'>customers analyzed</div>
            </div>
            <div style='padding:18px 20px; background:#fff6f1; border-radius:20px; border:1px solid rgba(205,93,57,0.14);'>
                <div style='font-size:36px; font-weight:700; line-height:1;'>100,000</div>
                <div style='font-size:14px; color:#7a6454; margin-top:8px;'>purchase records</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Data analysis":
    st.title("Data analysis")
    st.markdown("""
        <div style='max-width:1000px;'>
          <p style='font-size:18px; color:#5f4635; line-height:1.75;'>This section presents initial dataset analysis from the notebooks. It focuses on customer profile characteristics, purchase behavior, and early data quality insights before any clustering is applied.</p>
        </div>
    """, unsafe_allow_html=True)

    # Load dataset files
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
    c1.altair_chart(gender_chart, use_container_width=True)
    c2.subheader("Promotion purchase ratio")
    c2.altair_chart(promo_chart, use_container_width=True)

    st.markdown("### Average spend per category")
    st.altair_chart(spend_chart, use_container_width=True)

    st.markdown("""
        <div style='padding: 24px; border-radius: 24px; background: #fff4ed; border: 1px solid rgba(209,115,70,0.18);'>
          <h3 style='font-family:Garamond,serif; color:#3f2d22; margin-bottom:12px;'>Key insights from the initial dataset review</h3>
          <ul style='color:#5f4635; line-height:1.85; margin-left:18px;'>
            <li>The dataset includes <strong>33,038 customers</strong> and <strong>100,000 purchase invoices</strong>, based on the raw customer profile and basket data.</li>
            <li>Gender balance is nearly even, which supports representative customer profiling.</li>
            <li>Average promotion-driven purchases are around <strong>32%</strong>, highlighting early signs of promotional sensitivity.</li>
            <li>Groceries are the largest spend category, followed by electronics, vegetables, and non-alcoholic drinks.</li>
            <li>This analysis is intentionally preliminary and reflects the data before applying any segmentation or clustering.</li>
          </ul>
        </div>
    """,
    unsafe_allow_html=True)

elif page == "Data preprocessing":
    st.markdown("""
    <div style='padding: 28px; border-radius: 30px; background: #fff8f2; border: 1px solid rgba(111,79,53,0.14);'>
      <h2 style='font-family:Garamond,serif; color:#3f2d22; font-size:32px; margin-bottom:14px;'>Data preprocessing</h2>
      <p style='color:#5f4635; line-height:1.8; margin-bottom:18px;'>This section summarizes the notebook preprocessing workflow: handling invalid dates and negative values, cleaning customer names, engineering customer features, and protecting the dataset for segmentation.</p>
      <ul style='color:#7a6454; line-height:1.9; margin-left:18px;'>
        <li>Future transaction years are set to <code>NaN</code> instead of dropping rows.</li>
        <li>Negative promotion percentage values are corrected and invalid identifiers are excluded.</li>
        <li>Customer names are processed to extract education-level titles while preserving privacy.</li>
        <li>Outliers and skewed spending patterns are inspected to avoid distortion in clustering.</li>
      </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

elif page == "Customer segmentation and clustering":
    st.title("Customer segmentation and clustering")
    st.markdown("Segmentation categories extracted from the preprocessing and clustering-ready dataset.")
    cards = [
        ("Students", "23% · 7,821 customers", "Young, price-sensitive and promotion-driven."),
        ("Wellness Urbanites", "18% · 6,133 customers", "Health-conscious shoppers valuing quality and sustainability."),
        ("Tech Enthusiasts", "15% · 5,109 customers", "Early adopters driven by technology and premium brands."),
        ("Mature Independents", "14% · 4,769 customers", "Independent and established customers valuing quality and convenience."),
        ("Vegetarians", "12% · 4,086 customers", "Plant-based shoppers with health-driven choices."),
        ("Extended Households", "9% · 3,067 customers", "Large families shopping for multiple generations."),
        ("Makro Lovers", "9% · 3,075 customers", "Bulk shoppers looking for value and practicality."),
    ]
    cols = st.columns(4)
    for index, card in enumerate(cards):
        with cols[index % 4]:
            st.markdown(
                f"<div style='background:#fff7f0; border-radius:22px; padding:18px; border:1px solid rgba(111,79,53,0.12);'>"
                f"<h3 style='font-family:Garamond,serif; color:#3f2d22;'>{card[0]}</h3>"
                f"<p style='font-weight:700; color:#5f4635; margin:6px 0;'>{card[1]}</p>"
                f"<p style='color:#7a6454; margin:0;'>{card[2]}</p>"
                f"</div>",
                unsafe_allow_html=True,
            )

elif page == "Targeter promotion":
    st.title("Targeter promotion")
    st.write("Promotions targeting content will be added here once the campaign rules and segment mapping are ready.")

elif page == "Conclusion and recommendations":
    st.title("Conclusion and recommendations")
    st.write("This page is reserved for the final summary, strategic takeaways, and future recommendations.")

else:
    st.title("Page not found")
    st.write("The selected page is not available. Please choose a valid option from the sidebar.")

render_footer()
