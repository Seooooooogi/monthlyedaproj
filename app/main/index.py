from flask import Flask, Blueprint, render_template , flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')
 
@main.route('/', methods=['GET'])
def index():
    return render_template('/main/index.html')
