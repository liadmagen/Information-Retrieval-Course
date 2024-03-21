import sqlite3
from collections import defaultdict
from math import log
from pathlib import Path

from document_procesor import DocumentProcessor


class Indexer():

    def __init__(self, db_file: str = "index_sqlite.db") -> sqlite3.Cursor:
        self._index: dict[str, dict[str, int]] = \
            defaultdict(lambda: defaultdict(int))
        self._documents: dict[str, str] = {}

        with sqlite3.connect(db_file) as con:
            self.cur = con.cursor()
        return self.cur

    def index(self, doc: str, content: str) -> None:
        self._documents[doc] = content
        words = normalize_string(content).split(" ")
        for word in words:
            self._index[word][doc] += 1

    def bulk_index(self, documents: list[tuple[str, str]]):
        for doc, content in documents:
            self.index(doc, content)


    def get_docs(self, keyword: str) -> dict[str, int]:
        keyword = normalize_string(keyword)
        return self._index[keyword]


if __name__ == "__main__":
    docs = Path("../data/Sherlock_Holmes/").glob("*.txt")
    for doc in docs:
        DocumentProcessor(doc)