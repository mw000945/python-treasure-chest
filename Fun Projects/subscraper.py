from colorama import Fore, Style
from urllib.request import urlopen
from bs4 import BeautifulSoup

# put your urls here -> will be used for the 'update' function
URLS = []


# searches recent topics based on a user-entered keyword
def search():
    BASE_URL = 'https://www.reddit.com/search/?q='
    keyword = str(input('keyword: '))
    print(f"Searching for interesting posts on {Fore.GREEN + keyword + Style.RESET_ALL} ...\n")
    URL = BASE_URL + keyword
    html = urlopen(URL)
    bs = BeautifulSoup(html, 'lxml')
    h3_headings = bs.find_all('h3')

    print("========================================")
    print(f"\nResults for: {Fore.GREEN + keyword + Style.RESET_ALL}\n")
    for heading in h3_headings:
        print(f"{heading.get_text()}\n")
    print("========================================\n")


# searches recent topics on user-entered subreddits
def update(URL, html):
    bs = BeautifulSoup(html, 'lxml')
    h3_headings = bs.find_all('h3')
    subreddit = URL[25:-1]

    print("========================================")
    print(f"\nCurrent hot topics on: {Fore.GREEN + subreddit + Style.RESET_ALL}\n")
    for heading in h3_headings:
        print(f"{heading.get_text()}\n")
    print("========================================\n")


def menu():
    print("""Options: 

    Update [1]
    Search [2]
    Exit   [0]
    """)
    choice = int(input(": "))
    if choice == 1:
        for URL in URLS:
            html = urlopen(URL)
            update(URL, html)
    elif choice == 2:
        search()
    elif choice == 0:
        exit()
    else:
        menu()


if __name__ == '__main__':
    print(f"""==================
              {Fore.RED}Subreddit Scraper{Style.RESET_ALL}
              ==================\n""")
    menu()
