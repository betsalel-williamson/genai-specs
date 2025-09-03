# Docker Hardening & Optimization Best Practices

* **Multi-stage builds:** Minimize final image size.
* **Non-root user:** Run containers as a non-root user.
* **Clean up:** Remove build tools and caches in final image.
* **Pin versions:** Always pin dependency versions.
* **.dockerignore:** Exclude unnecessary files.
* **Image scanning:** Scan images (for example, with Trivy) before publishing.
