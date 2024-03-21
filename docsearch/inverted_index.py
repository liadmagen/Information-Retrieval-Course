import sqlite3
from pathlib import Path
from collections import defaultdict
from document_procesor import DocumentProcessor


class Indexer():

    def __init__(self, db_file: str = "index_sqlite.db") -> sqlite3.Cursor:
        self._index: dict[str, dict[str, int]] = \
            defaultdict(lambda: defaultdict(int))
        self._documents: dict[str, str] = {}

        with sqlite3.connect(db_file) as con:
            self.cur = con.cursor()
        return self.cur

    def setup(self):
        pass

if __name__ == "__main__":
    docs = Path("../data/Sherlock_Holmes/").glob("*.txt")
    for doc in docs:
        DocumentProcessor(doc)