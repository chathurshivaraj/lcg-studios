# LCG Studio — Linear Congruential Generator

A Streamlit application for exploring the recurrence:

`X_(n+1) = (a * X_n + c) % m`

## Current functionality

- Inputs for multiplier (`a`), seed (`X0`), increment (`c`), and modulus (`m`)
- Generation of the first eight values
- Step-by-step calculation table
- Validation that the seed is smaller than the modulus
- Internal cycle detection and period calculation
- Responsive dark-themed interface

> Scope note: the current implementation does not display a chart or normalized values and does not provide CSV export. These are not included in the current source implementation.

## Requirements

- Python 3.10 or newer
- Packages listed in `requirements.txt`

## Run locally

1. Install Python.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the app: `streamlit run app.py`
6. Open the local URL printed in the terminal, usually `http://localhost:8501`.

## Example

Use `X0=7`, `a=5`, `c=3`, `m=16`. The first eight generated values are `6, 1, 8, 11, 10, 5, 12, 15`.
