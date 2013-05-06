# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
    app.debug = True
    app.run()

