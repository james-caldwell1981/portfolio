from os import environ
from flask import Flask, request, render_template
from git import Repo
from validation.git_hook_val import is_valid_signature

app = Flask(__name__)


@app.route('/')
def landing():  # put application's code here

    # Currently using filler data for early testing

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

    contact = 'templates/contact.html'

    rows = [[heading1, content1], [heading2, content2], [heading3, content3]]

    # This is currently how the page is populated
    # Individual sections are a list of most recent items
    # This should be updated in the future for readability and modularity
    return render_template('page_intro.html',
                           title='Data James',
                           articles=articles,
                           projects=projects,
                           kaggles=kaggles,
                           tutorials=tutorials,
                           experiments=experiments,
                           contact=contact,
                           rows=rows,
                           custom_layout=None,
                           custom_script=None)


@app.route('/contact')
def contact():

    title = 'Get in Touch!'
    body = '        \
        At the moment, I will be interacting with everyone through my <a href="#">LinkedIn account</a>.<br /> \
        Future plans would include both an email option and direct message through this webpage.<br /> \
        I welcome all constructive criticisms, suggestions, content/functionality requests, etc.<br /> \
        Hope to hear from you soon! \
        '
    return render_template('contact.html',
                           title=title,
                           body=body
                           )


@app.route('/update_server', methods=['POST'])
def update_server():

    """
    This route receives a call from the github webhook detecting a new merge.
    After a successful merge, the webhook sends a push request to the deployed
    application which then attempts to verify identity. Upon success,
    the GitHub hook is allowed to push the new data to the deployed repo.

    :return: Plain text disposition and status code.
    """

    if request.method == 'POST':
        # Gets the x-hub-signature from the request header
        x_hub_signature = request.headers.get('X-Hub-Signature-256')

        # Load the secret from environment
        private_key = environ['SECRET_KEY']

        # If verification fails, return plaintext error with code
        if not is_valid_signature(x_hub_signature, request.data, private_key):
            return 'Invalid signature.', 401

        # Set up the repository and pull it's contents
        repo = Repo('/home/jamescaldwell1981/portfolio')
        origin = repo.remotes.origin
        origin.pull()

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


if __name__ == '__main__':
    app.run()
