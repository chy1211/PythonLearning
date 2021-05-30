import requests

for i in range(0, 335):
    response = requests.get("https://www.google.co.jp/landing/motto/tabplay/{}.jpg".format(i))
    if response.status_code == 200:
        f = open(f'C:/Users/henry/Documents/GitHub/temp/python/googlelanding/{i}.jpg', 'wb')
        print(f"正在執行爬蟲\n目前進度為:第{i}張")
        f.write(response.content)
        f.close()
