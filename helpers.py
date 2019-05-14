import re

def clean_text(text):
    text = re.sub('http://\S+|https://\S+|www.\S+|@\S+', '', text)
    return text
