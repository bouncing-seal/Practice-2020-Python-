from urllib.request import urlopen

url = 'https://stepik.org/media/attachments/lesson/209717/1.html'
# https://stepik.org/media/attachments/lesson/209717/1.html
html = urlopen(url).read().decode('utf-8')
ans = []
state = 0
for c in html:
	if c == '<':
		state = 1
	if c == '>':
		state = 0
	elif state == 0:
		ans.append(c)
html = ''.join(ans)

print(html.count('C++'))
