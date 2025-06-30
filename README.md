````
# 🚀 DevOps API Challenge

A simple cloud-native Flask API that echoes HTTP request headers, method, and body.  
This project is Dockerized, Helm-packaged, and deployed to a local Kubernetes cluster via Minikube.
---

## 📦 Features

- 🔁 Echoes back request header, method, and body
- 🐳 Dockerized for portability
- ⛴️ Deployed via Helm
- ☸️ Kubernetes-compatible (tested on Minikube)
- ✅ GitOps-ready structure (CI/CD friendly)
- 📈 (Optional) Prometheus metrics and Helm test support
---

## 🧪 Example Request & Response

### Request:
```bash
curl -X POST http://localhost:8080/api \
  -H "Content-Type: application/json" \
  -d '{"username": "himanshu", "password": "123"}'
````

### Response:

```json
Welcome to our demo API, here are the details of your request:

***Headers***:
Content-Type: application/json

***Method***:
POST

***Body***:
{"username": "himanshu", "password": "123"}
```

---

## 🧰 Tech Stack

| Layer         | Tool                      |
| ------------- | ------------------------- |
| Language      | Python + Flask            |
| Container     | Docker                    |
| Orchestration | Kubernetes (Minikube)     |
| Packaging     | Helm Chart                |
| CI/CD         | GitHub Actions (optional) |

---

## 🛠️ Local Development

### 1. Clone the repository

```bash
git clone https://github.com/HimanshuGupta08/DevOps-API-Challenge.git
cd DevOps-API-Challenge
```

### 2. Run locally with Python

```bash
pip install flask
python main.py
```

Then visit: [http://localhost:8080/api]

---

## 🐳 Docker

### Build image

```bash
docker build -t devops-challenge-api .
```

### Run container

```bash
docker run -p 8080:8080 devops-challenge-api
```

---

## ☸️ Kubernetes with Helm (Minikube)

### 1. Start Minikube

```bash
minikube start
```

### 2. Build image inside Minikube

```bash
eval $(minikube docker-env)
docker build -t devops-challenge-api .
```

### 3. Install Helm chart

```bash
helm install devops-api ./devops-api
```

### 4. Port forward and test

```bash
kubectl port-forward svc/devops-api 8080:8080
```

Then in a new terminal:

```bash
curl -X POST http://localhost:8080/api \
  -H "Content-Type: application/json" \
  -d '{"username": "himanshu", "password": "123"}'
```

---

## 📁 Project Structure

```
DevOps-API-Challenge/
├── main.py                  # Flask app
├── Dockerfile               # Docker build config
├── .github/workflows/       # (Optional) CI/CD configs
├── devops-api/              # Helm chart
│   ├── templates/           # Deployment, service, etc.
│   └── values.yaml          # Helm configuration
```
---

## 🧪 Helm Testing (Optional)

This chart includes a Helm test hook (Job) that performs a `/api` curl request to verify deployment.

To run it:

```bash
helm test devops-api
```

---

## 📈 Prometheus Metrics (Optional)

You can add a `/metrics` endpoint with [prometheus\_client](https://github.com/prometheus/client_python) by modifying `main.py`:

```python
from prometheus_client import Counter, generate_latest

REQUEST_COUNT = Counter("request_count", "Number of API requests", ["method"])

@app.route("/api", methods=["GET", "POST"])
def echo():
    REQUEST_COUNT.labels(request.method).inc()
    ...
```

---

## ✅ TODOs & Improvements

* [ ] Add Prometheus `/metrics` endpoint
* [ ] Add GitHub Actions pipeline for CI/CD
* [ ] Push Docker image to DockerHub
* [ ] Add Open Policy Agent (OPA) test in cluster
* [ ] Add `livenessProbe` and `readinessProbe` to `deployment.yaml`
---

## 👨‍💻 Author

**Himanshu Gupta**
