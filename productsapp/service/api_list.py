from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from productsapp.service.website import WebsiteResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(WebsiteResource, '/website')