import os
import re
import langchain_helper as lch
import streamlit as st

st.title("Question Answering")

with st.sidebar:
    with st.form(key="side_form"):
        selectbox1 = st.selectbox("Select exemple", ("1", "2", "3"), index=0)
        if selectbox1 == "1":
            st.write("Question Answering")
            question = st.text_area(
                label="Question:",
                value="What are major topics for this class?",
            )
        if selectbox1 == "2":
            st.write("Prompt")
            question = st.text_area(
                label="Question:",
                value="Is probability a class topic?",
            )
        if selectbox1 == "3":
            st.write("Map Reduce")
            question = st.text_area(
                label="Question:",
                value="Is probability a class topic?",
            )
        sumbit_button1 = st.form_submit_button(label="Submit", use_container_width=True)

docs_size = lch.get_vectordb_size()
st.text(f"Number of documents: {docs_size}")

if selectbox1 == "1" and question:
    result = lch.ask_qa_chain(question)

    st.markdown(result["result"])

if selectbox1 == "2" and question:
    result = lch.ask_prompt(question)
    st.text(
        """Instruction: Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer."""
    )
    for source in result["source_documents"]:
        st.text(source)

    st.markdown(result["result"])

if selectbox1 == "3" and question:
    result = lch.map_reduce(question)
    for source in result["source_documents"]:
        st.text(source)

    st.markdown(result["result"])
