# Docker Registry Commands Reference

## Docker Hub
```bash
# Login to Docker Hub
docker login

# Tag image for Docker Hub
docker tag myflaskapp:v1 anuradocker/myflaskapp:v1
docker tag myflaskapp:v1 anuradocker/myflaskapp:latest

# Push to Docker Hub
docker push anuradocker/myflaskapp:v1
docker push anuradocker/myflaskapp:latest

# Pull from Docker Hub
docker pull anuradocker/myflaskapp:v1
```

## GitHub Container Registry (GHCR)
```bash
# Login to GHCR using Personal Access Token
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Tag for GHCR
docker tag myflaskapp:v1 ghcr.io/anura/myflaskapp:v1

# Push to GHCR
docker push ghcr.io/anura/myflaskapp:v1

# Pull from GHCR
docker pull ghcr.io/anura/myflaskapp:v1
```

## Private Registry
```bash
# Run a local private registry
docker run -d -p 5000:5000 --name registry registry:2

# Tag for private registry
docker tag myflaskapp:v1 localhost:5000/myflaskapp:v1

# Push to private registry
docker push localhost:5000/myflaskapp:v1

# Pull from private registry
docker pull localhost:5000/myflaskapp:v1
```
