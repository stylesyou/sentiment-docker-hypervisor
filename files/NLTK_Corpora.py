from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("shakespeare-macbeth.txt")

tok = sent_tokenize(sample)

print(tok[5:15])
