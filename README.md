# Microsoft Certification Study Buddy Template 🎓

**AI-powered study companion generator for Microsoft certification exams**

This repository serves as a **template and generator** for creating personalized Microsoft certification study buddy workspaces powered by GitHub Copilot, MCP servers, and AI agents.

## 🌟 What This Does

Automatically generates a complete, production-ready study workspace for **any Microsoft certification exam**, including:

- ✅ **AI-102** - Designing and Implementing a Microsoft Azure AI Solution
- ✅ **AZ-900** - Microsoft Azure Fundamentals  
- ✅ **AZ-104** - Microsoft Azure Administrator
- ✅ **AZ-204** - Developing Solutions for Microsoft Azure
- ✅ **AZ-305** - Designing Microsoft Azure Infrastructure Solutions
- ✅ **DP-900** - Microsoft Azure Data Fundamentals
- ✅ **DP-203** - Data Engineering on Microsoft Azure
- ✅ **SC-900** - Microsoft Security, Compliance, and Identity Fundamentals
- ✅ **SC-200** - Microsoft Security Operations Analyst
- ✅ **MS-900** - Microsoft 365 Fundamentals
- ✅ **Any other Microsoft certification!**

## 🎯 Key Features

### 1. **Interactive Practice Questions**
- Exam-realistic scenarios with plausible distractors
- Two-phase delivery: question first, then answer after your response
- Detailed rationales for every option
- Supports hints and skip options
- Grounded in official Microsoft Learn documentation

### 2. **Hands-on Labs (10-20 minutes)**
- Focused, single-objective labs
- Step-by-step validation checkpoints
- Complete cleanup instructions
- Cost-aware (warns about Azure charges)
- Validated with Azure MCP for accuracy

### 3. **Personalized Study Planner**
- Confidence-based assessment across skill areas
- Prioritizes weak areas and high-weight topics
- Estimated study hours per area
- Direct links to Microsoft Learn modules
- Day-by-day study schedule with progress tracking

## 🚀 Quick Start

### Option 1: Use the Generator Agent (Easiest)

1. Clone this repository (the AI-102 template):
   ```bash
   git clone <this-repo-url>
   cd ai-102-cert-buddy
   code .
   ```

2. Ask the generator agent:
   ```
   @cert-buddy-generator Create a study buddy for AZ-204
   ```

3. The agent will:
   - Confirm exam details
   - Fetch official objectives from Microsoft Learn
   - Generate all workspace files
   - Configure MCP servers
   - Create a complete README

### Option 2: Use the Python Script

```bash
python generate_cert_buddy.py --exam AZ-204 \
  --name "Developing Solutions for Microsoft Azure" \
  --domain "Azure Development" \
  --output ../az204-cert-buddy
```

### Option 3: Manual Setup

1. Copy this template structure
2. Replace `ai102` with your exam code (e.g., `az204`)
3. Update objectives from Microsoft Learn
4. Customize copilot-instructions.md
5. Adjust agent, prompts, and skills

## 📁 Generated Workspace Structure

```
<exam-code>-cert-buddy/
├── .github/
│   ├── agents/
│   │   └── <exam>-cert-buddy-agent.agent.md      # Main AI agent
│   ├── prompts/
│   │   ├── <exam>-practice-questions.prompt.md   # Question generator
│   │   └── <exam>-practice-lab.prompt.md         # Lab generator
│   ├── skills/
│   │   ├── <exam>-item-creator/SKILL.md          # Question creation skill
│   │   ├── <exam>-lab-creator/SKILL.md           # Lab creation skill
│   │   └── <exam>-study-planner/SKILL.md         # Study planning skill
│   └── copilot-instructions.md                   # Copilot context
├── .vscode/
│   └── mcp.json                                   # MCP server config
├── references/
│   ├── <exam>-objectives.md                       # Official exam objectives
│   ├── fictional-companies.md                     # Scenario companies
│   └── style-guide.md                            # Microsoft style guide
├── README.md                                      # Getting started guide
└── .gitignore
```

## 🛠️ How It Works

### 1. **GitHub Copilot Agents**
Each generated workspace includes a specialized agent (`@<exam>-cert-buddy-agent`) that:
- Understands the exam objectives
- Generates realistic practice questions
- Creates validated hands-on labs
- Builds personalized study plans

### 2. **MCP Servers**
Three Model Context Protocol servers provide real-time data:
- **Context7** - Access to Microsoft Learn documentation
- **Azure MCP** - Validates Azure commands and resources  
- **MarkItDown** - Converts documentation formats

### 3. **Agent Skills**
Three specialized skills handle different tasks:
- **Item Creator** - Generates exam-realistic practice questions
- **Lab Creator** - Creates hands-on labs with validation
- **Study Planner** - Builds personalized study schedules

## 📋 Prerequisites

- **Visual Studio Code** with GitHub Copilot
- **Node.js** (v18 or later) for Context7 and Azure MCP
- **Python 3.8+** with `uvx` for MarkItDown MCP
- **Azure subscription** (optional, for hands-on labs)

### Install MCP Tools

```bash
# Install uvx for Python MCP servers
pip install uvx

# MCP servers are auto-installed via npx and uvx when first used
```

## 💡 Example Usage

After generating a workspace (e.g., for AZ-204):

```bash
cd ../az204-cert-buddy
code .
```

### Create a Study Plan
```
@az204-cert-buddy-agent help me create a study plan for AZ-204
```

### Generate Practice Questions
```
@az204-cert-buddy-agent give me 5 practice questions on Azure App Service
@az204-cert-buddy-agent create a hard question on Azure Functions
@az204-cert-buddy-agent generate 10 questions covering all skill areas
```

### Create Hands-on Labs
```
@az204-cert-buddy-agent create a 15-minute lab on deploying a web app
@az204-cert-buddy-agent make a lab for Azure Cosmos DB integration
@az204-cert-buddy-agent generate a lab on implementing Azure Key Vault
```

### Get Recommendations
```
@az204-cert-buddy-agent what should I study next?
@az204-cert-buddy-agent I'm weak in monitoring, help me practice
```

## 🎓 Supported Exam Types

### Azure Certifications
- **Fundamentals**: AZ-900, AI-900, DP-900, SC-900, MS-900
- **Associate**: AZ-104, AZ-204, AI-102, DP-203, SC-200, SC-300
- **Expert**: AZ-305, AZ-400, SC-100

### Exam-Specific Customizations

| Exam Type | Customizations |
|-----------|----------------|
| **Azure** (AZ-*, AI-*, DP-*) | Azure MCP, hands-on labs, Azure CLI examples |
| **Security** (SC-*) | Microsoft Entra ID, policy scenarios, compliance focus |
| **Microsoft 365** (MS-*) | M365 services, admin portal tasks |
| **Fundamentals** (*-900) | Simpler labs, conceptual focus, shorter study times |

## 🔧 Customization

### Add Exam-Specific Features

Edit the generated files to add:
- Custom terminology tables in `copilot-instructions.md`
- Domain-specific best practices
- Exam-specific scenario companies
- Custom validation approaches for labs

### Extend Skills

Add new skills by creating additional folders in `.github/skills/`:
```
.github/skills/
└── <exam>-flashcard-creator/
    └── SKILL.md
```

## 📚 Current Template (AI-102)

This repository contains the **reference implementation** for:
- **Exam**: AI-102 - Designing and Implementing a Microsoft Azure AI Solution  
- **Domain**: Azure AI services, NLP, Computer Vision, Knowledge Mining
- **Status**: Production-ready, fully tested

Use this as the baseline for generating other certification workspaces.

## 🤝 Contributing

Contributions are welcome! To add support for a new exam type:

1. Fork this repository
2. Generate a workspace for the new exam
3. Test the agent, skills, and prompts
4. Submit a PR with improvements to the template

## 📄 License

MIT License - Feel free to use this template for any Microsoft certification exam preparation.

## 🙏 Acknowledgments

- **Microsoft Learn** - Official certification documentation
- **GitHub Copilot** - AI-powered coding assistant
- **MCP Servers** - Context7, Azure MCP, MarkItDown
- **Microsoft Certification Community** - Feedback and testing

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Discussions**: Join the discussions tab
- **Documentation**: See generated README in each workspace

---

## 🎯 Generation Examples

### Example 1: AZ-204 (Azure Developer)
```bash
python generate_cert_buddy.py \
  --exam AZ-204 \
  --name "Developing Solutions for Microsoft Azure" \
  --domain "Azure Development"
```

### Example 2: SC-900 (Security Fundamentals)  
```bash
python generate_cert_buddy.py \
  --exam SC-900 \
  --name "Microsoft Security, Compliance, and Identity Fundamentals" \
  --domain "Security and Compliance"
```

### Example 3: DP-203 (Data Engineering)
```bash
python generate_cert_buddy.py \
  --exam DP-203 \
  --name "Data Engineering on Microsoft Azure" \
  --domain "Data Engineering"
```

---

**Ready to ace your Microsoft certification?** Generate your study buddy now! 🚀

```
@cert-buddy-generator Create a study buddy for <YOUR-EXAM>
```
