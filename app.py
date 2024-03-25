import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(layout="wide")

m = folium.Map(location=[ -3.061144, -59.968397], zoom_start=16)
folium.Marker(
        [ -3.061144, -59.968397],
        popup="Base REA TELECOM",
        tooltip="Base REA TELECOM"
    ).add_to(m)

st_data = st_folium(m, width = 725)