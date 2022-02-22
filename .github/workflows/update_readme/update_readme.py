def get_content(repo_directories):
    return_content = {}

    for directory in repo_directories:
        with open(f'./{directory}/{directory}_readme.md') as fh:
            tmp_contents = fh.read()
            print(tmp_contents)

            desc_end_idx = tmp_contents.find('-->')
            desc = tmp_contents[8:desc_end_idx]
            tmp_contents = tmp_contents.replace(desc, '').replace('<!--DESC', '').replace('-->', '')
            desc = desc.replace('<!--DESC', '').replace('-->', '')
        return_content[directory] = (tmp_contents.replace(desc, ''), desc)

    return return_content


repo_directories = (
    'static',
    'templates',
    'pages'
)

main_readme_path = 'README.md'
# Uncomment for local development
#main_readme_path = '../../../README.md'

content = get_content(repo_directories)
table_of_contents = ''
content_body = ''
i = 1

for heading, body_desc in content.items():

    if isinstance(heading, str) and isinstance(body_desc[0], str):
        heading_upper = heading[0].upper() + heading[1:]

        table_of_contents += f'{str(i)}. [{heading_upper}](#{heading}) - {body_desc[1]}\n'

        heading = f'<a id=\"{heading}\"></a>[{heading_upper}]({heading}/)'

        content_body += f'##{heading_upper}\n{body_desc[0]}\n\n'

        i += 1
        print(heading, content_body)

with open(main_readme_path, 'w') as readme:
    file_contents = table_of_contents + content_body

    readme.write(file_contents)
