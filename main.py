from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
def parse():
    url = "https://omgtu.ru/general_information/faculties/" # передаем необходимый URL адре

    page = requests.get(url,verify=False) # отправляем запрос методом Get на данный адрес, отключив проверку сертификата, и получаем ответ в переменную
    soup = BeautifulSoup(page.text,'html.parser') # передаем страницу в bs4
    block = soup.find('div',{'id':'pagecontent'}) # находим  контейнер
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег <a>
            s = data.text # записываем в переменную содержание тега
            s = s.strip() #обрезаем пробелы с обоих концов строки
            while '\n\n' in s: #Удаление пустот между строками
                s=s.replace('\n\n','\n')
            description+=s
    return description

if __name__ == '__main__':
    descriptions = parse() #вызываем функцию
    file = open('faculties.txt', 'w') #отктываем файл
    file.write(descriptions) #вывод в файл
    print(descriptions) #вывод в консоль
