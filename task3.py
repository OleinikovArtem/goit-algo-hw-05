import timeit

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def measure_search_time(fn, text, pattern):
    def run():
        return fn(text, pattern)

    times = timeit.repeat(run, number=1)
    return min(times)


text1 = load_text('resourse/article1.txt')
text2 = load_text('resourse/article2.txt')

# Підрядки для пошуку
real_substring = "реалізації бази даних рекомендаційної"  # Існуючий підрядок
fake_substring = "nonexistent substring"  # Неіснуючий підрядок

# Вимірювання часу для кожного алгоритму в кожному тексті
results = {}
for text, text_name in [(text1, "article1"), (text2, "article2")]:
    results[text_name] = {}
    for substring in [real_substring, fake_substring]:
        results[text_name][substring] = {}
        for algorithm in [kmp_search, boyer_moore_search, rabin_karp_search]:
            time_taken = measure_search_time(algorithm, text, substring)
            results[text_name][substring][algorithm.__name__] = time_taken

# Виведення результатів
for text_name, searches in results.items():
    print(f"\nResults for {text_name}:")
    for substring, times in searches.items():
        print(f"  Searching for '{substring}':")
        for algo_name, time in times.items():
            print(f"    {algo_name}: {time:.6f} seconds")
