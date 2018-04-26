import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

short_pos = open("/srv/files/positive.txt","r",encoding="ISO-8859-1").read()
short_neg = open("/srv/files/negative.txt","r",encoding="ISO-8859-1").read()    

all_words = []
documents = []

#j is adject, r is adverb, and v is verb
#allowed_word_types = ["J","R","V"]

allowed_word_type = ["J"]

for p in short_pos.split("\n"):
    documents.append( (p,"pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_type:
            all_words.append(w[0].lower())

for p in short_neg.split("\n"):
    documents.append( (p,"neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_type:
            all_words.append(w[0].lower())

save_documents = open("/srv/files/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()

    
all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

save_word_features = open("/srv/files/word_features5k.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()


def find_features(documents):
    words = word_tokenize(documents)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)

#positive data example:
training_set = featuresets[:10000]
testing_set = featuresets[10000:]


##negative data example:
##training_set = featuresets[:100]
##testing_set = featuresets[100:]


classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

#############
save_classifier = open("/srv/files/originalnaivebayes5k.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()


BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)


save_classifier = open("/srv/files/BernoulliNB_classifier5k.pickle","wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

#logisticRegression, SGDClassifier
#SVC, LinearSVC, NuSVC

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("/srv/files/LogisticRegression_classifier5k.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

##SVC_classifier = SklearnClassifier(SVC())
##SVC_classifier.train(training_set)
##print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)


LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

save_classifier = open("/srv/files/LinearSVC_classifier5k.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

##SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
##SGDClassifier_classifier.train(training_set)
#3print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

##save_classifier = open("/srv/files/SGD_classifier5k.pickle","wb")
##pickle.dump(SGD_classifier, save_classifier)
##save_classifier.close()

##NuSVC_classifier = SklearnClassifier(NuSVC())
##NuSVC_classifier.train(training_set)
##print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)
##
##save_classifier = open("pickled_algos/NuSVC_classifier5k.pickle","wb")
##pickle.dump(NuSVC_classifier, save_classifier)
##save_classifier.close()

voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  LogisticRegression_classifier,
                                  BernoulliNB_classifier)
                                  
print("voted classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)


def sentiment(text):
    feats = find_features(text)

    return voted_classifier.classify(feats)












