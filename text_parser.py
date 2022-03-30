from urllib.request import urlopen
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.len_clean_data = 0
        self.clean_data = []

    def handle_data(self, data):
        if 'ru' not in data and 'http' not in data and  '{' not in data and data != ' ' and \
                '     ' not in data and data!= ', ' and data!= '  ':
            self.len_clean_data += len(data)
            self.clean_data.append(data)

ref = urlopen('https://traveller-eu.ru/rim/').read().decode('utf-8')
#https://lifehacker.ru/kak-vospitat-sobaku/
#https://traveller-eu.ru/rim/
#http://dinozavrikus.ru/plotoyadnye-i-rastitelnoyadnye
#https://sibac.info/journal/student/175/241917
#https://www.psychologies.ru/articles/psikholog-rasskazal-kak-otlichit-sobstvennoe-mnenie-ot-navyazannogo/


#соотношение чистого текста ко всему содержимому. На разных сайтах разный объем текста.
# Мне кажется, что отталкиваться от этого мало эффективно.
'''parser = MyHTMLParser()
parser.feed(ref)
print(parser.len_clean_data/len(ref))'''

#убираем все header, footer включая их содержимое. Там не содержится основная информация сайта
words = [("<header", "header>"), ("<footer", "footer>")]
for pair in words:
    if ref.find(pair[0]) != -1 and ref.find(pair[1]) != -1:
        ref = ref[:ref.find(pair[0])] + ref[ref.rfind(pair[1])+len(pair[1]):]

#удалим боковое меню и формы
words = [("<aside", "aside>"), ("<form", "/form>")]
for pair in words:
    while ref.find(pair[0]) != -1 and ref.find(pair[1]) != -1:
        ref = ref[:ref.find(pair[0])] + ref[ref.find(pair[1])+len(pair[1]):]

ref = ref.replace('\n','')
ref = ref.replace('\r','')
ref = ref.replace('\t','')

parser = MyHTMLParser()
parser.feed(ref)
print(parser.clean_data)
'''for el in parser.clean_data:
    print(el)'''
with open('clean_data.txt', "w", encoding="utf-8") as f:
    for el in parser.clean_data:
        f.write(el + '\n')

#решение не идеально, но все же удалось избавиться от многих лишних вещей


#open_div = [i for i in range(len(ref)) if ref.startswith('<div', i)]
#close_div = [i for i in range(len(ref)) if ref.startswith('div>', i)]



