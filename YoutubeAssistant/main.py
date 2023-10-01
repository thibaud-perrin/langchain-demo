import streamlit as st
import langchain_helper as lch
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key="side_form"):
        st.write("Ask me something about the video.")
        youtube_url = st.text_area(
            label="What is the YouTube video URL?",
            max_chars=50,
            placeholder="https://www.youtube.com/watch?v=-Osca2Zax4Y",
            value="https://www.youtube.com/watch?v=-Osca2Zax4Y",
        )
        query = st.text_area(
            label="Your question:",
            max_chars=50,
            key="query",
            placeholder="What did the talk about Ransomware?",
            help="What did the talk about Ransomware?",
        )

        sumbit_button = st.form_submit_button(label="Submit", use_container_width=True)

if query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(video_url=youtube_url)
    response, docs = lch.get_response_from_query(db=db, query=query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=80))
    for index, doc in enumerate(docs):
        st.subheader(f"Document: {str(index + 1)}")
        st.text(textwrap.fill(doc.page_content, width=80))
