#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# Code Starts here not finalized yet but works alright

# In[2]:


import numpy as np
import pandas as pd
from tkinter import filedialog as fd
from tkinter import *
import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
global convo_data


# In[3]:


'''def interface():
    t1=Text(tk,width=60,height=30,borderwidth=8,font=('ARIAL',15))
    t1.place(x=10,y=10)
    t2=Text(tk,width=60,height=30,borderwidth=8,font=('ARIAL',15))
    t2.place(x=850,y=10)'''
def select_files():
    convo_data=open(fd.askopenfilename(),"r").readlines()
    print(type(convo_data))
    t1.insert(END,"\n"+str(convo_data))
    return convo_data
    #tk.withdraw()


# In[ ]:



'''b=Button(tk,text="Choose File",command=select_files())
b.place(x=699,y=80,bordermode="inside",height=50, width=100)'''


# Cleaning Data

# In[4]:


def Clean(convo_data):
    convo_text=[]
    print(convo_data)
    for t in convo_data:
        t=t.strip("\n")
        if t != '':
            convo_text.append(t)
    convo_data=convo_text
    return convo_data


# In[5]:


def lexical_diversity(convo_data):
    return len(convo_data)/len(set(convo_data))


# In[6]:


def display_cleaning():
    t1.delete('1.0',END)
    t1.insert(END,"\n"+str(conversation1))
    


# In[7]:


def Clean1(convo_data):
    for index,sent in enumerate(convo_data):
            if sent.count(':') > 0:
                previousSpeaker = sent.split(':')[0]
            if sent.count(':') == 0:
                convo_data[index] = previousSpeaker + ':' + sent
    conversation1 = []
    for sent in convo_data:
        convo = sent.split(':')
        if len(convo) > 2:
            convo[1] += ('-').join(convo[2:])
        convo = convo[:2]
        convo[1] = convo[1].strip()
        if convo[1] != '':
            conversation1.append([c for c in convo])
    return conversation1


# In[8]:


import json
def loading_dataset1(conversation1):
    with open("C:\\Users\\chava\\M_Dataset\\appos.json", "r") as read_file:
        data = json.load(read_file)

    appos = data['appos']
    processedConversation = []
    for speaker, dialog in conversation1:
        for (key, val) in appos.items():
            dialog = dialog.lower()
            dialog = dialog.replace(key, val)
            dialog = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", dialog)
            dialog = ' ' + dialog + ' '
            dialog = re.sub(' +', ' ',dialog)

        processedConversation.append([speaker, dialog])
    print(processedConversation)
    return processedConversation


# In[9]:


def display_1():
    t2.insert(END,"\n"+str(processedConversation))
    


# In[ ]:


'''import re
def Processing(conversation1,appos):
    appos=appos
    processedConversation = []
    for speaker, dialog in conversation1:
        for (key, val) in appos.items():
            dialog = dialog.lower()
            dialog = dialog.replace(key, val)
            dialog = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", dialog)
            dialog = ' ' + dialog + ' '
            dialog = re.sub(' +', ' ',dialog)

        processedConversation.append([speaker, dialog])
    print(processedConversation)
    return processedConversation
'''


# In[10]:


def loading_dataset2():
    with open("C:\\USers\\chava\\M_Dataset\\thirdperson.json", "r") as read_file:
        data = json.load(read_file)
    thirdperson = {}
    for (key, value) in data['thirdperson'].items():
        thirdperson[' ' + key + ' '] = ' ' + value + ' '
    print(thirdperson)
    return thirdperson


# In[11]:


def final_conv(thirdperson,processedConversation):
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
    return finalConversation


# In[12]:


def display_2():
    t2.delete('1.0',END)
    t2.insert(END,"\n"+str(finalConversation))
    


# In[13]:


import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS


# In[15]:



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


# In[ ]:


summary


# In[ ]:


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


# In[ ]:


from collections import Counter
freq_word=Counter(keyword)
freq_word.most_common(8)


# In[ ]:


max_freq=Counter(keyword).most_common(1)[0][1]
print(max_freq)
for word in freq_word.keys():
    freq_word[word]=(freq_word[word]/max_freq)
freq_word.most_common(5)


# In[ ]:


"""doc=nlp(dialog)
print("hello:",doc,"hi")
for sent in doc.sents:
    print(sent)"""


# In[ ]:


sent_strength={}
for sent in doc.sents:
    for word in sent:
        if word.text in freq_word.keys():
            if sent in sent_strength.keys():
                sent_strength[sent]+=freq_word[word.text]
            else:
                sent_strength[sent]=freq_word[word.text]
sent_strength


# In[ ]:


from heapq import nlargest
summarized_sentences=nlargest(20,sent_strength,key=sent_strength.get)
print(summarized_sentences)
final_sent=[w.text for w in summarized_sentences]
summary=' '.join(final_sent)
print(summary)
def onClick():
    t2.insert(END,'\n'+summary)


# In[16]:


convo_data=''
tk=Tk()
tk.title('Text Summarization')
t1=Text(tk,width=60,height=30,borderwidth=8,font=('ARIAL',15))
t1.place(x=10,y=10)
t2=Text(tk,width=60,height=30,borderwidth=8,font=('ARIAL',15))
t2.place(x=850,y=10)
b=Button(tk,text="Choose File",command=select_files)
b.place(x=699,y=80,bordermode="inside",height=50, width=100)
convo_data=b.invoke()
convo_data=Clean(convo_data)
lexical_diversity(convo_data)
conversation1=Clean1(convo_data)
b1=Button(tk,text="Summarize",command=display_cleaning)
b1.place(x=699,y=150,bordermode="inside",height=50, width=100)
processedConversation=loading_dataset1(conversation1)
#processedConversation=Processing(conversation1,appos)
thirdperson=loading_dataset2()
finalConversation=final_conv(thirdperson,processedConversation)

'''b2=Button(tk,text="After Processing",command=display_1)
b2.place(x=699,y=200,bordermode="inside",height=50, width=100)
b3=Button(tk,text="After Processing ",command=display_2)
b3.place(x=699,y=300,bordermode="inside",height=50, width=100)
b4=Button(tk,text="After Processing ThirdPerson",command=onClick)
b4.place(x=699,y=400,bordermode="inside",height=50, width=100)'''


tk.mainloop()


# In[ ]:




