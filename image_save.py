import os
import datetime
import requests
import time
import re

def image_save(user_name, media_links):
    #windowsでの禁止文字の除去
    name = re.sub(r'[\\/:*?"<>|]+','', user_name)

    #同名のディレクトリがない場合、ディレクトリを新規作成
    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    for link in media_links:
        dt_now = datetime.datetime.now()
        file_name = dt_now.strftime("%Y%m%d_%H%M%S") +'.jpg'

        response = requests.get(link)
        image = response.content

        with open('./' + name + '/' + file_name, "wb") as f:
            f.write(image)
        time.sleep(1)