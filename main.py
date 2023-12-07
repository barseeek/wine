import pandas
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime


def get_age_writing(age):
    age_exceptions = [11, 12, 13, 14, 111, 913, 2012]
    if age in age_exceptions:
        return "лет"
    if age % 10 == 1:
        return "год"
    if age % 10 in [2, 3, 4]:
        return "года"
    return "лет"


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    caps_template = env.get_template('caps_template.html')
    rendered_caps_page = caps_template.render(
        cap1_title="Красная кепка",
        cap1_text="$ 100.00",
        cap2_title="Чёрная кепка",
        cap2_text="$ 120.00",
        cap3_title="Ещё одна чёрная кепка",
        cap3_text="$ 90.00",
    )
    with open('caps.html', 'w', encoding="utf8") as file:
        file.write(rendered_caps_page)
    index_template = env.get_template('index_template.html')
    winery_age = datetime.now().year - 1920
    new_column_names = {
        'Категория': 'category',
        'Название': 'name',
        'Сорт': 'sort',
        'Цена': 'price',
        'Картинка': 'image'
    }
    read_wine_excel = pandas.read_excel('wine2.xlsx').rename(columns=new_column_names)
    wine_categories = {}
    for category in read_wine_excel["category"].unique():
        wine_categories[category] = []
    print(wine_categories)
    for wine in read_wine_excel.to_dict('records'):
        wine_categories[wine['category']].append(wine)
    print(wine_categories)
    rendered_index_page = index_template.render(
        age=winery_age,
        age_writing=get_age_writing(winery_age),
        wine_cards=read_wine_excel.to_dict('records')
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_index_page)
    
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
