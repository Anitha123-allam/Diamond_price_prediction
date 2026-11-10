from pathlib import Path
import pickle

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Diamond Price Studio",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

    :root {
        --ink: #f8f7ff;
        --muted: #c0c6dd;
        --purple: #a855f7;
        --purple-dark: #7c3aed;
        --gold: #ffd166;
        --line: rgba(179, 193, 255, .2);
    }

    .stApp {
        background:
            radial-gradient(ellipse at 8% 10%, rgba(0, 224, 255, .18), transparent 28%),
            radial-gradient(ellipse at 96% 28%, rgba(255, 65, 145, .17), transparent 27%),
            linear-gradient(145deg, #10152f 0%, #171b3f 52%, #211441 100%);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stMainBlockContainer"] { max-width: 1120px; padding-top: 2rem; }
    h1, h2, h3, p, label { font-family: 'DM Sans', sans-serif; }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 2.4rem 2.6rem;
        margin: 0 0 1.5rem;
        border: 1px solid rgba(255,255,255,.22);
        border-radius: 24px;
        color: #fff;
        background: linear-gradient(115deg, #00a6c7 0%, #6250e8 47%, #d63384 100%);
        box-shadow: 0 18px 44px rgba(0, 0, 0, .32);
    }
    .hero:after {
        content: '✧';
        position: absolute;
        right: 7%;
        top: -64px;
        color: rgba(255,255,255,.13);
        font-size: 290px;
        line-height: 1;
        pointer-events: none;
    }
    .eyebrow {
        position: relative;
        z-index: 1;
        color: #fff09a;
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .19em;
        text-transform: uppercase;
    }
    .hero h1 {
        position: relative;
        z-index: 1;
        margin: .55rem 0 .45rem;
        color: #fff;
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2.1rem, 5vw, 3.25rem);
        font-weight: 700;
        letter-spacing: -.025em;
    }
    .hero p {
        position: relative;
        z-index: 1;
        max-width: 570px;
        margin: 0;
        color: rgba(255,255,255,.9);
        font-size: 1.02rem;
        line-height: 1.65;
    }
    .section-heading {
        margin: .2rem 0 .15rem;
        color: #fff;
        font-size: 1.15rem;
        font-weight: 700;
    }
    .section-caption {
        margin: 0 0 1rem;
        color: #bfc8e3;
        font-size: .9rem;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid var(--line);
        border-radius: 18px;
        background: linear-gradient(145deg, rgba(33, 40, 82, .96), rgba(31, 25, 65, .96));
        box-shadow: 0 12px 30px rgba(0, 0, 0, .22);
    }
    [data-testid="stNumberInput"] label,
    [data-testid="stSelectbox"] label {
        color: #f2eeff;
        font-size: .88rem;
        font-weight: 600;
    }
    [data-testid="stNumberInput"] input,
    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        border-radius: 10px;
        background-color: #151a38;
        color: #fff;
        border-color: #505a8a;
    }
    [data-testid="stSelectbox"] [data-baseweb="select"] { color: #fff; }
    [data-testid="stSelectbox"] [data-baseweb="select"] svg { fill: #c4b5fd; }
    [data-testid="stNumberInput"] button {
        color: #fff;
        background: #282e5b;
        border-color: #505a8a;
    }
    [data-testid="stNumberInput"] input:focus {
        border-color: var(--purple);
        box-shadow: 0 0 0 1px var(--purple);
    }
    .stFormSubmitButton > button {
        min-height: 3rem;
        border: 0;
        border-radius: 11px;
        color: #fff;
        background: linear-gradient(100deg, #ff3d8d, #8b5cf6 52%, #00c2e0);
        font-weight: 700;
        box-shadow: 0 8px 22px rgba(167, 61, 235, .35);
        transition: transform .15s ease, box-shadow .15s ease;
    }
    .stFormSubmitButton > button:hover {
        border: 0;
        color: #fff;
        transform: translateY(-1px);
        box-shadow: 0 11px 24px rgba(0, 194, 224, .32);
    }
    [data-testid="stAlert"] { border-radius: 12px; }
    .result-card {
        margin-top: 1.1rem;
        padding: 1.25rem 1.5rem;
        border: 1px solid rgba(255, 209, 102, .55);
        border-radius: 16px;
        background: linear-gradient(110deg, #42217a, #76284f 58%, #594018);
        box-shadow: 0 12px 26px rgba(0, 0, 0, .2);
    }
    .result-label {
        color: #ffe28a;
        font-size: .8rem;
        font-weight: 700;
        letter-spacing: .12em;
        text-transform: uppercase;
    }
    .result-price {
        margin-top: .25rem;
        color: #fff;
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.2rem;
        font-weight: 700;
    }
    .footer-note {
        padding: 1.3rem 0 .3rem;
        color: #aab4d2;
        font-size: .8rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

project_dir = Path(__file__).resolve().parent
model_path = project_dir / "model.pkl"
if not model_path.exists():
    model_path = project_dir / "model .pkl"

try:
    with model_path.open("rb") as model_file:
        model = pickle.load(model_file)
    with (project_dir / "feature_columns.pkl").open("rb") as feature_file:
        feature_columns = pickle.load(feature_file)
    with (project_dir / "maps.pkl").open("rb") as maps_file:
        maps = pickle.load(maps_file)
except Exception as error:
    st.error(f"Could not load the model files. Run the notebook first. {error}")
    st.stop()

st.markdown(
    """
    <section class="hero">
      <div class="eyebrow">The Diamond Price Studio</div>
      <h1>Discover your diamond's value</h1>
      <p>Enter the stone's characteristics for a quick, data-informed price estimate.
      Every detail helps refine the prediction.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown('<div class="section-heading">01 &nbsp; Diamond profile</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Choose the quality attributes of your stone.</div>',
        unsafe_allow_html=True,
    )

    with st.form("diamond_details"):
        quality_col, grade_col = st.columns(2, gap="large")
        carat = quality_col.number_input(
            "Carat weight", min_value=0.0, max_value=10.0, value=0.70, step=0.01
        )
        cut = quality_col.selectbox(
            "Cut", ["Ideal", "Premium", "Very Good", "Good", "Fair"]
        )
        color = quality_col.selectbox(
            "Color grade · D is best", ["D", "E", "F", "G", "H", "I", "J"], index=3
        )
        clarity = grade_col.selectbox(
            "Clarity grade · IF is best",
            ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"],
            index=5,
        )

        st.markdown('<div class="section-heading">02 &nbsp; Measurements</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-caption">Enter the proportions and dimensions in millimetres.</div>',
            unsafe_allow_html=True,
        )
        measurement_col, dimension_col = st.columns(2, gap="large")
        depth = measurement_col.number_input(
            "Depth (%)", min_value=0.0, max_value=100.0, value=61.8, step=0.1
        )
        table = measurement_col.number_input(
            "Table (%)", min_value=0.0, max_value=100.0, value=57.0, step=0.1
        )
        x = dimension_col.number_input(
            "Length · x (mm)", min_value=0.0, max_value=30.0, value=5.70, step=0.01
        )
        y = dimension_col.number_input(
            "Width · y (mm)", min_value=0.0, max_value=30.0, value=5.72, step=0.01
        )
        z = dimension_col.number_input(
            "Depth · z (mm)", min_value=0.0, max_value=30.0, value=3.53, step=0.01
        )
        submitted = st.form_submit_button("✦  Estimate diamond price", use_container_width=True)

if submitted:
    if carat <= 0 or x <= 0 or y <= 0 or z <= 0:
        st.error("Carat weight and all three dimensions must be greater than zero.")
    else:
        depth_check = 2 * z / (x + y) * 100
        if abs(depth_check - depth) > 5:
            st.warning(
                f"Depth may not match the dimensions. The measurements imply "
                f"{depth_check:.1f}%; check x, y, z and depth."
            )

        size_ratio = carat / (x * y * z)
        if size_ratio < 0.005 or size_ratio > 0.0075:
            st.warning(
                "Carat weight may not match the dimensions of a typical diamond. "
                "Please check the values."
            )

        if carat > 6 or x > 12 or y > 12 or z > 8:
            st.warning(
                "These values are larger than most diamonds in the training data. "
                "The estimate may be less reliable."
            )

        try:
            input_df = pd.DataFrame(
                [
                    {
                        "carat": carat,
                        "cut": maps["cut"][cut],
                        "color": maps["color"][color],
                        "clarity": maps["clarity"][clarity],
                        "depth": depth,
                        "table": table,
                        "x": x,
                        "y": y,
                        "z": z,
                        "volume": x * y * z,
                        "log_carat": np.log(carat),
                        "carat_group": 0 if carat < 0.5 else 1 if carat < 1 else 2 if carat < 2 else 3,
                    }
                ]
            )[feature_columns]

            price = model.predict(input_df)[0]
            st.markdown(
                f"""
                <div class="result-card">
                  <div class="result-label">Estimated price · USD</div>
                  <div class="result-price">${price:,.0f}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        except Exception as error:
            st.error(f"Prediction failed: {error}")

st.markdown(
    '<div class="footer-note">Estimates are model-generated and intended as a guide, not a formal appraisal.</div>',
    unsafe_allow_html=True,
)
