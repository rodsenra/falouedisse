# -*- coding: utf-8 -*-

import unittest
from quote_from_news import fetch_article, find_quotes


class TestArticle(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.url = "http://g1.globo.com/economia/noticia/2014/06/suprimento-de-energia-esta-garantido-ate-o-final-de-2015-diz-zimmerman.html"
        self.article = fetch_article(self.url)

    def test_fetch_article(self):
        self.assertEqual(self.article.title, u'Suprimento de energia est\xe1 garantido at\xe9 o final de 2015, diz Zimmerman')

    def test_parse_quotes(self):
        matches = find_quotes(self.article.text)
        self.assertEqual(3, len(matches))
        self.assertEqual(matches[0][1], u'afirmou')
        self.assertEqual(matches[1][1], u'refor\xe7ou')
        self.assertEqual(matches[2][1], u'completou')
