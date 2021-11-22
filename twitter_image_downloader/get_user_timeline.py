"""
関数名: userTimelineGet
引数：api(Tweepy用のAPI変数), user_id(ユーザID), quantity(1度に取得するTweetの数), roop(リクエストを送る回数)
戻り値：user_name(ユーザ名), tweet_count(取得したTweetの総数), media_links(取得した画像リンクのリスト)
"""
def getUserTimeline(api, user_id, quantity, roop):
    tweet_count = 0
    media_links = []
    max_id = 0
    user_name = ''
    tmp_links = []
    tmp_id = 0

    #max_id定義の為の処理
    for status in api.user_timeline(id = user_id, count = 200):
        if (not 'RT @' in status.text):
            max_id = status.id
            user_name = status.user.name
            break

    #メディアリンク取得の処理
    for r in range(roop):
        for status in api.user_timeline(id = user_id, max_id = max_id, count = quantity):
            max_id = status.id
            tweet_count += 1
            if (not 'RT @' in status.text):
                #メディアリンクが複数あるとき
                if hasattr(status, "extended_entities"):
                    if ("media" in status.extended_entities):
                        if (len(status.extended_entities['media']) != 0):
                            for media in status.extended_entities['media']:
                                tmp_links.append(media['media_url_https'])
                                
                #メディアリンクが1つのとき
                elif hasattr(status, "entities"):
                    if ("media" in status.entities):
                        if (len(status.entities['media']) != 0):
                            for media in status.entities['media']:
                                tmp_links.append(media['media_url_https'])

                tmp_links.reverse()#1つのTweetに複数の画像があるとき、1→2→3→4を4→3→2→1に入れ替える処理(保存したときに漫画を読みやすくするため)
                media_links.extend(tmp_links)
                tmp_links = []
        if tmp_id != max_id:#さかのぼれるTweetの限界に達したかを判定する処理
            tmp_id = max_id
        else:
            break

    media_links = deleteDuplicate(media_links)#重複リンクの削除
    media_links.reverse()#古いTweetがリストの先頭に来るようにリバース
    return user_name, tweet_count, media_links

def deleteDuplicate(links):
    result = []

    for link in links:
        if link not in result:
            result.append(link)
    return result