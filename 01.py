import streamlit as st
import requests

# Bitly API endpoint
BITLY_API_ENDPOINT = "https://api-ssl.bitly.com/v4/shorten"

# Function to shorten URL using Bitly API
def shorten_url(long_url, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    payload = {"long_url": long_url}
    
    try:
        response = requests.post(BITLY_API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["link"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error shortening URL: {str(e)}")
        return None

# Function to expand shortened URL using Bitly API
def expand_url(short_url, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    
    try:
        response = requests.get(f"https://api-ssl.bitly.com/v4/expand?bitlink={short_url}", headers=headers)
        response.raise_for_status()
        return response.json()["long_url"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error expanding URL: {str(e)}")
        return None

st.title("URL Shortener (using Bitly)")

# Input for Bitly access token
access_token = st.text_input("Enter your Bitly access token:", type="password")

if not access_token:
    st.warning("Please enter your Bitly access token to use the URL shortener.")
    st.stop()

# Input for the long URL
long_url = st.text_input("Enter the URL to shorten:")

if st.button("Shorten URL"):
    if long_url:
        short_url = shorten_url(long_url, access_token)
        if short_url:
            st.success(f"Shortened URL: {short_url}")
    else:
        st.error("Please enter a URL to shorten.")

# Input for the shortened URL
st.subheader("Retrieve Original URL")
short_url_input = st.text_input("Enter the shortened URL:")

if st.button("Get Original URL"):
    if short_url_input:
        original_url = expand_url(short_url_input, access_token)
        if original_url:
            st.success(f"Original URL: {original_url}")
    else:
        st.error("Please enter a shortened URL.")
