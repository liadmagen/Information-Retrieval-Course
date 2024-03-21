# %%
import sqlite3
from pathlib import Path

class DocumentProcessor():

    def __init__(self, document_path: str):
        self.doc_txt = Path(document_path).read_text()

    def process_text(self):
        doc_lines = self.doc_txt.split("\n")
        doc_lines = [line.strip() for line in doc_lines]
        self.doc_txt = " ".join(doc_lines)

        self.tokens = self.doc_txt.split()
        self.vocab = set(self.tokens)


class Indexer():

    def __init__(self, db_file: str = "index_sqlite.db") -> sqlite3.Cursor:
        with sqlite3.connect(db_file) as con:
            self.cur = con.cursor()
        return self.cur

    def setup(self):
        pass
# %%
