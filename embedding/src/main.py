from embedding.src.code_managers import Git
from config import DOCUMENT_LOADER_CONFIG, REPOSITORY_CONFIG, TEXT_SPLITTER_CONFIG, VECTOR_STORE_CONFIG
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_openai import OpenAIEmbeddings
from vector_store_factory import VectorStoreFactory

load_dotenv()


def main():
    git_manager = Git(
        repo_url=REPOSITORY_CONFIG["url"], repo_path=REPOSITORY_CONFIG["local_path"])
    git_manager.update_code()

    # ドキュメントを読み込む
    loader = GenericLoader.from_filesystem(
        path=DOCUMENT_LOADER_CONFIG["path"],
        glob=DOCUMENT_LOADER_CONFIG["glob_pattern"],
        suffixes=DOCUMENT_LOADER_CONFIG["suffixes"],
        exclude=DOCUMENT_LOADER_CONFIG["exclude_patterns"],
        parser=LanguageParser()
    )
    docs = loader.load()

    # テキスト分割 (Chunking)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=TEXT_SPLITTER_CONFIG["chunk_size"],
        chunk_overlap=TEXT_SPLITTER_CONFIG["chunk_overlap"]
    )
    texts = text_splitter.split_documents(docs)

    # テキストを保存 (Embedding)
    vector_store = VectorStoreFactory.get_vector_store(
        store_type=VECTOR_STORE_CONFIG["store_type"])
    vector_store.embedding_and_save(
        texts, embedding=OpenAIEmbeddings(model=VECTOR_STORE_CONFIG["embedding_model"]))


if __name__ == "__main__":
    main()
