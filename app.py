from flask import Flask,jsonify,request
from data import data
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data": data
    })
@app.route("/star")
def planet():
    name=request.args.get("n")
    planet_data=next(i for i in data if i["name"]==name)
    return jsonify({
        "data":star_data
     
    })
if __name__=="__main__":
    app.run()
