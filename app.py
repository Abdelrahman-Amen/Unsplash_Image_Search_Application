import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
unsplash_api_key = os.getenv('UNSPLASH_ACCESS_KEY')   # Add your API


# Function to search for images on Unsplash based on a prompt
def search_images(prompt, num_images=20):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": prompt,
        "per_page": num_images,
        "client_id": unsplash_api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    image_urls = [result['urls']['regular'] for result in data['results']]
    return image_urls






# Streamlit setup
st.set_page_config(page_title='Image Search with Unsplash')
st.header('Unsplash Image Search Application')

# Input section for text prompt
prompt_input = st.text_input('Enter a prompt to search for images:', key='prompt_input')
submit = st.button('Search Images')

# Search and display images when the button is clicked
if submit and prompt_input:
    st.subheader('Found Images:')
    image_urls = search_images(prompt_input)
    
    # Display all images directly
    cols = st.columns(5)  # Create a 5-column layout for images
    for idx, img_url in enumerate(image_urls):
        with cols[idx % 5]:  # Distribute images across the columns
            st.image(img_url, caption=f"Image {idx + 1}", use_column_width=True)
