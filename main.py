import pandas
import collections
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime


def get_age_writing(age):
    if age % 100 in [11, 12, 13, 14]:
        return "лет"
    if age % 10 == 1:
        return "год"
    if age % 10 in [2, 3, 4]:
        return "года"
    return "лет"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for Winery Site')
    parser.add_argument(
        'file',
        nargs='?',
        default='wine_template.xlsx',
        help='Enter excel filename'
    )
    args = parser.parse_args()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    index_template = env.get_template('index_template.html')
    winery_age = datetime.now().year - 1920
    new_column_names = {
        'Категория': 'category',
        'Название': 'name',
        'Сорт': 'sort',
        'Цена': 'price',
        'Картинка': 'image',
        'Акция': 'special_offer'
    }
    wine_excel = pandas.read_excel(
        args.file,
        na_values=' ',
        keep_default_na=False
    ).rename(columns=new_column_names)
    wine_categories = collections.defaultdict(list)
    for wine in wine_excel.to_dict('records'):
        wine_categories[wine['category']].append(wine)
    rendered_index_page = index_template.render(
        age=winery_age,
        age_writing=get_age_writing(winery_age),
        wine_cards=wine_excel.to_dict('records'),
        wine_types=wine_categories
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_index_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
