from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

import re, string, random

class SentimentAnalysis:
    def __init__(self):
        self.classifier = None

        self.positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
        self.negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

        self.test_data = None
        self.train_data = None


    def remove_noise(self, tokens, stopwords = ()):
        cleaned_tokens = []

        for token, tag in pos_tag(tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
            token = re.sub("(@[A-Za-z0-9_]+)","", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 and token not in string.punctuation and token.lower() not in stopwords:
                cleaned_tokens.append(token.lower())
        return cleaned_tokens


    def get_all_words(self, cleaned_tokens_list):
        for tokens in cleaned_tokens_list:
            for token in tokens:
                yield token


    def get_tweets_for_models(self, cleaned_tokens_list):
        for tweet_tokens in cleaned_tokens_list:
            yield dict([token, True] for token in tweet_tokens)

    def create_model(self):
        stop_words = stopwords.words('english')
        # Cleaned tokens empty lists
        positive_cleaned_tokens_list = []
        negative_cleaned_tokens_list = []

        # Filling the positive empty list
        for tokens in self.positive_tweet_tokens:
            positive_cleaned_tokens_list.append(self.remove_noise(tokens, stop_words))
        

        # Filling the negative empty list
        for tokens in self.negative_tweet_tokens:
            negative_cleaned_tokens_list.append(self.remove_noise(tokens, stop_words))


        # All positive words
        all_pos_words = self.get_all_words(positive_cleaned_tokens_list)
        
        # Frequency of some frequently appearing words
        freq_dist_pos = FreqDist(all_pos_words)

        # Creating dictionary out of positive tokens
        positive_tokens_for_model = self.get_tweets_for_models(positive_cleaned_tokens_list)

        # Creating dictionary out of negative tokens
        negative_tokens_for_model = self.get_tweets_for_models(negative_cleaned_tokens_list)


        # Creating positive dataset
        positive_dataset = [(tweet_dict, "Positive") for tweet_dict in positive_tokens_for_model]

        # Creating negative dataset
        negative_dataset = [(tweet_dict, "Negative") for tweet_dict in negative_tokens_for_model]

        # Creating a mixed dataset with positive and negative values and shuffling the values
        dataset = positive_dataset + negative_dataset
        random.shuffle(dataset)

        # Test Train split
        self.train_data = dataset[:7000]
        self.test_data = dataset[7000:]

        # Training Naive Bayes Classifier
        self.classifier = NaiveBayesClassifier.train(self.train_data)



    def get_accuracy(self):
        return classify.accuracy(self.classifier, self.test_data)


    def predict_one_review(self, review):
        tokens = self.remove_noise(word_tokenize(review))
        return self.classifier.classify(dict([token, True] for token in tokens))

    def predict_many_reviews(self, reviews):
        predictions = []
        for review in reviews:
            tokens = self.remove_noise(word_tokenize(review))
            predictions.append([review, self.classifier.classify(dict([token, True] for token in tokens))])
        
        return predictions

