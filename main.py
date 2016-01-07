# -*- coding: utf-8 -*-

import socket

from flask import Flask, request, jsonify, render_template
from jinja2 import FileSystemLoader


app = Flask(__name__)
app.jinja_loader = FileSystemLoader(app.root_path)



@app.route('/')
def index():
    ip = request.remote_addr
    headers = list(request.headers)

    if request.args.get('json') == 'true':
        if request.args.get('iponly') == 'true':
            return jsonify(ip=ip)
        return jsonify(ip=ip, headers=headers)

    if request.args.get('iponly') == 'true':
        return render_template('index.html', ip=ip)
    return render_template('index.html', ip=ip, headers=headers)

@app.route('/reverse-dns')
def reverse_dns():
    ip = request.remote_addr

    try:
        name = socket.gethostbyaddr(ip)[0]
        return jsonify(hostname=name)
    except socket.herror as e:
        return jsonify(error=e[1])


if __name__ == '__main__':
    app.debug = True
    app.run()

