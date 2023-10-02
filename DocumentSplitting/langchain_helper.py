from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
    MarkdownHeaderTextSplitter,
)
from dotenv import load_dotenv

load_dotenv()


def splitters(chunk_size=26, chunk_overlap=4):
    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    c_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    token_splitter = TokenTextSplitter(chunk_size=1, chunk_overlap=0)

    return r_splitter, c_splitter, token_splitter
