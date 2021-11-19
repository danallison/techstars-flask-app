from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Helper function
def record_as_dict(record):
    return {
        'id': record[0],
        'text': record[1]
    }

@app.route('/')
def root():
    return jsonify({
        'routes': {
            '/': {
                'GET': {
                    'params': None,
                    'returns': 'json description of API routes'
                }
            },
            '/records': {
                'POST': {
                    'params': { 'text': '[string]' },
                    'returns': 'record object with ID'
                },
                'GET': {
                    'params': None,
                    'returns': 'list of all records'
                }
            },
            '/records/<id>': {
                'GET': {
                    'params': None,
                    'returns': 'record object with matching ID, if it exists'
                }
            }
        }
    })

@app.route('/records', methods=['GET'])
def list():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM records")
        records = cur.fetchall()
    return jsonify([record_as_dict(record) for record in records])

@app.route('/records/<id>', methods=['GET'])
def show(id):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM records WHERE id = ? LIMIT 1", (id,))
        record = cur.fetchone()
    return jsonify(record_as_dict(record))

@app.route('/records', methods=['POST'])
def create():
    data = request.get_json(force=True)
    text = data['text']
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO records (text) VALUES (?)", (text,))
        conn.commit()
        cur.execute("SELECT * FROM records WHERE id = ? LIMIT 1", (cur.lastrowid,))
        record = cur.fetchone()
    return jsonify(record_as_dict(record))
