import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Shoe Sales Dashboard", layout="wide")

# Title
st.title("Shoe Sales Dashboard")
st.subheader("Sales by Subsidiary for Selected Region")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset/SHOES.csv")  # Adjust the path as needed
    df.Sales = df.Sales.replace('[,$]', '', regex=True).astype('int64')
    df.Inventory = df.Inventory.replace('[,$]', '', regex=True).astype('int64')
    df.Returns = df.Returns.replace('[,$]', '', regex=True).astype('int64')
    return df

df = load_data()

# Region selection
regions = d
