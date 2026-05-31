# Common Workplace Automation Patterns (2025)

## Pattern 1: Email-to-Structured-Data Pipeline
**Problem**: Team members send free-form updates via email that someone manually
parses and enters into a spreadsheet or system.

**Solution**:
1. Trigger: New email received matching criteria (sender, subject keyword)
2. AI layer: LLM extracts structured fields from email body (project name, status,
   blockers, completion %) using JSON-mode response
3. Write: Append extracted data to SharePoint list / Excel / database
4. Validate: Flag emails where confidence is low or required fields are missing
5. Notify: Send Teams message confirming capture or requesting missing info

**Tools**: Power Automate + AI Builder (M365 teams) OR n8n + OpenAI API (flexible teams)
**Time to implement**: 3-5 days
**Typical time saving**: 2-4 hours/week

---

## Pattern 2: Automated Report Generation
**Problem**: Someone manually copies data from multiple sources into a
PowerPoint/Word report template every week.

**Solution**:
1. Schedule: Trigger every Friday at 3pm
2. Fetch: Pull data from all sources (Excel, Jira API, SharePoint, database)
3. Transform: Calculate KPIs, RAG status, trends using pandas/Power Query
4. Generate: Populate report template (python-pptx or Word template via python-docx)
5. AI layer: LLM generates executive summary paragraph from structured data
6. Distribute: Auto-send email with attached report via Outlook/SMTP

**Tools**: Python (pandas, python-pptx, openpyxl) + LLM API + Task Scheduler/cron
**Alternative**: Power Automate + Power BI scheduled export
**Time to implement**: 1-2 weeks
**Typical time saving**: 4-8 hours/week

---

## Pattern 3: Data Aggregation & Validation
**Problem**: Data is manually collected from multiple people/files and merged
into a master tracker. Errors happen when data is inconsistent or late.

**Solution**:
1. Standardise: Create a single input form (Power Apps / Google Forms / SharePoint form)
   instead of free-form files
2. Trigger: Form submission automatically triggers data processing
3. Validate: Business rules checked automatically (budget overrun %, date logic, etc.)
4. Alert: Notify contributor immediately if their submission has issues
5. Aggregate: Auto-merge into master tracker / database

**Tools**: Power Apps + Power Automate (M365) OR Google Forms + Google Sheets + Apps Script
**Time to implement**: 1 week (form) + 1 week (automation)
**Typical time saving**: 2-3 hours/week + error reduction

---

## Pattern 4: Status Escalation & Reminder Bot
**Problem**: A coordinator manually chases team members for updates before a deadline,
sends reminders, and follows up on overdue items.

**Solution**:
1. Schedule: Run 48h and 24h before deadline
2. Check: Query tracker/Jira to find who hasn't submitted / whose items are overdue
3. Send: Personalised reminder via Teams message or email with their specific items
4. Escalate: If still unresolved 4h before deadline, notify manager automatically
5. Log: Record all reminder activity in audit trail

**Tools**: Power Automate + Teams (M365) OR n8n + Jira API + Slack/Teams
**Time to implement**: 2-3 days
**Typical time saving**: 1-2 hours/week per coordinator

---

## Pattern 5: Document Q&A Bot (RAG)
**Problem**: Team members repeatedly ask the same questions about policies,
procedures, or past decisions that are buried in documents.

**Solution**:
1. Index: Chunk and embed all relevant documents into a vector database
2. Interface: Teams bot or SharePoint-hosted chat interface
3. Retrieve: Semantic search over document chunks for each query
4. Generate: LLM generates answer grounded in retrieved chunks with citations
5. Maintain: Auto-re-index when source documents are updated in SharePoint

**Tools**: Azure AI Search + Azure OpenAI (M365/enterprise) OR
          Chroma + OpenAI API + Streamlit (small team, self-hosted)
**Time to implement**: 2-3 weeks
**Typical time saving**: Reduces ad-hoc email questions by 60-80%

---

## Pattern 6: Meeting Notes & Action Item Extraction
**Problem**: Someone manually writes up meeting notes and action items after
each meeting, then emails them to participants.

**Solution**:
1. Record: Teams meeting auto-transcription (built-in with M365)
2. Process: LLM processes transcript to extract: decisions, action items (who/what/when)
3. Format: Generate structured meeting minutes in standard template
4. Distribute: Auto-send via email / post to Teams channel / create Jira tickets
          for action items

**Tools**: Microsoft Copilot (if M365 E3/E5) OR Teams transcript + Python + LLM API
**Time to implement**: 1-2 weeks (custom) or immediate (Copilot if licenced)
**Typical time saving**: 30-60 min per meeting

---

## Pattern 7: Scheduled Data Sync & Dashboard Refresh
**Problem**: Data is manually exported from system A and imported into system B
regularly to keep dashboards or trackers up to date.

**Solution**:
1. Schedule: Automated job runs on trigger (time-based or event-based)
2. Extract: Pull data from source API / database / file
3. Transform: Apply business logic, cleaning, enrichment
4. Load: Push to target system via API or direct DB write
5. Verify: Check row counts and flag anomalies; alert on failure

**Tools**: Python + cron (self-managed) OR Azure Data Factory (enterprise)
          OR Power Automate data flows
**Time to implement**: 3-5 days
**Typical time saving**: 1-3 hours/week + improved data freshness
