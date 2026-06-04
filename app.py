import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="Costumer Segmentation Project", layout="wide")

css = """
<style>
body {
    background: linear-gradient(180deg, #f6f1eb 0%, #fbf2ec 100%);
}
section[role="main"] {
    padding-top: 0px;
}
[data-testid="stSidebar"] {
    background: #fff3eb;
}
.css-1d391kg {
    background-color: #fff8f2;
}
.stButton>button {
    background-color: #c94f38;
    color: white;
    border-radius: 999px;
    border: none;
}
.st-bb {
    border-radius: 24px;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.sidebar.markdown(
    "<div style='padding: 8px 0 18px 0; font-family: Inter, sans-serif;'>"
    "<div style='font-size:26px; font-weight:800; color:#3f2d22;'>Costumer Segmentation</div>"
    "<div style='font-size:11px; margin-top:6px; color:#7a6454; text-transform:uppercase; letter-spacing:0.18em;'>Project</div>"
    "</div>",
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Introduction",
        "Data preprocessing",
        "Communities",
        "People",
        "Behaviors",
        "Opportunities",
        "Campaigns",
        "Signals",
        "Data sources",
    ],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='padding: 18px; border-radius: 22px; background: #fff7f0; border: 1px solid rgba(111,79,53,0.18);'>"
    "<div style='font-weight:700; color:#3f2d22; margin-bottom:6px;'>Administrator</div>"
    "<div style='color:#7a6454; font-size:14px;'>Dashboard</div>"
    "</div>",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")

def render_footer():
    st.markdown(
        """
        <div style='margin-top:48px; padding:30px; border-radius:32px; background:#fff9f5; border:1px solid rgba(111,79,53,0.12);'>
          <div style='display:grid; grid-template-columns:1.1fr 1.2fr 1fr 1fr; gap:24px; align-items:start;'>
            <div>
              <div style='text-transform:uppercase; font-size:12px; letter-spacing:0.22em; color:#7a6454; margin-bottom:14px;'>Navigation</div>
              <p style='color:#3f2d22; margin:0; line-height:1.8;'>Use the navigation bar on the left side of the screen.</p>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:12px; letter-spacing:0.22em; color:#7a6454; margin-bottom:14px;'>Work done by</div>
              <div style='display:flex; gap:12px; align-items:center; margin-bottom:12px;'>
                <div style='width:40px; height:40px; border-radius:50%; background:#c94f38;'></div>
                <div>
                  <div style='font-weight:700; color:#3f2d22;'>Carlota Marto</div>
                  <div style='font-size:13px; color:#7a6454;'>20241729</div>
                </div>
              </div>
              <div style='display:flex; gap:12px; align-items:center; margin-bottom:12px;'>
                <div style='width:40px; height:40px; border-radius:50%; background:#b77b45;'></div>
                <div>
                  <div style='font-weight:700; color:#3f2d22;'>Francisca Teixeira</div>
                  <div style='font-size:13px; color:#7a6454;'>20241702</div>
                </div>
              </div>
              <div style='display:flex; gap:12px; align-items:center;'>
                <div style='width:40px; height:40px; border-radius:50%; background:#8c6f53;'></div>
                <div>
                  <div style='font-weight:700; color:#3f2d22;'>Pedro Gouveia</div>
                  <div style='font-size:13px; color:#7a6454;'>Project Contributor</div>
                </div>
              </div>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:12px; letter-spacing:0.22em; color:#7a6454; margin-bottom:14px;'>Teacher</div>
              <div style='font-weight:700; color:#3f2d22; margin-bottom:6px;'>Ivo Bernardo</div>
              <div style='color:#7a6454;'>Machine Learning II</div>
            </div>
            <div>
              <div style='text-transform:uppercase; font-size:12px; letter-spacing:0.22em; color:#7a6454; margin-bottom:14px;'>Note</div>
              <p style='color:#3f2d22; line-height:1.8; margin:0;'>This project is optimized for executive-level business intelligence and strategic decision making.</p>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if page == "Introduction":
    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.markdown("""
        <div style='font-family:Garamond,serif; color:#3f2d22; font-size:66px; line-height:0.94; font-weight:700;'>
            Understand every customer.
            <br>
            Grow with purpose.
        </div>
        <p style='font-size:18px; color:#5f4635; max-width:660px; margin-top:18px;'>
            We turn data into human understanding so you can build stronger relationships, create relevant experiences, and drive sustainable growth.
        </p>
        """,
        unsafe_allow_html=True,
        )
        st.markdown(
            "<button style='padding: 14px 32px; font-weight:700; font-size:14px; background:#c94f38; color:#ffffff; border:none; border-radius:999px;'>Explore your communities</button>",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div style='position:relative; min-height:320px; border-radius:30px; background:linear-gradient(180deg,#f3e6dc 0%,#fef6ef 100%); padding:28px;'>
                <div style='position:absolute; top:22px; right:22px; width:120px; height:120px; border-radius:50%; background:rgba(201,79,56,0.18);'></div>
                <div style='position:absolute; bottom:24px; left:24px; width:140px; height:140px; border-radius:50%; background:rgba(183,123,69,0.14);'></div>
                <div style='position:absolute; top:100px; left:70px; width:108px; height:108px; border-radius:28px; background:#c94f38;'></div>
                <div style='position:absolute; top:152px; right:86px; width:78px; height:78px; border-radius:28px; background:#b77b45;'></div>
                <div style='position:absolute; bottom:70px; right:40px; width:96px; height:96px; border-radius:28px; background:#8c6f53;'></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("\n")
        st.markdown(
            "<div style='display:grid; grid-template-columns:1fr 1fr; gap:16px;'>"
            "<div style='padding:20px; border-radius:24px; background:#fff8f2; border:1px solid rgba(111,79,53,0.14);'>"
            "<div style='font-size:28px; font-weight:700; color:#3f2d22;'>34,060</div>"
            "<div style='color:#7a6454; margin-top:6px;'>customers analyzed</div>"
            "</div>"
            "<div style='padding:20px; border-radius:24px; background:#fff8f2; border:1px solid rgba(111,79,53,0.14);'>"
            "<div style='font-size:28px; font-weight:700; color:#3f2d22;'>7</div>"
            "<div style='color:#7a6454; margin-top:6px;'>communities discovered</div>"
            "</div>"
            "</div>",
            unsafe_allow_html=True,
        )

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

elif page == "Communities":
    st.title("Your 7 customer communities")
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

elif page == "People":
    st.title("People")
    st.write("Content is based on notebook preprocessing and is reserved for future dataset insights.")

elif page == "Behaviors":
    st.title("Behaviors")
    st.write("Behavioral insights are not yet available in this notebook.")

elif page == "Opportunities":
    st.title("Opportunities")
    st.write("Opportunity analysis is currently blank until notebook data is added.")

elif page == "Campaigns":
    st.title("Campaigns")
    st.write("Campaign insights will be added once the dataset is expanded.")

elif page == "Signals":
    st.title("Signals")
    st.write("Signals are not present in the current preprocessing notebook.")

else:
    st.title("Data sources")
    st.write("Data source details are blank because the notebook only includes preprocessing summary.")

render_footer()
