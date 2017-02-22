#main.py
import redis

conn = redis.Redis(host='127.0.0.1', port=6379)

'''
>> redis-server

conn.set('hello', 'world')

print(conn.get('hello'))
#b'world'
'''

from flask import Flask, request, session, redirect, url_for, abort, \
                render_template, json, jsonify, flash
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'



@app.route('/api/todos/', methods=['GET'])
def todo():
    arr = conn.lrange('arr',0,-1)
    for i in range(len(arr)):
        arr[i] = arr[i].decode()
    return jsonify({'code':'200','msg':'ok', 'data': arr})


@app.route('/api/push/', methods=['GET'])
def push():
    conn.lpush('arr','c')
    return jsonify({'code':'200','msg':'ok', 'data': {}})


@app.route('/api/clear/', methods=['GET'])
def clear():
    conn.delete('arr')
    return jsonify({'code':'200','msg':'ok', 'data': {}})

if __name__ == '__main__':
    app.run()