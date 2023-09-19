import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Logo.png'))

st.header('EvE Links!')

st.info('Links zu 3rd Party EvE Websites, by Salvage Tony')

icon_size = 20

st_button('pathfinder', 'https://pathfinder.lost-in-w.space', 'Pathfinder', icon_size)
st_button('goonpraisal', 'https://appraise.imperium.nexus', 'GoonPraisal', icon_size)
st_button('evetycoon', 'https://evetycoon.com/market', 'EvE Tycoon', icon_size)
st_button('zkill', 'https://zkillboard.com/', 'zKillboard', icon_size)
st_button('evescout', 'https://www.eve-scout.com/thera', 'Eve-Scout', icon_size)
st_button('dotlan', 'https://evemaps.dotlan.net/map', 'Dotlan', icon_size)
st_button('cerlestes', 'https://ore.cerlestes.de/ore', 'Cerlestes', icon_size)
