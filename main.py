import tweepy
import time

'''
    Auth
'''
auth = tweepy.OAuthHandler('7YZhADlmNX35BWIIq2dpVCF9q', 'i2k1boNIaGj0Fgii7QtfWj5FlETXg2mBLFkq7q7fzKOJXqQ68R')
auth.set_access_token('907665707202224128-2ExqKKi4ACUmN6y2palkKc8Ve1B1cjt', 'JDR0JFTRucPUzHWT1tGMELy3Yxh8KCT2jaGdepFp1izWI')
api = tweepy.API(auth)

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
    message = api.direct_messages(count='1', full_text='True')[0]
    if not is_duplicate(message.text):
        text_to_tweet = message.text
        api.update_status(status=text_to_tweet)
        with open('already_done.txt', 'a') as file:
            file.write(text_to_tweet)

'''
    Fire!
'''
while True:
    tweet_last_message()
    time.sleep(30)
