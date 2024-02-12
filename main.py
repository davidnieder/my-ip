import socket

from flask import Flask, request, jsonify, render_template, Response
from jinja2 import FileSystemLoader


app = Flask(__name__)
app.jinja_loader = FileSystemLoader(app.root_path)


@app.route('/')
@app.route('/html')
def html():
    ip = request.remote_addr
    headers = list(request.headers)
    return render_template('index.html', ip=ip, headers=headers)

@app.route('/plain')
def plain():
    body = '{}\n'.format(request.remote_addr)
    return Response(body, mimetype="text/plain")

@app.route('/json')
def json():
    return jsonify(ip=request.remote_addr)

@app.route('/reverse-dns')
def reverse_dns():
    ip = request.remote_addr

    try:
        name = socket.gethostbyaddr(ip)[0]
        return jsonify(hostname=name)
    except socket.herror as e:
        return jsonify(error=e.strerror)
