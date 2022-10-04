import tweepy
import time 
from api_keys import * 



auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



def retweet():
    print('retreiving and retweeting tweets')
    mentions = api.mentions_timeline()

    for mention in reversed(mentions):
        print(str(mention.id) + ' - '+ mention.text)
        if '#swe' in mention.text.lower():
            print('found #swe')
            print('retweeting....')
            api.retweet(mention.id)
        

while True:
    retweet()
    