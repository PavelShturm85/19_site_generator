from jinja2 import Template
import json
import os
import markdown
from livereload import Server


def create_pages():
    with open('templates.html') as templates:
        html_templates = Template(templates.read())
    with open('config.json') as json_file:
        json_content = json.load(json_file)['articles']
    for article in json_content:
        file_name = os.path.splitext(os.path.basename(article['source']))[0].\
            replace(' ', '_').replace('%', '').replace('$', '').\
            replace('@', '').replace('*', '').replace('!', '').\
            replace('&', '').replace(';', '')
        path_html = 'site/' + file_name + '.html'
        with open(path_html, 'w') as html:
            with open('articles/' + article['source'], 'r') as markdown_file:
                markdown_html = markdown.markdown(markdown_file.read())
                html.write(html_templates.render(
                    articles=json_content,
                    markdown_text=markdown_html,
                    title=article['title'],
                    )
                )


if __name__ == '__main__':
    server = Server()
    create_pages()
    server.watch('templates.html', create_pages)
    server.watch('articles/', create_pages)
    server.serve(root='site/')
