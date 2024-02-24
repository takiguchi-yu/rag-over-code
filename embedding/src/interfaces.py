from abc import ABC, abstractmethod
from typing import List

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


class ICodeManager(ABC):
    @abstractmethod
    def update_code(self) -> None:
        raise NotImplementedError()


class IVectorStore(ABC):
    @abstractmethod
    def embedding_and_save(self, documents: List[Document], embedding: Embeddings) -> None:
        raise NotImplementedError()
