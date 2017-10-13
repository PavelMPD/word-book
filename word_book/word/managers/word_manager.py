from word.managers import txt_parser


class WordManager(object):
    def import_from_txt_file(self, filename):
        parser = txt_parser.TxtParser(filename)
        for row in parser.parse():
            print(row)
