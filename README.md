# AI Agent Integration Hub — MCP Server

## Setup

\`\`\`powershell
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
\`\`\`

## Run

\`\`\`powershell
python server.py
\`\`\`

(Hangs with no output — that's normal for stdio, it's waiting for input.)

## Test with Inspector

\`\`\`powershell
npx @modelcontextprotocol/inspector "C:\path\to\.venv\Scripts\python.exe" server.py
\`\`\`

Open the URL it gives you, check connection status, go to **Tools** tab, run a tool.

## Adding new packages

\`\`\`powershell
uv pip install <package>
uv pip freeze > requirements.txt
\`\`\`

## Common issue

"Connection closed" / exit code 1 → server crashed on startup. Run `python server.py` directly to see the error. Also check for stray `print()` statements — they break the stdio connection.