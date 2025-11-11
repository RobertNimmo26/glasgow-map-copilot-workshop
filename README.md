# 🚀 GitHub Copilot Glasgow Workshop
# https://github.com/eroullit/glasgow-workshop

Welcome to the **GitHub Copilot Workshop playbook**!  
This workshop walks you through the newest Copilot capabilities — from *Ask* and *Edit* modes to *MCP-enabled issues*, the *Copilot Coding Agent*, and *AI PR reviews*.  
You’ll stay inside your own directory or repository, freely experimenting and discovering how Copilot reshapes everyday workflows.

---

## 🧭 Phase 1 – Setup & Preparation

**Goal:** Ready your environment and repository for Copilot experiments.

<details>
<summary>🔹 <b>1️⃣ Find a project or start from scratch and follow my lead! </b></summary>

- [ ] Choose a repository you’re comfortable iterating on — any language qualifies.  
  You can:
  - Work in a project you already maintain.  
  - Fork a public repo (browse [GitHub Explore](https://github.com/explore) for inspiration).
  - Start fresh and follow me where we will create a Python-based App.

- [ ] Copy these workshop notes into a new issue inside your repo so you can tailor them.  

- [ ] Git branches are cheap! Create a **dedicated branch**, e.g. `copilot-workshop`.  
  Keep all experiments here — avoid touching `main`.

> ⚠️ Copilot never commits without confirmation, but keeping the branch isolated protects your mainline.
</details>

---

<details>
<summary>🔹 <b>2️⃣ Ensure GitHub Copilot is enabled</b></summary>

- [ ] Confirm the **GitHub Copilot** extension is installed and active in your IDE.  
- [ ] Verify **Copilot Chat** is available (and optionally **Copilot Edits/Agent** if your IDE supports them).

📘 **Documentation:**
- [Getting started with GitHub Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/get-started/quickstart)
- [Setting up GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/setup)

> 💡 No need for separate installs — Copilot Chat and Edits ship with most IDE integrations.  
> Just make sure both completions and chat panes are visible.

⚠️ In case network restrictions are in place, [GitHub Codespaces](https://github.com/codespaces) can be used to create an ad-hoc development environment and experiment there.

</details>

---

<details>
<summary>🔹 <b>3️⃣ Configure the GitHub MCP server</b></summary>

We’ll use **Copilot MCP** so Copilot Chat can tap into your repo and issues.

- [ ] In your **feature branch**, ensure a `.vscode` folder exists (create it if needed).  
- [ ] Inside it, add a file named `mcp.json`.  
- [ ] Copy the content from 👉 [`.vscode/mcp.json`](https://github.com/eroullit/glasgow-workshop/blob/main/.vscode/mcp.json).  
- [ ] Commit the file on your branch.
- [ ] In VS Code, click the “start” link at the top of that `mcp.json` definition.

📘 **Learn more:**  
[Understanding MCP and connecting Copilot to external resources](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
</details>

---

## 💬 Phase 2 – Exploring Copilot Chat Modes

**Goal:** See how Copilot helps you investigate, understand, and reason about your code.

<details>
<summary>🔹 <b>4️⃣ Explore your code using Ask mode</b></summary>

Pick a file or function you seldom touch and experiment freely with **Copilot Chat**.

Prompt ideas:
- [ ] “Explain what this function does, step by step.”  
- [ ] “Where is this class referenced?”  
- [ ] “Could this function be simplified?”  
- [ ] “Generate a test for this logic.”  
- [ ] “Rewrite this using a different algorithm.”  

💡 **Stay curious.** Follow up with why/how questions, modify prompts, and try *Ask*, *Explain*, *Generate*, and *Edit* to compare behaviors.

- [ ] Switch between models (e.g. `GPT-5`, `Claude Sonnet 4.5`, `Claude Haiku 4.5`, `Gemini 2.5 Pro` ) and note reasoning differences.

📘 [Use Copilot Chat to understand code](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/explore-a-codebase)
</details>

---

<details>
<summary>🔹 <b>5️⃣ Generate a <code>copilot_instructions.md</code> file</b></summary>

Copilot can auto-generate **project context notes** — this file boosts Copilot’s understanding of your codebase.

### 💡 Why this matters
`copilot_instructions.md` works as a **briefing document** for Copilot.  
It covers:
- Project layout  
- Build/run steps  
- Key dependencies, conventions, and directories  

With this reference in place, Copilot can:
- Answer project questions more precisely.  
- Provide stronger suggestions for refactors, debugging, and tests.  
- Keep terminology and architecture choices consistent.

### 🧭 Steps
- [ ] Open the **Command Palette** (`Ctrl/Cmd + Shift + P`).  
- [ ] Search for **“Copilot: Generate Project Instructions”**.  
- [ ] Follow the prompts to create `copilot_instructions.md`.  

After generation, skim the file and add any clarifications you want Copilot to remember.

📘 **Documentation:**  
[Generate project instructions with Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
</details>

---

## 🧩 Phase 3 – Working with Issues via MCP

**Goal:** Use Copilot’s MCP connection to explore, discuss, and file issues.

<details>
<summary>🔹 <b>6️⃣ Explore and discuss issues (via MCP)</b></summary>

With the `github-remote` MCP server running:

- [ ] Ask Copilot Chat to list or summarize issues in your repo.  
  Example prompts:
  - “List open issues in this repo.”  
  - “Summarize issue #12.”  
  - “Suggest next steps for this bug.”  
  - “Where could we tighten code related to this issue?”

📘 [Using GitHub Copilot in Issues](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide)
</details>

---

<details>
<summary>🔹 <b>7️⃣ Analyze code relevant to an issue</b></summary>

- [ ] Pick a compelling issue.  
- [ ] Ask Copilot to point to the code surface area or describe the relevant logic.

Try:
> “Show me where this issue might originate in the code.”  
> “Explain how this module works.”  
> “What inputs could trigger this behavior?”
</details>

---

<details>
<summary>🔹 <b>8️⃣ Generate a new issue</b></summary>

After discussing a change, let Copilot Chat draft an issue.

- [ ] “Generate a new issue proposing a refactor of this method.”  
- [ ] “File an issue to add input validation.”  

Let Copilot supply the title, body, and context directly.
</details>

---

<details>
<summary>🔹 <b>9️⃣ Assign the new issue to Copilot Coding Agent</b></summary>

Choose one workflow:

- [ ] In Copilot Chat, say **“Assign this issue to the Copilot Coding Agent.”**  
- [ ] **Or** on **GitHub.com** → open the issue → click **Assignees** → select **@copilot**.

Watch how the Coding Agent interprets and plans the task.

📘 [Copilot Coding Agent overview](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
</details>

---

## 🧮 Phase 4 – Reviewing and Reflection

**Goal:** Let Copilot help review and reason about existing work.

<details>
<summary>🔹 <b>🔟 Request a Copilot code review (on GitHub.com)</b></summary>

- [ ] Visit your repository on **GitHub.com**.  
- [ ] Locate an existing Pull Request (your project or your branch).  
- [ ] Add **@copilot** as a reviewer.  

Copilot analyzes the diff and posts comments on the PR.

> ⚠️ This updates the PR with Copilot’s remarks.  
> 💡 Prefer a sandbox? Duplicate the PR from your workshop branch and request Copilot there to keep the original untouched.

📘 [Using Copilot for Pull Request reviews](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review)
</details>

---

## 🧠 Optional – Share Your Insights

- [ ] What surprised you most about Copilot’s behavior?  
- [ ] Did different models produce noticeably different answers?  
- [ ] Which feature felt most natural or valuable?

---

## ✅ Completion Checklist

| Step | Description | Done |
|------|--------------|------|
| 1 | Fork / create project branch | ☐ |
| 2 | Enable Copilot and Chat | ☐ |
| 3 | Add `.vscode/mcp.json` (in branch) | ☐ |
| 4 | Explore Ask mode + models | ☐ |
| 5 | Generate `copilot_instructions.md` | ☐ |
| 6–9 | Work with issues & Coding Agent | ☐ |
| 10 | Assign PR to Copilot for review | ☐ |
| ✨ | Share insights | ☐ |

---

Happy hacking — enjoy the exploration! 🎉
