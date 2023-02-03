import time

import tweepy

auth = tweepy.OAuthHandler('b0w5JutekQmNqBBSqVxP7czcf', 'dF8DkbbVMNYy2ksWAECccM8eyugVOTW3OPAgTbe1SNqKauz8zr')
auth.set_access_token('1022544103840591872-F7Zksg3ATZ2gZDw44M5lbPjHoi8pYz',
                      'C96O7sUwn5eiYdJhyb7sRGfR4MBhsodgWBv22VJUw94dC')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while 1:
            try:
                yield cursor.next()
            except StopIteration:
                break
    except tweepy.RateLimitError:
        time.sleep(1000)

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# # generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Amasiatu C. Athan':
#         follower.follow()
