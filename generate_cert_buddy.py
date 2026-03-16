#!/usr/bin/env python3
"""
Microsoft Certification Study Buddy Generator

This script generates a complete certification study companion workspace
based on the AI-102 template structure.

Usage:
    python generate_cert_buddy.py --exam AZ-204 --output ../az204-cert-buddy
    python generate_cert_buddy.py --exam SC-900 --domain security
"""

import argparse
import json
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import re


class CertBuddyGenerator:
    """Generates a certification study buddy workspace from the AI-102 template."""

    def __init__(self, exam_code: str, exam_name: str, domain: str, output_dir: str):
        self.exam_code = exam_code.lower()
        self.exam_code_upper = exam_code.upper()
        self.exam_name = exam_name
        self.domain = domain
        self.output_dir = Path(output_dir)
        self.template_dir = Path(__file__).parent.parent

    def generate(self) -> None:
        """Generate the complete workspace."""
        print(f"🚀 Generating {self.exam_code_upper} Certification Study Buddy...")
        print(f"   Exam: {self.exam_name}")
        print(f"   Domain: {self.domain}")
        print(f"   Output: {self.output_dir}")
        print()

        # Create directory structure
        self._create_directory_structure()

        # Generate all files
        self._generate_agent_file()
        self._generate_skill_files()
        self._generate_prompt_files()
        self._generate_copilot_instructions()
        self._generate_mcp_config()
        self._generate_objectives_file()
        self._copy_reference_files()
        self._generate_readme()
        self._generate_gitignore()

        print()
        print("✅ Workspace generated successfully!")
        print()
        print("📂 Next steps:")
        print(f"   1. cd {self.output_dir}")
        print(f"   2. code .")
        print(f"   3. Ask @{self.exam_code}-cert-buddy-agent for help")
        print()

    def _create_directory_structure(self) -> None:
        """Create the workspace directory structure."""
        print("📁 Creating directory structure...")

        dirs = [
            self.output_dir / ".github" / "agents",
            self.output_dir / ".github" / "prompts",
            self.output_dir / ".github" / "skills" / f"{self.exam_code}-item-creator",
            self.output_dir / ".github" / "skills" / f"{self.exam_code}-lab-creator",
            self.output_dir / ".github" / "skills" / f"{self.exam_code}-study-planner",
            self.output_dir / ".vscode",
            self.output_dir / "references",
        ]

        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)

    def _replace_template_vars(self, content: str) -> str:
        """Replace template variables in content."""
        replacements = {
            "ai102": self.exam_code,
            "AI-102": self.exam_code_upper,
            "ai102-cert-buddy-agent": f"{self.exam_code}-cert-buddy-agent",
            "ai102-item-creator": f"{self.exam_code}-item-creator",
            "ai102-lab-creator": f"{self.exam_code}-lab-creator",
            "ai102-study-planner": f"{self.exam_code}-study-planner",
            "ai102-practice-questions": f"{self.exam_code}-practice-questions",
            "ai102-practice-lab": f"{self.exam_code}-practice-lab",
            "ai102buddy-azure": f"{self.exam_code}buddy-azure",
            "ai102buddy-context7": f"{self.exam_code}buddy-context7",
            "ai102buddy-markitdown": f"{self.exam_code}buddy-markitdown",
            "Designing and Implementing a Microsoft Azure AI Solution": self.exam_name,
            "Azure AI solution": f"{self.domain} solution",
        }

        for old, new in replacements.items():
            content = content.replace(old, new)

        return content

    def _generate_agent_file(self) -> None:
        """Generate the agent configuration file."""
        print("🤖 Generating agent configuration...")

        source = self.template_dir / ".github" / "agents" / "ai102-cert-buddy-agent.agent.md"
        dest = self.output_dir / ".github" / "agents" / f"{self.exam_code}-cert-buddy-agent.agent.md"

        if source.exists():
            content = source.read_text()
            content = self._replace_template_vars(content)
            dest.write_text(content)

    def _generate_skill_files(self) -> None:
        """Generate skill definition files."""
        print("🎯 Generating skill files...")

        skills = ["item-creator", "lab-creator", "study-planner"]

        for skill in skills:
            source = self.template_dir / ".github" / "skills" / f"ai102-{skill}" / "SKILL.md"
            dest = self.output_dir / ".github" / "skills" / f"{self.exam_code}-{skill}" / "SKILL.md"

            if source.exists():
                content = source.read_text()
                content = self._replace_template_vars(content)
                dest.write_text(content)

    def _generate_prompt_files(self) -> None:
        """Generate prompt template files."""
        print("📝 Generating prompt files...")

        prompts = ["practice-questions", "practice-lab"]

        for prompt in prompts:
            # Check if prompt file exists
            source = self.template_dir / ".github" / "prompts" / f"ai102-{prompt}.prompt.md"
            dest = self.output_dir / ".github" / "prompts" / f"{self.exam_code}-{prompt}.prompt.md"

            if source.exists():
                content = source.read_text()
                content = self._replace_template_vars(content)
                dest.write_text(content)
            else:
                # Create a basic prompt template if source doesn't exist
                self._create_basic_prompt(dest, prompt)

    def _create_basic_prompt(self, dest: Path, prompt_type: str) -> None:
        """Create a basic prompt template if source doesn't exist."""
        if prompt_type == "practice-questions":
            content = f"""---
name: {self.exam_code}-practice-question
description: "Generate one exam-realistic {self.exam_code_upper} practice question grounded in Microsoft Learn."
argument-hint: "skillArea='...' objective='...' bloom='Apply' difficulty='medium' itemType='multiple-choice'"
agent: {self.exam_code}-cert-buddy-agent
tools:
  - {self.exam_code}buddy-azure/*
  - {self.exam_code}buddy-context7/*
  - {self.exam_code}buddy-markitdown/*
---

# {self.exam_code_upper} Practice Question

Generate **ONE** original, exam-realistic **{self.exam_code_upper}** practice question.

## Use this skill

You must follow the workspace skill **{self.exam_code}-item-creator** for item structure, guardrails, and delivery rules.

(Follow the same structure as AI-102 practice questions prompt)
"""
        else:  # practice-lab
            content = f"""---
name: {self.exam_code}-practice-lab
description: "Generate a hands-on {self.exam_code_upper} practice lab (10-20 minutes)."
argument-hint: "topic='...' duration='15' tool='Azure CLI'"
agent: {self.exam_code}-cert-buddy-agent
tools:
  - {self.exam_code}buddy-azure/*
  - {self.exam_code}buddy-context7/*
---

# {self.exam_code_upper} Practice Lab

Generate a hands-on practice lab for **{self.exam_code_upper}**.

## Use this skill

You must follow the workspace skill **{self.exam_code}-lab-creator** for lab structure and validation.

(Follow the same structure as AI-102 practice lab prompt)
"""

        dest.write_text(content)

    def _generate_copilot_instructions(self) -> None:
        """Generate copilot instructions file."""
        print("📋 Generating copilot instructions...")

        source = self.template_dir / ".github" / "copilot-instructions.md"
        dest = self.output_dir / ".github" / "copilot-instructions.md"

        if source.exists():
            content = source.read_text()
            content = self._replace_template_vars(content)
            dest.write_text(content)

    def _generate_mcp_config(self) -> None:
        """Generate MCP configuration file."""
        print("⚙️  Generating MCP configuration...")

        mcp_config = {
            "servers": {
                f"{self.exam_code}buddy-context7": {
                    "command": "npx",
                    "args": ["-y", "@upstash/context7-mcp@latest"]
                },
                f"{self.exam_code}buddy-markitdown": {
                    "type": "stdio",
                    "command": "uvx",
                    "args": ["markitdown-mcp@0.0.1a4"],
                    "gallery": "https://api.mcp.github.com",
                    "version": "0.0.1a4"
                },
                f"{self.exam_code}buddy-azure": {
                    "type": "stdio",
                    "command": "npx",
                    "args": ["-y", "@azure/mcp@latest", "server", "start"],
                    "gallery": "https://api.mcp.github.com"
                }
            }
        }

        dest = self.output_dir / ".vscode" / "mcp.json"
        dest.write_text(json.dumps(mcp_config, indent=2))

    def _generate_objectives_file(self) -> None:
        """Generate objectives file template."""
        print("🎯 Generating objectives file template...")

        content = f"""# {self.exam_code_upper}: {self.exam_name}

**Skills Measured (Update with official exam objectives)**

## Skill Area 1 (XX-XX%)

### Objective Category 1

- Specific objective 1
- Specific objective 2
- Specific objective 3

### Objective Category 2

- Specific objective 1
- Specific objective 2

## Skill Area 2 (XX-XX%)

### Objective Category 1

- Specific objective 1
- Specific objective 2

---

**Note:** Update this file with the official exam objectives from:
https://learn.microsoft.com/en-us/credentials/certifications/exams/{self.exam_code}/

Visit the official exam page and copy the "Skills measured" section to ensure accuracy.
"""

        dest = self.output_dir / "references" / f"{self.exam_code}-objectives.md"
        dest.write_text(content)

    def _copy_reference_files(self) -> None:
        """Copy reference files (fictional companies and style guide)."""
        print("📚 Copying reference files...")

        files = ["fictional-companies.md", "style-guide.md"]

        for filename in files:
            source = self.template_dir / "references" / filename
            dest = self.output_dir / "references" / filename

            if source.exists():
                shutil.copy2(source, dest)

    def _generate_readme(self) -> None:
        """Generate README file."""
        print("📄 Generating README...")

        content = f"""# {self.exam_code_upper} Certification Study Buddy

AI-powered certification study companion for **{self.exam_code_upper}: {self.exam_name}**.

## Features

### 🎯 Practice Questions
Generate exam-realistic practice questions with:
- Scenario-first approach
- Plausible distractors
- Two-phase interactive delivery
- Detailed rationales
- Microsoft Learn references

### 🔬 Hands-on Labs
Create focused 10-20 minute labs with:
- Step-by-step instructions
- Validation checkpoints
- Complete cleanup steps
- Cost awareness
- Azure MCP validation

### 📚 Study Planner
Get a personalized study plan based on:
- Your confidence assessment
- Exam skill area weights
- Estimated study hours
- Microsoft Learn modules
- Day-by-day schedule

## Quick Start

### 1. Open in VS Code
```bash
code .
```

### 2. Ask the Agent
The agent is available as `@{self.exam_code}-cert-buddy-agent`

### 3. Create Your Study Plan
```
@{self.exam_code}-cert-buddy-agent help me create a study plan for {self.exam_code_upper}
```

### 4. Generate Practice Questions
```
@{self.exam_code}-cert-buddy-agent give me a practice question on [topic]
```

### 5. Create Hands-on Labs
```
@{self.exam_code}-cert-buddy-agent create a 15-minute lab on [topic]
```

## Example Commands

- `@{self.exam_code}-cert-buddy-agent Create a study plan`
- `@{self.exam_code}-cert-buddy-agent Give me 5 practice questions on [skill area]`
- `@{self.exam_code}-cert-buddy-agent Create a lab on [topic]`
- `@{self.exam_code}-cert-buddy-agent Generate 10 medium difficulty questions`

## Workspace Structure

```
.github/
├── agents/              # Agent configurations
├── prompts/             # Prompt templates
└── skills/              # Skill definitions
.vscode/
└── mcp.json            # MCP server configuration
references/
├── {self.exam_code}-objectives.md    # Exam objectives
├── fictional-companies.md   # Scenario companies
└── style-guide.md          # Microsoft style guide
```

## MCP Servers

This workspace uses three MCP servers:

1. **Context7** - Microsoft Learn documentation access
2. **Azure MCP** - Azure command validation
3. **MarkItDown** - Document format conversion

## Prerequisites

- Visual Studio Code with GitHub Copilot
- Node.js (for Context7 and Azure MCP)
- Python with uvx (for MarkItDown MCP)
- Azure subscription (optional, for hands-on labs)

## Exam Information

- **Exam Code:** {self.exam_code_upper}
- **Exam Name:** {self.exam_name}
- **Domain:** {self.domain}
- **Official Page:** https://learn.microsoft.com/en-us/credentials/certifications/exams/{self.exam_code}/

## Study Tips

1. ✅ Start with the study planner to assess your confidence
2. ✅ Focus on weak areas first
3. ✅ Complete hands-on labs for practical experience
4. ✅ Take practice questions regularly
5. ✅ Review rationales for all questions, even correct ones

## Progress Tracking

Use `my-study-plan.md` to track your progress (this file is gitignored).

## Getting Help

Ask the agent for help at any time:
```
@{self.exam_code}-cert-buddy-agent What should I study next?
```

---

**Good luck with your {self.exam_code_upper} certification! 🚀**

Generated from the [Microsoft Certification Study Buddy Template](https://github.com/your-repo/cert-buddy-template)
"""

        dest = self.output_dir / "README.md"
        dest.write_text(content)

    def _generate_gitignore(self) -> None:
        """Generate .gitignore file."""
        print("🚫 Generating .gitignore...")

        content = """# Dependencies
node_modules/
venv/
env/

# User-specific files
my-study-plan.md
.env
.env.local

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/settings.json
.idea/

# Logs
*.log
npm-debug.log*
yarn-debug.log*

# Temporary files
*.tmp
*.temp
.cache/
"""

        dest = self.output_dir / ".gitignore"
        dest.write_text(content)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate a Microsoft Certification Study Buddy workspace"
    )
    parser.add_argument(
        "--exam",
        required=True,
        help="Exam code (e.g., AZ-204, SC-900, DP-900)",
    )
    parser.add_argument(
        "--name",
        help="Full exam name (e.g., 'Developing Solutions for Microsoft Azure')",
    )
    parser.add_argument(
        "--domain",
        help="Exam domain (e.g., 'Azure Development', 'Security')",
    )
    parser.add_argument(
        "--output",
        help="Output directory (default: ../<exam-code>-cert-buddy)",
    )

    args = parser.parse_args()

    exam_code = args.exam.upper()
    exam_name = args.name or f"Microsoft {exam_code} Certification"
    domain = args.domain or "Microsoft Azure"
    output_dir = args.output or f"../{exam_code.lower()}-cert-buddy"

    generator = CertBuddyGenerator(exam_code, exam_name, domain, output_dir)
    generator.generate()


if __name__ == "__main__":
    main()
