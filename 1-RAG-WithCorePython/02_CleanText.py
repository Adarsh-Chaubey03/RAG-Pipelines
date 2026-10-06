
'''
step 1 — Cleaning
Suppose:
"Hello     world!!!\n\nThis is   RAG."

We want something like:
"Hello world This is RAG."

'''

import re

def clean_text(text):
    text=re.sub(r'\s+',' ',text) # extra-whitespace
    text=re.sub(r'[^\w\s.,!?-]',' ',text) # whitespace
    return text.strip() # removes trailing and leading whitespaces

