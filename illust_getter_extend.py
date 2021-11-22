import tweepy
from constants import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, QUANTITY, ROOP
import image_save
import get_user_timeline

def main(user_id):
    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #result[0]:ユーザ名, result[1]: 取得したツイート数, result[2]:取得した画像リンクのリスト
    result = get_user_timeline.getUserTimeline(api, user_id, QUANTITY, ROOP)

    print(result[0])
    print('%d個のツイートを取得' % result[1])
    print('%d個のメディアリンクを取得' % len(result[2]))

    image_save.image_save(result[0], result[2])