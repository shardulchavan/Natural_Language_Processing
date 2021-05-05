#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import os 
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
#from nltk.corpus import stopwords
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.tokenize import sent_tokenize
import re
import numpy as np
import pandas as pd
import nltk
import sys


# In[4]:


b=Button(tk,text="READ",command=select_files)
b.place(x=990,y=80,bordermode="inside",height=50, width=100)
mainloop()


# Code Starts here not finalized yet but works alright

# In[1]:


import numpy as np
import pandas as pd
from tkinter import filedialog as fd
from tkinter import *
import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize


# In[2]:


tk=Tk()
convo_data=open(fd.askopenfilename(),"r").readlines()
tk.withdraw()
convo_data


# Cleaning Data

# In[3]:


convo_text=[]
for t in convo_data:
    t=t.strip("\n")
    if t != '':
        convo_text.append(t)
convo_data=convo_text
convo_data


# In[4]:


def lexical_diversity(convo_data):
    return len(convo_data)/len(set(convo_data))


# In[5]:


lexical_diversity(convo_data)


# In[6]:


for index,sent in enumerate(convo_data):
    if sent.count(':') > 0:
        previousSpeaker = sent.split(':')[0]
    if sent.count(':') == 0:
        convo_data[index] = previousSpeaker + ':' + sent
        


# In[7]:


conversation1 = []
for sent in convo_data:
    convo = sent.split(':')
    if len(convo) > 2:
        convo[1] += ('-').join(convo[2:])
    convo = convo[:2]
    convo[1] = convo[1].strip()
    if convo[1] != '':
        conversation1.append([c for c in convo])
conversation1


# In[8]:


import sys
sys.path


# In[9]:


import json
with open("C:\\Users\\chava\\M_Dataset\\appos.json", "r") as read_file:
    data = json.load(read_file)
    
appos = data['appos']
appos


# In[10]:


import re
processedConversation = []
for speaker, dialog in conversation1:
    for (key, val) in appos.items():
        dialog = dialog.lower()
        dialog = dialog.replace(key, val)
        dialog = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", dialog)
        dialog = ' ' + dialog + ' '
        dialog = re.sub(' +', ' ',dialog)
        
    processedConversation.append([speaker, dialog])
processedConversation


# In[11]:


with open("C:\\USers\\chava\\M_Dataset\\thirdperson.json", "r") as read_file:
    data = json.load(read_file)
thirdperson = {}
for (key, value) in data['thirdperson'].items():
    thirdperson[' ' + key + ' '] = ' ' + value + ' '
thirdperson


# In[12]:


finalConversation = []
previousSpeaker = ''
for speaker, dialog in processedConversation:
    for (key, val) in thirdperson.items():
        dialog = dialog.lower()
        dialog = dialog.replace(key, val)
        dialog = dialog.replace(' i ', ' ' +speaker + ' ')
        dialog = dialog.replace('i ', ' ' +speaker + ' ')
        dialog = dialog.replace('you', previousSpeaker if previousSpeaker != '' else 'them' )
    finalConversation.append([speaker, dialog])
finalConversation


# In[13]:


import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS


# In[14]:


summary = ''
summarySpeaker = None
for speaker, dialog in finalConversation:
    if summarySpeaker is None:
        doc = nlp(dialog)
        print(doc)
        for token in doc:
            if token.lemma_ == 'summarize':
                # this is the part where we hear someone summarize
                # point following this must be a part of the summarization
                summarySpeaker = speaker
    else:
        if speaker == summarySpeaker:
            summary = summary + dialog
        else:
            summarySpeaker = None


# In[15]:


summary


# In[16]:


from string import punctuation
keyword=[]
for speaker, dialog in finalConversation:
    doc=nlp(dialog)
    stopwords=list(STOP_WORDS)
    pos_tag=['PROPN','ADJ','NOUN','VERB']
    for token in doc:
        if(token.text in stopwords or token.text in punctuation):
            continue 
        if(token.pos_ in pos_tag):
            keyword.append(token.text)
keyword


# In[17]:


from collections import Counter
freq_word=Counter(keyword)
freq_word.most_common(8)


# In[18]:


max_freq=Counter(keyword).most_common(1)[0][1]
print(max_freq)
for word in freq_word.keys():
    freq_word[word]=(freq_word[word]/max_freq)
freq_word.most_common(5)


# In[19]:


"""doc=nlp(dialog)
print("hello:",doc,"hi")
for sent in doc.sents:
    print(sent)"""


# In[21]:


sent_strength={}
for sent in doc.sents:
    for word in sent:
        if word.text in freq_word.keys():
            if sent in sent_strength.keys():
                sent_strength[sent]+=freq_word[word.text]
            else:
                sent_strength[sent]=freq_word[word.text]


# In[22]:


from heapq import nlargest
summarized_sentences=nlargest(20,sent_strength,key=sent_strength.get)
summarized_sentences


# In[23]:


final_sent=[w.text for w in summarized_sentences]
summary=' '.join(final_sent)
print(summary)

