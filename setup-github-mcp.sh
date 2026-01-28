#!/bin/bash
# GitHub MCP Server Setup Script

echo "Setting up GitHub MCP server integration..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
    echo "Please edit .env to add your GitHub token"
fi

# Verify that the MCP servers directory exists
if [ ! -d ".mcp-servers" ]; then
    echo "Creating .mcp-servers directory..."
    mkdir -p .mcp-servers
fi

# Show the configuration
echo "GitHub MCP server configuration created:"
echo "- Config file: .mcp-servers/github-config.json"
echo "- Environment example: .env.example"
echo "- Documentation: docs/github-mcp-integration.md"

echo ""
echo "Next steps:"
echo "1. Edit .env file to add your GitHub token"
echo "2. Review the documentation in docs/github-mcp-integration.md"
echo "3. Ensure your token has appropriate permissions"