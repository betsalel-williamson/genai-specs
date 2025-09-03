# Docker Multi-Stage Build Key Stages

* **`builder`:** Installs all dependencies (including `devDependencies`) and build tools. Builds the application.
* **`pruner`:** Takes `node_modules` from `builder`, removes `devDependencies`, leaving only production dependencies.
* **`final`:** Production stage. Copies pruned `node_modules` and built application. Creates non-root user.
