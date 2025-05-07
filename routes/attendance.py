# Copyright (c) 2025 uncannystranger. Made with love.
# All rights reserved.

from flask import Blueprint, request, jsonify, Response
from models.attendance_model import (
    add_record, list_records, get_record_by_id, update_record, delete_record, export_csv, get_analytics
)
from functools import wraps

AUTH_TOKEN = "your-secret-token"  # Change this to a secure value

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {AUTH_TOKEN}":
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendance', methods=['POST'])
@require_auth
def add_attendance():
    record = request.json
    saved = add_record(record)
    return jsonify({'status': 'success', 'record': saved}), 201

@attendance_bp.route('/attendance', methods=['GET'])
@require_auth
def get_attendance():
    name = request.args.get('name')
    date = request.args.get('date')  # Format: YYYY-MM-DD
    data = list_records(name=name, date=date)
    return jsonify(data)

@attendance_bp.route('/attendance/<record_id>', methods=['GET'])
@require_auth
def get_attendance_by_id(record_id):
    record = get_record_by_id(record_id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(record)

@attendance_bp.route('/attendance/<record_id>', methods=['PUT'])
@require_auth
def update_attendance(record_id):
    updates = request.json
    updated = update_record(record_id, updates)
    if not updated:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify({'status': 'updated', 'record': updated})

@attendance_bp.route('/attendance/<record_id>', methods=['DELETE'])
@require_auth
def delete_attendance(record_id):
    success = delete_record(record_id)
    if not success:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify({'status': 'deleted'})

@attendance_bp.route('/attendance/export', methods=['GET'])
@require_auth
def export_attendance_csv():
    csv_data = export_csv()
    return Response(
        csv_data,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment;filename=attendance.csv'}
    )

@attendance_bp.route('/attendance/analytics', methods=['GET'])
@require_auth
def attendance_analytics():
    stats = get_analytics()
    return jsonify(stats)
