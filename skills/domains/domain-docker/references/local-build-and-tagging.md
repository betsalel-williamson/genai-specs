# Docker Local Build & Tagging

## Build and Tag

```sh
docker build -t ghcr.io/<your-org>/<image-name>:<tag> -f dagster_project/Dockerfile .
```

## Tag Existing Image

```sh
docker tag <local-image>:latest ghcr.io/<your-org>/<image-name>:<tag>
```
