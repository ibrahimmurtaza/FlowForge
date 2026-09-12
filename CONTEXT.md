# FlowForge

A purpose-built outreach automation platform for sales ops teams. Users build lead generation and outreach workflows as visual flowcharts, run them on demand or on schedule, and watch them execute in real time.

## Language

### Core Concepts

**Flow**:
A directed graph of Nodes that defines an outreach workflow — from finding companies to sending messages. A Flow is the unit users build, test, run, and schedule.
_Avoid_: Pipeline, sequence, recipe, automation

**Node**:
A single step in a Flow. Each Node has a type (Source, Enrichment, Filter, AI, Action) and a configuration. Nodes read from and write to the Company Record.
_Avoid_: Step, block, task, action (except as a Node category)

**Flow Run**:
A single execution of a Flow against a set of companies. A Flow Run tracks per-company progress, stores results, and references the Flow Version that produced it.
_Avoid_: Execution, job, run instance

**Flow Version**:
An immutable snapshot of a Flow's definition, created implicitly on every edit. Flow Runs reference the Version they executed, not the current Flow.
_Avoid_: Revision, draft

### Data Model

**Company Record**:
The implicit shared data object that moves through a Flow. Each Node reads fields from it and may add new fields. Field names are standardized across provider Nodes (e.g., always `company.employee_count`, never `num_employees`).
_Avoid_: Lead, contact, prospect, entity

**Source Node**:
A Node that produces the initial set of Company Records for a Flow Run. Two types: Search Node (queries a data provider) and List Upload Node (user-supplied CSV).
_Avoid_: Input node, trigger

**Enrichment Node**:
A Node that adds fields to a Company Record by calling an external data provider (Apollo, Clearbit, Hunter.io).
_Avoid_: Lookup node, data node

**Filter Node**:
A Node that removes Company Records that don't match user-defined boolean conditions. Uses a form-based rule builder with AND/OR logic.
_Avoid_: Condition node, gate, branch

**Generate Message Node**:
A Node that uses AI to write a personalized outreach message for each Company Record, based on enrichment data and a Prompt Configuration.
_Avoid_: AI node, writer node, compose node

**Send Email Node**:
A Node that delivers the generated message via the user's connected email account (Gmail or Outlook, OAuth). Respects Rate Limits and the Suppression List.
_Avoid_: Deliver node, output node

### AI & Messaging

**Prompt Configuration**:
The structured set of fields that guide AI message generation: company name/description, value proposition, target persona, pain points, call-to-action, tone, message length, and optional example message.
_Avoid_: Prompt template, AI config, message settings

**Credit Pack**:
A prepaid bundle of AI message generation credits. Free tier includes 50 messages/month; Starter includes 1,000/month; Pro is unlimited. Users may also bring their own AI API key.
_Avoid_: Token pack, AI credits, usage pack

**Reply Classification**:
AI-powered categorization of email replies as positive (interested), negative (not interested), or out-of-office. Opt-out classifications trigger automatic Suppression.
_Avoid_: Sentiment analysis, reply scoring

### Execution

**Rate Limit**:
User-configured throttle on the Send Email Node: maximum emails per hour and maximum emails per day. Applied per Flow.
_Avoid_: Throttle, send limit, quota

**Cooldown**:
A per-Flow deduplication window. A company that has been processed by a Flow will not be processed again by the same Flow until the Cooldown period expires (e.g., 90 days).
_Avoid_: Suppression window, dedup period, exclusion period

**Test Mode**:
A Flow Run mode that processes only the first N companies and skips the Send Email Node. Used to preview enrichment, filtering, and message generation before going live.
_Avoid_: Dry run, preview mode, sandbox

### Compliance

**Suppression List**:
An org-level registry of email addresses that must never be contacted. Populated by bounces, unsubscribe link clicks, and AI-detected opt-out replies. Admin-editable with CSV import/export.
_Avoid_: Blocklist, do-not-contact list, opt-out list

### Teams & Access

**Workspace**:
An organizational unit that groups users, Flows, Integrations, and the Suppression List. Maps to a company or team.
_Avoid_: Organization, tenant, account

**Integration**:
An account-level connection to a third-party service (Apollo, Clearbit, Hunter.io, Gmail, Outlook). Configured once per user account; available to all of that user's Flows.
_Avoid_: Connection, credential, API key (as a noun for the stored entity)

**Role**:
A user's permission level within a Workspace. Three roles: Admin (full control including billing and user management), Editor (create/edit/run Flows, view results), Viewer (view results only).
_Avoid_: Permission level, access tier
