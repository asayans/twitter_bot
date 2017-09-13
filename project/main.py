import tweepy
import time

'''
    OAuth
'''
consumer_key = 'x'
consumer_secret = 'x'
access_token = 'x'
access_token_secret = 'x'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

'''
    StreamListener
'''
class Listener(tweepy.StreamListener):
    def on_direct_message(self):
        tweet_last_message()

        return True

'''
    Functions
'''
# Check duplicates in already tweeted messages
# returns True if duplicated, False if not
def is_duplicate(text):
    with open('already_done.txt', 'r') as file:
        done = [line.rstrip() for line in file]
        if text in done:
            return True
        else:
            return False

# Get last message's text and tweet it
def tweet_last_message():
    last_id = 0
    while True:
        if last_id == 0:
            args = 'count=1'
        else:
            args = 'since_id=last_id'

        message = api.direct_messages(args)[0]
        last_id = message.id
        print(message)

        if not is_duplicate(message.text):
            text_to_tweet = message.text
            api.update_status(status=text_to_tweet)
            with open('already_done.txt', 'a') as file:
                file.write('\n' + text_to_tweet)

        time.sleep(1)


'''
    Fire!
'''
action = Listener()
action.on_direct_message()
