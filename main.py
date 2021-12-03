from datetime import datetime
import re

import requests

from color import cprint


friday = 4
weekdays = ["月", "火", "水", "木", "金", "土", "日"]

weekday = datetime.now().weekday()
if weekday != friday:
    print(f"今日は{weekdays[weekday]}曜日です")
    exit()

URL = "https://kinro.ntv.co.jp/lineup"
SEARCH_PATTERN = '<div class="title">.+?</div>'

content = requests.get(URL).content.decode()

div = re.findall(SEARCH_PATTERN, content)[0]
title = re.sub("<.+?>", "", div)

cprint(f"今日の金曜ロードショーは「{title}」", {"「.+?」": "YELLOW"})

