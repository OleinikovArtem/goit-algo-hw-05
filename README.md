## Висновки

На основі аналізу, алгоритм Boyer-Moore є найшвидшим для пошуку підрядків у текстах, перевершуючи алгоритми KMP та Rabin-Karp. Boyer-Moore ефективно мінімізує кількість порівнянь за рахунок добре розробленої таблиці зсувів. В той час як KMP демонструє нижчу швидкість через частіше повторення LPS, Rabin-Karp виявляється повільнішим через витрати на перерахунок хешів.

```cmd
    Results for article1:
    Searching for 'реалізації бази даних рекомендаційної':
        kmp_search: 0.002071 seconds
        boyer_moore_search: 0.000327 seconds
        rabin_karp_search: 0.002892 seconds
    Searching for 'nonexistent substring':
        kmp_search: 0.000962 seconds
        boyer_moore_search: 0.000229 seconds
        rabin_karp_search: 0.002289 seconds

    Results for article2:
    Searching for 'реалізації бази даних рекомендаційної':
        kmp_search: 0.000009 seconds
        boyer_moore_search: 0.000007 seconds
        rabin_karp_search: 0.000024 seconds
    Searching for 'nonexistent substring':
        kmp_search: 0.001202 seconds
        boyer_moore_search: 0.000266 seconds
        rabin_karp_search: 0.002975 seconds
```
