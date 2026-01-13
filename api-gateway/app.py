from flask import Flask, Response
import requests

app = Flask(__name__)


def proxy_get(url):
    resp = requests.get(url, timeout=5)
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get("Content-Type", "text/plain"))


@app.route("/users")
def users():
    return proxy_get("http://localhost:5001/users")


@app.route("/products")
def products():
    return proxy_get("http://localhost:5002/products")


@app.route("/orders")
def orders():
    return proxy_get("http://localhost:5003/orders")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
