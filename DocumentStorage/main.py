import os
import re
import langchain_helper as lch
import streamlit as st

st.title("Storage")

with st.sidebar:
    with st.form(key="side_form"):
        st.write("Exemples")
        selectbox1 = st.selectbox("Select exemple", ("1", "2"), index=0)

        if selectbox1 == "2":
            question = st.text_area(
                label="Question",
                value="Is there an email I can ask for help ?",
                help="what did they say about regression in the third lecture?",
            )
            k = st.number_input("Number of documents", value=3)
        sumbit_button1 = st.form_submit_button(label="Submit", use_container_width=True)


if selectbox1 == "1":
    sentence1 = "i like dogs"
    sentence2 = "i like canines"
    sentence3 = "the weather is ugly outside"
    embed1x2 = lch.get_embedding_dot(sentence1, sentence2)
    embed1x3 = lch.get_embedding_dot(sentence1, sentence3)
    embed2x3 = lch.get_embedding_dot(sentence2, sentence3)
    st.markdown(
        f"""
        **Sentences:**
        1. [{sentence1}]
        2. [{sentence2}]
        3. [{sentence3}]

        **Similarity:**
        - 1 x 2 : {embed1x2}
        - 1 x 3 : {embed1x3}
        - 2 x 3 : {embed2x3}
    """
    )

if selectbox1 == "2" and question:
    collection_size = lch.get_vectordb_size()

    docs = lch.similarity_search(question, k)

    st.markdown(
        f"""
        ## Files:
        - MachineLearning-Lecture01.pdf
        - MachineLearning-Lecture01.pdf
        - MachineLearning-Lecture02.pdf
        - MachineLearning-Lecture03.pdf

        ## Collection size:
        {collection_size}

        ## Question:
        - {question}
        
        ## Docs:
    """
    )
    for doc in docs:
        st.text(doc.metadata)
        st.text(doc.page_content)
