import json
import urllib.request
import time

URL = 'http://api.open-notify.org/iss-pass.json?lat=55.751244&lon=37.618423'
iss_pass_json_bin = urllib.request.urlopen(URL)
iss_pass = json.load(iss_pass_json_bin)
print("Всего пролетов", iss_pass.get("request").get("passes"))
print("Всего пролетов", len(iss_pass.get("response")))
# Для каждого пролета в ответе на запрос:
for issps in iss_pass.get("response"):
    rise = issps.get("risetime")
    dur = issps.get("duration")
    print("Начало пролета", time.ctime(rise))
    print("Конец пролета", time.ctime(rise+dur))