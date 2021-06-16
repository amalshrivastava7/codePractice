### Import Libraries

import nltk
from pprint import pprint
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random

### download sample data

# nltk.download('twitter_samples')


### Sample positive and negative tweets

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

print(len(all_positive_tweets))
print(len(all_negative_tweets))

### Pie chart for viewing data

# fig = plt.figure(figsize=(5, 5))

# labels for the two classes
# labels = 'Positives', 'Negative'
#
# # Sizes for each slide
# sizes = [len(all_positive_tweets), len(all_negative_tweets)]
#
# # Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
# plt.pie(sizes, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
#
# # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.axis('equal')
#
# # Display the chart
# plt.show()

### Preprocessing

tweet = all_positive_tweets[2277]
print(tweet)

# nltk.download('stopwords')

# print(stopwords)

import re                                  # library for regular expression operations
import string                              # for string operations

from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

# remove old style retweet text "RT"
tweet2 = re.sub(r'^RT[\s]+', '', tweet)

# remove hyperlinks
tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet2)

# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)

print(tweet2)


# instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                           reduce_len=True)

# tokenize tweets
tweet_tokens = tokenizer.tokenize(tweet2)

print()
print('Tokenized string:')
print(tweet_tokens)



#Import the english stop words list from NLTK
stopwords_english = stopwords.words('english')

print('Stop words\n')
print(stopwords_english)

print('\nPunctuation\n')
print(string.punctuation)


print()
print('\033[92m')
print(tweet_tokens)
print('\033[94m')

tweets_clean = []

for word in tweet_tokens: # Go through every word in your tokens list
    if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation
        tweets_clean.append(word)

print('removed stop words and punctuation:')
print(tweets_clean)



print()
print('\033[92m')
print(tweets_clean)
print('\033[94m')

# Instantiate stemming class
stemmer = PorterStemmer()

# Create an empty list to store the stems
tweets_stem = []

for word in tweets_clean:
    stem_word = stemmer.stem(word)  # stemming word
    tweets_stem.append(stem_word)  # append to the list

print('stemmed words:')
print(tweets_stem)



from codePractice.DeepLearning.utilsFunctions import process_tweet # Import the process_tweet function

# choose the same tweet
tweet = all_positive_tweets[2277]

print()
print('\033[92m')
print(tweet)
print('\033[94m')

# call the imported function
tweets_stem = process_tweet(tweet); # Preprocess a given tweet

print('preprocessed tweet:')
print(tweets_stem)