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
