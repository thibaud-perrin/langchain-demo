from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo

import numpy as np

from dotenv import load_dotenv

load_dotenv()

persist_directory = "./docs/chroma/"

embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)


def get_vectordb_size():
    return vectordb._collection.count()


def from_texts(texts):
    chroma = Chroma(collection_name="texts")
    if chroma._collection.count() > 0:
        chroma.delete_collection()
    return chroma.from_texts(texts, embedding=embedding, collection_name="texts")


def similarity_search(smalldb, question, k=2):
    return smalldb.similarity_search(question, k=k)


def max_marginal_relevance_search(smalldb, question, k=2, fetch_k=3):
    return smalldb.max_marginal_relevance_search(question, k=k, fetch_k=fetch_k)


# ~---------
def similarity_search2(question, filter):
    print(question, filter)
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    return vectordb.similarity_search(question, k=3, filter={"source": filter})


def get_relevant_documents(question):
    metadata_field_info = [
        AttributeInfo(
            name="source",
            description="The lecture the chunk is from, should be one of `./docs/cs229_lectures/MachineLearning-Lecture[xx].pdf` where [xx] is the lecture number",
            type="string",
        ),
        AttributeInfo(
            name="page",
            description="The page from the lecture",
            type="integer",
        ),
    ]
    document_content_description = "Lecture notes"
    llm = OpenAI(temperature=0)
    retriever = SelfQueryRetriever.from_llm(
        llm, vectordb, document_content_description, metadata_field_info, verbose=True
    )
    return retriever.get_relevant_documents(question)


# if __name__ == "__main__":
#     texts = [
#         """The Amanita phalloides has a large and imposing epigeous (aboveground) fruiting body (basidiocarp).""",
#         """A mushroom with a large fruiting body is the Amanita phalloides. Some varieties are all-white.""",
#         """A. phalloides, a.k.a Death Cap, is one of the most poisonous of all known mushrooms.""",
#     ]
#     question = "Tell me about all-white mushrooms with large fruiting bodies"
#     smalldb = from_texts(texts)
#     print(smalldb)
#     print(similarity_search(smalldb, question, k=2))
#     print("---")
#     print(max_marginal_relevance_search(smalldb, question, k=2, fetch_k=3))
