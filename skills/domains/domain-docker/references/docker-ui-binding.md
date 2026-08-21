# Docker UI Not Accessible from Host

**Date:** 2025-07-21

## Problem

Dagster UI was not accessible from the host, despite port forwarding. Logs showed Dagster listening on `127.0.0.1:3000` inside the container.

## Solution

Modified `Dockerfile` `CMD` to include `--host 0.0.0.0` for `dg dev` command, binding Dagster to all interfaces.

## Impact

Prevents external access to containerized services if they default to `127.0.0.1`. Causes significant debugging time.

## Takeaways

- Verify listening address (`0.0.0.0` for external access).
- Applications often default to `127.0.0.1` for security; override explicitly.
- Use `docker logs` to check internal application binding issues early.
