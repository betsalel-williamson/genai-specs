# Recommended Dockerfile Structure

Follow a multi-stage build pattern for Node.js (with `pnpm`, `sqlite3`) and Python applications to optimize image size and security. This structure leverages Docker's build cache and minimizes the final image size.

## Key Stages & Purpose

- **`base`:** Defines the base image (for example, `node:20-slim`, `python:3.12-slim`), sets the working directory, and includes common setup like enabling `corepack` for Node.js.
- **`builder`:** This stage is for all build-time operations. It installs build dependencies (for example, `build-essential`, `python3` for native addons), copies source code, installs _all_ project dependencies (including `devDependencies`), and performs the application build (for example, `pnpm run build`).
- **`pruner` (Node.js specific):** For Node.js applications, this optional stage takes the `node_modules` from the `builder` stage and removes `devDependencies`, leaving only the production dependencies. This significantly reduces the final image size.
- **`final`:** This is the lean production stage. It copies only the necessary artifacts (pruned `node_modules`, built application code) from previous stages. It sets up a non-root user for security, exposes application ports, and defines the `CMD` to run the application.

## Example Structure (Conceptual)

```dockerfile
# ---- Base Stage ----
FROM <base-image> AS base
WORKDIR /app
# RUN <common_setup_commands>

# ---- Builder Stage ----
FROM base AS builder
# RUN <install_build_dependencies>
COPY package.json pnpm-lock.yaml ./
# RUN <install_all_dependencies>
COPY . .
# RUN <build_application>

# ---- Pruner Stage (Node.js specific) ----
FROM base AS pruner
WORKDIR /app
COPY --from=builder /app/package.json /app/pnpm-lock.yaml ./
COPY --from=builder /app/node_modules ./node_modules
# RUN <prune_dev_dependencies>

# ---- Final Production Stage ----
FROM base AS final
WORKDIR /app

# RUN <create_and_switch_to_non_root_user>
USER <non-root-user>

COPY --from=pruner --chown=<user>:<group> /app/node_modules ./node_modules # For Node.js
# COPY --from=builder --chown=<user>:<group> /app/<built-code> ./<built-code>

EXPOSE <port>

CMD ["<command_to_run_app>"]
```
