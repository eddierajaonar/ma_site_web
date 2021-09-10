import streamlit as st
import os, re
import json
import config
import tweepy
import pandas as pd
import requests
from datetime import datetime
from bs4 import BeautifulSoup

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# en production: rajouter les infos de connexions dans un variables d'environnement puis:
# TWITTER_CONSUMER_KEY = os.version.get('TWITTER_CONSUMER_KEY')
# TWITTER_CONSUMER_SECRET = os.version.get('TWITTER_CONSUMER_SECRET')
# TWITTER_ACCESS_TOKEN = os.version.get('TWITTER_ACCESS_TOKEN')
# TWITTER_ACCESS_TOKEN_SECRET = os.version.get('TWITTER_ACCESS_TOKEN_SECRET')
# auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
# auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)


# current_month = datetime.now().strftime('%m')
# current_year = datetime.now().strftime('%Y')
# from_date = f"{current_year}{current_month}010000"
# today = datetime.now().strftime('%Y%m%d%H%M')

def apply_formatting(col):
    column = [1,3,5,7,9,11]
    
    if col.name in column:
        return ['background-color: green' for c in col.values]



def get_tweepy():
    st.title("Informations de la journée pour une action boursière")
    st.subheader("Veuillez indiquer l'action ici: ")
    hashtag = f"${st.text_input('symbol', 'AMZN')}"
    
    #get logo with bcs4 (for company name) and api lolo clearbit for logo:
    
    url_for_logo = f'https://finance.yahoo.com/quote/{hashtag[1:]}/'
    get_url = requests.get(url_for_logo)
    get_text = get_url.text
    soup = BeautifulSoup(get_text, "html.parser")
    
    elements = soup.find('h1', {'class': re.compile(r'D\(ib\)\sFz\(18px\)$')})
    p = re.compile(">(\w+)(.|,|\s)")
    try:
        company_name = p.search(str(elements)).group(1)
        st.markdown(f"""<img src="https://logo.clearbit.com/{company_name}.com" 
                    style="text-align: right;"
                    alt="{company_name}">""", unsafe_allow_html=True)
    except AttributeError:
        st.error(f"symbol inconnu !! ")
    
    tweets = tweepy.Cursor(api.search, q=hashtag).items(1)
    
    for tweet in tweets:
        st.markdown('---')
        st.header(hashtag[1:])
        st.write(tweet.text)
        st.image(f"https://finviz.com/chart.ashx?t={hashtag}")
        
    
    
    # get information (talbeau) in the web:
    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    
    url = f'https://finviz.com/quote.ashx?t={hashtag[1:]}'
    r = requests.get(url, headers=header)
    stock_info = pd.read_html(r.text)
    try:
        df = stock_info[5]
        df.style.apply(apply_formatting, subset=['column_name']) # axis=0 by default
        st.markdown('---')
        st.subheader(f"descriptif de la société {hashtag[1:]}: ")
        st.dataframe(df,800, 600)
    except :
        st.error(f"Erreur de syntaxe pour {hashtag[1:]}. Aussi, le details ne fonctionne que pour les entreprises coté en Bourse ")
                        
if __name__ == "__main__":
    
    get_tweety()

