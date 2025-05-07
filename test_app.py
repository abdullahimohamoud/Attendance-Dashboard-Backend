# Copyright (c) 2025 uncannystranger. Made with love.
# All rights reserved.
import pytest
import json
from app import app
from routes.attendance import AUTH_TOKEN

def auth_header():
    return {'Authorization': f'Bearer {AUTH_TOKEN}'}

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_and_list_attendance(client):
    # Add a record
    response = client.post('/attendance',
        data=json.dumps({'name': 'TestUser', 'status': 'present'}),
        content_type='application/json',
        headers=auth_header())
    assert response.status_code == 201
    data = response.get_json()
    assert data['record']['name'] == 'TestUser'
    # List records
    response = client.get('/attendance', headers=auth_header())
    assert response.status_code == 200
    records = response.get_json()
    assert any(r['name'] == 'TestUser' for r in records)

def test_auth_required(client):
    response = client.get('/attendance')
    assert response.status_code == 401

def test_analytics(client):
    response = client.get('/attendance/analytics', headers=auth_header())
    assert response.status_code == 200
    stats = response.get_json()
    assert 'total' in stats
    assert 'present' in stats
    assert 'absent' in stats

def test_export_csv(client):
    response = client.get('/attendance/export', headers=auth_header())
    assert response.status_code == 200
    assert response.mimetype == 'text/csv'
