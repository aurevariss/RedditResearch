f = open("../stray kids/collected_prep.txt", "r", encoding="utf-8")
text = str(f.read())
# print(text)

from nltk import word_tokenize
# токенизируем текст
text_tokens = word_tokenize(text)
# подключаем библиотеку для работы с текстом
import nltk
# переводим токены в текстовый формат
text = nltk.Text(text_tokens)
# подключаем статистику
from nltk.probability import FreqDist
# и считаем слова в тексте по популярности
fdist = FreqDist(text)
# print(fdist.most_common(5))


# подключаем модуль со стоп-словами
from nltk.corpus import stopwords
# добавляем русские и французские стоп-слова
eng_stopwords = stopwords.words("english")
# перестраиваем токены, не учитывая стоп-слова
text_tokens = [token.strip() for token in text_tokens if token not in eng_stopwords]
# снова приводим токены к текстовому виду
text = nltk.Text(text_tokens)
# считаем заново частоту слов
fdist_sw = FreqDist(text)
# показываем самые популярные
# print(fdist_sw.most_common(10))

# добавляем свои слова в этот список
eng_stopwords.extend(['song', 'like','lyrics','im', 'dont','really','know', "one", "also", "songs", "much", "always", "“", "”", "way", "han", "chan", "changbin", "even", "lot", "racha", "makes", "part", "go", "skz", "something", "right", "time", "listen", "stay", "ive", "track", "well", "say"])
# перестраиваем токены, не учитывая стоп-слова
text_tokens = [token.strip() for token in text_tokens if token not in eng_stopwords]
# снова приводим токены к текстовому виду
text = nltk.Text(text_tokens)
# считаем заново частоту слов
fdist_sw = FreqDist(text)
# показываем самые популярные
print(fdist_sw.most_common(10))

