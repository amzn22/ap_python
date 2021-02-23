from code_similarity.main import *

# Проверка с помощью библиотеки pycode_similar
print("Началась проверка с помощью библиотеки pycode_similar")
res_1 = start_lib()
print("Закончилась проверка с помощью библиотеки pycode_similar")
print()
# Проверка с помощью собственных алгоритмов
print("Началась проверка с помощью собственных алгоритмов")
res_2 = start_methods()
print("Закончилась проверка с помощью собственных алгоритмов")

print()
print()
print("Общий результат двух реализаций: {}".format((res_1 + res_2) / 2))
