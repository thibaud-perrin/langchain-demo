from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import numpy as np

from dotenv import load_dotenv

load_dotenv()

# Load PDF
loaders = [
    # Duplicate documents on purpose - messy data
    PyPDFLoader("./docs/cs229_lectures/MachineLearning-Lecture01.pdf"),
    PyPDFLoader("./docs/cs229_lectures/MachineLearning-Lecture01.pdf"),
    PyPDFLoader("./docs/cs229_lectures/MachineLearning-Lecture02.pdf"),
    PyPDFLoader("./docs/cs229_lectures/MachineLearning-Lecture03.pdf"),
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
embedding = OpenAIEmbeddings()

persist_directory = "./docs/chroma/"


def ex_r_splitter():
    splits = text_splitter.split_documents(docs)
    return splits


def get_embedding_dot(sentence1, sentence2):
    embd1 = embedding.embed_query(sentence1)
    embed2 = embedding.embed_query(sentence2)
    return np.dot(embd1, embed2)


vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)


def get_vectordb_size():
    return vectordb._collection.count()


def similarity_search(question, k=3):
    docs = vectordb.similarity_search(question, k=k)
    return docs


if get_vectordb_size() == 0:
    vectordb = Chroma.from_documents(
        documents=ex_r_splitter(),
        embedding=embedding,
        persist_directory=persist_directory,
    )

    vectordb.persist()
