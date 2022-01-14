"""Flask application."""
import warnings

import connexion
import flask

from .health import set_health_status
from .package import apt_cache_update

warnings.simplefilter('always')

SWAGGER = connexion.App(__name__, specification_dir='swagger/')
API_V1 = SWAGGER.add_api(
    'api_v1.yml', base_path='/v1', resolver=connexion.resolver.RestyResolver('packageresolve.api_v1'))

APP = SWAGGER.app
with APP.app_context():
    apt_cache_update()


@APP.route('/')
def default_api():
    """Redirect to the newest API version."""
    return flask.redirect(API_V1.base_path + '/ui')