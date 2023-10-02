import os
import langchain_helper as lch
import streamlit as st

st.title("Document Loading")

with st.sidebar:
    with st.form(key="side_form"):
        st.write("Load documents")
        uploaded_pdf = st.file_uploader(label="pdf")
        # Loading file
        if uploaded_pdf is not None:
            with open(
                os.path.join("DocumentLoading/uploaded", uploaded_pdf.name), "wb"
            ) as f:
                f.write(uploaded_pdf.getbuffer())
            pages = lch.pdf_loader(f"DocumentLoading/uploaded/{uploaded_pdf.name}")
            page_index = st.selectbox(
                "Display a page?", (x for x in range(len(pages))), index=0
            )

        web_url = st.text_area(
            label="Enter a web URL?",
            help="https://raw.githubusercontent.com/basecamp/handbook/master/37signals-is-you.md",
        )
        sumbit_button = st.form_submit_button(label="Submit", use_container_width=True)


if uploaded_pdf is not None and pages is not None:
    st.header("PyPDFLoader", divider="blue")
    st.subheader(uploaded_pdf.name)
    st.text(f"Number of page: {len(pages)}")
    page = pages[page_index]
    st.text(f"Metadata: {page.metadata}")
    st.text(f"First page[:500]:\n{page.page_content[0:500]}")

if web_url:
    docs = lch.web_Loader(web_url)
    st.header("WebBaseLoader", divider="blue")
    st.subheader(web_url)
    st.text(f"Number of page: {len(docs)}")
    st.text(f"Metadata: {docs[0].metadata}")
    st.text(f"Page content:\n{docs[0].page_content}")
