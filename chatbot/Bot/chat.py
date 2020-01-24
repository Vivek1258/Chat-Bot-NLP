import numpy as np 

 


import random 


import sklearn 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise  import cosine_similarity 
import nltk 
 
import string
  
import warnings 
warnings.filterwarnings('ignore')


from Bot.Data_preprocessing.textprocessing import Lem_Normalize , gen_greet 

nltk.download('punkt' , quiet = True)
nltk.download('wordnet' , quiet = True)


from Bot.Data_preprocessing.corpus import Gen_Corpus_From_docx




corpus = Gen_Corpus_From_docx('/home/vivek/Documents/vivC1.docx')  # you can generate corpus  from .txt , .pdf or website just change the function pattern 

#'/home/vivek/Documents/vivC.docx'

corpus=corpus.lower()# converts to lowercase



sent_tokens = nltk.sent_tokenize(corpus)# converts to list of sentences 
word_tokens = nltk.word_tokenize(corpus)# converts to list of words



def get_response(user_res):
    bot_res=''



    sent_tokens.append(user_res)



    TfidfVec = TfidfVectorizer(tokenizer=Lem_Normalize, stop_words='english')

    tfidf = TfidfVec.fit_transform(sent_tokens)
    sim = cosine_similarity(tfidf[-1], tfidf)

    idx=sim.argsort()[0][-2]


    flat = sim.flatten()
    flat.sort()
    req_tfidf = flat[-2]



    if(req_tfidf==0):
        bot_res= bot_res + "I am sorry! I am not getting this ..."
        return bot_res
    else:
        bot_res = bot_res+sent_tokens[idx]
        return bot_res



def start_chat ():


		flag=True
		print("Mr. DB : My name is Mr.DB. \n  I will answer your queries related to the cancer . \n  If you want to exit, type end!")
		while(flag==True):
		    
		    user_res = input("User :: ")
		    
		    user_res=user_res.lower()
		    
		    if(user_res!='end'):
		        
		        if(user_res=='thanks' or user_res=='thank you' ):
		            flag=False
		            print("Mr. DB : You are welcome..")
		        else:
		            if(gen_greet(user_res)!=None):
		                print("Mr. DB : "+ gen_greet(user_res))
		            else:
		                print("Mr. DB : ",end="")
		                print(get_response(user_res))
		                sent_tokens.remove(user_res)
		    else:
		        print("Mr. DB : Thanks for using our services .. ")
		        flag=False




