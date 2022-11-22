from flask import Flask
app = Flask(__name__)
from app import  views
import deploy_smart_contract
deploy_smart_contract