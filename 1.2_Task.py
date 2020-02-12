from re import findall
from urllib.request import urlopen
from collections import Counter
from bs4 import BeautifulSoup

url = 'https://stepik.org/media/attachments/lesson/209719/2.html'
html = urlopen(url).read().decode('utf-8')
result = findall('<code>(.*?)</code>', html) #Список со строками, которые находятся между <code> и </code>
print(Counter(result).most_common(4))

