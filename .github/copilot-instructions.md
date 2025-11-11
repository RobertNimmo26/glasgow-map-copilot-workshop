# 🧑‍💻 Copilot Coding Agent Instructions for Glasgow Workshop

## Project Overview
This repository is a sandbox for experimenting with GitHub Copilot, Copilot Chat, and the Copilot Coding Agent. The main example is a minimal Flask app (`app.py`) that serves a Glasgow Tree Preservation Map at the root URL. The project is designed for rapid prototyping and learning Copilot workflows, not for production use.

## Architecture & Key Files
- `app.py`: Minimal Flask web server. Entry point for all code experiments.
- `.vscode/mcp.json`: Configuration for MCP server integration. Required for Copilot Coding Agent and issue workflows.
- `README.md`: Workshop playbook and step-by-step instructions for using Copilot features in this repo.

## Developer Workflows
- **Run the app:**
  - Install dependencies: `pip install flask`
  - Start server: `python3 app.py`
  - Access at: `http://localhost:5000/`
- **No virtual environment is required.** Use system Python and pip for simplicity.
- **Branching:** All experiments should be done in a dedicated branch (e.g., `copilot-workshop`).
- **MCP Integration:** Ensure `.vscode/mcp.json` is present and configured before using Copilot Coding Agent features.

## Patterns & Conventions
- Keep code changes minimal and focused on learning Copilot features.
- Prefer single-file scripts for clarity and ease of experimentation.
- Document any new workflows or patterns in the `README.md` for future reference.
- Use Copilot Chat to generate, explain, and refactor code. Follow up with clarifying questions for deeper understanding.

## Integration Points
- **Flask** is the only external dependency. No database, authentication, or advanced integrations are present.
- **Copilot MCP** enables advanced AI workflows (issue management, agent assignment, PR reviews).

## Examples
- To add a new route, edit `app.py` and define a new `@app.route` function.
- To experiment with Copilot Coding Agent, create an issue describing the change, then assign it to Copilot.

## References
- See `README.md` for workshop steps and Copilot feature usage.
- See `.vscode/mcp.json` for MCP configuration details.

---

**For AI agents:**
- Always check `README.md` for the latest workflow and conventions.
- Keep changes isolated to the current branch unless instructed otherwise.
- Use Copilot Chat and Coding Agent features to automate, explain, and document your work.
