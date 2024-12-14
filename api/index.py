from flask import Flask, jsonify

# Criação do app Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Oi, meu nome é William!</p>"

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404


