from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

import numpy as np

from dotenv import load_dotenv

load_dotenv()

# Load PDF
loaders = [
    # Duplicate documents on purpose - messy data
    PyPDFLoader("../docs/cs229_lectures/MachineLearning-Lecture01.pdf"),
    PyPDFLoader("../docs/cs229_lectures/MachineLearning-Lecture01.pdf"),
    PyPDFLoader("../docs/cs229_lectures/MachineLearning-Lecture02.pdf"),
    PyPDFLoader("../docs/cs229_lectures/MachineLearning-Lecture03.pdf"),
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
embedding = OpenAIEmbeddings()


def ex_r_splitter():
    splits = text_splitter.split_documents(docs)
    return splits
