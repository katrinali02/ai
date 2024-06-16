import math
import re

class Bayes_Classifier:

    def __init__(self, REMOVE_STOPWORDS=False, stopwords_file='english.stop'):
        #self.REMOVE_STOPWORDS = REMOVE_STOPWORDS
        self.smoothing_factor = 1 #laplace; assumes words are seen once for each class
        #with open(stopwords_file, 'r') as file:
            #self.stopwords = set(file.read().strip().split())
        self.vocabulary = set([])
        self.logprior = {}
        self.loglikelihood = {}  # keys should be tuples in the form (w, c)

        self.n_doc = 0
        self.bigdoc = {'positive': [], 'negative': []}
        self.actual = []  #list to hold the actual star rating for each review
    
    def tokenize(self, text): #add better tokenizer that lowers text and removes non-word characters or whitespace
        return re.findall(r"\w+|[^\w\s]", text.lower())

    def train(self, lines):
        #make word_counts
        word_counts = {'positive': {}, 'negative': {}}
        self.n_doc = len(lines)

        #make n_c to initialize document count per class
        n_c = {'positive': 0, 'negative': 0}

        #process text
        for line in lines:
            line = line.replace('\n', '')
            fields = line.split('|')
            stars = fields[0]  #number of stars
            self.actual.append(stars)  #append star rating to actual list
            c = 'positive' if stars == '5' else 'negative' #define classes
            review = fields[2]  #extract the review text

            #tokenize, remove stopwords, and keep only keywords
            words = self.tokenize(review)
            #if self.REMOVE_STOPWORDS:
                #words = [word for word in words if word not in self.stopwords]

            n_c[c] += 1 #document/reviews count tracking per class
            #word frequency counting
            for word in words:
                self.vocabulary.add(word) #update every unique word found in review
                word_counts[c][word] = word_counts[c].get(word, 0) + 1 #initialize unseen words w/ count 0 and add 1 immediately --> done to avoid prob. of 0
                #^^modification allows code to handle cases where word not observed in training data for 1 class but might appear in test data

        #calculate logprior with class balance handling
        class_total_docs = sum(n_c.values())
        for c in n_c:
            self.logprior[c] = math.log((n_c[c] + self.smoothing_factor)/(class_total_docs + self.smoothing_factor * len(n_c)))

        #calculate loglikelihood with smoothing
        for c in word_counts:
            total_count = sum(word_counts[c].values())
            #num of word w occurances in all review text
            for word in self.vocabulary:
                word_count = word_counts[c].get(word, 0)
                #improved laplace smoothing
                numerator = word_count + self.smoothing_factor
                denominator = total_count + self.smoothing_factor * len(self.vocabulary)
                #calculation
                self.loglikelihood[(word, c)] = math.log(numerator/denominator)

    def score(self, doc, c):
        log_probability = self.logprior[c]
        words = self.tokenize(doc)
        for word in words:
            if word in self.vocabulary:
                if (word,c) in self.loglikelihood: #avoid key error to make sense when trying to access dictionary
                    log_probability += self.loglikelihood[(word, c)]
                else: #use smoothing for words not seen in training data and calculate log likelihood for these unseen words
                    log_probability += math.log(self.smoothing_factor/(self.smoothing_factor * len(self.vocabulary)))
        return log_probability

    def predict(self, doc):
        scores = {}
        for c in ['positive', 'negative']:
            scores[c] = self.score(doc,c)
        
        #determine if the review is predicted to be more positive or negative
        predicted_class = '5' if scores['positive'] > scores['negative'] else '1'
        return predicted_class

    def classify(self, lines):
        predictions = []
        for line in lines:
            #split the line and take the review text part for classification
            review = line.split('|')[2]
            predicted_class = self.predict(review)
            predictions.append(predicted_class)
        return predictions