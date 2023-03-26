from flask import Blueprint, jsonify, request
from models import *

view = Blueprint("view", __name__)

# Routes
@view.route("/", methods=["GET"])
def home():
    st=Store()
    db.session.add(st)
    db.session.commit()
    return jsonify({"message":"Hey! This is my API"}),200 # 200 OK

@view.route('/trigger_report', methods=['POST'])
def trigger_report():
    # report_id =
    # TODO: Generate report
    return jsonify({'report_id': report_id})

@view.route('/get_report/<report_id>', methods=['GET'])
def get_report(report_id):
    # TODO: Get report status and CSV file
    return 'Complete'
