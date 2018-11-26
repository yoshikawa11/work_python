import string
import os
import csv

customer = ''
best_restaurant = ''
path = "ranking.csv"

# 挨拶を読み込む
with open('text_template/template.txt') as f:
    t = string.Template(f.read())
    contents = t.substitute(name='Roboko', contents='私はあなたのアシスタントです。')
print(contents)

# 名前を入力
while True:
    customer_name = input('名前を入力してください:')
    if len(customer_name) != 0:
        print(customer_name)
        customer = customer_name
        break
    print('もう一度入力してください')

# レストラン情報があるときはそれを提示、ない場合は相手に好きなレストランを聞く
if not os.path.isfile(path):
    with open('text_template/template_norestaurant') as f:
        t = string.Template(f.read())
    contents = t.substitute(name=customer)
    print(contents)
    while True:
        restaurant_name = input('レストランの名前を入力してください:')
        if len(restaurant_name) != 0:
            str = restaurant_name
            restaurant = str.title()
            print(restaurant)
            # CSVにレストランを書き込む
            with open('ranking.csv', 'a') as csv_file:
                fieldnames = ['Name', 'Count']
                writer = csv.DictWriter(csv_file, fieldnames)
                writer.writeheader()
                writer.writerow({'Name': restaurant, 'Count': 1})
            break
        print('もう一度入力してください')

# レストラン情報を提示
else:
    data = {}
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader('csv_file')
        for row in reader:
            data.update(row)
    best_restaurant = max(data, key= data.get)
    with open('text_template/template_recommend') as f:
        t = string.Template(f.read())
    contents = t.substitute(restaurant=best_restaurant)   #CSVからの取得ができない
    print(contents)

# 別れの挨拶を読み込む
with open('text_template/template_onparting') as f:
    t = string.Template(f.read())
    contents = t.substitute(name=customer)
    print(contents)
