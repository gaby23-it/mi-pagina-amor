from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

DATA_FILE = "data.json"

def leer_datos():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route('/')
def inicio():
    data = leer_datos()
    return render_template("index.html", data=data)

@app.route('/guardar_mensaje', methods=['POST'])
def guardar_mensaje():
    data = leer_datos()
    data["mensaje"] = request.json["mensaje"]
    guardar_datos(data)
    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)