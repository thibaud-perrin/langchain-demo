import os
import langchain_helper as lch
import streamlit as st

st.title("Splitting")

with st.sidebar:
    with st.form(key="side_form"):
        st.write("RecursiveCharacterTextSplitter")
        chunk_size1 = st.number_input(label="chunk_size", value=26)
        chunk_overlap1 = st.number_input(label="chunk_overlap", value=4)
        selectbox1 = st.selectbox("Exemples", ("1", "2"), index=0)
        if selectbox1 == "1":
            text1 = st.text_area(label="text", value="abcdefghijklmnopqrstuvwxyz")
        elif selectbox1 == "2":
            text1 = st.text_area(
                label="text",
                value="""When writing documents, writers will use document structure to group content. \
This can convey to the reader, which idea's are related. For example, closely related ideas \
are in sentances. Similar ideas are in paragraphs. Paragraphs form a document. \n\n  \
Paragraphs are often delimited with a carriage return or two carriage returns. \
Carriage returns are the "backslash n" you see embedded in this string. \
Sentences have a period at the end, but also, have a space.\
and words are separated by space.""",
            )

        sumbit_button1 = st.form_submit_button(label="Submit", use_container_width=True)

    with st.form(key="side_form2"):
        st.write("CharacterTextSplitter")
        chunk_size2 = st.number_input(label="chunk_size", value=26)
        chunk_overlap2 = st.number_input(label="chunk_overlap", value=4)
        separator2 = st.text_area(label="separator", value="")
        text2 = st.text_area(label="text", value="abcdefghijklmnopqrstuvwxyz")

        sumbit_button2 = st.form_submit_button(label="Submit", use_container_width=True)

    with st.form(key="side_form3"):
        st.write("TokenTextSplitter")
        chunk_size3 = st.number_input(label="chunk_size", value=1)
        chunk_overlap3 = st.number_input(label="chunk_overlap", value=0)
        text3 = st.text_area(
            label="text",
            value="When writing documents, writers will use document structure to group content. initialisation",
        )

        sumbit_button3 = st.form_submit_button(label="Submit", use_container_width=True)

    with st.form(key="side_form4"):
        st.write("MarkdownHeaderTextSplitter")
        text4 = st.text_area(
            label="text",
            value="""# Title\n\n \
## Chapter 1\n\n \
Hi this is Jim\n\n Hi this is Joe\n\n \
### Section \n\n \
Hi this is Lance \n\n 
## Chapter 2\n\n \
Hi this is Molly""",
        )

        sumbit_button4 = st.form_submit_button(label="Submit", use_container_width=True)


if sumbit_button1 and text1:
    r_splitter = lch.ex_r_splitter(chunk_size1, chunk_overlap1)
    st.header("RecursiveCharacterTextSplitter", divider="blue")
    list_text = "\n - ".join(r_splitter.split_text(text1))
    st.markdown(f"- {list_text}")

if sumbit_button2 and text2:
    c_splitter = lch.ex_c_splitter(chunk_size2, chunk_overlap2, separator2)
    st.header("CharacterTextSplitter", divider="blue")
    list_text = "\n - ".join(c_splitter.split_text(text2))
    st.markdown(f"- {list_text}")

if sumbit_button3 and text3:
    t_splitter = lch.ex_t_splitter(chunk_size3, chunk_overlap3)
    st.header("TokenTextSplitter", divider="blue")
    list_text = "\n - ".join(t_splitter.split_text(text3))
    st.markdown(f"- {list_text}")

if sumbit_button4 and text4:
    m_splitter = lch.ex_m_splitter()
    st.header("MarkdownHeaderTextSplitter", divider="blue")
    for i, x in enumerate(m_splitter.split_text(text4)):
        st.subheader(f"Document: {i}")
        st.markdown(x.metadata)
        st.markdown(x.page_content)
