from typing import List

from interfaces import IVectorStore
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


class ChromaVectorStore(IVectorStore):
    def embedding_and_save(self, documents: List[Document], embedding: Embeddings) -> None:
        Chroma.from_documents(documents, embedding,
                              persist_directory="./chroma_db")


class FaissVectorStore(IVectorStore):
    def embedding_and_save(self, documents: List[Document], embedding: Embeddings) -> None:
        print("faiss")
        # 実装は省略
        pass
