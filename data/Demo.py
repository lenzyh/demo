import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
from PIL import Image

# Read the user information from the JSON file
# with open(r'C:\Users\YeHernYeow\Desktop\Demo\username.json', 'r') as json_file:
#     user_info = json.load(json_file)

df = pd.read_excel(r'C:\Users\YeHernYeow\Desktop\Demo\Global_Superstore2.xlsx')
image = Image.open(r'C:\Users\YeHernYeow\Desktop\Demo\RDA_Logo.png')
st.title('Testing :fire:')

st.image(image, caption='RDA')

# # Group multiple widgets in the sidebar:
# with st.sidebar.form(key='my_form'):
#     username = st.text_input('Username')
#     password = st.text_input('Password', type='password')  # Use password input type for security
#     login_button = st.form_submit_button('Login')

# # Check if the login is successful
# if login_button:
#     authenticated = False
#     for user in user_info:
#         if username == user['username'] and password == user['pass']:
#             authenticated = True
#             break

#     if authenticated:
#         st.success('Login successful!')

# Create a selectbox to choose the metric
selected_products = st.multiselect("Select Product(s)", df['Product Name'])
selected_metric = st.selectbox("Select Metric", ["Sales", "Quantity", "Profit"])

# Filter the dataframe based on the selected products and metric
filtered_df = df[df['Product Name'].isin(selected_products)][['Product Name', selected_metric]]

# Plot the line chart
st.bar_chart(filtered_df.set_index('Product Name'))

# Optional: You can also display the data table for the selected metric
st.write(":1234: Data Table:")
st.table(filtered_df)
    # else:
    #     st.error('Login failed. Please check your username and password.')