import json
import urllib.request
import time

URL = 'https://yandex.com/time/sync.json?geo=213'
time_json_bin = urllib.request.urlopen(URL)
time_data = json.load(time_json_bin)
# Время в миллисекундах с 1970 года поделили на 1000, получили секунды
tyme_now = time_data.get("time") / 1000
print(time.ctime(tyme_now))
# Разница Яндекс.времени и времени компьютера, в секундах
print(tyme_now - time.time())
print(time_data.get("clocks").get("213").get("sunrise"))
print(time_data.get("clocks").get("213").get("sunset"))
