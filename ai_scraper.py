import streamlit as st

from content import (
    url_content,
    clean_content,
    split_dom_content
)
from parse import parse_with_ollama


st.title("AI Web Scraper")
url = st.text_input("Enter the url you want to scrape.")

if "dom_content" not in st.session_state:
    st.session_state.dom_content = ""
log_message = st.empty()

if st.button('Scrape site'):
    log_message.write("Scraping your site...")

    body_content = url_content(url)
    if body_content:
        cleaned_content = clean_content(body_content)
        st.session_state.dom_content = cleaned_content
        log_message.write("Scraping successfull")

    else:
        st.write("No content found , please try another URL")

    
if st.session_state.dom_content:
    with st.expander("View DOM Content"):
        st.text_area('dom_content' , st.session_state.dom_content ,height=300)


if st.session_state.dom_content:
    parse_description = st.text_area("Specify what to scrape from the URL")
    parse_logs = st.empty()
    if st.button('Parse Content'):
        if parse_description:
            parse_logs.write("Working on your content...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            # print("dom chunks done")
            result = parse_with_ollama(dom_chunks , parse_description)
            if result:
               parse_logs.write("Completed!") 
            st.write(result)
        else:
            st.write("Please provide a description to parse the content.")




