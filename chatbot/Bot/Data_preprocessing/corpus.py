
import numpy as np
import random
import string 


import docx2txt
import tika
from tika import parser


import newspaper
from newspaper import Article


def Gen_Corpus_From_docx(loc):
	corpus = docx2txt.process(loc)
	corpus = corpus.lower()
	return corpus 


def Gen_Corpus_From_pdf(loc):
	corpus = parser.from_file(loc)
	corpus = corpus.lower()
	return corpus 


def Gen_Corpus_From_txt(loc):
	f=open( loc ,'r',errors = 'ignore')
	corpus=f.read()
	corpus = corpus.lower()
	return corpus 


def Gen_Corpus_From_web(loc):
        
		article = Article(loc)
		article.download()
		article.parse()
		article.nlp()
		corpus = article.text
		corpus = corpus.lower()
		return corpus 


