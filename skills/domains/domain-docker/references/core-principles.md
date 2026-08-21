# Docker Core Principles

Build optimized Docker images for Node.js (with `pnpm`, `sqlite3`) and Python applications. Focus on small, secure, and efficient images.

- **Multi-stage Builds:** Separate build from production for lean images.
- **Lean Base Images:** Use minimal images (for example, `node:20-slim`) to reduce size and attack surface.
- **Layer Caching:** Structure `Dockerfile` to leverage caching (install dependencies before copying code).
- **Non-root User:** Run applications as a non-root user for security.
