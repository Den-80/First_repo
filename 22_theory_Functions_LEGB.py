""" -------------------- """
    #Робота з функціями
""" -------------------- """
"""
Функція оголошується за допомогою ключового слова def. 
Після ключового слова вказується ім'я функції, за яким йде пара дужок (), 
у яких можна вказати імена деяких змінних, та двокрапка : в кінці рядка. 
Далі слідує блок команд, що складають функцію.
"""
def say_hello():
		# тіло функції
    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()


""" === Аргументи функції ==="""
"""
Параметри функції – це деякі вхідні дані, які ми можемо передати функції, щоб отримати результат, що відповідає цим даним.
Функції можуть приймати параметри, тобто деякі значення, що передаються в середину функції для того, щоб вона щось зробила з ними. 
Ці параметри схожі на змінні, за виключенням того, що значення цих змінних вказуються при виклику функції, та під час роботи функції їм вже присвоєні їх значення.

Параметри вказуються в дужках при оголошенні функції та розділяються комами. 
Аналогічно ми передаємо значення, коли викликаємо функцію.

Зверніть увагу на термінологію: імена, вказані при оголошенні функції, називаються параметрами, 
тоді як значення, які ви передаєте у функцію при її виклику, – аргументами.
"""
def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

""" === Типізація параметрів функції === """
"""
В Python, починаючи з версії 3.5, ви можете використовувати "type hints" (підказки типів) для вказівки очікуваних типів параметрів. 
Це дозволяє коду бути більш зрозумілим та може допомогти у виявленні можливих помилок.
Попередню функцію ми можемо записати тепер наступним чином:
"""
def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

""" === Повернення результату === """
"""
У Python немає синтаксичної різниці між функціями і процедурами. 
По суті, функція вміє повертати деякий результат своєї роботи, а процедура нічого не повертає та результатом її роботи може бути зміна стану вже існуючих змінних. 
Така форма використання функцій максимально наближена до функцій, з якими ми знайомі з уроків математики.

Повернення результату з функції в Python виконується за допомогою оператора return. 
Цей оператор завершує виконання функції та "повертає" значення, яке може бути використане в інших частинах програми. 
Це особливо корисно для отримання результатів обчислень, обробки даних та інших операцій. 
В Python ви можете явно вказати тип даних, який повертається функцією, використовуючи анотації типів.

Базовий синтаксис для повернення значення з функції виглядає наступним чином:
"""
def my_function() -> ReturnType:
    # виконати дії
    return result
"""
ReturnType вказує на тип даних, який функція має повертати. 
Це може бути будь-який тип даних, як-от int, float, str, list, dict, 
або навіть складніші типи, включаючи класи та інтерфейси, що ми побачимо згодом в курсі. 
Для повернення значення з функції необхідно вказати, що повернути після ключового слова return. 
Тому result - це значення або змінна, яку функція повертає.
"""
#Розглянемо приклад функції, яка сумує два числа та повертає результат:
def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum

result = add_numbers(5, 10)
print(result)  # Виведе: 15

#Приклад функції, що повертає рядок:
def greet(name: str) -> str:
    return f"Привіт, {name}!"

greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!

#Функція, що повертає булеве значення:
def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)  # Виведе: True

""" === Принципи змінності об'єктів у Python === """

"""
У Python всі об'єкти передаються за посиланням, 
але важливо розуміти різницю між змінними (mutable) та незмінними (immutable) типами даних, 
адже від цього залежить, як відбувається передача об'єктів та які помилки можуть виникати.

Незмінні типи в Python — це ті, що не можуть бути змінені після їх створення. 
Це включає типи, як-от цілі числа int, дійсні числа float, рядки str, кортежі tuple.

Коли незмінний об'єкт передається у функцію, фактично передається його копія, 
і будь-які зміни цього об'єкту в функції не впливають на оригінальний об'єкт.
"""
def modify_string(original: str) -> str:
    original = "змінено"
    return original

str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал

# У цьому прикладі, навіть після зміни рядка в функції modify_string, оригінальна змінна str_var залишається незмінною.

"""
Змінні типи, як списки [list], словники {dict}, множини (set), можуть змінюватися. 
Коли змінний об'єкт передається у функцію, передається посилання на цей об'єкт, і зміни, зроблені всередині функції, відображаються на оригінальному об'єкті.
"""
def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]

"""
При "копіюванні" змінного об'єкта шляхом простого присвоєння new_list = old_list ви копіюєте посилання, а не сам об'єкт.
Це означає, що зміни в одному списку відображатимуться й у іншому. 
Фактично в середині функції modify_list відбулося присвоювання lst = my_list
"""
# Використовуйте метод copy() для створення копій змінних об'єктів, якщо не хочете змінювати оригінал.
def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]
# Тут список my_list після виконання функції modify_list вже не зазнає змін.

""" === Задача на функцію === """
"""
Для закріплення отриманих знань, розглянемо наступний приклад. 
Уявімо, що перед нами стоїть задача: конвертувати кожен символ у рядку в його відповідний код ASCII. 
Це класична задача, що демонструє взаємодію з рядками в Python та їх обробку.
"""
def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes
"""----------------------------------------------------------------------------------------------------"""

""" ------------------------- """
    #Області видимості (LEGB)
""" ------------------------- """
"""
Область видимості — це область у програмі (коді), в межах якої ви можете звернутися за ім'ям до вмісту змінної. 
Ці області видимості діляться на чотири рівні в порядку пошуку імен змінних, та відомі як LEGB-правило:

L - Local (Локальна): Це внутрішній рівень, де ім'я визначено всередині функції або блоку коду.
E - Enclosing (Охоплювана): Це область видимості, яка охоплює локальну область видимості. Якщо функція знаходиться всередині іншої функції, імена, визначені в охоплюваній функції, будуть доступні для внутрішньої функції.
G - Global (Глобальна): Це область видимості на рівні модуля або сценарію. Змінні, визначені на цьому рівні, доступні у всьому модулі.
B - Built-in (Вбудована): Це самий зовнішній рівень, який містить імена, вбудовані в Python. Наприклад розглянуті нами вбудовані функції, len, range тощо.
"""

""" --- Local --- """
"""
У Python кожна змінна, оголошена всередині функції, є локальною для цієї функції. 
Це означає, що локальні змінні існують лише в межах блоку коду, де вони були оголошені, і не доступні за його межами.
"""
x = 50

def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('Глобальний x як і раніше', x)  # x як і раніше 50

""" --- Enclosing --- """
"""
Охоплювана (Enclosing) область видимості виникає, коли функція визначена всередині іншої функції. 
Змінні в функції, що охоплює доступні у внутрішній (вкладеній) функції, але не навпаки. 
Це означає, що внутрішня функція може читати але не змінювати змінні, визначені в функції, що її охоплює.

Тут enclosing_var є змінною в функції outer_func, що охоплює функцію inner_func. 
Вона доступна для читання в вкладеній функції inner_func, але не може бути змінена в inner_func без використання ключового слова nonlocal.
"""
def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()

outer_func()

"""
Для того, щоб розібратися як змінювати змінні в функції, що охоплює внутрішню функцію, розглянемо приклад:
"""
def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x

result = func_outer()  # 5
"""
Коли ми перебуваємо всередині функції func_inner, змінна x, визначена у першому рядку функції func_outer,
знаходиться в enclosing області видимості для неї. 
Якщо ми захочемо використати саме цю змінну x, ми повинні оголосити її nonlocal x всередині функції func_inner. 
Це означає, що змінна x, яку вона буде змінювати, є не локальною для func_inner, а знаходиться на більш високому рівні — в нашому випадку, в func_outer. 
Тому, коли func_inner змінює x на 5, ця зміна відображається на x в func_outer.
"""

""" --- Global --- """
"""
Для того, щоб змінити глобальну змінну всередині функції, необхідно використовувати ключове слово global. 
Це вказує Python, що змінна не є локальною, а належить до глобальної області видимості. 
Без застосування зарезервованого слова global неможливо присвоїти значення змінній, визначеній за межами функції.

Зарезервоване слово global використовується для того, щоб оголосити, що x – це глобальна змінна, 
а значить, коли ми присвоюємо значення імені x всередині функції, ця зміна відобразиться на значенні змінної x в основному блоку програми. 
Використовуючи одне зарезервоване слово global, можна оголосити відразу декілька змінних: global x, y, z.

Використовувати global варто з великою обережністю і не потрібно зловживати такою можливістю.
"""
x = 50

def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)# Значення x складає 2

""" --- Ключові аргументи функції --- """
"""
Якщо є деяка функція з великою кількістю параметрів, і при її виклику вимагається вказати тільки деякі з них, 
значення цих параметрів можуть задаватися за їх ім'ям. Це називається !!!ключовими параметрами!!!.

Ключові аргументи в функціях Python — це спосіб передачі аргументів функції, при якому кожному аргументу присвоюється ім'я. 
Це дозволяє вказувати аргументи у будь-якому порядку під час виклику функції, не дотримуючись порядку, визначеного у її оголошенні. 
Ключові аргументи роблять код більш читабельним та дозволяють використовувати значення за замовчуванням для деяких аргументів.
"""
#Визначимо функцію з ключовими аргументами
def greet(name, message="Привіт"):
    print(f"{message}, {name}!")
"""
У цьому прикладі name — це позиційний параметр, а message — ключовий параметр зі значенням за замовчуванням "Привіт". 
При виклику функції можна не вказувати message, і тоді буде використано значення за замовчуванням.
"""
# використовує значення за замовчуванням для message
greet("Олексій")  

# передача власного значення для message
greet("Марія", message="Добрий день")  

""" Розглянемо наступний приклад для демонстрації гнучкості ключових аргументів, та можливості змінювати порядок аргументів або використовувати значення за замовчуванням."""
def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)

""" Функція з ім'ям say використовується для виведення на екран рядка, вказаного число разів. """
def say(message, times=1):
    print(message * times)

say('Привіт') 
say('Світ', 5)

"""
Значеннями за замовчуванням можуть бути забезпечені тільки параметри, що знаходяться у кінці списку параметрів. 
Таким чином, у списку параметрів функції параметр зі значенням за замовчуванням не може передувати параметру без значення за замовчуванням. 
Це пов'язано з тим, що значення надаються параметрам відповідно до їх положення. 
Наприклад, def func(a, b=5) — допустимо, а def func(a=5, b) – не допустимо та призведе до помилки в коді.
"""

"""
Розглянемо типову задачу, яка відображає реальну ситуацію в області торгівлі та фінансів, де потрібно часто обраховувати ціни зі знижками. 
Нам необхідно створити функцію для розрахунку вартості товарів з урахуванням можливої знижки.

Для розрахунку реальної ціни з врахуванням дисконту створимо функцію real_cost. 
Функція real_cost повинна приймати два аргументи: базову ціну товару base та розмір знижки discount, який за замовчуванням будемо вважати 0. 
Вона повинна повертати вартість товару після застосування знижки.

Функція використовує формулу base * (1 - discount) для обрахунку остаточної вартості. 
Якщо знижка відсутня, то використовується лише базова ціна.
Ціна на хліб price_bread завжди без знижки і вона не застосовується, тому при визові функції real_cost використовується лише базова ціна. 
Для масла price_butter та цукру price_sugar застосовуємо знижки 5% та 7% відповідно.
"""
def real_cost(base: int, discount: int = 0) -> int:
    return base * (1 - discount)

price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f'Нова вартість хліба: {current_price_bread}')
print(f'Нова вартість масла: {current_price_butter}')
print(f'Нова вартість цукру: {current_price_sugar}')

"""----------------------------------------------------------------------------------------------------"""

""" ----------------------------- """
    #Змінна кількість параметрів
""" ----------------------------- """
"""
Змінна кількість параметрів у функції в Python дозволяє функції приймати нефіксовану кількість аргументів. 
Це корисно у ситуаціях, коли ви хочете дозволити передавати різну кількість параметрів у свою функцію.

У Python існує два способи реалізації змінної кількості параметрів.

1. Параметр *args. Він дозволяє функції приймати довільну кількість позиційних аргументів. Аргументи, передані функції, зберігаються у вигляді кортежу.
2. Параметр **kwargs. Він дозволяє функції приймати довільну кількість ключових аргументів. Але аргументи, передані функції, зберігаються вже у вигляді словника.