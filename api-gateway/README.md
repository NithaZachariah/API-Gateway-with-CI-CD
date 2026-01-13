API Gateway

This simple API Gateway proxies requests to local microservices.

Endpoints:
- /users -> http://localhost:5001/users
- /products -> http://localhost:5002/products
- /orders -> http://localhost:5003/orders

Run locally (requires Python 3.9+):

```bash
pip install flask requests
python app.py
```

Build the Docker image:

```bash
docker build -t api-gateway ./api-gateway
```

Run the gateway container:

```bash
docker run -p 8000:8000 api-gateway
```

Access via http://localhost:8000/users etc.
