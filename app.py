from flask import Flask
from routes.attendance import attendance_bp

app = Flask(__name__)
app.register_blueprint(attendance_bp)

if __name__ == '__main__':
    app.run(debug=True)
