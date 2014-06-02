# -*- coding: utf-8 -*-
import newspaper
import nltk
from nltk.tokenize import WordPunctTokenizer
import re

PUNCTUATION_TO_REMOVE = ['.', ',', '!', '?']

ATTRIBUTION_WORDS_STEMMED = [u'disse', u'afirmou', u'comentou', u'completou', u'concluiu', u'reforçou', u'admitiu',
                             u'negou', u'apontou']

PRONOUNS = ['ele', 'ela']


def find_quotes(text):
    pat = re.compile(r"\"(.*?)\",\s+(\w+)", re.UNICODE)
    matches = pat.findall(text)
    return matches


def fetch_article(url, language='pt'):
    article = newspaper.Article(url, language=language)
    article.download()
    article.parse()
    return article


sentence_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
word_tokenizer = WordPunctTokenizer()


def text_to_sentences(raw_text):
    sentences = sentence_tokenizer.tokenize(raw_text)
    tokenized_sentences = (word_tokenizer.tokenize(sentence) for sentence in sentences)
    return tokenized_sentences

if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    article = fetch_article(url)
    sentences = text_to_sentences(article.text)

# http://g1.globo.com/politica/noticia/2014/06/ministro-volta-negar-que-snowden-tenha-pedido-asilo-ao-brasil.html
# http://g1.globo.com/economia/noticia/2014/06/epe-diz-que-mais-de-mil-projetos-se-inscreveram-para-leilao-52014.html
# http://g1.globo.com/economia/noticia/2014/02/lobao-diz-que-nao-faltara-energia-no-pais-sob-nenhuma-circunstancia.html
# http://g1.globo.com/economia/noticia/2014/06/suprimento-de-energia-esta-garantido-ate-o-final-de-2015-diz-zimmerman.html
