try:
    # python 2
    from urllib2 import Request, urlopen
except ImportError:
    # python 3
    from urllib.request import Request, urlopen


GITIGNORE_FILE = '.gitignore'


def fetch_gitignore(languages='python'):
    print("Fetching gitignore from gitignore.io for languages: " + languages)
    # We need to spoof the user-agent, as Cloudflare doesn't allow the default urllib one
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = 'https://www.gitignore.io/api/' + languages
    request = Request(url, None, {'User-agent': user_agent})
    response = urlopen(request)
    return response.read()


def generate_gitignore(languages='python'):
    contents = fetch_gitignore(languages=languages)
    with open(GITIGNORE_FILE, 'wb') as f:
        f.write(contents)


generate_gitignore()
