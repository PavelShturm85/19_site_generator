from jinja2 import Template
import json
import os
import markdown
from livereload import Server


def open_html_templates():
    with open('templates.html') as html:
        return Template(html.read())


def load_data_json():
    with open('config.json') as json_file:
        json_content = json.load(json_file)['articles']
    return json_content


def get_article(input_json):
    for article in input_json:
        yield article


def create_pages(articles):
    for article in articles:
        file_name = os.path.splitext(os.path.basename(article['source']))[0].\
            replace(' ', '_').replace('%', '').replace('$', '').\
            replace('@', '').replace('*', '').replace('!', '').\
            replace('&', '').replace(';', '')
        path_html = 'pages/' + file_name + '.html'
        with open(path_html, 'w') as html:
            with open('articles/' + article['source'], 'r', encoding='utf-8')\
             as markdown_file:
                markdown_html = markdown.markdown(markdown_file.read())
                html.write(open_html_templates().render(
                    articles=get_article(load_data_json()),
                    markdown_text=markdown_html,
                    title=article['title'],
                    )
                )


if __name__ == '__main__':
    create_pages(get_article(load_data_json()))
