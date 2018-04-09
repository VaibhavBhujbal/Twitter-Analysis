import tweepy
from textblob import TextBlob
import pandas as pd
import config

tweetlist = []
sentiments = []
labels = []


auth = tweepy.OAuthHandler(config.consumerkey, config.consumersecret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

#Search for keyword in tweet...polarity measures how positive or negative the tweet is...subjectivity measures opinion or factual
public_tweet = api.search('Trump')

for tweet in public_tweet:
     tweetlist.append(tweet.text)
     analysis = TextBlob(tweet.text)
     sentiments.append((analysis.sentiment[0]))
tweetdataframe = pd.DataFrame(data=tweetlist, columns=['Tweets'], index=None)
for sent in sentiments:
     if (float(sent)<-0.05) :
          labels.append("Negative")
     elif (float(sent)>0.05):
          labels.append("Positive")
     else:
          labels.append("Neutral")

tweetdataframe.insert(1, "Labels", labels)
tweetdataframe.to_csv("Tweets.csv", sep=',')

print(tweetdataframe)