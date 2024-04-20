""" ---------------------------------- """
    # Робота з випадковими величинами
""" ---------------------------------- """
"""
Робота з випадковими величинами є важливою частиною багатьох областей, включаючи статистику, інженерію, науку про дані та фінанси. 
Випадкова величина — це змінна, значення якої є результатом випадкових явищ або експериментів. 
Існують два основних типи випадкових величин: дискретні та неперервні.

1. Дискретні випадкові величини: Це такі, які приймають обмежену кількість значень або значення, які можна перелічити. 
Наприклад, кількість монет, що випали решкою у серії підкидань, є дискретною випадковою величиною.
2. Неперервні випадкові величини: Вони можуть приймати будь-яке значення у певному діапазоні. 
Наприклад, змінна, яка представляє час, необхідний для виконання певної задачі, є неперервною випадковою величиною.

Робота з випадковими величинами в програмуванні є ключовим елементом багатьох програмних застосунків, від ігор до наукових симуляцій. 
Для генерації випадкових (псевдовипадкових) чисел у Python є пакет random. Він досить хороший для ряду звичайних завдань, але не для криптографії. 
Бо на жаль, вбудований генератор псевдовипадкових чисел досить скоро починає повторюватися і не є достатньо криптостійким. 
Проте, для прикладних завдань поза сферою криптографії його цілком вистачає. 
Розглянемо основні методи пакету які можуть нам знадобиться в роботі.
"""
# 1. Для отримання випадкового цілого числа з рівномірного розподілу в інтервалі між a та b включно треба використати метод random.randint(a, b).
# Він повертає випадкове ціле число N таке, що a <= N <= b:
import random
random.randint(1, 1000)

import random
dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

# 2. Метод random.random() потрібен, щоб отримати випадкове число в інтервалі 0, 1. 
# Він генерує випадкове дійсне число між 0.0 (включно) та 1.0 (не включно):
import random
num = random.random()
print(num)

#Оскільки це випадкове число вивід кожен раз буде іншим.
#Припустимо, вам потрібно симулювати випадкове відсоткове заповнення. 
#Можна використовувати random.random() для цього:
import random
fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")
"""
Тут в f рядку з'явилось форматування {fill_percentage:.2f} яке вказує, яким чином відображати змінну fill_percentage. 
Вираз .2 це кількість знаків після десяткової крапки. 
У цьому випадку вказано, що потрібно відображати два знаки для дійсного числа. 
Символ f означає, що число має бути відображене у форматі дійсного числа.
"""

# 3. Метод random.randrange(start, stop[, step]) повертає випадково вибране число з заданого діапазону.
import random
print(random.randrange(10))  # Верхня межа є 10, але не включається

# Наприклад симуляція пострілу по мішені, але необхідно вибрати випадковий номер від 1 до 10, та лише непарні числа:
import random
target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

# 4. метод random.shuffle(x), де x - список, який потрібно перемішати.
import random
cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Перемішана колода: {cards}")

# 5. метод random.choice(seq), де seq - послідовність для вибору: список або кортеж. Якщо потрібно вибрати випадковий елемент зі списку
import random
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

# 6. Щоб вибрати більше чим один випадковий елемент зі списку, нам необхідний метод random.choices().
"""
Синтаксис методу random.choices() наступний:

random.choices(population, weights=None, cum_weights=None, k=1)

population - послідовність список, з якої має бути зроблений вибір.
weights - опціональний список, який вказує ймовірності (ваги) кожного елемента в списку population. Ці ваги визначають, наскільки ймовірно, що конкретний елемент буде обраний. Довжина списку weights має бути дорівнювати довжині списку population.
cum_weights - теж опціональний список кумулятивних ваг. Якщо він вказаний, то список weights ігнорується. Кумулятивна вага кожного елемента визначається як сума його ваги плюс ваги всіх попередніх елементів.
k: Кількість елементів для вибору. За замовчуванням k=1.
"""
import random
items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item)  

# Вибір декількох елементів з можливістю повторень:
import random
numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)

# Вибір з вагами:
import random
colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)  

# 7. метод random.sample(population, k). Якщо виникає необхідність вибрати N елементів зі списку і вони при цьому не повторювалися
# Створення випадкової команди з 4 учасників з групи з 10 осіб:
import random
participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

# 8. Метод random.uniform(a, b). Метод повертає випадкове дійсне число N, таке що a <= N <= b.
import random
price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")

""" ============================================================== """
    # Ключові аспекти: методи для роботи з випадковими величинами
""" ============================================================== """
"""
- random.randint(a, b): Отримання випадкового цілого числа з рівномірного розподілу в інтервалі між a та b включно.
- random.random(): Отримання випадкового числа в інтервалі між 0.0 (включно) та 1.0 (не включно).
- random.randrange(start, stop[, step]): Отримання випадкового числа з заданого діапазону, з можливістю вказати крок між значеннями.
- random.shuffle(x): Перемішування порядку елементів у списку x.
- random.choice(seq): Вибір випадкового елемента з послідовності seq (списку або кортежу).
- random.choices(population, weights=None, cum_weights=None, k=1): Генерація випадкової вибірки з можливістю зазначити ймовірності для кожного елемента та повторення у вибірці.
- random.sample(population, k): Отримання унікальних випадкових елементів зі списку population довжиною k.
- random.uniform(a, b): Отримання випадкового дійсного числа N такого, що a <= N <= b.
"""

""" -------------- """
    # Модуль math
""" -------------- """
"""
Пакет math у Python надає доступ до математичних функцій, визначених стандартом мови C. 
Цей пакет включає функції для різних математичних операцій, включаючи тригонометричні обчислення, логарифми, квадратний корінь та інше.

Розглянемо деякі з ключових функцій і констант, які надає цей пакет:

Константи:
- math.pi - константа π (приблизно 3.14159...);
- math.e - константа e, основа натуральних логарифмів (приблизно 2.71828...);
- math.tau - константа τ, дорівнює 2π (приблизно 6.28318...);
- math.inf - позначення нескінченності;
- math.nan - позначення 'Not a Number' (не число);

Функції округлення чисел:
- math.ceil(x) - виконує округлення дійсного числа x до найближчого більшого цілого числа;
- math.floor(x) - виконує округлення дійсного числа x до найближчого меншого цілого числа;
- math.trunc(x) - виконує обрізання дробової частини дійсного числа x, та повертає цілу частину числа;
"""
import math
x = 3.7 # Вихідне число

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)

"""
Тригонометричні функції:
+ math.sin(x) - синус x, де x в радіанах;
+ math.cos(x) - косинус x;
+ math.tan(x) - тангенс x;
+ math.asin(x) - арксинус x;
+ math.acos(x) - арккосинус x;
+ math.atan(x) - арктангенс x;

Експоненційні та логарифмічні функції:
+ math.exp(x) - число e в ступені x;
+ math.log(x[, base]) - Логарифм x за основою base. Якщо base не вказано, обчислюється натуральний логарифм;

Ступінь та корінь
+ math.pow(x, y) - x у ступені y;
+ math.sqrt(x) - квадратний корінь з x;

Деякі інші функції:
+ math.fabs(x) - модуль (абсолютне значення) x;
+ math.factorial(x) - факторіал числа x;
+ math.gcd(x, y) - найбільший спільний дільник для x та y;
"""
import math

# Використання констант
print(math.pi)  # Виведе приблизне значення π

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2
 
"""
 Якщо вам потрібна комплексна математика, то можна скористатися пакетом cmath. 
 Він надає той самий API, але вміє працювати з комплексними числами.
"""

""" ------------------------------------- """
    # Правильне порівняння дійсних чисел
""" ------------------------------------- """
"""
Дійсні числа в комп'ютерних програмах часто можуть викликати неточності через їхню бінарну природу. 
Це може призвести до несподіваної поведінки при порівнянні чисел. 
Розглянемо кілька прикладів та способи їх порівняння в Python.
"""
# Виконаємо наступне пряме порівняння
print(0.1 + 0.2 == 0.3)  # Це повертає False

# Функція math.isclose використовується для порівняння двох чисел з певною допустимою похибкою. 
# Це корисно для порівняння дійсних чисел, де пряме порівняння може бути ненадійним.
import math
r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True

# Також ми можемо виконувати порівняння з маленькою похибкою:
import math
r = math.isclose(0.1, 0.10000000009)
print(r)  # Це поверне True
