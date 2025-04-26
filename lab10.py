import psycopg2
import csv

# 连接到数据库
conn = psycopg2.connect(
    database="phonebook1",
    user="postgres",
    password="112233",  # ⚠️ 用你的真实数据库密码
    host="localhost",
    port="5432"
)
conn.autocommit = True
cur = conn.cursor()

# 创建表
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook1 (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
        )
    """)
    print("✅ Кесте құрылды немесе бар кесте тексерілді.")

# 控制台插入数据
def insert_from_console():
    username = input("👤 Атыңды енгіз: ")
    phone = input("📞 Телефон номеріңді енгіз: ")
    cur.execute("INSERT INTO phonebook1 (username, phone_number) VALUES (%s, %s)", (username, phone))
    print("✅ Жаңа жазба енгізілді.")
    print_all()

# CSV 文件插入
def insert_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook1 (username, phone_number) VALUES (%s, %s)", (row[0], row[1]))
    print("✅ CSV файлынан деректер енгізілді.")
    print_all()

# 显示所有数据
def print_all():
    cur.execute("SELECT user_id, username, phone_number FROM phonebook1")
    rows = cur.fetchall()
    print("\n📄 Барлық жазбалар:")
    for row in rows:
        print(row)

# 更新数据
def update_data():
    user_id = input("Өзгерткің келетін user_id енгіз: ")
    new_username = input("Жаңа аты (қалдыр бос болса, өзгермейді): ")
    new_phone = input("Жаңа телефон нөмірі (қалдыр бос болса, өзгермейді): ")
    if new_username:
        cur.execute("UPDATE phonebook1 SET username = %s WHERE user_id = %s", (new_username, user_id))
    if new_phone:
        cur.execute("UPDATE phonebook1 SET phone_number = %s WHERE user_id = %s", (new_phone, user_id))
    print("✅ Жазба жаңартылды.")
    print_all()

# 删除数据
def delete_data():
    target = input("Аты немесе телефон нөмірін енгіз (жою үшін): ")
    cur.execute("DELETE FROM phonebook1 WHERE username = %s OR phone_number = %s", (target, target))
    print("🗑️ Жазба жойылды.")
    print_all()

# 查询手机号以 9 немесе 5 басталатындар
def filter_phone():
    cur.execute("SELECT * FROM phonebook1 WHERE phone_number LIKE '9%%' OR phone_number LIKE '5%%'")
    rows = cur.fetchall()
    print("\n📱 Телефон нөмірі 9 немесе 5 басталатындар:")
    for row in rows:
        print(row)

# 主菜单
def menu():
    create_table()
    while True:
        print("""
====================
📱 PHONEBOOK МӘЗІР:
1 - Консоль арқылы енгізу
2 - CSV файлынан енгізу
3 - Барлығын шығару
4 - Жаңарту (Update)
5 - Жою (Delete)
6 - 9/5 басталатын телефондарды көру
0 - Шығу
====================
        """)
        choice = input("Команданы таңда: ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            csv_path = input("CSV файлының жолын енгіз: ")
            insert_from_csv(csv_path)
        elif choice == '3':
            print_all()
        elif choice == '4':
            update_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            filter_phone()
        elif choice == '0':
            print("🚪 Бағдарламадан шығу...")
            break
        else:
            print("❗ Қате таңдау. Қайтадан көр.")

    cur.close()
    conn.close()

menu()
