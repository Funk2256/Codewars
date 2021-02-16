from urllib.parse import urlsplit

def domain_name(url):
    test_url = urlsplit(url)
    if test_url.netloc == '':
        return test_url.path.split('.')[1]
    else:
        return test_url.hostname.split('.')[0]


print(domain_name('http://google.com'))