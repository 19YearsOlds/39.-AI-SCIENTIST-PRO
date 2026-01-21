from utils.text_tools import split_into_claims

class ReaderAgent:
    def read(self, text):
        return split_into_claims(text)