import tweepy
import time

# Auth
auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

# FIRE! #
already_done = []

# get last message's text and tweet it
def tweet_last_message():
    message = api.direct_messages(count='1', full_text='True')[0]
    if message.id in already_done or message.id == '':
        time.sleep(30)
    else:
        text_to_tweet = message.text
        api.update_status(status=text_to_tweet)
        already_done.append(message.id)


while True:
    tweet_last_message()
    time.sleep(30)
