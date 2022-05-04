import nltk
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


data = pd.read_csv("C:/Users/ASUS/Desktop/ponctuation/puntuation.txt", sep='\t', header=None)
data.columns = ['label', 'Content']

en_stopwords = nltk.corpus.stopwords.words('english')
wn = nltk.WordNetLemmatizer()


#determiner le pos_tag de chaque phrase
def pos_tagged(sentence):
    token = nltk.word_tokenize(sentence)
    nature = nltk.pos_tag(token)
    pos_tagged=[]
    for i in range(len(nature)):
        pos_tagged+=nature[i][1].split()
    return pos_tagged
data['pos_tagged']=data['Content'].apply(lambda x: pos_tagged(x))

#colonne de punctuation rate qui sert principallement a donner une valeur a l ensemble de ponctuation dans la phrase
def count_punctuation(text):
    binary_array = [1 for ch in text if ch in string.punctuation] 
    nb_ponctuation = sum(binary_array)
    total = len(text) - text.count(" ")
    return round(nb_ponctuation/(total), 4)*100

data['punctuation_rate'] = data['Content'].apply(lambda x: count_punctuation(x))


#colonne des stop words qui sert principalement de differer les types interrogatives de ceux qui ne le sont pas 
def stop_words(email):
    result = "".join([word for word in email if word not in string.punctuation])
    text = re.split('\W+', result)
    x=[ "what", "which","who", "whom",  "is", "are", "was", "be",  "does", "did", "while",  "where", "why", "how", "any",  "can", "will"]
    text = " ".join([wn.lemmatize(word) for word in text if word in x  ])
    return text
data['stop_words'] = data['Content'].apply(lambda x: stop_words(x.lower()))



def clean_sentence(sentence):
    result = "".join([word for word in sentence if word not in string.punctuation])#enlever la ponctuation
    tokens = re.split('\W+', result)#tokenize les phrases
    text = [wn.lemmatize(word) for word in tokens if word not in en_stopwords]#faire la lemmitization et enlever les stopwords
    return text

data['Clean']=data['Content'].apply(lambda x: clean_sentence(x))



from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(data[['Content', 'stop_words', 'pos_tagged','punctuation_rate']], data['label'], random_state=45)
from sklearn  import svm
vectorisation = TfidfVectorizer(analyzer=clean_sentence)
vectorisation_model = vectorisation.fit(X_train['Content'])

stopwords_train = vectorisation_model.transform(X_train["stop_words"])#vectoriser la colonne stop word 
postag_train = vectorisation_model.transform(X_train['pos_tagged'])
stopwords_test = vectorisation_model.transform(X_test["stop_words"])#vectoriser la colonne stop word 
postag_test = vectorisation_model.transform(X_test['pos_tagged'])


vect_train = vectorisation_model.transform(X_train['Content'])
vect_test = vectorisation_model.transform(X_test['Content'])


final_train_vect = pd.concat([pd.DataFrame(vect_train.toarray()),pd.DataFrame(stopwords_train.toarray()),pd.DataFrame(postag_train.toarray()), X_train[[ 'punctuation_rate']].reset_index(drop=True)], axis=1)
final_test_vect = pd.concat([pd.DataFrame(vect_test.toarray()),pd.DataFrame(stopwords_test.toarray()),pd.DataFrame(postag_test.toarray()), X_test[[ 'punctuation_rate']].reset_index(drop=True)], axis=1)




alg_svm= svm.SVC(kernel = 'linear', random_state=45,C=1.1, decision_function_shape= 'ovo', break_ties=False)
alg_svm.fit(final_train_vect, Y_train)
predictions = alg_svm.predict(final_test_vect)

from nltk.tokenize import sent_tokenize
text='It is seen that over the past few years, social media has developed tremendously and has captured over millions of users worldwide? Referring to this social media essay in English is the best way for us to learn about the pros and cons of social media. Suppose we are preparing for the board exam; in that case, we will also find the ‘impact of social media essay’ a beneficial topic. We can prepare ourselves for the board exams by reading up this short social media essay.Meanwhile, Social Media is a lot more than just blogging or posting pictures. As the reach for social media is far and high, it goes beyond impressing people, to impacting or influencing them with the help of these vital tools. However, a wide range of people believe that social media has negatively impacted human relationships.Human interaction has also deteriorated because of it.Nevertheless, social media also has a positive effect. It enables us to connect with our family and friends globally, while even sending out security warnings. Check out the advantages and disadvantages of social media essay to know more about the pros and cons.Reading through the advantages of social media essay is the best way to learn about its positive aspects. We can learn a lot with its help, thus enabling society’s social development. We can also quickly gain information and news via social media. It is a great tool that is used to create awareness about social evils or reform. It is also a good platform that reduces the distance between loved ones and brings them closer. Another advantage is that it is a good platform for young aspirants to showcase their knowledge and skills. At the same time, companies use social media to promote their brand and services/ products.Psychiatrists believe that social media impacts a person negatively. Social media is also considered to be one of the leading causes of depression and anxiety in society. This ‘disadvantages of social media essay’ depicts the adverse effects very well. Students may use it to cheat in exams. Lack of privacy is another evil effect of social media. Spending too much time on social media also results in the drop of grades and the students’ failing performance. Social media users are also very vulnerable to hacking, identity theft, phishing crimes and other cybercrimes.Thus, in conclusion, we can say that we have to be diligent while using social media. We should use our discretion while using social media, thus balancing our social life with our studies, work, family, and social media use.'
doc=sent_tokenize(text)
predicted_data=pd.DataFrame({"sentences": doc}) 

predicted_data['pos_tagged']=predicted_data['sentences'].apply(lambda x: pos_tagged(x))
predicted_data['punctuation_rate'] = predicted_data['sentences'].apply(lambda x: count_punctuation(x))
predicted_data['stop_words'] = predicted_data['sentences'].apply(lambda x: stop_words(x.lower()))
stopwords_predict = vectorisation_model.transform(predicted_data["stop_words"])#vectoriser la colonne stop word 
postag_predict = vectorisation_model.transform(predicted_data['pos_tagged'])
vect_predict = vectorisation_model.transform(predicted_data['sentences'])
final_predict_vect = pd.concat([pd.DataFrame(vect_predict.toarray()),pd.DataFrame(stopwords_predict.toarray()),pd.DataFrame(postag_predict.toarray()), predicted_data[[ 'punctuation_rate']].reset_index(drop=True)], axis=1)

predictions = alg_svm.predict(final_predict_vect)



#assemblage liste de tuple (sentence : type_of_sentence)
def assemblage(list_prediction,list_sentences):
    liste=[]
    for i in range(len(list_prediction)):
        tuple=()
        tuple+=(list_sentences['sentences'][i],list_prediction[i])
        liste.append(tuple)
    return liste



#verifier la ponctuation 
L=assemblage(predictions,predicted_data)
def punctuation_rate(liste,punctuationGrade):
    count=0
    for i in range(len(liste)):
        if liste[i][1]=='declarative':
            ch=liste[i][0]
            if ch[len(ch)-1]!='.':
                count+=1
        if liste[i][1]=='interrogative':
            ch=liste[i][0]
            if ch[len(ch)-1]!='?':
                count+=1
        if liste[i][1]=='exclamations':
            ch=liste[i][0]
            if ch[len(ch)-1]!='!':
                count+=1
    return (count/len(liste))*punctuationGrade
print(punctuation_rate(L))

                
