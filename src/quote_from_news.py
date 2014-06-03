# -*- coding: utf-8 -*-
import newspaper
import nltk
from nltk.tokenize import WordPunctTokenizer
import re

PUNCTUATION_TO_REMOVE = ['.', ',', '!', '?']

ATTRIBUTION_WORDS_STEMMED = [u'disse', u'afirmou', u'comentou', u'completou', u'concluiu', u'reforçou', u'admitiu',
                             u'negou', u'apontou']

PRONOUNS = ['ele', 'ela']


class Quotation(object):

    def __init__(self, phrase, verb):
        self.phrase = phrase
        self.verb = verb

    def contains(self, sentence):
        word_present = 0
        for word in sentence:
            if word in self.phrase:
                word_present += 1
        return (word_present > len(sentence) - 4)

    def __unicode__(self):
        return self.phrase


def find_quotes(text):
    pat = re.compile(r"\"(.*?)\",\s+(\w+)", re.UNICODE)
    normalized = text.replace(u'\u201c', '"')
    normalized = normalized.replace(u'\u201d', '"')
    matches = pat.findall(normalized)
    return [Quotation(phrase, verb) for phrase, verb in matches]


def annotate_quotes_with_line_numbers(quotes, sentences):
    numbered_sentences = list(enumerate(sentences))
    for quotation in quotes:
        positions = []
        for pos, sentence in numbered_sentences:
            if quotation.contains(sentence):
                positions.append(pos)
        quotation.positions = positions


def fetch_article(url, language='pt'):
    article = newspaper.Article(url, language=language)
    article.download()
    article.parse()
    return article


def ner_candidates(tree, symbol):
    candidate = []
    for production in tree.productions():
        if production.is_nonlexical():
            continue
        if production.lhs().symbol() == symbol:
            candidate.append(" ".join(i[0] for i in production.rhs()))
    return candidate


def heuristic_elect_candidate(candidates):
    names = {}
    for pos, candidate_list in candidates:
        for candidate in candidate_list:
            try:
                names[candidate] = names[candidate] + 1
            except KeyError:
                names[candidate] = 1

    for other_name, count in names.copy().items():
        for name in names:
            if name == other_name:
                continue
            if other_name in name:
                names[name] += count
    won = sorted(((v, k) for k, v in names.items()))[-1][1]
    return won


sentence_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
word_tokenizer = WordPunctTokenizer()


def text_to_sentences(raw_text):
    sentences = sentence_tokenizer.tokenize(raw_text)
    tokenized_sentences = [word_tokenizer.tokenize(sentence) for sentence in sentences]
    return tokenized_sentences

if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    article = fetch_article(url)
    sentences = text_to_sentences(article.text)
    tagged_sentences = [nltk.pos_tag(s) for s in sentences]
    ner_sentences = [nltk.ne_chunk(s) for s in tagged_sentences]
    candidates = [(pos, ner_candidates(s, 'PERSON')) for pos,s in enumerate(ner_sentences)]
    quotes = find_quotes(article.text)
    annotate_quotes_with_line_numbers(quotes, sentences)
    who = heuristic_elect_candidate(candidates)
    print("\n{0}\n".format(who))
    for quotation in quotes:
        print(quotation.phrase)
        print("\n")

# MIXED  = http://g1.globo.com/politica/noticia/2014/06/ministro-volta-negar-que-snowden-tenha-pedido-asilo-ao-brasil.html
# BUG = http://g1.globo.com/economia/noticia/2014/06/epe-diz-que-mais-de-mil-projetos-se-inscreveram-para-leilao-52014.html
# http://g1.globo.com/economia/noticia/2014/02/lobao-diz-que-nao-faltara-energia-no-pais-sob-nenhuma-circunstancia.html
# http://g1.globo.com/economia/noticia/2014/06/suprimento-de-energia-esta-garantido-ate-o-final-de-2015-diz-zimmerman.html
