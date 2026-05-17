import urllib.request
import re

url = 'https://aeonmall-hadong.com.vn/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = re.findall(r'src="([^"]+\.(?:jpg|png|jpeg))"', html)
    print("Found images:")
    for img in set(images):
        if 'http' not in img:
            img = 'https://aeonmall-hadong.com.vn' + img
        print(img)
except Exception as e:
    print(e)
