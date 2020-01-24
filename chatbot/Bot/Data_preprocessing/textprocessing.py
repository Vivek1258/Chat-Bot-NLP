import numpy as np
import random
import string 

import nltk 

import warnings 
warnings.filterwarnings('ignore')

nltk.download('punkt' , quiet = True)
nltk.download('wordnet' , quiet = True)

# Pre-processing the raw text


lemmer = nltk.stem.WordNetLemmatizer()  #WordNet is a semantically-oriented dictionary of English included in NLTK.


def Lemmer_Tokens(tokens):
    
    T = [lemmer.lemmatize(token) for token in tokens]
    return T

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def Lem_Normalize(text):
    
    T = text.lower().translate(remove_punct_dict)
    
    LT = Lemmer_Tokens(nltk.word_tokenize(T))
    
    return LT


# Keyword  matching 

# greetings 

Greet_input = ['hello' , 'hi' , 'greetings' , 'hola' ,'hey' , "sup", "what's up"  ]

Greet_output =  ['Hello!' , 'Hi!' , 'Greetings ' , 'Hola' , 'It\'s nice to meet you.'  , 'Hey there ' ,  "I am glad! You are talking to me" ]



# generate random greeting responce 

# we can create a function  that can generate a random greeting responce 

def gen_greet(sent):
    for word in sent.split():
        if word.lower() in Greet_input :
            return random.choice(Greet_output)

#sent = input()
#gen_greet(sent)




def sim_measure (sen1 , sen2):
            # Here this methord is good for just two sentence , otherwise we can use direct cosine_similarity from sklearn.metrics.pairwise

            sen1 = sen1.lower()
            sen2 = sen2.lower()

            sen1_list = nltk.word_tokenize(sen1)  # tokenization 
            sen2_list = nltk.word_tokenize(sen2) 

            st_w = nltk.stopwords.words('english')   #   the list of stopwords 

            V1 =[]
            V2 =[] 

            sen1_set = {word  for word in sen1_list if not word in st_w}  # remove stop words from the sentence 

            sen2_set = {word  for word in sen2_list if not word in st_w} 


        
        
        
            US = sen1_set.union(sen2_set)  # form a set containing keywords of both strings  

            for w in US: 
                if w in sen1_set: l1.append(1) # create a vector 
                else: l1.append(0) 
                if w in sen2_set: l2.append(1) 
                else: l2.append(0) 
            c = 0

            # cosine formula  
            for i in range(len(US)): 
                    c+= l1[i]*l2[i] 
            cosine = c / float((sum(l1)*sum(l2))**0.5) 


            return cosine 
