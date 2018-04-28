import urllib.request
import urllib.error
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    try:    
        req = urllib.request.urlopen(path + "robots.txt", data=None)
        data = io.TextIOWrapper(req, encoding='utf-8')
        return data.read()
    except urllib.error.HTTPError as e:
        print('HTTP Error (robots.txt): ', e.code)
    except urllib.error.URLError as e:
        print('URL Error (robots.txt): ', e.reason)

#print(get_robots_txt('https://www.thenewboston.com'))






