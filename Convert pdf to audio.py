#!/usr/bin/env python
# coding: utf-8

# ### convert pdf to audio

# In[1]:


pip install pyttsx3


# In[ ]:


pip install PyPDF2


# In[ ]:


import pyttsx3

import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()


# In[ ]:




