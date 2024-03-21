from pathlib import Path
from typing import Union

class DocumentProcessor():

    def __init__(self, document_path: Union[str | Path]):
        self.doc_txt = Path(document_path).read_text()

    def process_text(self, doc_text: str):
        doc_lines = self.doc_txt.split("\n")
        doc_lines = [line.strip() for line in doc_lines]
        self.doc_txt = " ".join(doc_lines)

        self.tokens = self.doc_txt.split()
        self.vocab = set(self.tokens)
