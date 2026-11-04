import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GTA SA 3D Studio", page_icon="🚗", layout="wide")
st.markdown(
    "<style>.block-container{padding:0.5rem 0.5rem 0 0.5rem;max-width:100%}"
    "header,footer{visibility:hidden}</style>",
    unsafe_allow_html=True,
)

here = Path(__file__).parent
html = (here / "studio.html").read_text(encoding="utf-8")

# Optional: put your ped.ifp next to this file and every visitor gets the
# animation list automatically (no upload needed).
ifp = here / "ped.ifp"
if ifp.exists():
    b64 = base64.b64encode(ifp.read_bytes()).decode()
    html = html.replace("/*IFP_B64*/", f'window.PED_IFP_B64="{b64}";')

components.html(html, height=800, scrolling=False)
