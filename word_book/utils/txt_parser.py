# -*- coding: utf-8 -*-
import re


class TxtParser(object):
    WORD = 'word'
    EXPLANATION = 'explanation'
    EXAMPLE = 'example'
    UNKNOWN = 'unknown'

    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        with open(file=self.filename, mode='rt', encoding='utf-8-sig') as stream:
            for row in stream:
                if not row.strip():
                    continue
                type_, text = self.get_object(row)
                yield type_, text

    def get_object(self, row):
        text = row.strip()
        type_ = self.get_type(row)
        return type_, text

    def get_type(self, row):
        if not re.match('\t', row):
            return self.WORD
        elif re.match('\t+:', row):
            return self.EXPLANATION
        elif re.match('\t+', row):
            return self.EXAMPLE
        return self.UNKNOWN


if __name__ == '__main__':
    parser = TxtParser('./data/word list 20171013.txt')
    for o in parser.parse():
        print(o)
