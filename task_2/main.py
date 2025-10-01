# Ввод данных
n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))

# Делим яблоки
apple_per_student = k // n   # целое деление
left_in_basket = k % n       # остаток

# Вывод результата
print(f"{apple_per_student} яблок достанется каждому школьнику")
print(f"{left_in_basket} яблок останется в корзинке")