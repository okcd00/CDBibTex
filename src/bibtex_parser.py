import bibtexparser


class BibTexParser(object):
    LOWER_CASE = "a, an, the, and, but, or, for, nor, on, at, to, by, in, of, up, as, so, yet, off, if, per, via, out"

    def __init__(self):
        self.database = None
        self.lower_case_map = {v.strip().title(): v.strip() for v in self.LOWER_CASE.split(',')}

    def load_bibtex(self, fp):
        with open(fp, 'r', encoding='utf-8') as file:
            self.database = bibtexparser.load(file)
    
    def dump_bibtex(self, fp):
        with open(fp, 'w', encoding='utf-8') as bibtex_file:
            bibtexparser.dump(self.database, bibtex_file)

    def _normalized_title(self, title):
        words = title.strip().lstrip('{').rstrip('}').strip().title().split()
        return '{ ' + ' '.join([self.lower_case_map.get(t, t) for t in words]) + ' }'

    def normalized_title(self):
        # APA Style: 
        # https://blog.apastyle.org/apastyle/capitalization/
        # https://blog.apastyle.org/apastyle/2012/03/how-to-capitalize-and-format-reference-titles-in-apa-style.html
        for item in self.database.entries:
            item['title'] = self._normalized_title(item['title'])


if __name__ == "__main__":
    btp = BibTexParser()
    btp.load_bibtex('bibtex/cd_refs_publication.bib')
    btp.normalized_title()
    btp.dump_bibtex('release/test.bib')
