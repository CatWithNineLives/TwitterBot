import tweepy
import time
import logging
from connection import connect_account

logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


class Listener(tweepy.StreamListener):
    """
      This is a class which overrides tweepy.StreamListener and adds own code.
    """

      usernames = []

       def __init__(self, api):
            self.api = api
            self.me = api.me()

        def on_status(self, tweet):
            """
            Attributes: 
            self (object): Listener object. 
            tweet (object): Status object. 
            """

            print("On status block")
            logger.info(f"Processing tweet id {tweet.id}")
            self.usernames.append(tweet.user.screen_name)

            if not tweet.favorited:
                # Like if not done yet
                try:
                    tweet.favorite()
                except Exception as e:
                    logger.info(f"Already Liked tweet {tweet.id}")
                    logger.error("Error on liking", exc_info=True)
                logger.info(f"Liked tweet {tweet.id}")
            user = self.api.get_user(tweet.user.screen_name)
            follow(self.api, user)
            time.sleep(2.4)

        def on_error(self, status_code):
            """
            Attributes: 
            self (object): Listener object. 
            status_code (int): Error code. 
            """

            if status_code == 420:
                # returning False in on_error disconnects the stream
                return False


def follow_usernames(api, usernames):
    """
    Attributes: 
        api (object): tweepy.API() object which is the bot's account authenticated using the given keys. 
        usernames (list): List of usernames input which have to be followed. 
    """
    for name in usernames:
        try:
            user = api.get_user(name)
            follow(api, user)

        except Exception as e:
            logger.error("User doesnot exist", exc_info=True)


def follow(api, user):
    """
    Attributes: 
        api (object): tweepy.API() object which is the bot's account authenticated using the given keys. 
        user (object): User object. 
    """

    print("Follow block")
    if not user.following:
        try:
            api.create_friendship(user.id)
        except Exception as e:
            logger.info(f"Already following {user.name}")
            logger.error("Error on following", exc_info=True)
        logger.info(f"Followed {user.name}")


def listen(api, keywords):
    """
    Attributes: 
        api (object): tweepy.API() object which is the bot's account authenticated using the given keys. 
        keywords (list): List of hashtags that have to be searched for 
    """
    print("Listen block")
    tweets_listener = Listener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
