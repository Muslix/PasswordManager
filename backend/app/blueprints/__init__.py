from flask import Blueprint

api_blueprint = Blueprint("api", __name__)

from .passwords import *
from .categories import * 