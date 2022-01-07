import sys

# add your project directory to the sys.path
project_home = u'/home/jamescaldwell1981/portfolio/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from flask_app import app as application