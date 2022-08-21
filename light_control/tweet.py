import tweepy
from credentials import api_key, api_secrets, access_token, access_secret

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def tweet(status):
    api.update_status(status=status)


def tweet_image(status, path):
    media = api.media_upload(path)
    api.update_status(status, media_ids=[media.media_id])


def send_dm(username, path, status):
    user = api.get_user(screen_name=username)
    recipient_id = user.id_str

    media = api.media_upload(path)  # send with media
    api.send_direct_message(recipient_id=recipient_id, text=status,
                            attachment_type='media', attachment_media_id=media.media_id)
