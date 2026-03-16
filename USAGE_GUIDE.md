# Certification Study Buddy - Usage Guide

This guide explains how to use the Microsoft Certification Study Buddy Template to generate and use study workspaces.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Generating a New Workspace](#generating-a-new-workspace)
3. [Using Your Study Buddy](#using-your-study-buddy)
4. [Advanced Usage](#advanced-usage)
5. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Prerequisites Check

Before you begin, ensure you have:

```bash
# Check Node.js (required for Context7 and Azure MCP)
node --version  # Should be v18 or later

# Check Python (required for MarkItDown MCP)
python3 --version  # Should be 3.8 or later

# Install uvx for Python MCP servers
pip install uvx

# Verify VS Code with GitHub Copilot
code --version
```

### Clone the Template

```bash
git clone <repo-url> cert-buddy-template
cd cert-buddy-template
code .
```

---

## Generating a New Workspace

### Method 1: Using the Generator Agent (Recommended)

1. **Open the template in VS Code**
   ```bash
   cd cert-buddy-template
   code .
   ```

2. **Ask the generator agent** in the Copilot chat:
   ```
   @cert-buddy-generator Create a study buddy for AZ-204
   ```

3. **Answer the prompts**:
   - Confirm exam code (e.g., AZ-204)
   - Verify exam name (e.g., "Developing Solutions for Microsoft Azure")
   - Specify domain (e.g., "Azure Development")
   - Choose output directory (default: `../az204-cert-buddy`)

4. **Wait for generation** (30-60 seconds)

5. **Review the output**:
   ```
   ✅ Workspace Generated Successfully!
   
   Exam: AZ-204 - Developing Solutions for Microsoft Azure
   Location: ../az204-cert-buddy
   Files Created: 15
   ```

### Method 2: Using the Python Script

```bash
# Basic usage
python generate_cert_buddy.py --exam AZ-204

# Full options
python generate_cert_buddy.py \
  --exam AZ-204 \
  --name "Developing Solutions for Microsoft Azure" \
  --domain "Azure Development" \
  --output ../az204-cert-buddy
```

### Method 3: Manual Duplication

1. Copy the entire `ai-102-cert-buddy` folder
2. Rename to `<your-exam>-cert-buddy`
3. Find and replace `ai102` with your exam code
4. Update objectives from Microsoft Learn
5. Customize copilot-instructions.md

---

## Using Your Study Buddy

### Step 1: Open the Generated Workspace

```bash
cd ../az204-cert-buddy  # Or your exam code
code .
```

### Step 2: Verify MCP Servers

Check that MCP servers are configured:
1. Open `.vscode/mcp.json`
2. Verify three servers are listed:
   - `<exam>buddy-context7`
   - `<exam>buddy-azure`
   - `<exam>buddy-markitdown`

### Step 3: Update Exam Objectives

1. Open `references/<exam>-objectives.md`
2. Visit the official Microsoft Learn exam page
3. Copy the "Skills Measured" section
4. Paste into the objectives file
5. Format using the provided structure

**Example**: For AZ-204, visit:
https://learn.microsoft.com/en-us/credentials/certifications/exams/az-204/

### Step 4: Create Your Study Plan

Ask your agent:
```
@az204-cert-buddy-agent help me create a study plan for AZ-204
```

The agent will:
1. Show the 5 skill areas with exam weights
2. Ask for your confidence in each area (Strong/Moderate/Weak/Unknown)
3. Generate a prioritized study plan with:
   - Estimated study hours per area
   - Microsoft Learn module links
   - Key objectives to focus on
   - Recommended study sequence

### Step 5: Follow Your Study Plan

The study plan includes:
- **Week-by-week breakdown** by priority
- **Microsoft Learn modules** for each area
- **Practice question recommendations**
- **Hands-on lab suggestions**

### Step 6: Practice with Questions

Generate practice questions:

```
# Single question
@az204-cert-buddy-agent give me a practice question on Azure App Service

# Multiple questions
@az204-cert-buddy-agent generate 5 medium difficulty questions on Azure Functions

# Specific skill area
@az204-cert-buddy-agent create 10 questions covering Azure Storage solutions

# Mixed difficulty
@az204-cert-buddy-agent give me 3 easy, 4 medium, and 3 hard questions on monitoring
```

**Interactive Flow**:
1. Agent presents the question with 4 options (A-D)
2. You reply with your answer (A, B, C, or D)
3. Agent reveals if correct and provides rationale for all options
4. Agent includes Microsoft Learn references

**Special Commands**:
- Type `hint` for a clue that eliminates one distractor
- Type `skip` to see the answer immediately

### Step 7: Complete Hands-on Labs

Create practice labs:

```
# Single lab
@az204-cert-buddy-agent create a 15-minute lab on deploying a web app to Azure App Service

# Specific technology
@az204-cert-buddy-agent make a lab for implementing Azure Functions with Cosmos DB

# With tool preference
@az204-cert-buddy-agent generate a lab using Azure CLI for Key Vault integration
```

**Lab Structure**:
- Prerequisites and starting state
- Task-by-task instructions
- Validation steps after each task
- Expected outputs
- Troubleshooting tips
- Complete cleanup instructions

### Step 8: Track Your Progress

Update your study plan as you go:
1. Check off completed study sessions
2. Record practice question scores
3. Mark completed labs
4. Add notes on weak areas

---

## Advanced Usage

### Custom Question Parameters

Generate questions with specific parameters:

```
@az204-cert-buddy-agent generate a practice question with:
- Skill area: Implement Azure App Service Web Apps
- Objective: Configure web app settings
- Bloom level: Apply
- Difficulty: Hard
- Item type: Multiple choice
```

### Batch Generation

Generate multiple items at once:

```
# 10 questions across all skill areas
@az204-cert-buddy-agent create a 10-question practice exam covering all skill areas proportionally

# 5 labs on different topics
@az204-cert-buddy-agent generate 5 labs covering: App Service, Functions, Storage, Cosmos DB, and Monitoring
```

### Domain-Specific Customization

Edit `.github/copilot-instructions.md` to add:

```markdown
## AZ-204 Specific Guidance

### Key Services to Emphasize
- Azure App Service (Web Apps, API Apps)
- Azure Functions
- Azure Storage (Blobs, Tables, Queues)
- Azure Cosmos DB
- Azure Key Vault
- Application Insights

### Common Scenario Companies
- Contoso Ltd. (web applications)
- Fabrikam, Inc. (microservices)
- Tailwind Traders (e-commerce)

### Best Practices
- Always use managed identities over connection strings
- Implement retry logic for transient faults
- Use Azure Key Vault for secrets
- Enable Application Insights for monitoring
```

### Creating Custom Skills

Add a new skill folder:

```
.github/skills/az204-flashcard-creator/
└── SKILL.md
```

Example flashcard skill:
```markdown
---
name: az204-flashcard-creator
description: Generate spaced-repetition flashcards for AZ-204 concepts
---

# Skill: Flashcard Creator

Generate flashcards for key AZ-204 concepts...
```

Then reference it in your agent:
```markdown
skills:
  - az204-item-creator
  - az204-lab-creator
  - az204-study-planner
  - az204-flashcard-creator  # New skill
```

### Integrating External Resources

Use MarkItDown MCP to import study materials:

```
@az204-cert-buddy-agent analyze this PDF study guide and create practice questions
[Attach PDF file]
```

---

## Troubleshooting

### MCP Servers Not Working

**Symptom**: Agent says MCP tools are unavailable

**Fix**:
1. Check `.vscode/mcp.json` exists and is valid JSON
2. Restart VS Code
3. Verify Node.js and Python are installed
4. Check MCP server output in VS Code output panel

### Agent Not Responding

**Symptom**: Agent doesn't respond or gives generic answers

**Fix**:
1. Verify agent name matches: `@<exam-code>-cert-buddy-agent`
2. Check `.github/agents/<exam>-cert-buddy-agent.agent.md` exists
3. Ensure skills are referenced correctly in agent file
4. Restart VS Code to reload agents

### Objectives File Empty

**Symptom**: Study planner can't find exam objectives

**Fix**:
1. Visit official Microsoft Learn exam page
2. Copy "Skills Measured" section
3. Paste into `references/<exam>-objectives.md`
4. Format using the template structure

### Practice Questions Not Exam-Realistic

**Symptom**: Questions don't feel like real exam questions

**Fix**:
1. Update `references/<exam>-objectives.md` with official objectives
2. Add exam-specific scenarios to `.github/copilot-instructions.md`
3. Review and update fictional company usage
4. Ensure agent is grounding answers in Microsoft Learn

### Labs Fail Validation

**Symptom**: Lab validation steps show errors

**Fix**:
1. Verify Azure subscription is active
2. Check Azure CLI is installed and authenticated: `az login`
3. Ensure proper permissions (Contributor role)
4. Verify free tier resources are available
5. Check resource naming conflicts (names must be globally unique)

### Generation Script Errors

**Symptom**: Python script fails with errors

**Fix**:
```bash
# Install dependencies
pip install -r requirements.txt  # If requirements file exists

# Check Python version
python3 --version  # Must be 3.8+

# Run with verbose output
python generate_cert_buddy.py --exam AZ-204 --output ../az204-cert-buddy
```

---

## Tips for Success

### 1. Start with the Study Planner
Always begin by creating a personalized study plan based on your confidence levels.

### 2. Focus on Weak Areas First
The study planner prioritizes weak areas and high-weight topics. Follow this order.

### 3. Complete Labs for Practical Experience
Hands-on experience is crucial. Complete at least one lab per skill area.

### 4. Review All Rationales
Even when you answer correctly, review the rationales for all options to deepen understanding.

### 5. Use Microsoft Learn References
Click through to Microsoft Learn URLs provided in question rationales and lab references.

### 6. Track Your Progress
Use the checkboxes in `my-study-plan.md` to track daily progress.

### 7. Practice Regularly
Consistent daily practice (2 hours) is more effective than marathon study sessions.

### 8. Simulate Exam Conditions
Periodically take timed practice exams without references.

### 9. Update Objectives Regularly
Microsoft updates exam objectives. Check quarterly and update your objectives file.

### 10. Join Study Groups
Share your generated workspace with study partners (remove `my-study-plan.md` first).

---

## Example Workflows

### Workflow 1: Complete Exam Prep (4-6 Weeks)

**Week 1-2**: Weak areas (NLP, Knowledge Mining)
- Morning: Microsoft Learn modules
- Evening: Practice questions (5-10 per day)
- Weekend: One hands-on lab

**Week 3-4**: Moderate areas (Planning, Bots)
- Morning: Microsoft Learn modules
- Evening: Practice questions (5-10 per day)
- Weekend: One hands-on lab

**Week 5**: Strong areas (Computer Vision)
- Quick review of Microsoft Learn
- Practice questions for retention

**Week 6**: Final prep
- Mixed practice exams
- Review weak areas from practice
- Final lab review

### Workflow 2: Targeted Skill Practice

Focus on one skill area:
```
@az204-cert-buddy-agent I need to focus on Azure App Service this week. 
Give me a study plan for this skill area only.
```

Then:
1. Complete recommended Microsoft Learn modules
2. Generate 10-15 practice questions on the topic
3. Complete 2-3 hands-on labs
4. Take a mini practice exam on the topic

### Workflow 3: Pre-Exam Cram (1 Week)

**Not recommended but sometimes necessary**:

```
@az204-cert-buddy-agent I have my exam in 7 days. 
Create an intensive study plan focusing on the highest-weight skill areas.
```

Then:
- 4 hours/day study time
- Focus only on high-weight areas (25-30%)
- Practice questions over labs
- Review rationales thoroughly
- Final practice exam 2 days before

---

## Next Steps

1. **Generate your first workspace** using the method that works best for you
2. **Update the objectives file** with official Microsoft Learn content
3. **Create your study plan** and assess your confidence
4. **Start practicing** with questions and labs
5. **Track your progress** daily
6. **Adjust your plan** based on practice question performance

**Questions?** Ask your cert-buddy agent for help at any time!

```
@<exam>-cert-buddy-agent How should I use this workspace effectively?
```

---

**Good luck with your certification journey! 🚀**
