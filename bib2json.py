from tinydb import TinyDB
from bibtexparser.bparser import BibTexParser
db = TinyDB('paper.json')

with open('paper.bib', 'r', encoding='utf-8') as bib_file:
    bib_content = bib_file.read()
    paper_table = db.table('papers')
    parser = BibTexParser()
    bib_database = parser.parse(bib_content)
    for entry in bib_database.entries:
        paper_table.insert(entry)

print('Paper1.bib has been imported into the database.')
