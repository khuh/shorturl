import streamlit as st
import hashlib
import base64

# In-memory storage for URL mappings
url_mapping = {}

def shorten_url(url):
    # Create a hash of the URL
    hash_object = hashlib.md5(url.encode())
    hash_digest = hash_object.digest()
    
    # Convert the hash to a base64 string and take the first 8 characters
    short_url = base64.urlsafe_b64encode(hash_digest).decode()[:8]
    
    # Store the mapping
    url_mapping[short_url] = url
    
    return short_url

def get_original_url(short_url):
    return url_mapping.get(short_url)

st.title("URL Shortener")

# Input for the long URL
long_url = st.text_input("Enter the URL to shorten:")

if st.button("Shorten URL"):
    if long_url:
        short_url = shorten_url(long_url)
        st.success(f"Shortened URL: http://short.url/{short_url}")
    else:
        st.error("Please enter a URL to shorten.")

# Input for the shortened URL
st.subheader("Retrieve Original URL")
short_url_input = st.text_input("Enter the shortened URL:")

if st.button("Get Original URL"):
    if short_url_input:
        # Extract the last part of the URL (the short code)
        short_code = short_url_input.split("/")[-1]
        original_url = get_original_url(short_code)
        if original_url:
            st.success(f"Original URL: {original_url}")
        else:
            st.error("Shortened URL not found.")
    else:
        st.error("Please enter a shortened URL.")