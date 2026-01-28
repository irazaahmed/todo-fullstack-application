# GitHub MCP Server Integration

This project includes integration with GitHub via Model Context Protocol (MCP) server configuration.

## Setup

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Add your GitHub Personal Access Token to the `.env` file:
   ```
   GITHUB_TOKEN=your_actual_token_here
   ```

3. The token should have appropriate scopes for the operations you want to perform.

## Security Notice

⚠️ **Important Security Information:**
- Never commit the `.env` file to version control
- The `.env` file is already included in `.gitignore`
- Keep your GitHub token secure and limit its scope to only necessary permissions
- Regenerate the token if it's ever compromised

## Configuration

The GitHub MCP server configuration is located in `.mcp-servers/github-config.json` and provides endpoints for:
- Repository information retrieval
- Issue management
- Pull request listing
- User information retrieval

## Required Token Scopes

Depending on your usage, you may need one or more of these scopes:
- `repo` - for repository operations
- `read:user` - for reading user information
- `gist` - for gist operations
- `notifications` - for notifications access