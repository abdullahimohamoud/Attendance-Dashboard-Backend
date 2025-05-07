# Copyright (c) 2025 uncannystranger. Made with love.
# All rights reserved.

import os
import json
import uuid
from datetime import datetime
import csv

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/attendance.json')

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_record(record):
    data = load_data()
    record['id'] = str(uuid.uuid4())
    record['timestamp'] = datetime.now().isoformat()
    data.append(record)
    save_data(data)
    return record

def list_records(name=None, date=None):
    data = load_data()
    if name:
        data = [r for r in data if r.get('name', '').lower() == name.lower()]
    if date:
        data = [r for r in data if r['timestamp'].startswith(date)]
    data.sort(key=lambda r: r['timestamp'], reverse=True)
    return data

def get_record_by_id(record_id):
    data = load_data()
    for r in data:
        if r.get('id') == record_id:
            return r
    return None

def update_record(record_id, updates):
    data = load_data()
    for r in data:
        if r.get('id') == record_id:
            r.update(updates)
            save_data(data)
            return r
    return None

def delete_record(record_id):
    data = load_data()
    new_data = [r for r in data if r.get('id') != record_id]
    if len(new_data) == len(data):
        return False
    save_data(new_data)
    return True

def export_csv():
    data = load_data()
    if not data:
        return ''
    keys = sorted(data[0].keys())
    from io import StringIO
    s = StringIO()
    writer = csv.DictWriter(s, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)
    return s.getvalue()

def get_analytics():
    data = load_data()
    total = len(data)
    present = sum(1 for r in data if r.get('status', '').lower() == 'present')
    absent = sum(1 for r in data if r.get('status', '').lower() == 'absent')
    per_day = {}
    for r in data:
        day = r['timestamp'][:10]
        per_day.setdefault(day, 0)
        per_day[day] += 1
    return {
        'total': total,
        'present': present,
        'absent': absent,
        'per_day': per_day
    }
