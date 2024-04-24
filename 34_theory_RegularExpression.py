""" ------------------- """
    # Регулярні вирази
""" ------------------- """
"""
Регулярні вирази (regular expressions, часто скорочують як regex або regexp) - це потужний інструмент для роботи з текстом, 
який дозволяє шукати, замінювати або витягувати певні шаблони в тексті за допомогою спеціального синтаксису. 
Регулярні вирази широко використовуються в програмуванні, обробці тексту, а також у різних програмах та інструментах для роботи з даними.

Основні компоненти регулярних виразів включають:

1. Літерали. Пряме відображення символів (наприклад, a, B, 1).
2. Метасимволи. Символи, які мають спеціальне значення в регулярних виразах (наприклад, . (крапка) відповідає будь-якому символу).
3. Квантифікатори. Визначають, скільки разів елемент повинен відповідати (наприклад * означає 0 або більше повторень).
4. Класи символів. Визначають групи символів (наприклад, [a-z] відповідає будь-якій малій літері).
5. Групи та діапазони. Використовуються для групування частин виразу (наприклад, (abc) визначає групу символів).
6. Альтернації. Відповідає одному з декількох шаблонів (наприклад, a|b відповідає a або b).
7. Якорі. Визначають позиції у тексті (наприклад, ^ для початку рядка, $ для кінця рядка).

Регулярні вирази дозволяють шукати певні шаблони в рядках, виконувати заміни, розбивати рядки на частини і багато іншого. 
Для роботи з регулярними виразами в Python використовується модуль re.

Основні функції модуля re які ми розглянемо далі це:
1. re.search(pattern, string) - виконує пошук першого входження шаблону в рядку.
2. re.findall(pattern, string) - виконує знаходження всіх входжень шаблону в рядку.
3. re.sub(pattern, repl, string) - виконує заміну входжень шаблону на інший рядок.
4. re.split(pattern, string) виконує розбивання рядка за шаблоном.

Регулярний вираз або коротко "регулярка" складається зі звичайних символів і спеціальних командних послідовностей. 
Наприклад, \d задає будь-яку цифру, а \d+ — задає будь-яку послідовність з однієї або більше цифр. 
Це називається шаблони регулярних виразів.

Регулярні вирази використовують спеціальні символи для створення шаблонів. Вони складаються з блоків та модифікаторів.
Прикладом блоку може бути:
\w — будь-яка цифра або буква [a-zA-Z0-9_] (\W — все, крім букви або цифри [^a-za-z0-9_])
\d — будь-яка цифра [0-9] (\D — усе, крім цифри [^0-9])
\s — будь-який пробільний символ [\t\n\r\f\v] (\S — усе, крім пробільних символів [^\t\n\r\f\v])
\b — межа слова
[...] — один із символів у дужках ([^ ] — будь-який символ, крім тих, що в дужках)
^ і $ — початок і кінець рядка відповідно
( ) — групує вираз і повертає знайдений текст
\t, \n, \r — символ табуляції, нового рядка та повернення каретки

Модифікатори можуть вказувати на кількість повторень блоку у виразі, наприклад:
. — один будь-який символ, крім рядка \n
? — 0 або 1 входження шаблону зліва
+ — 1 і більше входжень шаблону зліва
* — 0 і більше входжень шаблону зліва
\ — екранування спец.символів (приклад: \. — означає крапку або \+ — знак "плюс")
{n} суворо n разів (n ціле число)
{n,m} — від n до m входжень (приклад: {,m} — від 0 до m)
a|b — відповідає a або b. Сам символ | означає "або" між двома шаблонами
( ) — групує вираз і повертає знайдений текст
"""
import re

# Метод search() - Пошук першого входження шаблону в рядку.
"""
Регулярний вираз - це шаблон, який використовується для знаходження певних комбінацій символів у рядках.

Синтаксис:
re.search(pattern, string)

pattern: Регулярний вираз (шаблон), який ви хочете знайти.
string: Рядок, у якому ви хочете знайти шаблон.

Результат виконання re.search() це спеціальний об'єкт Match, якщо знаходить відповідність. 
Якщо відповідність не знайдена, повертає None.

Об'єкт Match має властивості та методи, що використовуються для отримання інформації про пошук та результат:

Match.span() повертає кортеж, що містить початкову та кінцеву позиції збігу.
Match.string повертає рядок, переданий у функцію,
Match.group() повертає частину рядка, в якому був збіг

Ви можете використати метод .group() у цьому об'єкті, щоб отримати відповідну частину рядка.
"""
import re

text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")

# Тепер використаємо метасимволи, та виконаємо пошук слова, що починається на "в" та закінчується на "м".
import re

text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())
"""
Тут змінна pattern зберігає регулярний вираз r"в\w*м":

r означає "сирий" рядок (raw string), який каже Python ігнорувати спеціальні символи такі як \n, \t тощо, оскільки це рядок для регулярних виразів.
в - шукаємо слово яке починається на букву "в".
\w* - це означає будь-яка кількість букв включно з нулем букв. Бо \w відповідає будь-якому "словесному" символу, а * є квантифікатором, який означає "нуль або більше входжень попереднього елемента".
м - шукаємо слово яке закінчується на "м".

В функцію search ми передаємо параметр re.IGNORECASE, який робить пошук нечутливим до регістру. 
А отже слово може бути як з великих так і малих літер.
"""

# Розглянемо простеньку задачу - знаходження електронної адреси в рядку.
import re

text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())

# Припустимо, у нас є рядок з електронною адресою, і ми хочемо вилучити ім'я користувача та домен цієї електронної адреси окремо. 
# Треба розділити "username@domain.com" на "username" (ім'я користувача) та "domain.com" (домен).
import re

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)
""" ------------------------------------- """

# Метод findall() - знаходження всіх входжень шаблону, заданого регулярним виразом, у заданому рядку.
"""
Синтаксис методу:

matches = re.findall(pattern, string)

- pattern - регулярний вираз, який ви шукаєте.
- string - рядок, у якому потрібно знайти відповідності.

Метод повертає список всіх знайдених відповідностей. Якщо відповідностей не знайдено, повертається пустий список.
"""
# Необхідно знайти всі числа у рядку. Для цього нам знадобиться використання блоку \d, щоб знайти всі цифри в тексті.
import re

text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches) # ['2023', '2022']
""" -------------------------------------- """

# Метод sub() - икористовується для заміни входжень регулярного виразу pattern в рядку string на рядок repl. 
"""
Це дуже корисно для модифікації тексту.

Синтаксис:
modified_string = re.sub(pattern, repl, string)

- pattern - регулярний вираз, який вказує на частину рядка, яку потрібно замінити.
- repl - рядок, на який буде замінено збіги.
- string - рядок, в якому відбувається заміна.

Метод повертає рядок, у якому всі входження pattern замінені на repl.
"""

"""
Розглянемо приклад. 
У нас є назва файлу з пробілами, наприклад, "Мій документ Python.txt". 
Нам потрібно перетворити цю назву так, щоб замість пробілів були підкреслення, отримуючи "Мій_документ_Python.txt". 
І в майбутньому це прийдеться робить багато разів і нам хочеться автоматизувати цей процес.
"""
import re

file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)  # Мій_документ_Python.txt

# Видалимо всі пунктуаційні знаки з рядка.
import re

text = "Python - потужна, універсальна; мова!"
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)

print(modified_text)  # Python  потужна універсальна мова

# Розглянемо, ще один корисний приклад - форматування телефонних номерів. 
# Нам необхідно змінити формат телефонних номерів. 
# В тексті в нас телефони записані в такому форматі 050-171-1634, нам необхідно замінити їх на формат (050) 171-1634
import re

phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)
""" ------------------------------------------------ """

# Метод split() - використовується для розбивання рядка за заданим регулярним виразом. 
"""
Це дозволяє розділяти текст на частини за складнішими критеріями, ніж простий рядковий метод split().

Синтаксис:

list_of_elements = re.split(pattern, string)

- pattern - регулярний вираз, який використовується як роздільник.
- string - рядок, який потрібно розділити.

Метод повертає список рядків, розділених за заданим регулярним виразом.
"""
# Почнемо з простого, та розділимо рядок на слова, використовуючи пробіли як роздільники.
import re

text = "Python - це проста, але потужна мова програмування."
pattern = r"\s+"
words = re.split(pattern, text)

print(words)  # Виведе список слів у рядку ['Python', '-', 'це', 'проста,', 'але', 'потужна', 'мова', 'програмування.']

# Спробуємо розділити рядок на частини, використовуючи пунктуаційні знаки як роздільники.
import re

text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)  # Виведе список частин, розділених пунктуацією ['Python', 'потужна', 'проста', 'універсальна', 'мова', '']
"""
Останній пустий елемент, кінець рядка, можна видалити зрізами elements[:-1:], якщо є бажання. 
Чому він виник? 
Коли ви використовуєте re.split() для розділення рядка, 
функція шукає входження шаблону (роздільника) і розбиває рядок кожного разу, коли знаходить цей шаблон. 
Якщо шаблон присутній на кінці рядка, а в нас в кінці рядка знак оклику !, 
re.split() розділить рядок після цього шаблону, що призводить до створення додаткового пустого рядка.
"""

# Виконаємо, ще один розділ рядка за шаблоном, що містить кілька можливих роздільників. Зауважимо, що звичайний метод split() таке вже зробити не зможе.
import re

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(fruits) # ['apple', 'banana', 'mango', 'orange', 'kiwi']
""" ------------------------------------------------------------ """

""" ============================================= """
    # Ключові аспекти: основні функції модуля re
""" ============================================= """
"""
Регулярні вирази в Python - потужний інструмент для пошуку, заміни та маніпуляції текстовою інформацією. 
Вони дозволяють виконувати складні операції над рядками за допомогою досить лаконічного синтаксису. 
Основні функції модуля re, які ми розглянули:

re.search(pattern, string) - використовується для пошуку першого входження шаблону в рядку. Повертає об'єкт Match, якщо відповідність знайдена.
re.findall(pattern, string) - знаходить всі входження шаблону в рядку. Повертає список всіх знайдених відповідностей.
re.sub(pattern, repl, string) - замінює всі входження шаблону в рядку на інший рядок. Використовується для модифікації та форматування тексту.
re.split(pattern, string) - розбиває рядок за заданим шаблоном. Повертає список рядків, отриманих після розділення.

Використання регулярних виразів вимагає розуміння їхнього синтаксису та особливостей. 
Спеціальні символи, такі як *, +, ?, квадратні та круглі дужки, мають конкретні функції у регулярних виразах. 
Розуміння цих елементів дозволяє виконувати складні операції пошуку та редагування з текстом.

Коректне застосування регулярних виразів може значно спростити обробку тексту, автоматизацію задач та вирішення складних проблем обробки даних.
"""
