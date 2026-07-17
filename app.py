import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    layout="wide"
)

df = pd.read_csv("netflix_titles.csv")

# Cleaning

df['date_added'] = pd.to_datetime(
    df['date_added'],
    errors='coerce'
)

df['year_added'] = df['date_added'].dt.year

df['duration_num'] = (
    df['duration']
    .astype(str)
    .str.extract(r'(\d+)')[0]
)

df['duration_num'] = pd.to_numeric(
    df['duration_num'],
    errors='coerce'
)

# Sidebar

st.sidebar.header("Filters")

type_filter = st.sidebar.multiselect(
    "Select Type",
    options=df['type'].dropna().unique(),
    default=df['type'].dropna().unique()
)

rating_filter = st.sidebar.multiselect(
    "Select Rating",
    options=df['rating'].dropna().unique(),
    default=df['rating'].dropna().unique()
)

filtered_df = df[
    (df['type'].isin(type_filter))
    &
    (df['rating'].isin(rating_filter))
]

# Title

st.title("Netflix Analytics Dashboard")

# KPIs

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Total Titles",
    filtered_df.shape[0]
)

c2.metric(
    "Movies",
    filtered_df[
        filtered_df['type']=="Movie"
    ].shape[0]
)

c3.metric(
    "TV Shows",
    filtered_df[
        filtered_df['type']=="TV Show"
    ].shape[0]
)

c4.metric(
    "Countries",
    filtered_df['country'].nunique()
)

# Movies vs TV Shows

fig = px.bar(
    filtered_df['type']
    .value_counts()
    .reset_index(),
    x='type',
    y='count',
    title='Movies vs TV Shows'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Release Trend

release = (
    filtered_df
    .groupby('release_year')
    .size()
    .reset_index(name='Count')
)

fig = px.line(
    release,
    x='release_year',
    y='Count',
    title='Release Trend'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Rating Distribution

fig = px.pie(
    names=filtered_df['rating']
    .value_counts()
    .index,
    values=filtered_df['rating']
    .value_counts()
    .values,
    title='Rating Distribution'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Top Countries

country = (
    filtered_df['country']
    .fillna("Unknown")
    .value_counts()
    .head(10)
)

fig = px.bar(
    x=country.index,
    y=country.values,
    title='Top Countries'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Top Genres

genres = (
    filtered_df['listed_in']
    .str.split(',')
    .explode()
    .value_counts()
    .head(10)
)

fig = px.bar(
    x=genres.values,
    y=genres.index,
    orientation='h',
    title='Top Genres'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success("Dashboard Loaded Successfully")