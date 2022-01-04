from flask import Flask
from flask import render_template
from flask import url_for

import pages


app = Flask(__name__)


@app.route('/')
def landing():  # put application's code here

    heading1 = 'Etiam finibus tempus felis eget ullamcorper'
    content1 = 'Cras pellentesque neque, consectetur adipiscing elit. Fusce venenatis elit ac ligula euismod varius. Maecenas feugiat purus quam, vel aliquet tellus sodales eu. Integer vitae vestibulum turpis, in sollicitudin quam. Aliquam vulputate non felis non luctus. Vestibulum eget augue nulla. Aliquam dignissim nibh mi, ut bibendum quam dapibus eget. Nam nec nisi vel sapien pulvinar ultrices. Curabitur rutrum nisl sagittis, pretium velit eget, convallis lacus. Nulla fermentum nulla ut lacus maximus, ut porttitor neque varius. Nullam sed vulputate sem. Sed bibendum porttitor metus.'

    heading2 = 'Fusce venenatis elit'
    content2 = 'Maecenas feugiat purus quam, vel aliquet tellus sodales eu. Integer vitae vestibulum turpis, in sollicitudin quam. Aliquam vulputate non felis non luctus. Vestibulum eget augue nulla. Aliquam dignissim nibh mi, ut bibendum quam dapibus eget. Nam nec nisi vel sapien pulvinar ultrices. Curabitur rutrum nisl sagittis, pretium velit eget, convallis lacus. Nulla fermentum nulla ut lacus maximus, ut porttitor neque varius. Nullam sed vulputate sem.'

    heading3 = 'venenatis elit'
    content3 = 'aliquet tellus sodales eu. Integer ce venenatis elit ac lig, vel aliquet tellus sodales eu.'

    articles = [
        ('Name 1', '#'),
        ('Name 2', '#'),
        ('Name 3', '#'),
        ('Name 4', '#'),
    ]

    projects = [
        ('Name 1', '#'),
        ('Name 2', '#'),
        ('Name 3', '#'),
        ('Name 4', '#'),
    ]

    kaggles = [
        ('Name 1', '#'),
        ('Name 2', '#'),
        ('Name 3', '#'),
        ('Name 4', '#'),
    ]

    tutorials = [
        ('Name 1', '#'),
        ('Name 2', '#'),
        ('Name 3', '#'),
        ('Name 4', '#'),
    ]

    experiments = [
        ('Name 1', '#'),
        ('Name 2', '#'),
        ('Name 3', '#'),
        ('Name 4', '#'),
    ]


    rows = [[heading1, content1], [heading2, content2], [heading3, content3]]
    return render_template('page_intro.html',
                           title='Viral',
                           articles=articles,
                           projects=projects,
                           kaggles=kaggles,
                           tutorials=tutorials,
                           experiments=experiments,
                           rows=rows,
                           custom_layout=None,
                           custom_script=None)


if __name__ == '__main__':
    app.run()
