import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit App Title
st.set_page_config(page_title="Shoe Sales Dashboard", layout="wide")
st.title("Shoe Sales Dashboard")
st.markdown("Visualize sales data by region and subsidiary")

# Load and clean the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset/SHOES.csv")  # Make sure this path is correct
    df['Sales'] = df['Sales'].replace('[,$]', '', regex=True).astype(int)
    df['Inventory'] = df['Inventory'].replace('[,$]', '', regex=True).astype(int)
    df['Returns'] = df['Returns'].replace('[,$]', '', regex=True).astype(int)
    return df

df = load_data()

# Show available regions
regions = df['Region'].unique()
selected_region = st.selectbox("Select a Region", regions)

# Filter by region
filtered_df = df[df['Region'] == selected_region]

# Show bar chart of Sales by Subsidiary
fig = px.bar(
    filtered_df,
    x="Subsidiary",
    y="Sales",
    title=f"Sales by Subsidiary in {selected_region}",
    labels={"Sales": "Sales ($)", "Subsidiary": "Subsidiary"},
    color="Subsidiary"
)
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)
