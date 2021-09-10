import streamlit as st #web app 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns 
from collections import Counter
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import os
from pathlib import Path

SOURCE_FILE = Path(__file__).resolve() # pour recuperer le realpath au cas où c'est un lien symbolique
SOURCE_DIR = SOURCE_FILE.parent
DATA_DIR = SOURCE_DIR / "data"

def analytics():

    st.title("Analyse de données e-commerce")

    st.subheader("Données utilisés: Online Sales data (Kaggle) 🏷️ 📈")
    st.markdown('<u>echantillon de données:</u>', unsafe_allow_html=True)
    
    df = pd.read_csv(DATA_DIR/'BlackFriday.csv')
    st.dataframe(df.head())
    
    st.markdown('---')


    st.markdown("### Key Metrics")

    kpi1, kpi2, kpi3 = st.columns(3)

    my_dynamic_value = 333.3335 

    new_val = 222

    final_val = my_dynamic_value / new_val

    kpi1.metric(label = "visite moyenne",
                value = 3.5,
                delta = -1.4)

    kpi2.metric(label = "taux de rebond",
                value = 78,
                delta = -5,
                delta_color = 'inverse')
    kpi3.metric(label = "Visiteurs uniques",
                value = "%.2f" %final_val )
    
    st.markdown("---")
    st.markdown("### ➡️ Qui a le + de pouvoir d'achats  ? 👨👩")
    
    explode = (0.1,0)  
    fig1, ax1 = plt.subplots(figsize=(12,7))
    ax1.pie(df['Gender'].value_counts(), explode=explode,labels=['Male','Female'], autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')  
    plt.tight_layout()
    plt.legend()
    st.pyplot(fig1)
    
    st.markdown("---")
    st.markdown("### ➡️ categorie d'âges des acheteurs: 👦👨👩👴🏽")
    fig1, ax1 = plt.subplots(figsize=(12,7))
    sns.countplot(x=df['Age'],hue=df['Gender'])
    st.pyplot(fig1)
    
    st.markdown("---")
    st.markdown("### ➡️ dans quel ville viennent les acheteurs ? 🏠🏙️")
    
    df2 = df.copy()
    vals_to_replace = {'A':'Paris', 'B':'Bordeaux', 'C':'Lyon'}
    df2["City_Category"] = df2["City_Category"].map(vals_to_replace)

    explode = (0.1, 0, 0)
    figure, ax1 = plt.subplots(figsize=(12,7))
    ax1.pie(df2.groupby('City_Category')['Purchase'].sum(),explode=explode, labels=df2['City_Category'].unique(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')  
    plt.tight_layout()
    plt.legend()
    st.pyplot(figure)

    st.markdown("---")
    st.markdown("### ➡️ Dans chaque ville, dans quel tranche d'âge on achète le plus ?  🏠🏙️")
    fig1, ax1 = plt.subplots(figsize=(12,7))
    sns.countplot(x=df2['City_Category'],hue=df2['Age'])
    st.pyplot(fig1)
    
    st.markdown("""<u> interprétation </u><br/>
                sans surprise, il apparait que les individus de 26 à 35 ans ont un grand impact sur le chiffres d'affaires
                de cette entreprise e-commerce, et font leur cible principale, peut importe la ville où il habitent.<br/>
                En outre, les jeunes de moins de 17 ans et les + de 55 ans ont un part très faible. Comme nous sommes dans 
                un environnement e-commerce, il faut voir les raisons de cela, par exemple:<br/>
                <b>=> pour les + 55 ans</b>:<br/>
                -- difficulté d'effectuer un achat en ligne ?,<br/>
                -- produits vendus ne correpondant pas vraiment à leur besoin ?,<br/>
                -- etc...<br/><br/>
                <b>=> pour les - 17 ans</b>:<br/>
                -- restrictions aux niveaux de leur parents ( ex: carte bancaire bloqué) ?<br/>
                -- les produits vendus ne correspondent pas nons plus à leur besoins ?<br/>
                -- l'entreprise n'a pas assez communiqués ? (ex: publicité bien ciblé )<br/>
                --etc ...""",unsafe_allow_html=True )
    
    
    
if __name__ == "__main__":
    analytics()
