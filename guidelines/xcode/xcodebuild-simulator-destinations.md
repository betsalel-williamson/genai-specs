# xcodebuild Simulator Destination Configuration

## Problem

When specifying iOS simulator destinations with xcodebuild, including an explicit OS version parameter can fail with "iOS X.0 is not installed" even when point releases (e.g., iOS 18.4, 18.5, 18.6) are available.

This typically manifests in CI environments where only specific iOS runtime versions are installed:

```bash
xcodebuild -destination 'platform=iOS Simulator,OS=18.4,name=iPhone 16 Pro'
# Error: Unable to find a destination matching the provided destination specifier:
#        { platform:iOS Simulator, OS:18.4, name:iPhone 16 Pro }
# Ineligible destinations for the "MyScheme" scheme:
#        { platform:iOS, ..., error:iOS 18.0 is not installed. To use with Xcode,
#          first download and install the platform }
```

The issue occurs because xcodebuild looks for the base platform SDK (iOS 18.0) when an OS parameter is provided, even though point releases are installed.

## Solution

Omit the OS parameter from the destination specifier and let xcodebuild automatically select the appropriate runtime:

```bash
# ❌ Don't specify OS version
xcodebuild -destination 'platform=iOS Simulator,OS=18.4,name=iPhone 16 Pro'

# ✅ Let xcodebuild auto-select runtime
xcodebuild -destination 'platform=iOS Simulator,name=iPhone 16 Pro'
```

### Makefile Implementation

```makefile
# Auto-detect first available iPhone simulator
comma := ,

# Detect first available iPhone simulator from any available runtime
DETECTED_DEVICE := $(shell xcrun simctl list devices available 2>/dev/null | \
                    grep -m 1 "iPhone" | awk '{print $$1,$$2,$$3}' | xargs)
ifeq ($(DETECTED_DEVICE),)
DETECTED_DEVICE := iPhone 15
endif

# Don't specify OS - let xcodebuild pick the right runtime automatically
SIMULATOR ?= platform=iOS Simulator$(comma)name=$(DETECTED_DEVICE)
```

### Why This Works

When the OS parameter is omitted, xcodebuild:
1. Identifies the specified device name
2. Automatically selects the most appropriate runtime from available options
3. Doesn't require the base SDK version to be installed

This approach is more robust across different CI environments and developer machines with varying iOS runtime installations.

### GitHub Actions Integration

For CI/CD pipelines using GitHub Actions, see [GitHub Actions iOS CI](../github/github-actions-ios-ci.md) for comprehensive guidance on:
- Matrix strategies for multi-version testing
- Xcode version selection
- Environment configuration
- Device-version pairing

The key difference between local and CI configuration:
- **Local**: Omit OS parameter for automatic runtime selection
- **CI**: Specify exact OS versions for controlled testing across multiple runtimes

## Impact

- Eliminates CI failures due to missing base iOS SDK versions
- Works reliably across different Xcode and iOS runtime configurations
- Reduces maintenance overhead by not requiring runtime version management
- Improves local development experience with diverse simulator configurations

## Takeaways

- **Local development**: Omit the OS parameter and let xcodebuild auto-select the runtime
- **CI/CD**: Explicitly specify OS versions to test against multiple runtimes (see [GitHub Actions iOS CI](../github/github-actions-ios-ci.md))
- Use `xcrun simctl list runtimes available` to see what runtimes are actually installed
- Auto-detection in Makefiles provides robust local development experience
- Pair device names appropriately with iOS versions (e.g., iPhone 17 Pro for iOS 26.0)

