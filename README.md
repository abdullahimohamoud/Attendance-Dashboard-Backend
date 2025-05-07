<<<<<<< HEAD
your local version
=======
remote (GitHub) version
>>>>>>> main

# Attendance Dashboard Backend

A simple, organized Python backend for managing attendance records.

## Project Structure

- `app.py` — Main entry point, runs the Flask app
- `routes/attendance.py` — API endpoints for attendance
- `models/attendance_model.py` — Data access and storage logic
- `data/attendance.json` — Stores attendance records
- `copyright.txt` — Copyright and credits

## Usage

1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the server:
   ```bash
   python app.py
   ```
3. API Endpoints:
   - `POST /attendance` — Add a record (JSON: `{ "name": "Alice", "status": "present" }`)
   - `GET /attendance` — List all records

## Copyright
See `copyright.txt`.

---
Made with love @uncannystranger

# Attendance-Dashboard-Backend
A secure, organized Python backend for attendance management. Built with Flask, it supports token-based authentication, CRUD operations, filtering, CSV export, and analytics. Data is stored in JSON for simplicity. The project is modular, easy to extend, and ideal for small teams or educational use.
