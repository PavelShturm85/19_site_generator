from jinja2 import Template
import json
import os
import markdown
from livereload import Server


def open_templats():
    with open('templates.html') as templates:
        return Template(templates.read())


def open_json():
    with open('config.json') as json_file:
        return json.load(json_file)['articles']


def create_path(json_content):
    for article in json_content:
        file_name = os.path.splitext(os.path.basename(article['source']))[0].\
            replace(' ', '_').replace('%', '').replace('$', '').\
            replace('@', '').replace('*', '').replace('!', '').\
            replace('&', '').replace(';', '')
        yield 'pages/' + file_name + '.html', article


def open_markdown(article_in_content):
    article = article_in_content[1]
    with open('articles/' + article['source'], 'r') as markdown_file:
        return markdown.markdown(markdown_file.read())


def fill_page(html_templates, json_content, markdown_html, article_in_content):
    path_html = article_in_content[0]
    article = article_in_content[1]
    with open(path_html, 'w') as html:
        html.write(html_templates.render(
            articles=json_content,
            markdown_text=markdown_html,
            title=article['title'],
            )
        )


if __name__ == '__main__':
    server = Server()

    for content in create_path(open_json()):
        fill_page(open_templats(), open_json(),
                  open_markdown(content), content)

    server.watch('templates.html', fill_page)
    server.watch('articles/', fill_page)
    server.serve(root='pages/')
