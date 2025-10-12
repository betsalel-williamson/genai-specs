# GitHub Actions iOS CI/CD

## Problem

Setting up continuous integration for iOS projects in GitHub Actions requires careful configuration of Xcode versions, iOS runtimes, and simulator destinations to ensure comprehensive testing across multiple iOS versions.

## Solution

### Xcode Version Selection

Ensure your CI environment has the matching Xcode version with the required iOS SDK. Different Xcode versions include different iOS SDKs.

```yaml
- name: Select Xcode version with iOS 18.x SDK
  run: |
    # Use Xcode 16.1+ which includes iOS 18.x SDKs
    if [ -d "/Applications/Xcode_16.4.app" ]; then
      sudo xcode-select -s /Applications/Xcode_16.4.app/Contents/Developer
    else
      sudo xcode-select -s /Applications/Xcode_16.1.app/Contents/Developer
    fi
```

### Matrix Strategy for Multi-Version Testing

Use a matrix strategy to test against multiple iOS versions:

```yaml
jobs:
  build-and-test:
    name: Build and Test (iOS ${{ matrix.ios-version }})
    runs-on: macos-15

    strategy:
      fail-fast: false
      matrix:
        ios-version: ['18.4', '18.5', '18.6', '26.0']
        include:
          - ios-version: '18.4'
            device: 'iPhone 16 Pro'
          - ios-version: '18.5'
            device: 'iPhone 16 Pro'
          - ios-version: '18.6'
            device: 'iPhone 16 Pro'
          - ios-version: '26.0'
            device: 'iPhone 17 Pro'

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Select Xcode version
      run: sudo xcode-select -s /Applications/Xcode_16.4.app/Contents/Developer

    - name: Run CI pipeline
      env:
        SIMULATOR: 'platform=iOS Simulator,OS=${{ matrix.ios-version }},name=${{ matrix.device }}'
      run: make ci
```

### Key Configuration Points

1. **fail-fast: false**: Ensures all matrix jobs run even if one fails, providing complete test coverage results
2. **Device-version pairing**: Match device names to appropriate iOS versions (e.g., iPhone 17 Pro for iOS 26.0)
3. **Explicit OS versions**: In CI, specify exact iOS versions to test against multiple runtimes
4. **Runner selection**: Use `macos-15` or later for recent Xcode versions

### Local vs CI Configuration

**Local Development**:
```bash
# Omit OS parameter for auto-selection
SIMULATOR='platform=iOS Simulator,name=iPhone 16 Pro'
```

**CI/CD**:
```bash
# Specify exact OS version for matrix testing
SIMULATOR='platform=iOS Simulator,OS=18.4,name=iPhone 16 Pro'
```

See [xcodebuild Simulator Destinations](../xcode/xcodebuild-simulator-destinations.md) for detailed explanation of destination configuration.

## Impact

- Provides comprehensive testing across multiple iOS versions
- Clear feedback if specific versions fail
- Reduces maintenance overhead with automated testing
- Improves confidence in iOS compatibility

## Takeaways

- Use matrix strategy to test multiple iOS versions in parallel
- Set `fail-fast: false` to run all matrix jobs
- Pair device names appropriately with iOS versions
- Select appropriate Xcode version for target iOS SDK
- Explicitly specify OS versions in CI for controlled testing
- Use environment variables to pass configuration to Makefile

