# RPA & Workflow Automation Tools (2025)

## Microsoft Power Automate
- **Type**: Cloud workflow automation (Microsoft 365 native)
- **Pricing**: Included in most M365 plans; Premium connectors from €12/user/month
- **Strengths**: Native integration with Outlook, Excel, SharePoint, Teams, Jira;
  no-code/low-code; pre-built connectors for 900+ apps; runs on existing M365 licence
- **Weaknesses**: Can get slow with complex logic; premium connectors add cost;
  limited AI capabilities without Copilot add-on
- **Integration Complexity**: 1/5
- **Best for**: Teams on Microsoft 365 who want quick wins without new tools
- **Common automations**: Email parsing & routing, form submission workflows,
  SharePoint document triggers, Teams notifications, Excel data aggregation

## Zapier
- **Type**: Cloud workflow automation (no-code)
- **Pricing**: Free (5 Zaps, 100 tasks/month); Starter $19.99/month (750 tasks);
  Professional $49/month (2,000 tasks)
- **Strengths**: Easiest setup (minutes to first automation), 7,000+ app integrations,
  no technical skills needed, excellent for cross-platform workflows
- **Weaknesses**: Gets expensive at scale, limited data transformation, US data processing
- **Integration Complexity**: 1/5
- **Best for**: Small teams, quick integrations between SaaS tools
- **Common automations**: Email-to-spreadsheet, form-to-CRM, Slack notifications

## n8n (Open Source)
- **Type**: Self-hostable workflow automation
- **Pricing**: Free self-hosted; Cloud from $20/month (2,500 executions)
- **Strengths**: Self-hosted option (EU data), visual builder, code nodes for custom logic,
  500+ integrations, AI nodes built-in (LLM calls, embeddings), active open source community
- **Weaknesses**: Requires server setup for self-hosted; steeper than Zapier
- **Integration Complexity**: 2/5
- **Best for**: Teams with basic DevOps capability that need EU data residency or complex logic
- **Common automations**: Data pipelines, AI-enhanced workflows, multi-step integrations

## UiPath
- **Type**: Enterprise RPA platform
- **Pricing**: Community free; Enterprise custom pricing (typically €1,000s/month)
- **Strengths**: Handles legacy desktop apps (no API needed), screen scraping,
  attended/unattended bots, enterprise governance
- **Weaknesses**: Expensive, complex to maintain, overkill for web-based tasks
- **Integration Complexity**: 4/5
- **Best for**: Large enterprises automating legacy systems with no API
- **Common automations**: ERP data entry, legacy app scraping, document processing at scale

## Python Scripts + Scheduling
- **Type**: Custom scripting (openpyxl, pandas, python-pptx, smtplib)
- **Pricing**: Free (open source libraries)
- **Strengths**: Maximum flexibility, no licensing cost, integrates with any API,
  version controlled, maintainable by developers
- **Weaknesses**: Requires Python skills, needs scheduling infrastructure (cron/Task Scheduler)
- **Integration Complexity**: 3/5
- **Best for**: Teams with Python skills needing custom data transformation
- **Common automations**: Excel data processing, report generation, email sending,
  API data fetching, file manipulation

## Microsoft Power Apps + Power BI
- **Type**: App builder + BI reporting (M365 ecosystem)
- **Pricing**: Power Apps from €4.60/user/month; Power BI Pro €8.40/user/month
- **Strengths**: Replaces manual data collection forms, live dashboards replace static reports,
  integrates with SharePoint and Excel natively
- **Best for**: Replacing manual data collection and static Excel/PowerPoint reporting

## Make (formerly Integromat)
- **Type**: Visual workflow automation
- **Pricing**: Free (1,000 ops/month); Core $9/month (10,000 ops)
- **Strengths**: More powerful than Zapier, better data transformation, cheaper at scale,
  EU-based company (GDPR compliant)
- **Integration Complexity**: 2/5
- **Best for**: Teams needing Zapier-like simplicity but with EU data and more logic
