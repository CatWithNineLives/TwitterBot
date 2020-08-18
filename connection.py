import tweepy
import logging

logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def connect_account():
    api_key = 'cLMY6JHREdl5uNz0hQFWoBw9G'
    api_secret_key = 'LZ0cE0bLWYiyhtunIGGrDOZQXWkNX2ILD9uoqWWgtVmQyb4HmP'
    access_token = '1295259613999243264-O5DRKeX8iwRVBpb1YrQxaTrVviVCYg'
    access_token_secret = 'F4CErM0Nnwa1mb4lqPLToO2PBJa8buOrV7hTkLBwtZjPx'

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
