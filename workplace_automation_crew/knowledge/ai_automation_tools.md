# AI-Powered Automation Tools (2025)

## LLM APIs for Document & Text Processing

### OpenAI GPT-4o / GPT-4o-mini
- **Use cases**: Email summarisation, executive summary generation, data extraction
  from unstructured text, RAG status assessment, natural language report writing
- **Pricing**: GPT-4o-mini $0.15/1M input tokens (very cheap for text processing)
- **Integration**: REST API, Python SDK, available in Power Automate AI Builder
- **Best for**: Text generation, summarisation, structured data extraction from emails

### Anthropic Claude (via LiteLLM gateway)
- **Use cases**: Long document analysis, multi-step reasoning, report drafting,
  complex instruction following
- **Pricing**: Via internal gateway (Sonnet 4.5) — negligible per-document cost
- **Integration**: OpenAI-compatible API, Python SDK
- **Best for**: Complex report generation, nuanced summarisation, compliance-aware writing

### Microsoft Copilot Studio
- **Type**: Microsoft's AI automation platform (built on Azure OpenAI)
- **Pricing**: $200/month per tenant (includes 25,000 messages)
- **Strengths**: Deep M365 integration, no data leaves Microsoft tenant, Teams bot,
  Word/Excel/Outlook Copilot, EU data residency available
- **Weaknesses**: Expensive, limited to Microsoft ecosystem
- **Best for**: Enterprise teams fully on M365 who want AI without leaving Microsoft

## Document Intelligence & OCR

### Azure Document Intelligence (Form Recognizer)
- **Use cases**: Extract structured data from PDFs, scanned forms, invoices
- **Pricing**: $1.50/1,000 pages
- **Strengths**: Pre-trained models for invoices/receipts, custom model training
- **Best for**: Processing scanned documents, PDFs, forms

### AWS Textract
- **Use cases**: OCR + table extraction from documents
- **Pricing**: $1.50/1,000 pages
- **Best for**: Teams on AWS needing document data extraction

## AI Email Processing

### Power Automate + AI Builder
- **Use cases**: Classify incoming emails, extract data from email body,
  route emails based on content, trigger workflows from email keywords
- **Pricing**: AI Builder credits included in some M365 plans; otherwise ~€0.40/500 credits
- **Best for**: Teams already on Power Automate who want AI email classification

### LLM-based email parser (custom Python)
- **Use cases**: Extract structured updates from free-form team emails,
  identify missing information, flag late submissions
- **Implementation**: Python script calling LLM API with structured output (JSON mode)
- **Cost**: ~€0.001 per email at GPT-4o-mini pricing
- **Best for**: Teams with Python skills needing flexible email parsing

## Reporting & Presentation Automation

### python-pptx
- **Type**: Python library for PowerPoint generation
- **Pricing**: Free, open source
- **Use cases**: Generate slide decks from data, update existing templates,
  auto-populate tables and charts
- **Best for**: Teams with Python skills generating weekly/monthly reports

### Google Slides API / Microsoft Graph API
- **Type**: REST APIs for presentation generation
- **Use cases**: Programmatically fill PowerPoint/Google Slides templates from data
- **Best for**: Cloud-native automation pipelines

### Power BI (automated refresh + export)
- **Use cases**: Replace static PowerPoint with live dashboard,
  auto-distribute reports via email subscription, embed in Teams
- **Best for**: Replacing repetitive reporting with self-serve dashboards

## AI Scheduling & Meeting Tools

### Calendly / Microsoft Bookings
- **Use cases**: Replace manual meeting scheduling via email chains
- **Best for**: Quick win for any coordination-heavy task

## Vector Search for Internal Knowledge

### Chroma (embedded)
- **Use cases**: Build internal knowledge base over team documents,
  enable semantic search over past reports, power a Q&A bot over policy docs
- **Pricing**: Free, self-hosted
- **Best for**: RAG over internal documents when data must stay on-premises
