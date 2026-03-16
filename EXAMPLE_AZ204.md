# Example: Generating an AZ-204 Study Buddy

This document demonstrates the complete process of generating and using a study buddy for **AZ-204: Developing Solutions for Microsoft Azure**.

## Step-by-Step Example

### Step 1: Generate the Workspace

#### Using the Generator Agent

Open the cert-buddy-template workspace and ask:

```
@cert-buddy-generator Create a study buddy for AZ-204
```

**Agent Response:**

```
I'll help you create a study buddy for AZ-204. Let me confirm the details:

📋 Exam Details:
- Code: AZ-204
- Name: Developing Solutions for Microsoft Azure
- Domain: Azure Development

📂 Target Directory:
- Default: ../az204-cert-buddy
- You can specify a different path if needed

Would you like to proceed with these details? (yes/no)
```

**You respond:** `yes`

**Agent continues:**

```
🚀 Generating AZ-204 Certification Study Buddy...

✓ Creating directory structure...
✓ Generating agent configuration...
✓ Creating skill files...
✓ Generating prompt templates...
✓ Configuring MCP servers...
✓ Fetching exam objectives from Microsoft Learn...
✓ Copying reference files...
✓ Generating README...

✅ Workspace generated successfully!

📂 Location: ../az204-cert-buddy
📄 Files Created: 15

Next steps:
1. cd ../az204-cert-buddy
2. code .
3. Update references/az204-objectives.md with official exam objectives
4. Ask @az204-cert-buddy-agent for help

Would you like me to open the new workspace now?
```

#### Using the Python Script

Alternatively, run:

```bash
python generate_cert_buddy.py \
  --exam AZ-204 \
  --name "Developing Solutions for Microsoft Azure" \
  --domain "Azure Development" \
  --output ../az204-cert-buddy
```

**Output:**

```
🚀 Generating AZ-204 Certification Study Buddy...
   Exam: Developing Solutions for Microsoft Azure
   Domain: Azure Development
   Output: ../az204-cert-buddy

📁 Creating directory structure...
🤖 Generating agent configuration...
🎯 Generating skill files...
📝 Generating prompt files...
📋 Generating copilot instructions...
⚙️  Generating MCP configuration...
🎯 Generating objectives file template...
📚 Copying reference files...
📄 Generating README...
🚫 Generating .gitignore...

✅ Workspace generated successfully!

📂 Next steps:
   1. cd ../az204-cert-buddy
   2. code .
   3. Ask @az204-cert-buddy-agent for help
```

---

### Step 2: Open the Generated Workspace

```bash
cd ../az204-cert-buddy
code .
```

**Workspace Structure:**

```
az204-cert-buddy/
├── .github/
│   ├── agents/
│   │   └── az204-cert-buddy-agent.agent.md
│   ├── prompts/
│   │   ├── az204-practice-questions.prompt.md
│   │   └── az204-practice-lab.prompt.md
│   ├── skills/
│   │   ├── az204-item-creator/SKILL.md
│   │   ├── az204-lab-creator/SKILL.md
│   │   └── az204-study-planner/SKILL.md
│   └── copilot-instructions.md
├── .vscode/
│   └── mcp.json
├── references/
│   ├── az204-objectives.md
│   ├── fictional-companies.md
│   └── style-guide.md
├── README.md
└── .gitignore
```

---

### Step 3: Update Exam Objectives

1. Visit the official exam page:
   https://learn.microsoft.com/en-us/credentials/certifications/exams/az-204/

2. Copy the "Skills measured" section

3. Open `references/az204-objectives.md`

4. Replace the template content with:

```markdown
# AZ-204: Developing Solutions for Microsoft Azure

**Skills Measured (as of April 2025)**

## Develop Azure compute solutions (25-30%)

### Implement containerized solutions

- Create and manage container images for solutions
- Publish an image to Azure Container Registry
- Run containers by using Azure Container Instance
- Create solutions by using Azure Container Apps

### Implement Azure App Service Web Apps

- Create an Azure App Service Web App
- Enable diagnostics logging
- Deploy code to a web app
- Configure web app settings
- Implement autoscaling

### Implement Azure Functions

- Create and deploy Azure Functions apps
- Implement input and output bindings
- Implement function triggers by using data operations, timers, and webhooks

## Develop for Azure storage (15-20%)

### Develop solutions that use Azure Cosmos DB

- Perform operations on containers and items
- Implement partitioning strategies
- Set the appropriate consistency level
- Manage change feed notifications

### Develop solutions that use Azure Blob Storage

- Set and retrieve properties and metadata
- Perform operations on data by using the appropriate SDK
- Implement storage policies and data lifecycle management

... (continue with all skill areas)
```

---

### Step 4: Create Your Study Plan

Ask the agent:

```
@az204-cert-buddy-agent help me create a study plan for AZ-204
```

**Agent Response:**

```markdown
I'll help you create a personalized study plan for the AZ-204 certification! 
Let me first show you the five skill areas and their exam weights, then I'll 
ask for your confidence in each area.

## AZ-204 Skill Areas (as of April 2025)

| Skill Area | Exam Weight |
|------------|-------------|
| Develop Azure compute solutions | 25-30% |
| Develop for Azure storage | 15-20% |
| Implement Azure security | 20-25% |
| Monitor, troubleshoot, and optimize Azure solutions | 15-20% |
| Connect to and consume Azure services and third-party services | 15-20% |

## Rate Your Confidence

Please rate your confidence level in each of these five areas. Use one of these ratings:

- **Strong** — comfortable with most objectives; needs only light review
- **Moderate** — familiar with the concepts but needs targeted practice
- **Weak** — limited experience; needs focused study
- **Unknown** — not sure; I'll treat this as weak

Please provide your confidence rating for each area:

1. **Develop Azure compute solutions** (App Service, Functions, Containers)
2. **Develop for Azure storage** (Cosmos DB, Blob Storage)
3. **Implement Azure security** (Managed identities, Key Vault)
4. **Monitor, troubleshoot, and optimize** (Application Insights, caching)
5. **Connect to and consume services** (API Management, Event Grid, Service Bus)
```

**You respond:**

```
1: Moderate
2: Weak
3: Weak
4: Moderate
5: Strong
```

**Agent generates your plan:**

```markdown
## Your Personalized AZ-204 Study Plan

Based on your confidence levels, here is your prioritized study plan:

---

### Priority 1: Develop for Azure storage (exam weight: 15-20%)

**Your confidence:** Weak
**Estimated study time:** 8-10 hours

**Focus objectives:**
- Perform operations on Azure Cosmos DB containers and items
- Implement partitioning strategies for Cosmos DB
- Perform operations on Azure Blob Storage using SDK
- Implement storage policies and lifecycle management

**Recommended Microsoft Learn modules:**
- [Develop solutions that use Azure Cosmos DB](https://learn.microsoft.com/training/modules/work-with-cosmos-db/)
- [Work with Azure Blob Storage](https://learn.microsoft.com/training/modules/work-azure-blob-storage/)

---

### Priority 2: Implement Azure security (exam weight: 20-25%)

**Your confidence:** Weak
**Estimated study time:** 10-12 hours

**Focus objectives:**
- Implement managed identities for Azure resources
- Create and manage secrets in Azure Key Vault
- Implement secure app configuration
- Manage certificates

**Recommended Microsoft Learn modules:**
- [Implement managed identities](https://learn.microsoft.com/training/modules/implement-managed-identities/)
- [Secure app configuration data](https://learn.microsoft.com/training/modules/implement-azure-key-vault/)

---

### Priority 3: Develop Azure compute solutions (exam weight: 25-30%)

**Your confidence:** Moderate
**Estimated study time:** 5-6 hours

**Focus objectives:**
- Review Azure App Service configuration and deployment
- Review Azure Functions triggers and bindings
- Review container solutions (Container Instances, Container Apps)

**Recommended Microsoft Learn modules:**
- [Deploy a website to Azure with App Service](https://learn.microsoft.com/training/modules/host-a-web-app-with-azure-app-service/)
- [Create serverless applications with Azure Functions](https://learn.microsoft.com/training/modules/create-serverless-logic-with-azure-functions/)

... (continues with remaining priorities)

---

**Total estimated study time:** 30-38 hours

Ready to start? I can generate practice questions or a hands-on lab on **Azure Cosmos DB** 
(your Priority 1).
```

---

### Step 5: Generate a Study Schedule

Ask:

```
@az204-cert-buddy-agent write this study plan into a markdown file with a day-by-day 
breakdown. Assign 1 hour block in the morning and 1 hour in the evening. Start today 
(Monday, March 17, 2026).
```

**Agent creates `my-study-plan.md`** with a complete 19-day schedule similar to the AI-102 example.

---

### Step 6: Start Practicing

#### Generate Practice Questions

```
@az204-cert-buddy-agent give me a practice question on Azure Cosmos DB partitioning
```

**Agent Response:**

```markdown
### Phase 1

#### Metadata

- **Exam:** AZ-204
- **Skill area:** Develop for Azure storage
- **Objective:** Implement partitioning strategies for Azure Cosmos DB
- **Bloom:** Apply
- **Difficulty:** Medium

#### Question

You are developing a social media application for Contoso Ltd. that stores user 
posts in Azure Cosmos DB. Each user can create multiple posts, and the application 
must efficiently query all posts from a specific user. The database will contain 
millions of posts from thousands of users. You need to choose an appropriate 
partition key that provides even distribution and efficient querying.

Which property should you use as the partition key?

A. Post ID (unique identifier for each post)
B. User ID (identifier of the user who created the post)
C. Timestamp (when the post was created)
D. Post content hash

*(Please reply with your choice: A, B, C, or D)*
```

**You respond:** `B`

**Agent responds (Phase 2):**

```markdown
**Result:** Correct! The correct answer is **B**.

#### Rationale

- **A:** This is incorrect because using Post ID as the partition key would create 
  a separate partition for each post, resulting in millions of partitions. This 
  violates the principle of co-locating related data and would make it impossible 
  to efficiently query all posts from a specific user since they would be scattered 
  across many partitions.

- **B:** This is correct because User ID provides even distribution across users 
  while co-locating all posts from the same user in one partition. This enables 
  efficient querying of all posts from a specific user with a single partition query, 
  and assuming users create a similar number of posts, the data will be evenly 
  distributed across partitions.

- **C:** This is incorrect because using Timestamp as the partition key would 
  create hot partitions where all new posts go to the same partition (the current 
  time), causing write throttling. Additionally, querying all posts from a specific 
  user would require a cross-partition query, which is less efficient and more expensive.

- **D:** This is incorrect because a hash of post content would create random 
  distribution without any logical grouping. While this might provide even 
  distribution, it would make it impossible to efficiently query related posts 
  (such as all posts from a user) since they would be randomly scattered across 
  partitions.

#### References

- [Partitioning in Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/partitioning-overview)
- [Choose a partition key](https://learn.microsoft.com/azure/cosmos-db/partition-key-best-practices)
```

#### Create a Hands-on Lab

```
@az204-cert-buddy-agent create a 15-minute lab on implementing Azure Functions 
with Cosmos DB input binding
```

**Agent Response:**

```yaml
lab:
  title: "Implement Azure Functions with Cosmos DB Input Binding"
  objective: "Create an Azure Function that uses an input binding to retrieve data from Azure Cosmos DB"
  skill_area: "Develop Azure compute solutions + Develop for Azure storage"
  estimated_time: "15 min"
  
  prerequisites:
    - "Azure subscription with Contributor permissions"
    - "Azure CLI installed (version 2.50 or later) or Azure Cloud Shell"
    - "Basic familiarity with Azure Functions and Cosmos DB"
  
  starting_state:
    - "No existing Function App or Cosmos DB account required"
    - "You will create all resources from scratch"

  cost_warning: |
    ⚠️ **Cost Information:** This lab uses Azure Functions Consumption plan 
    (free tier: 1 million executions/month) and Azure Cosmos DB serverless 
    mode (pay per request, no minimum charge). Estimated cost: Less than $0.50 
    for the lab duration. Remember to complete cleanup steps to avoid ongoing charges.

  tasks:
    - name: "Create Azure Cosmos DB account and container"
      steps: |
        1. Set variables:
           ```bash
           RG="rg-az204-functions-lab"
           LOCATION="eastus"
           COSMOS_ACCOUNT="cosmos$(date +%s)"
           DATABASE="ProductsDB"
           CONTAINER="Products"
           ```
        
        2. Create resource group:
           ```bash
           az group create --name $RG --location $LOCATION
           ```
        
        3. Create Cosmos DB account (serverless):
           ```bash
           az cosmosdb create \
             --name $COSMOS_ACCOUNT \
             --resource-group $RG \
             --locations regionName=$LOCATION \
             --capabilities EnableServerless
           ```
        
        4. Create database and container:
           ```bash
           az cosmosdb sql database create \
             --account-name $COSMOS_ACCOUNT \
             --resource-group $RG \
             --name $DATABASE
           
           az cosmosdb sql container create \
             --account-name $COSMOS_ACCOUNT \
             --resource-group $RG \
             --database-name $DATABASE \
             --name $CONTAINER \
             --partition-key-path "/category"
           ```
        
        5. Add sample data:
           ```bash
           az cosmosdb sql container create \
             --account-name $COSMOS_ACCOUNT \
             --resource-group $RG \
             --database-name $DATABASE \
             --name $CONTAINER \
             --partition-key-path "/category"
           ```

      validation:
        - "Run: `az cosmosdb show --name $COSMOS_ACCOUNT --resource-group $RG --query provisioningState`"
        - "Expected: `Succeeded`"

... (continues with remaining tasks)
```

---

### Step 7: Track Progress

Update your `my-study-plan.md`:

```markdown
### Week 1 Progress
- [x] Day 1 Morning | [x] Day 1 Evening
- [x] Day 2 Morning | [ ] Day 2 Evening  ← Currently here
- [ ] Day 3 Morning | [ ] Day 3 Evening
...

### Practice Question Scores

| Date | Topic | Score | Notes |
|------|-------|-------|-------|
| 3/17 | Cosmos DB | 4/5 | Review partitioning strategies |
| 3/17 | Blob Storage | 3/5 | Need more practice on lifecycle policies |
```

---

## Complete Example Workflow

### Day 1: Setup and Planning
1. Generate workspace ✓
2. Update objectives ✓
3. Create study plan ✓
4. Generate day-by-day schedule ✓

### Day 2-8: Focus on Storage (Priority 1)
- **Morning**: Microsoft Learn modules
- **Evening**: 5 practice questions
- **Weekend**: 1 hands-on lab

### Day 9-16: Focus on Security (Priority 2)
- **Morning**: Microsoft Learn modules
- **Evening**: 5 practice questions
- **Weekend**: 1 hands-on lab

### Day 17-20: Review Compute and Monitoring
- **Morning**: Quick module review
- **Evening**: Mixed practice questions

### Day 21: Final Practice Exam
- 40 questions (timed, 100 minutes)
- Review weak areas
- Take exam within 1 week

---

## Tips from This Example

1. **Always update objectives first** - Get official content from Microsoft Learn
2. **Be honest about confidence** - The study planner works best with accurate self-assessment
3. **Start with weak areas** - Tackle difficult topics first while motivation is high
4. **Complete labs on weekends** - Hands-on practice needs more focus time
5. **Review all rationales** - Even for correct answers, rationales provide context
6. **Track progress daily** - Check boxes and record scores to stay motivated
7. **Adjust as needed** - If a topic is harder than expected, add more study time

---

**Ready to create your own?** Use this example as a template for any Microsoft certification!

```
@cert-buddy-generator Create a study buddy for <YOUR-EXAM>
```
