import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type(res)
# res.status_code == requests.codes.ok
# len(res.text)
# print(res.text[:250])

# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#   res.raise_for_status()
# except Exception as exc:
#   print('There was a problem: %s' % (exc))

res.raise_for_status()
playFile = open('Romeo and Juliet.txt', 'wb')
for chunk in res.iter_content(100000):
  playFile.write(chunk)

playFile.close()