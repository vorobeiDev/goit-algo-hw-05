import timeit

from algorithms.boyer_moore_search import boyer_moore_search
from algorithms.kmp_search import kmp_search
from algorithms.rabin_karp_search import rabin_karp_search

if __name__ == '__main__':
    # Завантаження тексту з файлів
    with open("files/article1.txt", "r", encoding="windows-1251") as f:
        text1 = f.read()

    with open("files/article2.txt", "r", encoding="windows-1251") as f:  # Виправлено на article2.txt
        text2 = f.read()

    # Визначення підрядків для пошуку
    existing_substring = "стандартна бібліотека"
    fictional_substring = "наднова"

    # Функція для вимірювання часу
    def measure_search_time(search_function, pattern, text):
        setup_code = f'''
from __main__ import {search_function.__name__} as search_func
pattern = "{pattern}"
text = """{text}"""
        '''
        return timeit.timeit(stmt=f"search_func(pattern, text)", setup=setup_code, number=10, globals=globals())

    # Вимірювання часу
    texts = [("Article 1", text1), ("Article 2", text2)]
    patterns = [("Existing substring", existing_substring), ("Fictional substring", fictional_substring)]
    algorithms = [("Boyer Moore search", boyer_moore_search), ("KMP search", kmp_search), ("Rabin Karp search", rabin_karp_search)]

    for article_name, text_content in texts:
        for pattern_name, pattern in patterns:
            print(f"\n{article_name}, {pattern_name}: '{pattern}'")
            for algorithm_name, search_function in algorithms:
                print(f"Algorithm: {algorithm_name} - {measure_search_time(search_function, pattern, text_content)} seconds")
