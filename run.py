from flask import Flask, jsonify
import connexion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'APxCV2UAX5TdzvfvEvlMpQsHkZUoyoJ7'



@app.errorhandler(404)
def page_not_found(e):
  return jsonify({"msg":str(e), "status": 404}), 404


@app.route('/v1/api')
def hello_world():
  return jsonify({ "msg": "Hello Debjit", "status": 200, "authuser": str(connexion.request.headers.get("authuser")) }), 200


if __name__ == "__main__":
  app.run()