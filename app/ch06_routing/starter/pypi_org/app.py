import os
import sys
import flask

# folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, folder)
app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=True)



def register_blueprints():
    from views import home_views
    from views import package_views
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)


if __name__ == '__main__':
    main()