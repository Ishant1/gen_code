# from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language
from langchain_text_splitters import RecursiveCharacterTextSplitter
from git import Repo



class DataExtractor:
    def __init__(self,githublink: str, data_path: str, languages: str=Language.PYTHON):
        self.githublink = githublink
        self.data_path = data_path
        self.languages=languages

        self.documents = None

    def get_git_code(self):
        Repo.clone_from(self.githublink, to_path=self.data_path)

    def load_github_data_from_local(self, suffixes=[".py"], parser_threshold=500):
        # Load
        loader = GenericLoader.from_filesystem(
            self.data_path,
            glob="**/*",
            suffixes=suffixes,
            exclude=["**/non-utf8-encoding.py"],
            parser=LanguageParser(language=self.languages, parser_threshold=parser_threshold),
        )

        self.documents = loader.load() 

    def split_documents(self, documents, chunk_size=2000, chunk_overlap=200):
        code_splitter = RecursiveCharacterTextSplitter.from_language(
            language=self.languages, chunk_size=chunk_size, chunk_overlap=chunk_overlap
            )
        split_documents = code_splitter.split_documents(documents)
        return split_documents

    def get_all_text(self):
        page_based_text = [doc_.page_content for doc_ in self.documents]
        file_names = [doc_.metadata.get("source") for doc_ in self.documents]

        combined_text = ""
        for page_text_, filename_ in zip(page_based_text, file_names):
            file_text = f"{filename_}\n {page_text_}"
            combined_text = f"{combined_text}\n\n{file_text}"

        return combined_text
