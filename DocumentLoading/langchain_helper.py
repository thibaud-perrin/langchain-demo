from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import WebBaseLoader

from dotenv import load_dotenv

load_dotenv()


def pdf_loader(pdf):
    loader = PyPDFLoader(pdf)
    pages = loader.load()

    return pages


def web_Loader(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs
