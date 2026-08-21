# Docker Multi-Stage Build Strategy

- **Per-Service Dockerfiles:** Each Node.js or Python service has its own `Dockerfile`.
- **Optimization:** Multi-stage builds optimize image size and security.
- **Current Base Images:** Currently use official base images (for example, `node:XX`, `python:3.12-slim`).
- **Future:** Will introduce hardened, organization-specific base images (`Dockerfile.base`).
