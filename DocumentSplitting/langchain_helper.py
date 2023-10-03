from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
    MarkdownHeaderTextSplitter,
)
from dotenv import load_dotenv

load_dotenv()


def ex_r_splitter(chunk_size=26, chunk_overlap=4):
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )


def ex_c_splitter(chunk_size=26, chunk_overlap=4, separator=""):
    return CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=separator
    )


def ex_t_splitter(chunk_size=1, chunk_overlap=0):
    return TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)


def ex_m_splitter():
    return MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
    )
