# DevOps Lab Assignment - Docker
## Semester 6 | Subject: DevOps

---

## Topics Covered

### 1. Image Building & Container Management
- Dockerfile core concepts
- Basic instructions: FROM, RUN, COPY, ADD, CMD, ENTRYPOINT, WORKDIR, ENV, EXPOSE, VOLUME
- Build context & .dockerignore

### 2. Image Creation in Detail
- `docker build` process
- Image tagging & versioning
- Inspecting images (history, layers)

### 3. Docker Networking
- Bridge, host & overlay networks
- DNS inside Docker
- Linking containers
- Port mapping

### 4. Docker Storage
- Volumes vs bind mounts
- Copy-on-write mechanism
- Backing data on host

### 5. Registries
- Docker Hub
- GitHub Container Registry (GHCR)
- Private registries
- Authentication & access tokens

---

## Folder Structure

```
DevOps_Docker_Lab/
├── 01_Dockerfile_Basics/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── .dockerignore
├── 02_Image_Building/
│   ├── Dockerfile.multistage
│   └── app/
├── 03_Networking/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── docker-compose.yml
│   └── html/
├── 04_Storage/
│   ├── Dockerfile
│   └── entrypoint.sh
├── 05_Registries/
│   └── registry_commands.md
├── screenshots/
│   └── *.png  (30 terminal screenshots)
└── README.md
```

---

## Student Info
- **Name:** Anura
- **Subject:** DevOps
- **Semester:** 6
