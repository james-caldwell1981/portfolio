from pathlib import Path

import jinja2
from jinja2 import Template


def get_content(repo_directories):
    return_content = {}

    for directory in repo_directories:
        if directory in repo_directories:
            new_content = Path(f'./{directory}/{directory}_readme.md').read_text()
            # Uncomment for local development
            # new_content = Path(f'../../../{directory}/{directory}_readme.md').read_text()
            return_content[directory] = new_content

    return return_content


repo_directories = (
    'static',
)

main_readme_template_path = 'README.md'
# Uncomment for local development
# main_readme_template_path = '../../../README.md'

content = get_content(repo_directories)
table_of_contents = ''
content_body = ''
print(content)
for heading, body in enumerate(content):
    if isinstance(heading, str) and isinstance(body, str):
        table_of_contents += f'* {heading}\n'
        body += f'{heading}<br />\n' \
                f'{body}\n' \
                f'<br /><br />\n'

template = Template(Path(main_readme_template_path).read_text())
Path(main_readme_template_path).write_text(
        template.render(
            table_of_contents=table_of_contents,
            body=body
            )
        )
