import os
import re
import langchain_helper as lch
import streamlit as st

st.title("Retrievial")

with st.sidebar:
    with st.form(key="side_form"):
        selectbox1 = st.selectbox("Select exemple", ("1", "2", "3"), index=0)
        if selectbox1 == "1":
            st.write("Naive")
            texts = [
                """The Amanita phalloides has a large and imposing epigeous (aboveground) fruiting body (basidiocarp).""",
                """A mushroom with a large fruiting body is the Amanita phalloides. Some varieties are all-white.""",
                """A. phalloides, a.k.a Death Cap, is one of the most poisonous of all known mushrooms.""",
            ]
            for index, text in enumerate(texts):
                texts[index] = st.text_area(label=f"Text N°{index}:", value=text)

            question = st.text_area(
                label="Question:",
                value="Tell me about all-white mushrooms with large fruiting bodies",
            )
            selectbox2 = st.selectbox(
                "Select exemple",
                ("Similarity search", "Max marginal relevance search"),
                index=0,
            )
        if selectbox1 == "2":
            st.write("Filter")
            question = st.text_area(
                label="Question:",
                value="what did they say about regression in the third lecture?",
            )
            source_filter = st.text_area(
                label="Source Filter:",
                value="./docs/cs229_lectures/MachineLearning-Lecture03.pdf",
            )
        if selectbox1 == "3":
            st.write("Self Query Retriever")
            question = st.text_area(
                label="Question:",
                value="what did they say about regression in the third lecture?",
            )
        sumbit_button1 = st.form_submit_button(label="Submit", use_container_width=True)

docs_size = lch.get_vectordb_size()
st.text(f"Number of documents: {docs_size}")

if selectbox1 == "1":
    smalldb = lch.from_texts(texts)

    if selectbox2 == "Similarity search":
        st.subheader(selectbox2, divider="orange")

        docs_v1 = lch.similarity_search(smalldb, question, k=2)

        for doc in docs_v1:
            st.text(doc.metadata)
            st.text(doc.page_content)
            st.text("-------")

    elif selectbox2 == "Max marginal relevance search":
        st.subheader(selectbox2, divider="blue")

        docs_v1 = lch.max_marginal_relevance_search(smalldb, question, k=2)
        for doc in docs_v1:
            st.text(doc.metadata)
            st.text(doc.page_content)
            st.text("-------")

if selectbox1 == "2":
    docs_v2 = lch.similarity_search2(question, filter=source_filter)
    for doc in docs_v2:
        st.text(doc.metadata)
        st.text(doc.page_content)
        st.text("-------")

if selectbox1 == "3":
    docs_v3 = lch.get_relevant_documents(question)
    for doc in docs_v3:
        st.text(doc.metadata)
        st.text(doc.page_content)
        st.text("-------")
