import spacy
nlp=spacy.load('en_core_web_sm')
import os.path
def load_data(path):
    """
    Input  : path and file_name
    Purpose: loading text file
    Output : list of paragraphs/documents and
             title(initial 100 words considred as title of document)
    """
    documents_list = []
    #titles=[]
    with open( os.path.join(path) ,"r") as fin:
        for line in fin.readlines():
            text = line.strip()
            documents_list.append(text)
    #titles.append( text[0:min(len(text),100)] )
    return documents_list#,titles
import nltk
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))
test=load_data("C:/Users/ASUS/Desktop/htext.txt")
sujet=load_data(("C:/Users/ASUS/Desktop/hsujet.txt"))
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))
def return_token(sentence):
    # Tokeniser la phrase
    doc = nlp(sentence)
    # Retourner le texte de chaque token
    return [X.text for X in doc ]
clean_words = []
for token in return_token(test[0]):
    if token not in stopWords:
        clean_words.append(token)

def return_token_sent(sentence):
    # Tokeniser la phrase
    doc = nlp(sentence)
    # Retourner le texte de chaque phrase
    return [X.text for X in doc.sents]
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='french')

def return_stem(sentence):
    doc = nlp(sentence)
    return [stemmer.stem(X.text) for X in doc]
import numpy as np

def return_word_embedding(sentence):
    # Tokeniser la phrase
    doc = nlp(sentence)
    # Retourner le vecteur lié à chaque token
    return [(X.vector) for X in doc]
def return_mean_embedding(sentence):
    # Tokeniser la phrase
    doc = nlp(sentence)
    # Retourner la moyenne des vecteurs pour chaque phrase
    return np.mean([(X.vector) for X in doc], axis=0)
subject=''
for i in range(len(sujet)):
    subject+=sujet[i]
def semantic_rate(test,sujet,semantic_grade):
    count=0
    count1=0
    L=[]
    cc=0
    similarity=0
    rate=0
    for i  in range(len(test)):
        count1=np.linalg.norm(return_mean_embedding(test[i])-return_mean_embedding(sujet[0]))
        for j in range(1,len(sujet)):
            count=np.linalg.norm(return_mean_embedding(test[i])-return_mean_embedding(sujet[j]))
            the_min=min(count1,count)
            L.append(the_min)
        cc=sum(L)/len(L)
    similarity=cc/(len(test))
    if(similarity<0.25):
        rate=1-similarity
    else :rate =0
    return rate*semantic_grade
print(semantic_rate(test,sujet,5))
        
                   
