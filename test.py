import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

text_file  = open("text.txt")

#read file
text = text_file.read()

#Data type 
print(type(text))
print(len(text))
print(text)

#tokenize text by sentences
sentences = sent_tokenize(text)
print(sentences)

#tokenize text by words
words = word_tokenize(text)
print(words)

#frequecy of words
fDist = FreqDist(words)
fDist.most_common(2)

#Remove punctuation marks
words_no_punc = []
for w in words:
  if w.isalpha():
    words_no_punc.append(w.lower())

#Print words without punctuations
print("Words without punctuations: {}".format(words_no_punc))
print("\n")

#Remove Stopwords
stopwords = stopwords.words("french")
#print(stopwords)
clean_words = []
for w in words_no_punc:
  if w not in stopwords:
    clean_words.append(w.lower())

#Print clean words
print("Clean words: {}".format(clean_words))

