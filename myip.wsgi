import sys

activate_this = '/home/david/www-apps/myip/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0, '/home/david/www-apps/myip')


from main import app as application
