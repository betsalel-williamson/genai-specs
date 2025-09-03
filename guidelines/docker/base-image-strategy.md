# Docker Base Image Strategy

We use a polyglot approach for base images to optimize and secure each language runtime independently.

* **Node.js:** Uses `Dockerfile.base` (to be hardened for dev/prod).
* **Python:** Uses a separate `Dockerfile.base` (to be created and hardened).
