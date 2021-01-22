import os

from app import create_app

environment = os.getenv('FLASK_ENV')
if type(environment) is not str:
    environment = "default"

app = create_app(environment)


@app.shell_context_processor
def make_shell_context():
    pass
