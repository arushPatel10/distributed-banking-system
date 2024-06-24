# Distributed Banking System Implementation Using gRPC and Docker

## Overview

This project implements a distributed banking system using gRPC for communication between multiple branch servers and a client API. The system is containerized using Docker to facilitate easy deployment and scalability across different environments. Kubernetes is used for orchestrating the deployment of containers, ensuring high availability and load balancing. Additionally, a Flask-based API is provided for dynamic input and handling real-time banking transactions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [Testing the API](#testing-the-api)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Distributed architecture with multiple branch servers
- Communication between components using gRPC
- Containerized using Docker for easy deployment
- Dynamic input handling through a Flask-based API
- Orchestrated deployment using Kubernetes
- Detailed logging and error handling

## Architecture

The system consists of the following components:

- **Branch Servers**: Each branch server handles transactions for a specific set of customers.
- **Client API**: A Flask-based API that handles dynamic input and routes transactions to the appropriate branch server.
- **gRPC Communication**: Used for communication between the client API and branch servers.
- **Docker**: Used to containerize the components for easy deployment.
- **Kubernetes**: Used for orchestrating the deployment of containers, ensuring high availability and load balancing.

## Setup and Installation

### Prerequisites

- Docker
- Docker Compose
- Kubernetes (Minikube for local development)
- Python 3.9
- `grpcio` and `grpcio-tools`

### Clone the Repository

```sh
git clone https://github.com/arushPatel10/distributed-banking-system.git
cd distributed-banking-system
```

### Set Up Virtual Environment

Create and activate a virtual environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

Install the required Python packages.

```sh
pip install -r requirements.txt
```

### Generate gRPC Code

Generate the gRPC code from the `bank.proto` file.

```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. bank.proto
```

## Running the Project

### Run the gRPC Server

Build and run the Docker container for the branch servers.

```sh
docker build -t arushpatel/banking-system-server -f Dockerfile.server .
docker run -d -p 5001:5001 arushpatel/banking-system-server
```

### Run the Client API

Build and run the Docker container for the Flask-based API.

```sh
docker build -t arushpatel/banking-system-api -f Dockerfile.api .
docker run -d -p 5002:5002 arushpatel/banking-system-api
```

### Verify Running Containers

Check if the containers are running.

```sh
docker ps
```

## Testing the API

### Initialize a Branch

Initialize a branch with a specific branch ID and initial balance.

```sh
curl -X POST -H "Content-Type: application/json" -d '{"branch_id": 1, "initial_balance": 1000}' http://localhost:5002/initialize_branch
```

### Perform Transactions

Perform transactions such as deposit, withdraw, and query balance.

#### Deposit

```sh
curl -X POST -H "Content-Type: application/json" -d '{"customer_id": 1, "type": "deposit", "amount": 100}' http://localhost:5002/transaction
```

#### Withdraw

```sh
curl -X POST -H "Content-Type: application/json" -d '{"customer_id": 1, "type": "withdraw", "amount": 50}' http://localhost:5002/transaction
```

#### Query Balance

```sh
curl -X POST -H "Content-Type: application/json" -d '{"customer_id": 1, "type": "query"}' http://localhost:5002/transaction
```

## Kubernetes Deployment

### Start Minikube

Start Minikube for local Kubernetes development.

```sh
minikube start
```

### Create Kubernetes Deployment Files

Create deployment YAML files for the branch server and client API.

**server-deployment.yaml**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: banking-system-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: banking-system-server
  template:
    metadata:
      labels:
        app: banking-system-server
    spec:
      containers:
      - name: banking-system-server
        image: arushpatel/banking-system-server
        ports:
        - containerPort: 5001
---
apiVersion: v1
kind: Service
metadata:
  name: banking-system-server
spec:
  type: NodePort
  ports:
    - port: 5001
      nodePort: 30001
  selector:
    app: banking-system-server
```

**api-deployment.yaml**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: banking-system-api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: banking-system-api
  template:
    metadata:
      labels:
        app: banking-system-api
    spec:
      containers:
      - name: banking-system-api
        image: arushpatel/banking-system-api
        ports:
        - containerPort: 5002
---
apiVersion: v1
kind: Service
metadata:
  name: banking-system-api
spec:
  type: NodePort
  ports:
    - port: 5002
      nodePort: 30002
  selector:
    app: banking-system-api
```

### Deploy to Kubernetes

Apply the deployment files to Kubernetes.

```sh
kubectl apply -f server-deployment.yaml
kubectl apply -f api-deployment.yaml
```

### Access Services

Get the Minikube IP and access the services.

```sh
minikube ip
```

Use the Minikube IP with the exposed NodePorts (30001 for the server and 30002 for the API).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
