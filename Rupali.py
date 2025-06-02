import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Shoe Sales Dashboard", layout="wide")

# Title
st.title("Shoe Sales Dashboard")
st.subheader("Sales by Subsidiary in Selected Region")

# Load and clean data
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset/SHOES.csv")  # Adjust the path if needed
    df['Sales'] = df['Sales'].replace('[,$]', '', regex=True).astype('int64')
    df['Inventory'] = df['Inventory'].replace('[,$]', '', regex=True).astype('int64')
    df['Returns'] = df['Returns'].replace('[,$]', '', regex=True).astype('int64')
    return df

df = load_data()

# Region dropdown
regions = df['Region'].unique()
selected_region = st.selectbox("Select a Region", regions)

# Filter data for selected region
filtered_df = df[df['Region'] == selected_region]

# Plot Sales by Subsidiary
fig = px.bar(
    filtered_df,
    x='Subsidiary',
    y='Sales',
    title=f"Sales in {selected_region}",
    labels={'Sales': 'Sales ($)', 'Subsidiary': 'Subsidiary'},
    color='Subsidiary'
)
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)
