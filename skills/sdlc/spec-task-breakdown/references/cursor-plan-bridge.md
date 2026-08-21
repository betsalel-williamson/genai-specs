# Active Work Tracking with Cursor Plans (Cursor-Specific)

**Note:** This section is specific to development workflows using Cursor's planning system. If using a different IDE or planning system, adapt this pattern to match that system's conventions.

## Symlink Pattern for Active Features

When actively working on a feature, create a symbolic link from `.cursor/plans/` to the canonical task file in `.work-items/{feature_name}/task.md`. This establishes a clear bridge between:

1. **Canonical source of truth**: `.work-items/{feature_name}/task.md` - the permanent, version-controlled task breakdown
2. **Active planning workspace**: `.cursor/plans/{feature_name}-task.plan.md` - symlink for easy access during active development

## Creating the Symlink

From the project root:

```bash
cd .cursor/plans
ln -s ../../.work-items/{feature_name}/task.md {feature_name}-task.plan.md
```

## Naming Convention

- **Task breakdown symlinks**: `{feature_name}-task.plan.md`
- **Implementation plans**: `{feature_name}-{description}-{uuid}.plan.md`

This convention makes it immediately clear which files are task definitions versus implementation plans.

## Symlink Lifecycle

- **Create**: When beginning active work on a feature
- **Maintain**: The symlink remains while work is in progress
- **Remove**: When work is complete, paused, or moved to a different phase
- **Preserve**: The original `.work-items/{feature_name}/task.md` is never deleted

## Benefits

- **Single source of truth**: All edits to either file location are automatically synchronized
- **Easy discovery**: Active work is visible in `.cursor/plans/` directory
- **No duplication**: Eliminates the need to maintain separate copies
- **Clear lifecycle**: Symlink presence indicates active work status
- **Version control friendly**: Symlinks are tracked in git, showing which features are active

## Example Directory Structure

```txt
/.work-items/single-face-scan/
├── task.md                    # Canonical task definition
├── 01_setup.md
└── 02_implementation.md

/.cursor/plans/
├── single-face-scan-task.plan.md              # Symlink → ../../.work-items/single-face-scan/task.md
```
