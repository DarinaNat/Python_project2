import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS fragrances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    img TEXT NOT NULL,
    categoria  TEXT NOT NULL,
    ingradients TEXT NOT NULL,
    price INTEGER NOT NULL
)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS basket_fragrances (
id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    img TEXT NOT NULL,
    categoria  TEXT NOT NULL,
    ingradients TEXT NOT NULL,
    price INTEGER NOT NULL
)''')

conn.commit()
conn.close()


def select_price_min():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    products = cur.execute('''SELECT * FROM fragrances ORDER BY price ASC''').fetchall()
    conn.close()
    return products

def select_price_max():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    products = cur.execute('''SELECT * FROM fragrances ORDER BY price DESC''').fetchall()
    conn.close()
    return products

print(select_price_max())
def select_categoria(categoria_p):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    products = cur.execute('''SELECT * FROM fragrances WHERE name=?''',
                           (categoria_p,)).fetchall()
    conn.close()
    return products

def select_ingradients(ingradients_p):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    products = cur.execute('''SELECT * FROM fragrances  WHERE INSTR(ingradients, ?) > 0''',
                           (ingradients_p,)).fetchall()
    conn.close()
    print(products)
    return products

def select_name(name_p):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    name_p = name_p.lower()
    products = cur.execute('''SELECT * FROM fragrances WHERE LOWER(img) LIKE ?'''
                           , (f'%{name_p}%',)).fetchall()
    conn.close()
    return products

def select_product(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    product = cur.execute('''SELECT * FROM fragrances WHERE id=?''', (id,)).fetchone()
    conn.close()
    return product
def add_product_basket(name,description,img,categoria,ingradients,price):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO basket_fragrances (name,description,img,categoria,ingradients,price)
                VALUES (?,?,?,?,?,?)''', (name,description,img,categoria,ingradients,price))
    conn.commit()
    conn.close()

def select_price(min,max):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    products = cur.execute('''SELECT * FROM fragrances WHERE price BETWEEN ? AND ? ORDER BY price ASC;''',(min,max)).fetchall()
    conn.close()
    return products
def select_all_basket():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    products = cur.execute('''SELECT * FROM basket_fragrances ''').fetchall()
    conn.close()
    return products

def delete_product_basket(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''DELETE FROM basket_fragrances WHERE id=?''',(id,))
    conn.commit()
    conn.close()

def add_product(name,description,img,categoria,ingradients,price):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO fragrances (name,description,img,categoria,ingradients,price) VALUES (?,?,?,?,?,?) ''',
                (name,description,img,categoria,ingradients,price))
    conn.commit()
    conn.close()

def select_all():
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        perfumes = cur.execute('''SELECT * FROM fragrances ''').fetchall()
        conn.close()
        return perfumes

#
# add_product('Природа',
#             'forest_cold.jpeg',
#             'Лісова прохолода',
#             'Аромат для шанувальників природи з нотками моху, свіжої хвої, кори дерев і краплі ранкової роси.',
#             'мох, хвоя, деревна кора, ранкова роса',
#             1000)

#add_product('Квіти',
#             'flower_sunset.jpeg',
#             'Квітковий захід',
#             'Романтичний та елегантний аромат, як багатий букет з півонії, жасмину, фрезії з легким теплом амбри.',
#             'півонія, жасмин, фрезія, амбра',
#             1200)
#
#add_product('Природа',
#             'city_wind.jpeg',
#             'Міський вітер',
#             'Для енергійних жителів мегаполісу з цитрусовими нотами, м’ятою, кедром і легкий дотиком бензину для образу великого міста.',
#            'цитрусові, м’ята, кедр, бензин',
#             1150)
#
#add_product('Фрукти|Ягоди',
#             'tea.jpeg',
#             'Чайна церемонія',
#             'Спокій та гармонія в кожній ноті бо додані делікатні нотки зеленого чаю, жасмину, бамбука і легкий аромат рисового паперу.',
#             'зелений чай, жасмин, бамбук, рисовий папір',
#            950)
#
#add_product('Фрукти|Ягоди',
#             'grape_night.jpeg',
#             'Виноградна ніч',
#             'Чуттєвий вечірній аромат з солодкими виноградними нотами з вкрапленнями бергамоту, чорної смородини і дубового моху.',
#             'виноград, бергамот, чорна смородина, дубовий мох',
#            1300)
#
#add_product('Природа',
#            'morning_meadow.jpeg',
#             'Ранковий луг',
#             'Весняний аромат для легкості та свіжості з конюшиною, трояндою, ромашкою і крапелькою меду для нот весняного лугу.',
#             'конюшина, троянда, ромашка, мед',
#             1100)
#
#add_product('Фрукти|Ягоди',
#             'northern_berry.jpeg',
#             'Північна ягода',
#             'Свіжий і соковитий аромат з нотками м’яти як ягідний мікс з чорниці, журавлини і кедра, з легким акордом м’яти.',
#             'чорниця, журавлина, кедр, м’ята',
#             1250)
#
#add_product('Квіти',
#             'night_orchid.jpeg',
#             'Нічна орхідея',
#             'Аромат для особливих вечорів з чуттєвими акордими орхідеї, іланг-ілангу, темного дерева і трохи ладану.',
#             'орхідея, іланг-іланг, темне дерево, ладан',
#            1450)
#
#add_product('Осінь',
#             'caramel_latte.jpeg',
#             'Карамельний латте',
#             'Теплий і солодкий аромат для затишку з солодкими нотками карамелі, кавових зерен, мигдалевого молока і ванілі.',
#             'карамель, кавові зерна, мигдалеве молоко, ваніль',
#             1350)
#
#add_product('Квіти',
#             'garden_dream.jpeg',
#             'Сад мрій',
#             'Мрійливий і романтичний аромат, як багатий квітковий букет з лаванди, троянди, ірису і нотою меду.',
#             'лаванда, троянда, ірис, мед',
#             1400)
#
#add_product('Природа',
#             'ancient_city.jpeg',
#            'Сторовинне місто',
#            'Теплий і загадковий аромат з деревними нотками сандалу, кипариса, шкіри з легким дотиком пахощів старих книг.',
#             'сандал, кипарис, шкіра, пахощі старих книг',
#             1500)
#
#add_product('Природа',
#             'winter_vanilla.jpeg',
#             'Зимова ваніль',
#             'Затишок і тепло холодної зими, як теплий аромат ванілі з нотами мигдалю, білого мускусу і легкого дотику деревної кори.',
#             'ваніль, мигдаль, білий мускус, деревна кора',
#             1350)
#
#add_product('Осінь',
#             'spicy_pumpkin.jpeg',
#             'Пряний гарбуз',
#             'Сезонний аромат для осіннього настрою з теплими нотками гарбузової пряності з корицею, мускатним горіхом, ваніллю та кремовим мускусом.',
#             'гарбуз, кориця, мускатний горіх, ваніль, кремовий мускус',
#             1250)
#
#add_product('Фрукти|Ягоди',
#             'pink_pomegranate.jpeg',
#             'Рожевий гранат',
#            'Свіжий і соковитий ароматб з нотками граната, червоних ягід, злегка підсолоджені білою амброю.',
#             'гранат, червоні ягоди, біла амбра',
#            1200)
#
#add_product('Квіти',
#             'saffron_night.jpeg',
#             'Шафранова ніч',
#            'Загадковий і насичений вечірній ароматб як східний мікс шафрану, деревини уд, сандалу та трохи чорного перцю.',
#             'шафран, уд, сандал, чорний перець',
#             1600)
#
#add_product('Осінь',
#             'warm_honey.jpeg',
#             'Теплий мед',
#            'Солодкий аромат для особливих моментів з цукровим ароматом меду з додаванням жасмину, амбри та краплі бурштину.',
#            'мед, жасмин, амбра, бурштин',
#             1300)
#
#add_product('Квіти',
#             'violet_morning.jpeg',
#             'Фіалковий ранок',
#             'Легкий і квітковий ранковий аромат, як ніжний аромат фіалки, білих квітів і легкого дотику роси.',
#             'фіалка, білі квіти, роса',
#            1100)
#
#add_product('Фрукти|Ягоди',
#             'sunny_passionfruit.jpeg',
#             'Сонячна маракуя',
#             'Яскравий тропічний аромат з нотами маракуї, ананаса, лайма і ніжного білого мускусу.',
#             'маракуя, ананас, лайм, білий мускус',
#             1250)
#
#add_product('Квіти',
#             'lavender_silk.jpeg',
#             'Лаванда і шовк',
#             'Ніжний і спокійний аромат, як поєднання заспокійливої лаванди, білого шовку, фіалки і легкого деревного відтінку.',
#             'лаванда, білий шовк, фіалка, деревний відтінок',
#             1400)
#
#add_product('Фрукти|Ягоди',
#             'forest_blackberry.jpeg',
#             'Лісова ожина',
#             'Свіжий аромат для натхнення з кисло-солодкими нотами ожини, чорної смородини, ялівцю і краплі білого мускусу.',
#             'ожина, чорна смородина, ялівець, білий мускус',
#             1150)
#
#add_product('Осінь',
#             'autumn_forest.jpeg',
#             'Осінній ліс',
#             'Затишний осінній аромат, як сухе листя, мох, крапля диму, кедр і пряні ноти кориці.',
#             'сухе листя, мох, дим, кедр, кориця',
#             1450)
#
#add_product('Квіти',
#             'peach_camellia.jpeg',
#             'Персикова камелія',
#             'Легкий та ніжний аромат з нотками камелії, соковитого персика, мускусу і краплинки амбри.',
#             'камелія, персик, мускус, амбра',
#            1350)


