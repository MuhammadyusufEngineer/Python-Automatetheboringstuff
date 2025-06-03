#! python3
# searchpypi.py  - Opens several search results.

# import requests, sys, webbrowser, bs4
# print('Searching...')    # display text while downloading the search result page
# headers = {
#     'User-Agent': 'Mozilla/5.0 (TARS/Interstellar Bot)'
# }
# res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]), headers=headers)

# res.raise_for_status()
# # Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# # Open a browser tab for each result.
# linkElems = soup.select('.package-snippet')
# print(f"Found {linkElems}.")
# print(f"Found {len(linkElems)} packages.")
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
#     print('Opening', urlToOpen)
#     webbrowser.open(urlToOpen)
from requests_html import HTMLSession
import webbrowser

session = HTMLSession()
query = 'requests'
r = session.get(f'https://pypi.org/search/?q={query}')
r.html.render()  # <-- render JS!

linkElems = r.html.find('.package-snippet')
print(f"Found {len(linkElems)} packages.")

for elem in linkElems[:5]:
    url = 'https://pypi.org' + elem.attrs['href']
    print('Opening', url)
    webbrowser.open(url)

# 
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# linkElems = soup.select('.package-snippet')

# print(f"Found {linkElems}.")
# # print(f"Found {len(linkElems)} packages.")

# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
#     print('Opening', urlToOpen)
#     webbrowser.open_new_tab(urlToOpen)

