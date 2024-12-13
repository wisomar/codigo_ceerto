from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Oi Meu Nome é William!</p>"

# Ponto de entrada para o Vercel
def handler(environ, start_response):
    from werkzeug.wrappers import Request, Response
    request = Request(environ)
    response = app.dispatch_request()
    return response(environ, start_response)
