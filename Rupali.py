import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Title of the app
st.title("Shoe Sales Dashboard")
st.subheader("Sales by Subsidiary in Selected Region")

# Load data
df = pd.read_csv("Dataset/SHOES.csv")  # Update path as needed

# Clean columns
df.Sales = df.Sales.replace('[,$]', '', regex=True).astype('int64')
df.Inventory = df.Inventory.replace('[,$]', '', regex=True).astype('int64')
df.Returns = df.Returns.replace('[,$]', '', regex=True).astype('int64')

# Dropdown for region selection
regions = df.Region.unique()
selected_region = st.selectbox("Select a Region", regions)

# Filter data
reg = df[df.Region == selected_region]

# Plot
fig, ax = plt.subplots()
sb.barplot(x='Subsidiary', y='Sales', data=reg, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
