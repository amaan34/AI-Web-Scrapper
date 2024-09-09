# 1. Creating a Streamlit User Interface
# This UI makes it easier to interact with LLM's
# 2. Grab DATA from the website that we want to scrape (Using Selenium)
# Selenium allows to Automate a Web Browser so we can navigate to a webpage and grab its content and pass it through a LLM 
# We can then use that LLM to parse through the DATA 

import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content,
)
from parse import parse_with_ollama

st.title("AI Web Scraper by AM3AN")
url = st.text_input ("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the Website")
   
    result = scrape_website (url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# The Next Step would be to Parse the Content through a LLM
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the Content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)