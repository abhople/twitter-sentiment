from textblob import TextBlob
import tweepy

consumer_key = '' #<<your key>>
consumer_secret = '' #<<your key>>

accessToken = '' #<<your key>>
accessSecret = '' #<<your key>>

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth)

public_tweets = api.search('happy')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity) #polarity of the tweets
