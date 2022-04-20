# -------------

import streamlit as st
import pandas as pd
import os

import plotly.express as px

st.set_page_config(layout="wide")


path = os.path.dirname(__file__)



st.markdown("# Bias in media coverage of severe conflicts between May 2019 and April 2022")

# -------------
# 
# -------------
df = pd.read_pickle(path+'/df_1.pkl')

fig = px.choropleth(df, locations="iso3",
                    color="fatalities",
                    hover_name="country",
                    animation_frame="event_date",
                    title = "Conflicts with more than 100 fatalities",
                    color_continuous_scale=px.colors.sequential.PuRd,
                    range_color = (df["fatalities"].min(),df["fatalities"].max()))
 
st.plotly_chart(fig, use_container_width=True)


# -------------
# 
# -------------
df = pd.read_pickle(path+'/df_2.pkl')

fig = px.choropleth(df, locations="iso3",
                    color="fatalities",
                    title = "Accumulated fatalities for regions of interest",
                    color_continuous_scale=px.colors.sequential.PuRd,
                    range_color = (df["fatalities"].min(),df["fatalities"].max()))

st.plotly_chart(fig, use_container_width=True)


# -------------
# 
# -------------
df = pd.read_pickle(path+'/df_3.pkl')

fig = px.choropleth(df, locations="iso3",
                    color="fatalities",
                    title = "Accumulated fatalities world wide",
                    color_continuous_scale=px.colors.sequential.PuRd,
                    range_color = (df["fatalities"].min(),df["fatalities"].max()))

st.plotly_chart(fig, use_container_width=True)


# -------------
# 
# -------------

st.markdown("## Fatalities and media coverage")

df = pd.read_pickle(path+'/df_4.pkl')



df = df.sort_values(by=['country'])

fig = px.scatter(df, x="event_date_datetime", y="fatalities", color="country",# symbol="event_type",
                 size='fatalities',
                 hover_data=['country','event_type'], labels=dict(event_date_datetime="Event date", 
                fatalities="Fatalities", country="Country", event_type ="Event type"))

st.plotly_chart(fig, use_container_width=True)

# -------------
# 
# -------------
df = pd.read_pickle(path+'/df_5.pkl')

df = df.sort_values(by=['country'])

fig = px.scatter(df, x="date", y="AccNumArticles", color="country",
                 labels=dict(date="Date", AvgTone="Average Tone", country="Country", AccNumArticles ="Accumulated number of articles"))
st.plotly_chart(fig, use_container_width=True)


fig = px.scatter(df, x="date", y="AvgTone", color="country",
                 labels=dict(date="Date", AvgTone="Average Tone", country="Country", AccNumArticles ="Accumulated number of articles"))


st.plotly_chart(fig, use_container_width=True)