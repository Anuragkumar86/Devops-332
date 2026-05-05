# Docker Commands Reference — Complete List

## Image Management
| Command | Description |
|---------|-------------|
| `docker build -t name:tag .` | Build image from Dockerfile |
| `docker images` | List all images |
| `docker tag src:tag dst:tag` | Tag an image |
| `docker history image` | Show image layer history |
| `docker inspect image` | Detailed image metadata |
| `docker rmi image` | Remove image |
| `docker pull image` | Pull from registry |
| `docker push image` | Push to registry |

## Container Management
| Command | Description |
|---------|-------------|
| `docker run -it image` | Run interactively |
| `docker run -d image` | Run in detached mode |
| `docker run -p 8080:80 image` | Port mapping |
| `docker run -v vol:/path image` | Mount volume |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop container` | Stop container |
| `docker rm container` | Remove container |
| `docker exec -it cont bash` | Execute inside container |
| `docker logs container` | View container logs |

## Networking
| Command | Description |
|---------|-------------|
| `docker network ls` | List networks |
| `docker network create name` | Create network |
| `docker network inspect name` | Inspect network |
| `docker network connect net cont` | Connect container to network |
| `docker network rm name` | Remove network |

## Storage / Volumes
| Command | Description |
|---------|-------------|
| `docker volume create vol` | Create volume |
| `docker volume ls` | List volumes |
| `docker volume inspect vol` | Inspect volume |
| `docker volume rm vol` | Remove volume |
| `docker volume prune` | Remove unused volumes |
| `docker diff container` | Show filesystem changes |
