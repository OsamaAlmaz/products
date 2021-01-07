from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from productsapp.service.website import WebsiteResource

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
#make sure that you add a


api.add_resource(WebsiteResource, '/website/<int:id>')
app.register_blueprint(api_bp)