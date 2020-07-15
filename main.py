import tweepy
import time


auth = tweepy.OAuthHandler("Re4z4ibwKg8WoejeSQMLqvYwM",
                           "9FnIChUoDPT7bnB7dqsRKT3D3s2v3zBTHz6lhtOAcBuBvbtHl2")
auth.set_access_token("1140892292615565317-MK7UZS90fOqcfOGBcmZKT0bADzT1mh",
                      "FkgIjyNXMjOEFPFXUaWLkQYlwhDAwPAfHAxNBiCk1Azrk")

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

user = api.me()


search = "Author Amish"
noTweets = 500


for tweet in tweepy.Cursor(api.search, search).items(noTweets):
    try:
        print("RTd and liked")
        tweet.retweet()
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break