# MCP Skills Server Setup

Optional MCP bridge for loading the same skill tree outside native Cursor skill discovery.

## Recommended server

Evaluate [dunialabs/mcp-skills](https://github.com/dunialabs/mcp-servers/tree/HEAD/mcp-skills) or any MCP server implementing:

- `listSkills`
- `getSkill`
- `readSkillFile`

## Project config stub

See [`.mcp/skills-server.json`](../../.mcp/skills-server.json) for a documented example pointing at `./skills`.

Add to `.cursor/mcp.json` when ready:

```json
{
  "mcpServers": {
    "genai-specs-skills": {
      "command": "npx",
      "args": ["-y", "@dunialabs/mcp-skills", "/absolute/path/to/genai-specs/skills"]
    }
  }
}
```

Replace the package and args with your chosen MCP skills server.

## Boundaries

- **Skills** (`skills/`): procedural SDLC knowledge, progressive markdown loading
- **MCP tools**: external APIs, databases, GitHub, filesystem operations
- Use `markdown-context-protocol` for in-repo reference sharding without MCP

## Arm C eval

Arm C in the A/B matrix enables this MCP server alongside native skills. Compare trigger accuracy and token usage against Arm B.
