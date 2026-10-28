import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="LCG Studio",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# UI-only styling: retain the existing calculations and application behavior.
st.markdown(
    """
    <style>
    :root {
        --lcg-bg: #0b1020;
        --lcg-panel: #111a2e;
        --lcg-panel-soft: #151f35;
        --lcg-border: #26334d;
        --lcg-text: #edf2ff;
        --lcg-muted: #9aa9c4;
        --lcg-accent: #9b8cff;
        --lcg-accent-bright: #b4a8ff;
    }

    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stHeader"] {
        background: var(--lcg-bg);
        color: var(--lcg-text);
    }
    [data-testid="stHeader"] { background: rgba(11, 16, 32, .92); }
    [data-testid="stMainBlockContainer"] {
        max-width: 1180px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, h4, p, label,
    [data-testid="stMarkdownContainer"],
    [data-testid="stWidgetLabel"] p { color: var(--lcg-text); }
    h1 { letter-spacing: -.045em; font-weight: 750; }
    h2, h3 { letter-spacing: -.025em; font-weight: 680; }
    p, label { line-height: 1.65; }
    [data-testid="stCaptionContainer"] { color: var(--lcg-muted); }

    .lcg-eyebrow {
        color: var(--lcg-accent-bright);
        font-size: .76rem;
        font-weight: 750;
        letter-spacing: .16em;
        text-transform: uppercase;
        margin-bottom: .55rem;
    }
    .lcg-subtitle { color: var(--lcg-muted); font-size: 1.02rem; max-width: 720px; }
    .lcg-formula {
        border: 1px solid var(--lcg-border);
        border-radius: 16px;
        background: linear-gradient(135deg, #151f37, #11172a);
        padding: 1.15rem 1.4rem;
        margin: 1rem 0 1.6rem 0;
    }
    .lcg-formula-label {
        color: var(--lcg-muted);
        font-size: .72rem;
        font-weight: 700;
        letter-spacing: .12em;
        text-transform: uppercase;
        margin-bottom: .35rem;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--lcg-border) !important;
        background: var(--lcg-panel);
        border-radius: 18px;
    }
    [data-testid="stNumberInput"] input,
    input, textarea {
        background: #0c1426 !important;
        color: var(--lcg-text) !important;
        border: 1px solid #34415e !important;
        border-radius: 10px !important;
    }
    [data-testid="stNumberInput"] button {
        color: var(--lcg-text) !important;
        background: #17223a !important;
        border-color: #34415e !important;
    }
    .stButton > button[kind="primary"] {
        width: 100%;
        min-height: 2.9rem;
        background: var(--lcg-accent) !important;
        color: #101126 !important;
        border: 1px solid var(--lcg-accent) !important;
        border-radius: 11px !important;
        font-weight: 750 !important;
        transition: background .18s ease, transform .18s ease;
    }
    .stButton > button[kind="primary"]:hover {
        background: var(--lcg-accent-bright) !important;
        border-color: var(--lcg-accent-bright) !important;
        transform: translateY(-1px);
    }
    .stButton > button:focus { box-shadow: 0 0 0 .2rem rgba(155, 140, 255, .24) !important; }
    [data-testid="stDataFrame"] {
        border: 1px solid var(--lcg-border);
        border-radius: 12px;
        overflow: hidden;
    }
    [data-testid="stAlert"] { border-radius: 12px; }
    [data-testid="stCode"] {
        border: 1px solid var(--lcg-border);
        border-radius: 12px;
        background: #0c1426;
    }
    hr { border-color: var(--lcg-border); }

    @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] { padding: 1.25rem 1rem 2rem; }
        h1 { font-size: 2rem !important; }
        .lcg-formula { padding: .9rem 1rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Application heading
st.markdown('<div class="lcg-eyebrow">P1 · Randomness toolkit</div>', unsafe_allow_html=True)
st.title("LCG Studio")
st.markdown(
    '<div class="lcg-subtitle">Explore a linear congruential generator with clear inputs and transparent, step-by-step calculations.</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.caption("THE RECURRENCE")
    st.latex(r"X_{n+1} = (aX_n + c) \bmod m")

# Inputs
st.subheader("Generator parameters")
st.caption("Set the four parameters, then generate a sequence to inspect each calculation.")
with st.container(border=True):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        multiplier = st.number_input("Multiplier (a)", min_value=0, value=5, step=1)
    with col2:
        seed = st.number_input("Seed (X₀)", min_value=0, value=7, step=1)
    with col3:
        increment = st.number_input("Increment (c)", min_value=0, value=3, step=1)
    with col4:
        modulus = st.number_input("Modulus (m)", min_value=2, value=16, step=1)

    generate = st.button("Generate sequence", type="primary")

if generate:
    # Validate seed
    if seed >= modulus:
        st.error(
            "Seed must be smaller than the modulus. "
            "Choose X₀ such that 0 ≤ X₀ < m."
        )
    else:
        a = int(multiplier)
        c = int(increment)
        x0 = int(seed)
        m = int(modulus)

        # Generate the first 8 values
        count = 8
        x = x0
        rows = []

        for n in range(1, count + 1):
            previous = x
            x = (a * x + c) % m
            rows.append({
                "Step": n,
                "Previous value": previous,
                "Calculation": f"({a} × {previous} + {c}) mod {m}",
                "New value": x,
            })

        st.divider()
        st.subheader("Generated sequence")
        st.caption("The first eight values produced from the selected parameters.")
        sequence = [row["New value"] for row in rows]
        st.code(", ".join(map(str, sequence)))

        st.subheader("Step-by-step calculation")
        st.dataframe(pd.DataFrame(rows), width="stretch", hide_index=True)

        # Existing cycle analysis retained without changing its behavior.
        x_cycle = x0
        seen_cycle = {}
        cycle_states = []
        while x_cycle not in seen_cycle:
            seen_cycle[x_cycle] = len(cycle_states)
            cycle_states.append(x_cycle)
            x_cycle = (a * x_cycle + c) % m

        cycle_start = seen_cycle[x_cycle]
        period = len(cycle_states) - cycle_start
        full_period = cycle_start == 0 and period == m
else:
    st.info("Enter your parameters above and select **Generate sequence** to view the output.")

st.divider()
st.caption("LCG Studio · Educational tool for exploring deterministic pseudo-random sequences")
