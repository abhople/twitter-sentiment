from textblob import TextBlob
import tweepy

consumer_key = 'qHUfehDpzdSvTIesjst8iDkc3'
consumer_secret = '4ljEjAZfVFYQX3mablhkNlGJ46qQ8ilQbNZZLsYQssstR1g996'

accessToken = '56479932-J65KpbpVJkpSvLdBgwBeSXVbgODm7SypVsO62we09'
accessSecret = 'Z39xUnCgVDlzOtuJlD3jfaRuD496bjM4O51mAkE96MTHS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth)

# public_tweets = api.user_timeline('iamsrk')
public_tweets = api.search('hate')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)