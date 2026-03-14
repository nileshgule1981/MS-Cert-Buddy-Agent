---
name: ai102-study-planner
description: Generates a personalized AI-102 study plan based on the user's self-assessed confidence across exam skill areas, prioritizing weak areas with estimated hours and Microsoft Learn module links.
---

# Skill: ai102.study_planner.personalized

**Description:** Generates a personalized AI-102 study plan based on the user's self-assessed confidence across exam skill areas, prioritizing weak areas with estimated hours and Microsoft Learn module links.

## Grounding

**Required sources:**

- `references/ai102-objectives.md` (AI-102 skills measured, April 2025)
- Microsoft Learn (access via Context7 and Copilot web search for current Learn module URLs)
- Context7 MCP (resolve Learn module links and verify they are current)

## Workflow

1. **Present skill areas with weights.** Show the five AI-102 skill areas and their exam weight percentages:

   | Skill Area | Exam Weight |
   | --- | --- |
   | Plan and manage an Azure AI solution | 25-30% |
   | Implement decision support solutions | 15-20% |
   | Implement computer vision solutions | 20-25% |
   | Implement natural language processing solutions | 25-30% |
   | Implement knowledge mining and document intelligence solutions | 10-15% |

2. **Ask for confidence ratings.** Ask the user to rate their confidence in each area using one of these levels:
   - **Strong** -- comfortable with most objectives; needs only light review.
   - **Moderate** -- familiar with the concepts but needs targeted practice.
   - **Weak** -- limited experience; needs focused study.
   - **Unknown** -- not sure; treat as weak.

3. **Generate a prioritized study plan.** Based on the user's ratings:
   - Order areas from weakest to strongest.
   - Within equal confidence levels, prioritize areas with higher exam weight.
   - For each area, provide:
     - Estimated study hours (weak: 8-12 hours, moderate: 4-6 hours, strong: 1-2 hours).
     - Two to three specific Microsoft Learn module links (grounded via Context7 or web search).
     - Key objectives to focus on (from `references/ai102-objectives.md`).
   - Include a total estimated hours range at the bottom.

4. **Offer to start practicing.** After presenting the plan, ask: "Would you like to start with practice questions or a lab on **[first recommended topic]**?"

## Output format

```markdown
## Your Personalized AI-102 Study Plan

### Priority 1: [Skill Area Name] (exam weight: XX-XX%)

**Your confidence:** [rating]
**Estimated study time:** X-X hours

**Focus objectives:**
- [Objective 1]
- [Objective 2]
- [Objective 3]

**Recommended Microsoft Learn modules:**
- [Module title](URL)
- [Module title](URL)

---

### Priority 2: [Skill Area Name] (exam weight: XX-XX%)

... (repeat for each area)

---

**Total estimated study time:** XX-XX hours

Ready to start? I can generate practice questions or a hands-on lab on **[first recommended topic]**.
```

## Guardrails

- Do not skip any of the five skill areas. Even "strong" areas should appear in the plan with a light review recommendation.
- Do not invent Microsoft Learn module URLs. Use Context7 or web search to find real, current module links.
- Treat "unknown" confidence the same as "weak."
- Always use current Microsoft product names. See the rename table in `.github/copilot-instructions.md`.
- No contractions.

## Delivery rules

Deliver the full study plan in a single message after the user provides their confidence ratings. Do not split the plan across multiple messages.