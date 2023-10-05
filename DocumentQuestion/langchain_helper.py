from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

persist_directory = "./docs/chroma/"
llm_name = "gpt-3.5-turbo"

embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
llm = ChatOpenAI(model_name=llm_name, temperature=0)


def get_vectordb_size():
    return vectordb._collection.count()


qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever())


def ask_qa_chain(question):
    return qa_chain({"query": question})


def build_prompt():
    # Build prompt
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
    {context}
    Question: {question}
    Helpful Answer:"""
    return PromptTemplate.from_template(template)


def ask_prompt(question):
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": build_prompt()},
    )
    return qa_chain({"query": question})


def map_reduce(question):
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type="map_reduce",
    )
    return qa_chain({"query": question})
