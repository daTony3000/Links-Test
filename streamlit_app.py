import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Logo.png'))

st.header('EvE Links!')

st.info('Links zu 3rd Party EvE Websites, by Salvage Tony')

icon_size = 20

st_button('https://pathfinder.lost-in-w.space', 'Pathfinder')
st_button('https://appraise.imperium.nexus', 'GoonPraisal')
st_button('https://evetycoon.com/market', 'EvE Tycoon')
st_button('https://zkillboard.com/', 'zKillboard')
st_button('https://www.eve-scout.com/thera', 'Eve-Scout')
st_button('https://evemaps.dotlan.net/map', 'Dotlan')
st_button('https://ore.cerlestes.de/ore', 'Cerlestes')
