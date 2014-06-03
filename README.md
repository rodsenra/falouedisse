falouedisse
===========

Application to mine quotes from news articles


Other relevant sources of information
=====================================

Politics Verbatim
(fora do ar atualmente, mas com resquícios no web archive wayback machine)

http://californiawatch.org/dailyreport/california-watch-launches-politics-verbatim-2724
Today, we’re unveiling a website built by our own Chase Davis called Politics Verbatim. This new site will attempt to track every quote, promise and statement made by our two major candidates for governor in California – Democrat Jerry Brown and Republican Meg Whitman.

https://web.archive.org/web/20101022081945/http://www.politicsverbatim.org/
https://web.archive.org/web/20101114110107/http://www.politicsverbatim.org/candidates/jerry-brown/

Artigo sobre empreitada semelhante em Data Journalism
http://cironline.org/blog/post/using-machine-learning-extract-quotes-text-3687
We've had great results using simple machine learning techniques for several projects this year, and we're starting to realize that higher-order data science can bring real value to the practice of data journalism.
...
One practical lesson I've learned tinkering with machine learning over the last couple of years is that, applied correctly, classifiers can do a much better job of information extraction and pattern recognition than regular expressions.
...
http://cironline.org/blog/post/mapreducing-news-3193
The process, which involved about 60 million document comparisons, took about three hours to run on four mid-size Amazon EC2 instances. In other words, it was pretty much MapReduce or nothing if we wanted to get it done.

Tools
=====

https://github.com/cirlabs/citizen-quotes/
A project to demonstrate maximum entropy models for extracting quotes from news articles in Python.
cdavis@cironline.org
http://cironline.org/person/chase-davis

https://github.com/grangier/python-goose
The aim of the software is is to take any news article or article type web page and not only extract what is the main body of the article but also all meta data and most probable image candidate.

Theory
======

More information about the math can be found here:
http://en.wikipedia.org/wiki/Principle_of_maximum_entropy

Great description of the algorithm here:
http://www.cs.cmu.edu/afs/cs/user/aberger/www/html/tutorial/tutorial.html

And here's some reference info for maxent in NLTK:
http://nltk.googlecode.com/svn/trunk/doc/book/ch06.html

http://www.opencalais.com/
