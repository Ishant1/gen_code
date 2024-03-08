# from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language
from langchain_text_splitters import RecursiveCharacterTextSplitter
from git import Repo


def get_git_code(github_link, repo_name):
    repo_path = f"Rag/Dataset/{repo_name}"
    Repo.clone_from(github_link, to_path=repo_path)
    return repo_path


def load_github_data_from_local(data_path, suffixes=[".py"], language=Language.PYTHON, parser_threshold=500):
    # Load
    loader = GenericLoader.from_filesystem(
        data_path,
        glob="**/*",
        suffixes=suffixes,
        exclude=["**/non-utf8-encoding.py"],
        parser=LanguageParser(language=language, parser_threshold=parser_threshold),
    )
    return loader.load()


def split_documents(documents, language=Language.PYTHON, chunk_size=2000, chunk_overlap=200):
    code_splitter = RecursiveCharacterTextSplitter.from_language(
        language=language, chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
    split_documents = code_splitter.split_documents(documents)
    return split_documents



