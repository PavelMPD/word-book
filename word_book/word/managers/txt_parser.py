from word import models


class TxtParser(object):
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        with open(self.filename, mode='rt', encoding='UTF-8') as stream:
            for row in stream:
                yield row

    def detect_object(self, row):
        text = row.strip()
        if text:
            return models.Word(name=text)
        return None
