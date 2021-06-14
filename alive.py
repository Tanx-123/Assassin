from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html= urlopen("https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634")
except HTTPError as e :
    print("HTTP error")
except URLError as e:
    print("Url error")
else:
    print("HTML details:")
    print(html.read())