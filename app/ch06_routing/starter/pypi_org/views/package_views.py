import os
import sys
import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


from infrastructure.view_modifiers import response

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
    return "package details for {}".format(package_name)

@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def popular(rank: int):
    return "The details for the  {}th most popular package".format(rank)
