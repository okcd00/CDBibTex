import bibtexparser
 
with open('bibtex/cd_refs_publication.bib', 'r', encoding='utf-8') as file:
    bib_database = bibtexparser.load(file)
 
# 输出解析后的BibTeX条目
for entry in bib_database.entries:
    print(entry)