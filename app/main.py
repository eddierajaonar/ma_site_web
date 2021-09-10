import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import os, base64
from get_tweet import get_tweepy
from dashboard import analytics
from finance import finance_dashboard
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.palettes import Spectral10
from bokeh.plotting import figure
from bokeh.models import FactorRange
from pathlib import Path
import streamlit.components.v1 as components

SOURCE_FILE = Path(__file__).resolve() # pour recuperer le realpath au cas où c'est un lien symbolique
SOURCE_DIR = SOURCE_FILE.parent
COMPONENT_DIR = SOURCE_DIR / "components"

# function #1 to generate a HREF for an image 
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# function #2 to generate a HREF for an image 
@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}" target="_blank">
            <img style="width:75px;height:75px;" src="data:images/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code


photo = get_img_with_href('images/eddie.png', '#')
badge_django = get_img_with_href('images/django-200x200.png', 'https://skillvalue.com/fr/user/certificate/i7N4up4Jc9Hg9Ua6k8A99ywWFu33kripQdHd3UznUDTwvhNVBDKv17Le7Ges')
badge_splunk = get_img_with_href('images/SplunkEnterprise_Certified-Admin-600px.png', 'https://www.credly.com/badges/748bd1da-1720-483f-8917-1336665f9fe9')
badge_bigdata = get_img_with_href('images/BigData.png', 'https://www.youracclaim.com/badges/3f121e42-6182-4dab-859e-1b8480dd598c/public_url')
badge_hadoop = get_img_with_href('images/hadoop.png', 'https://www.youracclaim.com/badges/8e445f33-a425-4e8f-9659-a6a3def8c4d6/public_url')


st.sidebar.markdown("""<h2><strong>Eddie RAJAONARIVELO</strong></h2>\
                    Consultant Big Data - Data engineer<br> \
                    Developpeur Python orienté Data<br> \
                    <span style="color:blue">@: e.rajaonarivelo (at) gmail.com </span><br><br>""", unsafe_allow_html=True)

with st.sidebar:
    col1, col2, col3,col4 = st.columns(4)
    col1.markdown(badge_django, unsafe_allow_html=True)
    col2.markdown(badge_splunk, unsafe_allow_html=True)
    col3.markdown(badge_bigdata, unsafe_allow_html=True)
    col4.markdown(badge_hadoop, unsafe_allow_html=True)

st.sidebar.markdown('---')

option = st.sidebar.selectbox("MENU : ", ('à propos', 'action (stocks)', 'Analyse de données', 'finance dashboard', 'pattern'), 0)

st.sidebar.markdown('---')
st.sidebar.markdown("""<h3><strong>Technos utilisés: </strong></h3><br/>
    <ul>
    <li>numpy / pandas</li>
    <li>streamlit</li>
    <li>yfinance</li>
    <li>tweepy</li>
    <li>bokeh/matplotlib</li>
    <li>seaborn</li>
    <li>json rest API</li>
    <li>web scraping</li>
</ul>""", unsafe_allow_html=True)

if option =="à propos":
    
    with open(COMPONENT_DIR/"about.html", "r", encoding='utf-8') as file:
        about = file.read()
        
    components.html(about, height = 600)
    
    skills = ["python","spark","hadoop","kafka", "linux", "sql", "javascript", "splunk", "powerbi", "docker"]
    note = [85, 40, 40, 50, 75, 50, 35, 75, 30, 45]
    
    source = ColumnDataSource(data=dict(skills=skills, note=note, color=Spectral10))

    p = figure(x_range=skills, y_range=(0,100), plot_height=500, plot_width=760, title="skills",
            toolbar_location=None, tools="")

    p.vbar(x='skills', top='note', width=0.7, color='color', legend_field="skills", source=source)
    
    labels = LabelSet(x='skills', y='note', text='note', level='glyph',
        x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    p.add_layout(labels)
    
    # displaying the model
    st.bokeh_chart(p)


if option == 'action (stocks)':
    get_tweepy()
    
if option == 'Analyse de données':
    analytics()

if option == 'finance dashboard':
    finance_dashboard()
