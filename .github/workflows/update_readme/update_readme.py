from pathlib import Path
from jinja2 import Template


repo_directories = (
    'static',
)

def get_content(repo_directories):
    return_content = {}

    for directory in repo_directories:
        new_content = Path(f'{directory}_readme.md').read_text()
        return_content[directory] = (directory, new_content)

    return return_content


main_readme_template_path = '../../README.md'
readme_path = '../../../README.md'

template = Template(Path(main_readme_template_path).read_text())
Path(readme_path).write_text(
        template.render(
            table_of_contents='Testing',
            body=get_content(['.github/workflows']),
            )
        )
