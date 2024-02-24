from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationSummaryMemory
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

db = Chroma(persist_directory="../embedding/chroma_db",
            embedding_function=OpenAIEmbeddings(model="text-embedding-3-large"))
retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 8})

llm = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(
    llm=llm, retriever=retriever, memory=memory)

question = "aws-cdk のスタック名を教えて"
result = qa(question)
print(result["answer"])
