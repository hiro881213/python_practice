import json
import webbrowser
from urllib.request import urlopen

print("Let's find an old website.")

#対象URLを指定
site = input("Type a website URL :")

#期間を指定する
era = input("Type a year, month, and day, like 20150613:")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
#レスポンスを受け取る
response = urlopen(url)

#コンテキストで受け取る
contents = response.read()

#コンテキストをデコードする
text = contents.decode("utf-8")

data = json.loads(text)

try:
    
    old_site = data["archived_snapshots"]["chosest"]["url"]
    
    print("Found this copy:", old_site)
    print("It should appear in your browser now.")
    
    webbrowser.open(old_site)

except:
    print("Sorry, no luck finding, site")
    
