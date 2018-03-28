import tweepy
from textblob import TextBlob
import pandas as pd
tweetlist = []
sentiments = []
labels=[]
consumerkey='NxH92yhijufZba8Dw0ix1g5ny'
consumersecret='Cj0Q04dB2i6vzIC7f9sF9m0GRnc5ws1QELdR80owxaWiTaPAn4'
access_token='608187295-Qhp7nEeYLGaKv3QdM3r8X0oDsZMBhBftdBqZbvvt'
access_token_secret='E1io74vAIQWFm7XrGt3YfZejtdEicBP3mIxIlIO5i96Q4'

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(access_token, access_token_secret)

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




