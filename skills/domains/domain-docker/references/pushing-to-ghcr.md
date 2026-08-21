# Docker Pushing to GitHub Container Registry (GHCR)

## Authenticate

```sh
echo $GITHUB_TOKEN | docker login ghcr.io -u <your-github-username> --password-stdin
```

## Push Image

```sh
docker push ghcr.io/<your-org>/<image-name>:<tag>
```
