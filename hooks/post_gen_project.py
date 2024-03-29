try:
    # python 2
    from urllib2 import Request, urlopen
except ImportError:
    # python 3
    from urllib.request import Request, urlopen

import os
import shutil


GITIGNORE_FILE = '.gitignore'
IS_WEB_APP = '{{cookiecutter.is_web_app}}'.lower() == 'true'

CONDITIONAL_FILES = {
    '{{cookiecutter.snake_name}}/lambda_handler.py': not IS_WEB_APP,
    'tests/test_lambda_handler.py': not IS_WEB_APP,
    '{{cookiecutter.snake_name}}/web/': IS_WEB_APP,
}


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

def remove(filename):
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def remove_conditional_files():
    for filename, keep_condition in CONDITIONAL_FILES.items():
        if not keep_condition:
            remove(filename)


def bootup_help():
    print("")
    print("#" * shutil.get_terminal_size().columns)
    print("Thank you for using the Hatchery.")
    print("To finish the setup, you will need to run 3 more commands from your new project.")
    print("")
    print("$ make install install-deploy-deps build-cd-workflow")
    print("$ git init; git add .; git commit -m 'chore: Initial Setup from gh:FundingOptions/hatchery'")


generate_gitignore(languages='python,node,serverless')
remove_conditional_files()
bootup_help()
