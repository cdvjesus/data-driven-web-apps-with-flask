import flask
from infrastructure.view_modifiers import response


app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {"name": "package1", "version": "1.0.0"},
        {"name": "package2", "version": "2.0.0"},
        {"name": "package3", "version": "3.0.0"},
    ]

@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)

@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {}


if __name__ == "__main__":
    app.run(debug=True)