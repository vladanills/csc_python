from urllib.request import urlopen
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.len_clean_data = 0
        self.clean_data = []
        self.start_tags = []

    def handle_starttag(self, tag, attrs):
        self.start_tags.append(tag)

    def handle_data(self, data):
        if 'ru' not in data and 'http' not in data and  '{' not in data and data != ' ' and \
                '     ' not in data and data!= ', ' and data!= '  ':
            self.len_clean_data += len(data)
            self.clean_data.append(data)

'''Есть 2 случая. Первый - когда таблица представлена тегом table.
               Второй - когда таблица представлена тегами div, span'''

ref = urlopen('https://calendar.yoip.ru/zodiac/').read().decode('utf-8')
#сайты с table
#https://calendar.yoip.ru/zodiac/
#https://tablici.info/semiletnyaya-vojna-1756-1763-gg.html

#сайты с div
#https://www.amalgama-lab.com/songs/e/eminem/lose_yourself.html


#сначала ищем и выгружаем все table, если они есть
tables = []
words = [('<table', 'table>')]
i = 0
for pair in words:
    while ref.find(pair[0]) != -1 and ref.find(pair[1]) != -1:
        tables.append(ref[ref.find(pair[0]):ref.find(pair[1])+len(pair[1])])
        ref = ref.replace(tables[i], ' ')
        i = i+1

ref = urlopen('https://www.amalgama-lab.com/songs/e/eminem/lose_yourself.html').read().decode('windows-1251')
parser = MyHTMLParser()
parser.feed(ref)
print(parser.start_tags)
#теперь упорядочим пути от корня по частоте для поиска таблиц из div
#как это сделать непонятно


