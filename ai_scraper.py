import streamlit as st

from AI_SCRAPER.content import (
    url_content,
    clean_content,
    split_dom_content
)
from AI_SCRAPER.parse import parse_with_ollama


st.title("AI Web Scraper")
url = st.text_input("Enter the url you want to scrape.")

if "dom_content" not in st.session_state:
    st.session_state.dom_content = ""

if st.button('Scrape site'):
    st.write("Scraping your site...")

    body_content = url_content(url)
    if body_content:
        cleaned_content = clean_content(body_content)
        st.session_state.dom_content = cleaned_content

    else:
        st.write("No content found , please try another URL")

    
if st.session_state.dom_content:
    with st.expander("View DOM Content"):
        st.text_area('dom_content' , st.session_state.dom_content ,height=300)


if st.session_state.dom_content:
    parse_description = st.text_area("Specify what to scrape from the URL")

    if st.button('Parse Content'):
        if parse_description:
            st.write("Parsing the content...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks , parse_description)
            st.write(result)
        else:
            st.write("Please provide a description to parse the content.")




