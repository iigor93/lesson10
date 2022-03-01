from flask import Flask
import json

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)


@app.route('/')
def main():
    string_to_return = '<pre><br>'
    for items in json_data:
        string_to_return += 'Имя кандидата - ' + items.get('name') + '<br>'
        string_to_return += 'Позиция кандидата - ' + items.get('position') + '<br>'
        string_to_return += 'Навыки - ' + items.get('skills') + '<br>'
        string_to_return += '<br>'
    string_to_return += '</pre>'
    return string_to_return

@app.route('/candidate/<int:uid>/')
def candidate_data(uid):
    photo_link = 'https://avatars.mds.yandex.net/i?id=81113664ac71b0cc444a0dc2ea53dffc-5616093-images-thumbs&n=13&exp=1'

    for items in json_data:
        if items.get('id') == uid:
            string_to_return = f'<img src = "{photo_link} width = 200 height = 100"><br><pre>'
            string_to_return += 'Имя кандидата - ' + items.get('name') + '<br>'
            string_to_return += 'Позиция кандидата - ' + items.get('position') + '<br>'
            string_to_return += 'Навыки - ' + items.get('skills') + '<br>'
            string_to_return += '<br>'
            string_to_return += '</pre>'

            return string_to_return

    return 'Нет такого кандидата'


@app.route('/skill/<skill_name>')
def skills_view(skill_name):
    pass