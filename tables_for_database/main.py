import psycopg2
import random
import string
from datetime import datetime, timedelta
from faker import Faker

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

num_of_nutrition = 20
num_of_body = 100
num_of_tendrils = 50
num_of_paws = 100
num_of_wings = 200
num_of_users = 100
num_of_status_type = 6

num_of_species_book = 10000

num_of_statuses = (1, 3)
num_of_butterflies = (5, 10)
num_of_photoes = (1, 5)
num_of_videos = (1, 2)

# Список кортежей с данными для вставки в nutrition
data_to_insert = [
    ("Iron", "Forest"),
    ("Calcium", "Meadow"),
    ("Copper", "River"),
    ("Zinc", "Mountain"),
    ("Magnesium", "Lake"),
    ("Potassium", "Desert"),
    ("Selenium", "Valley"),
    ("Phosphorus", "Ocean"),
    ("Sodium", "Field"),
    ("Chromium", "Canyon"),
    ("Manganese", "Pond"),
    ("Cobalt", "Savanna"),
    ("Nickel", "Tundra"),
    ("Boron", "Marsh"),
    ("Fluorine", "Plateau"),
    ("Iodine", "Glacier"),
    ("Vanadium", "Volcano"),
    ("Molybdenum", "Plain"),
    ("Lithium", "Steppe"),
    ("Silicon", "Hill")
]

# SQL-запрос для вставки данных
sql_query = "INSERT INTO nutrition (essential_trace_elements, favorite_places) VALUES (%s, %s)"
# Выполнение запроса с помощью метода executemany
cur.executemany(sql_query, data_to_insert)
print("nutrition finished")

# Заранее заданные массивы для цветов и орнаментов
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
ornaments = ["Stripes", "Polka Dots", "Checks", "Floral", "Plaid", "Geometric", "Abstract", "Tribal", "Animal Print", "Solid"]

# Генерация 100 неповторяющихся записей для body
data_to_insert = []
existing_combinations = set()  # Множество для отслеживания уже сгенерированных комбинаций
while len(data_to_insert) < num_of_body:
    color = random.choice(colors)
    ornament = random.choice(ornaments)
    combination = (color, ornament)
    # Проверка на уникальность комбинации
    if combination not in existing_combinations:
        data_to_insert.append(combination)
        existing_combinations.add(combination)

sql_query = "INSERT INTO body (color, ornament) VALUES (%s, %s)"
cur.executemany(sql_query, data_to_insert)

print("body finished")

# Заранее заданные массивы для цветов и особенностей
lengths = [5, 10, 15, 20, 25, 30]
colors = ["Red", "Brown", "Black", "White"]
features = ["Long", "Short", "White tips", "Straight", "Wavy", "Stripes", "Thick", "Thin", "Knotted", "Smooth"]

# Генерация 50 неповторяющихся записей для tendrils
data_to_insert = []
existing_combinations = set()  # Множество для отслеживания уже сгенерированных комбинаций
while len(data_to_insert) < num_of_tendrils:
    length = random.choice(lengths)
    color = random.choice(colors)
    feature = random.choice(features)
    combination = (length, color, feature)
    # Проверка на уникальность комбинации
    if combination not in existing_combinations:
        data_to_insert.append(combination)
        existing_combinations.add(combination)

sql_query = "INSERT INTO tendrils (len, color, features) VALUES (%s, %s, %s)"
cur.executemany(sql_query, data_to_insert)

print("tendrils finished")

# Заранее заданные массивы для длин и цветов лап
lengths = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]

# Генерация 100 неповторяющихся записей для paws
data_to_insert = []
existing_combinations = set()  # Множество для отслеживания уже сгенерированных комбинаций
while len(data_to_insert) < num_of_paws:
    length = random.choice(lengths)
    color = random.choice(colors)
    combination = (length, color)
    # Проверка на уникальность комбинации
    if combination not in existing_combinations:
        data_to_insert.append(combination)
        existing_combinations.add(combination)

sql_query = "INSERT INTO paws (len, color) VALUES (%s, %s)"
cur.executemany(sql_query, data_to_insert)

print("paws finished")

# Заранее заданные массивы для цветов, орнаментов, особенностей орнаментов и форм крыльев
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
ornaments = ["Stripes", "Polka Dots", "Checks", "Floral", "Plaid", "Geometric", "Abstract", "Tribal", "Animal Print", "Solid"]
ornament_features = ["Shiny", "Matte", "Textured", "Smooth", "Reflective", "Glittering", "Translucent", "Opaque", "Metallic", "Sparkling"]
shapes = ["Round", "Oval", "Triangular", "Diamond", "Spherical", "Irregular"]

# Генерация 200 неповторяющихся записей для wings
data_to_insert = []
existing_combinations = set()  # Множество для отслеживания уже сгенерированных комбинаций
while len(data_to_insert) < num_of_wings:
    color = random.choice(colors)
    ornament = random.choice(ornaments)
    ornament_feature = random.choice(ornament_features)
    shape = random.choice(shapes)
    wingspan = random.randint(1, 100)
    combination = (color, ornament, ornament_feature, shape, wingspan)
    # Проверка на уникальность комбинации
    if combination not in existing_combinations:
        data_to_insert.append(combination)
        existing_combinations.add(combination)

sql_query = "INSERT INTO wings (color, ornament, ornament_features, shape, wingspan) VALUES (%s, %s, %s, %s, %s)"
cur.executemany(sql_query, data_to_insert)

print("wings finished")

#таблица status type
"""
statuses = [
    "вероятно исчезнувшие",
    "находящиеся под угрозой исчезновения",
    "сокращающиеся в численности и/или распространении",
    "редкие",
    "не определенные по статусу",
    "восстанавливаемые и восстанавливающиеся"
]
"""
statuses = [
    "likely extinct",
    "endangered",
    "declining in population and/or distribution",
    "rare",
    "undetermined status",
    "recoverable and recovering"
]

data_to_insert = [(status,) for status in statuses]

sql_query = "INSERT INTO status_type (status_name) VALUES (%s)"
cur.executemany(sql_query, data_to_insert)

print("status type finished")

# Генерация случайной строки заданной длины
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Генерация 100 записей user_
fake = Faker()
additional_random_names = [fake.first_name() for _ in range(num_of_users+1)]

data_to_insert = []
for i in range(num_of_users):
    login = additional_random_names[i]
    password = generate_random_string(random.randint(20, 30))  # Генерация случайной строки для пароля
    name = login + generate_random_string(random.randint(1, 5))  # Генерация случайного имени
    data_to_insert.append((login, password, name))

sql_query = "INSERT INTO user_ (user_login, user_password, user_name) VALUES (%s, %s, %s)"
cur.executemany(sql_query, data_to_insert)

print("user finished")

data_to_insert = []
unique_combinations = set()
# species_book
while len(data_to_insert) < num_of_species_book:
    wings_id = random.randint(1, 200)
    paws_id = random.randint(1, 100)
    tendrils_id = random.randint(1, 50)
    body_id = random.randint(1, 100)
    nutrition_id = random.randint(1, 20)
    life_expectancy = random.randint(10, 150)
    species_name = f"name {len(data_to_insert) + 1}"
    combination = (wings_id, paws_id, tendrils_id, body_id, nutrition_id)

    # Проверка уникальности комбинации
    if combination not in unique_combinations:
        unique_combinations.add(combination)
        data_to_insert.append((species_name, wings_id, paws_id, tendrils_id, body_id, nutrition_id, life_expectancy))

sql_query = "INSERT INTO species_book (species_name, wings_id, paws_id, tendrils_id, body_id, nutrition_id, life_expectancy)\
 VALUES (%s, %s, %s, %s, %s, %s, %s)"
cur.executemany(sql_query, data_to_insert)

print("species book finished")

# Генерация случайной даты в определенном диапазоне
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

data_to_insert = []  # status

for i in range(1, num_of_species_book + 1):
    num_of_statuses_for_species = random.randint(num_of_statuses[0], num_of_statuses[1])
    species_id = i
    for _ in range(num_of_statuses_for_species):
        status_type = random.randint(1, 6)

        start_date = datetime(1950, 1, 1)  # Начальная дата
        end_date = datetime(2024, 12, 31)  # Конечная дата

        assignment_date = random_date(start_date, end_date)  # Пример даты назначения статуса
        if random.randint(-1, 50) > 0:
            cancellation_date = random_date(assignment_date, end_date)   # Пример даты отмены статуса
            cancellation_date_str = cancellation_date.strftime("%d-%m-%Y")
        else:
            cancellation_date_str = "-"

        assignment_date_str = assignment_date.strftime("%d-%m-%Y")

        data_to_insert.append((status_type, assignment_date_str, cancellation_date_str, species_id))

# SQL-запрос для вставки данных
sql_query = "INSERT INTO status (status_type, assignment_date, cancellation_date, species_id) VALUES (%s, %s, %s, %s)"

# Вставка данных в таблицу
cur.executemany(sql_query, data_to_insert)

print("status finished")

#butterfly
def generate_random_coordinates():
    degrees_lat = random.uniform(-90, 90)  # Генерация случайной широты от -90 до 90
    degrees_lon = random.uniform(-180, 180)  # Генерация случайной долготы от -180 до 180

    direction_lat = "N" if degrees_lat >= 0 else "S"  # Определение направления широты
    direction_lon = "E" if degrees_lon >= 0 else "W"  # Определение направления долготы

    # Форматирование координат в требуемый формат
    coordinates = "{:.4f}°{} {:.4f}°{}".format(abs(degrees_lat), direction_lat, abs(degrees_lon), direction_lon)

    return coordinates

data_to_insert_butterfly = []
num_of_butterflies_in_tab = 0
for i in range(1, num_of_species_book + 1):
    num_of_butterflies_for_species = random.randint(num_of_butterflies[0], num_of_butterflies[1])
    species_id = i
    for _ in range(num_of_butterflies_for_species):
        author_id = random.randint(1, num_of_users)
        coordinates = generate_random_coordinates()
        data = random_date(datetime(2008, 1, 1), datetime(2024, 12, 31))
        data = data.strftime("%d-%m-%Y")

        data_to_insert_butterfly.append((author_id, species_id, coordinates, data))
        num_of_butterflies_in_tab += 1

# SQL-запрос для вставки данных
sql_query_butterfly = "INSERT INTO butterfly (author_id, species_id, coordinates, data) VALUES (%s, %s, %s, %s)"

# Вставка данных в таблицу
cur.executemany(sql_query_butterfly, data_to_insert_butterfly)

print("butterfly finished")

#photo
data_to_insert = []
photo_num = 1
for i in range(1, num_of_butterflies_in_tab + 1):
    num_of_photoes_for_butterfly = random.randint(num_of_photoes[0], num_of_photoes[1])
    butterfly_id = i
    for j in range(num_of_photoes_for_butterfly):
        photo = f"photo {photo_num}"
        data_to_insert.append((butterfly_id, photo))
        photo_num+=1

# SQL-запрос для вставки данных
sql_query_butterfly = "INSERT INTO photo (butterfly_id, photo) VALUES (%s, %s)"

# Вставка данных в таблицу
cur.executemany(sql_query_butterfly, data_to_insert)

print("photo finished")

#video
data_to_insert = []
video_num = 1
for i in range(1, num_of_butterflies_in_tab + 1):
    num_of_videos_for_butterfly = random.randint(num_of_videos[0], num_of_videos[1])
    butterfly_id = i
    for j in range(num_of_videos_for_butterfly):
        video = f"video {video_num}"
        data_to_insert.append((butterfly_id, video))
        video_num+=1

# SQL-запрос для вставки данных
sql_query_butterfly = "INSERT INTO video (butterfly_id, video) VALUES (%s, %s)"

# Вставка данных в таблицу
cur.executemany(sql_query_butterfly, data_to_insert)

print("video finished")

# Фиксация изменений
conn.commit()
cur.close()
conn.close()