import pandas as pd
import nltk
import re
import os
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger') 
nltk.download('tagsets')
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
count = 0




def complexe_sentence(text):
    
    tagged_sent = nltk.pos_tag(text.split())
    for x in tagged_sent:
        if x[0] in conj :
            n=tagged_sent.index(x)
            for i in range(n+1,len(tagged_sent)):
                if tagged_sent[i][1] in liste:
                    
                    tagged_sent[n]=('.', '.')
                    
    sentence=""
    for x in tagged_sent:
        sentence+= " " + x[0]
    print(sentence)
    
    return sentence
conj=['for', 'and', 'nor', 'but', 'or', 'yet', 'so'
'both', 'either', 'neither',' not', 'only',' whether',
'after', 'although', 'as', 'as if', 'as long as', 'as much as', 'as soon as', 'as though', 'because', 'before',
'by the time', 'even if', 'even though', 'if', 'in order that', 'in case', 'in the event that', 'lest ', 'now that',' once', 
'only', 'only if', 'provided that',' since', 'so', 'supposing', 'that', 'than', 'though', 
'till',' unless',' until', 'when', 'whenever', 'where', 'whereas', 'wherever', 'whether or not', 'while' ]
liste=['VBZ' ,'VB' ,'VBD' ,'VBG' ,'VBN','VBP']                
fp = open("text.txt")
countph =0;
data = fp.read()
sentences = nltk.sent_tokenize(data)
raw_sentences=[]
for i in sentences:
   
    if(complexe_sentence(i)!=i):
        d=complexe_sentence(i).split('.')
        raw_sentences+=d
    else:
        raw_sentences.append(i)
        
tokenized_sentences = []
for raw_sentence in raw_sentences:
    if len(raw_sentence) > 0:
        tokenized_sentences.append(raw_sentence)
print(tokenized_sentences)
grammar1 = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP | V V NP | V V PP | V S | Adv V NP | V PP  | V V Adj | V Adv Adj PP | V V Adv Adj PP | V Adv V NP | V Adj
    NP -> N | Det N | Det N PP | A N H | N Adj N | Det N Adv PP | N H | N Adj PP | N PP | Adj N | Det Adj X  | N Adv PP | Adj N N X  | Adv NP
    PP -> P NP | P VP | P V S | P NP VP
    H -> NP | Conj NP
    X -> NP | N
    A -> Adj M | Adj
    M -> Conj Adj 
    V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
    V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
    V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
    V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows"
    V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" 
    V -> "increased" | "congested" 
    V -> "make" | "need" | "participating" | "shouldn" | "stay" | "suffer" | "notice" | "get" | "lead"
    V -> "classified" | "follows" | "ve" | "saw" | "went" | "existing"
    V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
    N -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
    N -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
    N -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
    N -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
    N -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
    N -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
    N -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
    N -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight" 
    N -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
    N -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
    N -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
    Det -> "a" | "an" | "the" | "my" | "this" | "These" | "your" | "Most" | "some" | "its" | "both" | "more"
    Conj -> "until" | "and" | "if" | "But" | "or" | "If" 
    P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
    P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
    P -> "with" | "his" | "that" | "over" | "through" 
    Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
    Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
    Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
    Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
    Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
    Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
    Adj -> "elegant" | "strange" | "her" | "bad" | "your"
    Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
    Adv -> "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"  | "not" | "continuously" | "almost" | "so"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier"
    WH ->  "should" | "must" | "who" | "which" | "what" | "when" | "where"
    WH1 -> "how"
    WH2 -> "what"
  """)

#interrogative1
grammar2 = nltk.CFG.fromstring("""
    S1 -> WH S
    S -> NP VP
    PP -> P NP
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | Adj N | Adj Adj N | N | N Adj N
    VP -> V NP | V NP PP | Aux V NP | Aux V PP | Adv V NP | V PP  | Aux V Adj
    PP -> P NP
    V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
    V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
    V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
    V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
    V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
    V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
    V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
    N -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
    N -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
    N -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
    N -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
    N -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
    N -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
    N -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
    N -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
    N -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
    N -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
    N -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
    Det -> "These" | "the" | "some" | "this" | "an" | "a" | "my" | "to" | "those" | "its" | "both" | "more"
    Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as" 
    P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
    P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
    P -> "with" | "his" | "that" | "over" | "through"
    Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
    Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
    Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
    Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
    Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
    Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
    Adj -> "elegant" | "strange" | "her" | "bad" | "your"
    Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
    Aux -> "can" | "is" | "am" | "are" | "will" 
    Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
    WH ->"will" | "should" | "must" | "who" | "which" | "what" | "when" | "where" | "how" | "did"
    WH1 -> "how"
    WH2 -> "what"
    """)
#interrogative2
grammar3 = nltk.CFG.fromstring("""
    S1 -> WH V S | WH Aux S
    S -> NP VP
    PP -> P NP
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | Adj N | Adj Adj N | N | N Adj N
    VP -> V NP | V NP PP | Aux V NP | Aux V PP | Adv V NP | V PP  | Aux V Adj
    PP -> P NP
    V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
    V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
    V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
    V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
    V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
    V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
    V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
    N -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
    N -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
    N -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
    N -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
    N -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
    N -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
    N -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
    N -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
    N -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
    N -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
    N -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
    Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
    Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as"
    P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
    P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
    P -> "with" | "his" | "that" | "over" | "through"
    Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
    Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous" 
    Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
    Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
    Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
    Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
    Adj -> "elegant" | "strange" | "her" | "bad" | "your"
    Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
    Aux -> "can" | "is" | "am" | "are" | "will" 
    Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
    WH ->"will" | "should" | "must" | "who" | "which" | "what" | "when" | "where" 
    WH1 -> "how"
    WH2 -> "what"
    """)
#interrogative3
grammar4 = nltk.CFG.fromstring("""
    S -> WH1 X
    X -> A | A VP | Adv VP 
    VP -> NP V | NP V NP
    NP -> Det Noun | Noun | Noun PP
    A -> Adj M | Adj
    M -> Conj Adj
    PP -> P NP
    WH ->"will" | "should" | "must" | "who" | "which" | "what" | "when" | "where"
    WH1 -> "how"
    V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
    V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
    V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
    V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
    V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
    V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
    V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
    Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
    Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
    Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
    Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
    Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
    Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
    Adj -> "elegant" | "strange" | "her" | "bad" | "your"
    Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
    Noun -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
    Nounoun -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
    Noun -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
    Noun -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
    Noun -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
    Noun -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
    Noun -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
    Noun -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
    Noun -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
    N -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
    N -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
    Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
    Aux -> "can" | "is" | "am" | "are" | "will" 
    P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
    P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
    P -> "with" | "his" | "that" | "over" | "through"
    Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
    WH2 -> "what"
    WH1 -> "how"
    Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as" | "if" 
    
    """)
#exclamative1
grammar5 = nltk.CFG.fromstring("""
    S1 -> WH2  S 
    S -> NP VP | NP 
    NP -> Det A Noun  | Noun | A Noun
    A -> Adj M | Adj
    M -> Conj Adj
    VP  -> Noun V | pp
    pp -> P Noun
    V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
    V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
    V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
    V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
    V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
    V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
    V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
    P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
    P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
    P -> "with" | "his" | "that" | "over" | "through"
    WH2 -> "what"
    WH1 -> "how"
    Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
    Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
    Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
    Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
    Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
    Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
    Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
    Adj -> "elegant" | "strange" | "her" | "bad" | "your"
    Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
    Noun -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
    Noun -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
    Noun -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
    Noun -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
    Noun -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
    Noun -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
    Noun -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
    Noun -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
    Noun -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
    Noun -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
    Noun -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
    Aux -> "can" | "But" | "or" | "If" | "and" | "and" | "until"  
    Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
    Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as" | "if"
    WH ->"will" | "should" | "must" | "who" | "which" | "what" | "when" | "where"


""")
#exclamative such
grammar6 = nltk.CFG.fromstring("""
   S -> S1 SS S2
   S1 -> NP VP
   S2 -> NP | NP VP | NP PP
   NP -> Noun | Det Noun | Det A Noun | Noun Conj X1 | A Noun 
   VP -> V | Aux V | PP V NP | PP Adv V NP | NP V
   PP -> P NP 
   X1 -> Noun | NP
   A -> Adj | Adj M
   M -> Conj Adj | Adj
   P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
   P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
   P -> "with" | "his" | "that" | "over" | "through"
   Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
   Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
   Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
   Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
   Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
   Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
   Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
   Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
   Adj -> "elegant" | "strange" | "her" | "bad" | "your"
   Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
   Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as" | "if" 
   Noun -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
   Noun -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
   Noun -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
   Noun -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
   Noun -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
   Noun -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
   Noun -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
   Noun -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
   Noun -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
   Noun -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
   Noun -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
   Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
   V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
   V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
   V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
   V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
   V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
   V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
   V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
   Aux -> "can" | "have"
   SS -> "such" | "so"
   WH ->"will" | "should" | "must" | "who" | "which" | "what" | "when" | "where"
   WH1 -> "how"
   WH2 -> "what"
""")
#exclamative so
grammar7 = nltk.CFG.fromstring("""
   S -> S1 SS S2
   S1 -> NP VP
   S2 -> Adj | Adj Adv S1 | Adj PP VP
   NP -> Noun | A Noun | Det A Noun | Noun Conj X1 | A Noun PP | Det Noun
   VP -> V | Adv V | V Adv | V Adv X2 | Aux V
   PP -> P NP
   X1 -> Noun | NP
   X2 -> VP
   A -> Adj | Adj M
   M -> Conj Adj | Adj
   P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
   P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
   P -> "with" | "his" | "that" | "over" | "through"
   Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
   Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
   Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
   Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
   Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
   Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
   Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
   Adj -> "elegant" | "strange" | "her" | "bad" | "your"
   Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
   Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as" | "if"
   Noun -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
   Noun -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
   Noun -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
   Noun -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
   Noun -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
   Noun -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
   Noun -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
   Noun -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
   Noun -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
   Noun -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
   Noun -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
   Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
   V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
   V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
   V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
   V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
   V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
   V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
   V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
   Aux -> "can" | "have"
   SS -> "such" | "so"
   WH ->"will" | "should" | "must" | "who" | "which" | "what" | "when" | "where"
   WH1 -> "how"
   WH2 -> "what"
   
""")
#exclamative such
grammar8 = nltk.CFG.fromstring("""
   S -> S1 SS S2
   S1 -> NP VP | NP VP X3
   X3 -> NP VP 
   S2 -> Adj | Adj Adv S1 | Adj PP VP
   NP -> Noun | A Noun | Det A Noun | Noun Conj X1 | A Noun PP | Det Noun
   VP -> V | Adv V | V Adv | V Adv X2 | Aux V | V NP
   PP -> P NP
   X1 -> Noun | NP
   X2 -> VP
   A -> Adj | Adj M
   M -> Conj Adj | Adj
   P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
   P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
   P -> "with" | "his" | "that" | "over" | "through"
   Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
   Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
   Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
   Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
   Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
   Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
   Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
   Adj -> "elegant" | "strange" | "her" | "bad" | "your"
   Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
   Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as" | "if"
   Noun -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
   Noun -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
   Noun -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
   Noun -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
   Noun -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
   Noun -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
   Noun -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
   Noun -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
   Noun -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
   Noun -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
   Noun -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
   Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
   V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
   V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
   V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
   V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
   V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
   V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
   V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
   Aux -> "can" | "have"
   SS -> "such" | "so"
   WH -> "will" | "should" | "must" | "who" | "which" | "what" | "when" | "where"
   WH1 -> "how"
   WH2 -> "what"
   
""")
#imperative1 verb/let
grammar9 = nltk.CFG.fromstring("""
  S -> V S1
  S1 -> NP VP | NP | NP Conj VP | NP PP | Adv 
  NP -> Det Noun | A Noun | Noun Adv | Noun Noun Adv | Det A Noun | Noun Noun | Noun
  PP -> P NP
  VP -> V | V NP | Adv V NP | V X
  X -> WH V S1
  A -> Adj | Adj M
  M -> Adj | Con Adj
  P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
  P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
  P -> "with" | "his" | "that" | "over" | "through"
  WH -> "what" | "how" | "should" | "must" | "who" | "which" | "what" | "when" | "where" 
  Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
  Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
  Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
  Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
  Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
  Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
  Adj -> "elegant" | "strange" | "her" | "bad" | "your"
  Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
  V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
  V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
  V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
  V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
  V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
  V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
  V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
  Noun -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
  Noun -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
  Noun -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
  Noun -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
  Noun -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
  Noun -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
  Noun -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
  Noun -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
  Noun -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
  Noun -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
  Noun -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
  Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "s" | "if"
  Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
    Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
  Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
  
  
""")
#imperative2 do/dont
grammar10 = nltk.CFG.fromstring("""
  S -> D S1
  S1 -> NP | X VP NP | X VP 
  NP -> Noun | Det Noun | Det Noun PP | Det A Noun PP | Det A Noun | Noun Adv | Noun Noun | A Noun 
  VP -> V | V Adv
  A -> Adj | Adj M
  M -> Adj | Conj Adj
  PP -> P NP
  P ->  "to" | "up" | "of" | "with" | "from" | "for" | "by" | "in" | "with" | "during" | "on"
  P -> "as" | "with" | "in" | "before" | "from" | "During" | "at" | "In" | "without" | "to" | "by"
  P -> "with" | "his" | "that" | "over" | "through"
  Adj -> "Certain" | "associated" | "burning" | "raised" | "high" | "mobile" | "affected" | "short" | "existing" | "long" | "increased" | "effective" | "busy"
  Adj -> "congested" | "new" | "strange" | "good" | "free" | "dangerous"
  Adj -> "common" | "crazy" | "lovely" | "interesting" | "pretty" | "lovely" | "bright" | "big" | "smart" | "last" | "some" | "wonderful"
  Adj -> "normal" | "standard" | "Most" | "short" | "effective" | "busy" | "cold" | "calm" |
  Adj -> "hot" | "sunny" | "strenuous" | "outdoor" | "sure" | "such" | "able" | "medical" | "much" | "crazy" 
  Adj -> "smart" | "last" | "thankful"  | "some" | "wonderful" | "my" | "new" |
  Adj -> "elegant" | "strange" | "her" | "bad" | "your"
  Adj -> "based" | "technical" | "academic" | "corporate" | "online" | "various" | "based"
  V -> "become" | "is" | "ve" | "saw" | "ate" | "walked" | "went" | "did" | "be" | "give" | "read" | "will" | "should" | "must" | "consider" | "modifying"
  V -> "let" | "have" | "take" | "bring" | "do" | "read" | "write" | "see"  | "doing" | "sit" | "me" | "will" | "didn" | "increase" | "think" | "acknowledges"
  V -> "like" | "wears" | "know" | "been" | "was" | "couldn" | "laughed" | "don" | "may" | "experience" | "speak" | "consider" | "spend" | "affect"
  V -> "has" | "lead" | "can" | "am" | "are" | "receive" | "aren" | "could" | "reduce"  | "avoid" | "follows" | "shouldn" | "stay" | "suffer" | "participating" 
  V -> "associated" | "burning" | "raised" | "Jump" | "subscribe" | "cost" | "affected" | "notice" | "get" | "lead" | "make" | "need"
  V -> "increased" | "congested" | "go" | "rising" | "saw" | "went" | "existing" | "classified" | "follows" | "ve"
  V -> "go" | "rising" | "takes" | "impart" | "transformed" | "used" | "made" | "turning" | "gain" | "allows" 
  Noun -> "Air" | "pollution" | "health" | "weather" | "conditions" | "build" | "pollutants" | "emissions" | "transport" | "fuel" | "levels" | "air" 
  Noun -> "table" | "contents" | "alerts" | "text" | "service" | "You" | "your" | "phone" | "you" | "heart" | "lung" | "symptoms" | "america" | "work" 
  Noun -> "Aware" | "AIR" | "Alerts" | "messages" | "rate" | "Advice" | "people" | "t" | "term" | "peaks" | "homework" | "chapter" | "i" | "mistake" 
  Noun -> "treatment" | "doctor" | "time" | "streets" | "breathing" | "days" | "activity" | "day" | "walk" | "reliever" | "medicines" | "school"
  Noun -> "medication" | "asthma" | "inhaler" | "Children" | "part" | "games" | "They" | "their" | "use" | "night" | "me" | "three" | "park" | "everyone"
  Noun -> "condition" | "change" | "advice" | "Weather" | "winter" | "level" | "travelling" | "thing" | "neighbour" | "clothes" | "Mike" | "bouquet" 
  Noun -> "ground" | "summer" | "wind" | "concentrations" | "quality" | "measurement" | "particulate" | "summary" | "s" | "he" | "telescope" | "fact"
  Noun -> "matter" | "sulphur" | "dioxide" | "nitrogen" | "carbon" | "monoxide" | "ozone" | "film" | "she" | "girl" | "they" | "grown"  | "sunlight"
  Noun -> "flowers" | "John" | "Mary" | "Bob" | "man" | "dog" | "cat" | "friends" |"sense" | "fashion" | "we" | "story" | "boss" | "It" | "it" | "nature"
  Noun -> "learning" | "training" | "place" | "network" | "internet" | "company" | "institution" | "intranet" | "roots" | "world" | "computer" | "concept" | "tool"
  Noun -> "inroads" | "college" | "education" | "students" | "knowledge" | "courses" | "universities" | "subjects" | "E" | "e"
  Conj -> "But" | "or" | "If" | "and" | "and" | "until" | "as" | "if"
  Adv -> "when" | "when" | "outdoors" | "away" | "still" | "also" | "every" | "up" | "upstairs" | "then" | "always" | "t" | "out" | "never" | "down"
  Adv -> "usually" | "However" | "lately" | "into" | "widely"  | "Now" | "mostly" | "Earlier" | "almost" | "so"
  Det -> "These" | "the" | "some" | "this" | "an" | "a" | "an" | "my" | "to" | "its" | "both" | "more"
  D -> "do" | "don"
  X -> "not" | "t"
  WH -> "what" | "how" | "should" | "must" | "who" | "which" | "what" | "when" | "where"
""")

def check (sentences):
    countSim = 0
    count=0
    countInter1 = 0
    countInter2 = 0
    countInter3 = 0
    countExc1 = 0
    countExc2 = 0
    countExc3 = 0
    countExc4 = 0
    countImp1 = 0
    countImp2 = 0
    i=0
    test=False
    while(test== False and i==0):
        tab = re.sub("[^a-zA-Z0-9]"," ",sentences )
        sent = tab.split()
        ch="non sentence"
        rd_parser1 = nltk.ChartParser(grammar1)
        for tree in rd_parser1.parse(sent):
            countSim=1
        if(countSim>0) :
            ch="simple1"
            test=True

        rd_parser2 = nltk.ChartParser(grammar2)
        for tree in rd_parser2.parse(sent):
            countInter1=1
        if(countInter1>0) :
            ch="simple3"
            test=True
            
        rd_parser3 = nltk.ChartParser(grammar3)
        for tree in rd_parser3.parse(sent):
            
            countInter2=1
        if(countInter2>0) :
            ch="simple4"
            test=True
            
        rd_parser4 = nltk.ChartParser(grammar4)
        for tree in rd_parser4.parse(sent):
            
            countInter3=1
        if(countInter3>0) :
            test=True
            ch="simple5"
             
    
        rd_parser5 = nltk.ChartParser(grammar5)
        for tree in rd_parser5.parse(sent):
            
            countExc1=1
        if(countExc1>0) :
            ch="simple6"
            test=True             
    
        rd_parser6 = nltk.ChartParser(grammar6)
        for tree in rd_parser6.parse(sent):
            
            countExc2=1
        if(countExc2>0) :
            test=True
            ch="simple7"
            
       
        rd_parser7 = nltk.ChartParser(grammar7)
        for tree in rd_parser7.parse(sent):
            
            countExc3=1
        if(countExc3>0) :
            ch="simple8"
            test=True
            
        rd_parser8 = nltk.ChartParser(grammar8)
        for tree in rd_parser8.parse(sent):
            
            countExc4=1
        if(countExc4>0) :
            ch="simple9"
            test=True
            
        rd_parser9 = nltk.ChartParser(grammar9)
        for tree in rd_parser9.parse(sent):
            print("cc")
            countImp1=1
        if(countImp1>0) :
            ch="simple10"
            test=True
            
        rd_parser10 = nltk.ChartParser(grammar10)
        for tree in rd_parser10.parse(sent):
            print("cc")
            countImp2=1
        if(countImp2>0) :
            ch="simple11"
            test=True
        i=1
    count += countSim + countInter1 +countInter2 + countInter3 + countExc1 + countExc2 + countExc3 + countExc4 +countImp1 + countImp2            
   
    return count







def porcentage (countph,tokenized_sentences,grammerGrade):
    for i in tokenized_sentences:
        print(len(tokenized_sentences))
    porcent=(countph/ len(tokenized_sentences))*grammerGrade
    print(porcent)
    return porcent
    
for i in tokenized_sentences:
    countph+=check(i)
print(countph,"countph")    

print(porcentage(countph,tokenized_sentences,5))
