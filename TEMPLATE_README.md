# Microsoft Certification Study Buddy Template

This workspace serves as a **template** for generating personalized Microsoft certification study companions using GitHub Copilot.

## What This Template Does

This template can generate a complete certification study buddy workspace for any Microsoft certification exam, including:

- **AI-102** - Designing and Implementing a Microsoft Azure AI Solution
- **AZ-900** - Microsoft Azure Fundamentals
- **AZ-104** - Microsoft Azure Administrator
- **AZ-204** - Developing Solutions for Microsoft Azure
- **DP-900** - Microsoft Azure Data Fundamentals
- **SC-900** - Microsoft Security, Compliance, and Identity Fundamentals
- **And any other Microsoft certification exam**

## Generated Workspace Structure

Each generated certification study buddy includes:

```
<exam-name>-cert-buddy/
├── .github/
│   ├── agents/
│   │   └── <exam>-cert-buddy-agent.agent.md
│   ├── prompts/
│   │   ├── <exam>-practice-questions.prompt.md
│   │   └── <exam>-practice-lab.prompt.md
│   ├── skills/
│   │   ├── <exam>-item-creator/
│   │   │   └── SKILL.md
│   │   ├── <exam>-lab-creator/
│   │   │   └── SKILL.md
│   │   └── <exam>-study-planner/
│   │       └── SKILL.md
│   └── copilot-instructions.md
├── .vscode/
│   └── mcp.json
├── references/
│   ├── <exam>-objectives.md
│   ├── fictional-companies.md
│   └── style-guide.md
├── README.md
└── .gitignore
```

## Features

### 1. **Practice Questions (Item Creator)**
- Generates exam-realistic practice questions
- Scenario-first approach with plausible distractors
- Two-phase interactive delivery (question first, then rationale after user responds)
- Grounded in Microsoft Learn documentation
- Supports hints and skip options

### 2. **Hands-on Labs (Lab Creator)**
- Creates 10-20 minute focused labs
- Includes validation steps after each task
- Complete cleanup instructions
- Cost-aware (warns about charges)
- Validated with Azure MCP for accuracy

### 3. **Study Planner**
- Personalized study plans based on confidence assessment
- Prioritizes weak areas and high-weight topics
- Provides estimated study hours
- Links to specific Microsoft Learn modules
- Day-by-day breakdown with progress tracking

## How to Use This Template

### Option 1: Use the Generator Agent (Recommended)

Ask the **cert-buddy-generator** agent to create a new certification workspace:

```
@cert-buddy-generator Create a study buddy for AZ-204
```

The agent will:
1. Ask you to confirm the exam details
2. Fetch the official objectives from Microsoft Learn
3. Generate all workspace files with proper structure
4. Set up MCP server configurations
5. Create README with getting started instructions

### Option 2: Manual Setup

If you want to manually create a certification study buddy:

1. Copy this template structure
2. Replace all instances of `<exam>` with your exam code (e.g., `az204`, `sc900`)
3. Update the objectives file from Microsoft Learn
4. Customize the copilot-instructions.md with exam-specific terminology
5. Adjust the agent, prompts, and skills to match the exam domain

## Current Template (AI-102)

This workspace is the **reference implementation** for the template, configured for:
- **Exam:** AI-102 - Designing and Implementing a Microsoft Azure AI Solution
- **Domain:** Azure AI services, NLP, Computer Vision, Knowledge Mining

## MCP Servers Used

All generated workspaces include three MCP servers:

1. **Context7 MCP** - Access to Microsoft Learn documentation
2. **Azure MCP** - Validate Azure commands and resources
3. **MarkItDown MCP** - Convert documentation formats

## Prerequisites

- Visual Studio Code with GitHub Copilot
- Node.js (for Context7 and Azure MCP)
- Python with uvx (for MarkItDown MCP)
- Azure subscription (optional, for hands-on labs)

## Getting Started After Generation

1. Open the generated workspace in VS Code
2. The agent will be automatically available as `@<exam>-cert-buddy-agent`
3. Start by asking for a study plan: `@<exam>-cert-buddy-agent help me create a study plan`
4. Generate practice questions: `@<exam>-cert-buddy-agent give me a practice question on [topic]`
5. Create hands-on labs: `@<exam>-cert-buddy-agent create a 15-minute lab on [topic]`

## Example Commands

- `@az204-cert-buddy-agent Create a study plan for Azure Developer`
- `@az900-cert-buddy-agent Give me 5 practice questions on Azure basics`
- `@dp900-cert-buddy-agent Create a lab on Azure SQL Database`

## Contributing

This template is designed to be:
- **Extensible** - Easy to add new exam types
- **Maintainable** - Centralized terminology and style rules
- **Consistent** - All generated workspaces follow the same structure

## License

MIT License - Feel free to use this template for any Microsoft certification exam preparation.

---

**Ready to generate your certification study buddy?** Ask the generator agent to get started! 🚀
