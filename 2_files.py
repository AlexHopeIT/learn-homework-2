"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('/home/alexhope/pythonProject/LP lessons/L3/referat.txt', 
              'r', encoding='utf-8') as ref:
        referat = ref.read()
        lenght_text = len(referat)
        print('Длина текста: ', lenght_text)

        all_words = referat.split()
        print('Всего слов в тексте: ', len(all_words))

        referat2 = referat.replace('.', '!')
        print('Исправленный текст: ', referat2)

        with open('referat2.txt', 'w', encoding='utf-8') as ref2:
            ref2.write(referat2)


if __name__ == "__main__":
    main()
