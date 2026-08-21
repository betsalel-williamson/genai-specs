# Node.js/TypeScript Module Resolution Complexities

**Rationale:** Understanding how Node.js resolves modules, especially with TypeScript compilation targets (CommonJS vs. ES Modules) and external libraries, is crucial for avoiding subtle bugs and build issues.

**Guideline:**

- **Prefer ES Modules (`import`/`export`)**: When starting new modules or projects, favor ES Module syntax. This is the modern standard and aligns with browser environments.
- **Be Aware of `package.json` `"type"` field**: The `"type": "module"` in `package.json` dictates how Node.js treats `.js` files (as ES Modules). If omitted or set to `"commonjs"`, `.js` files are treated as CommonJS.
- **Transpilation Targets**: When compiling TypeScript, the `"module"` option in `tsconfig.json` (for example, `"commonjs"`, `"esnext"`) significantly impacts how imports/exports are generated. Mismatches between the Node.js runtime expectation and the compiled output are a common source of `TypeError: xxx isn't a function` or `ERR_UNKNOWN_FILE_EXTENSION`.
- **External Library Imports**: Some older or specific libraries might still primarily expose CommonJS modules. When importing these into an ES Module context (or vice-versa), you might need to use specific import syntaxes (for example, `import * as library from 'library';` or `const library = require('library');`) or rely on bundlers to handle the import.
- **`ts-node` and Runtime Execution**: While `ts-node` simplifies direct execution of TypeScript files, it can sometimes mask underlying module resolution issues that become apparent in compiled environments or specific Node.js versions. For robust scripts, consider compiling to JavaScript first and then running the compiled output.
- **Default vs. Named Exports**: Pay close attention to whether a module exports a `default` or `named` exports. Incorrectly importing a default export as a named one (or vice-versa) is a frequent cause of `TypeError: xxx isn't a function`.
