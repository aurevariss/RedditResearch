import spacy
nlp = spacy.load('fr_core_news_md')
f = open("../manga/collected_manga_prep.txt", "r", encoding="utf-8")
doc = str(f.read())

doc = nlp(doc)
for token in doc:
    print(token, token.lemma_)
