# ML multi app deployment

## Info
* A machine learning project deployment scenario with multiple applications / docker containers
* The main code for training the model can be found in another [repo](https://github.com/AbhishekRS4/ML_water_potability_fastapi_deployment)
* The project involves a streamlit application for the frontend and a FastAPI application for the backend / ML service

## Backend
* Run the following command to build the container for backend
```
cd backend/
docker build -t ml_water_potability_backend -f backend.dockerfile .
```

## Frontend
* Run the following command to build the container for frontend
```
cd frontend/
docker build -t ml_water_potability_frontend -f frontend.dockerfile .
```

## Deployment with docker-compose (locally)
* Run the following command (in the same directory with the docker-compose.yaml file) to deploy and run both the containers
```
docker-compose up
```

## Deployment with kubernetes (locally)
* Install [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) and [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
* Setup a kind cluster with the following command
```
kind create cluster
```
* To check the cluster info, run the following commads
```
kubectl cluster-info --context kind-kind
```
* To check services, pods, deployments; run the following commands
```
kubectl get service
kubectl get pod
kubectl get deployment
```
