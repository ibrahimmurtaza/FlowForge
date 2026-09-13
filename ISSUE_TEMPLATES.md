# FlowForge Issues - Comprehensive Descriptions

This document contains detailed descriptions for all 50 FlowForge MVP feature issues. Each follows the brieflyy format with "What to build", "Acceptance criteria", and "Blocked by" sections.

---

## [01] User Registration & Login via Supabase Auth

### What to build
Users can create a new account with email/password and log in via Supabase Auth. This is the foundation for all subsequent user-scoped features.

### Acceptance criteria
- [ ] Sign-up form accepts email and password, creates Supabase Auth account
- [ ] Login form authenticates users via Supabase and sets session token
- [ ] Session persists across page reloads (stored in secure cookie or localStorage)
- [ ] Authenticated user can access protected dashboard pages
- [ ] Unauthenticated users redirected to login page

### Blocked by
None (can start immediately)

---

## [02] Workspace Creation

### What to build
After logging in, users can create a Workspace to organize their Flows, team members, and Integrations. A Workspace is the top-level organizational unit; all subsequent work happens within a Workspace context.

### Acceptance criteria
- [ ] Authenticated user sees "Create Workspace" form on first login
- [ ] Workspace creation stores workspace name, owner, and creation timestamp
- [ ] User is assigned Admin role in their own Workspace
- [ ] Subsequent logins default to user's Workspace (or show selector if multiple)
- [ ] Workspace is queryable by owner and all members have isolated access

### Blocked by
#3 (User Registration & Login)

---

## [03] Role-Based Access Control (RBAC) Foundation

### What to build
Set up the database and API layer to support three Roles within a Workspace: Admin (full control), Editor (create/edit/run Flows), and Viewer (view results only). This is the foundation for User Invitation and multi-user Workspaces.

### Acceptance criteria
- [ ] User model stores role field (Admin, Editor, Viewer) per Workspace
- [ ] API endpoints check user role before allowing mutations (e.g., only Editor+ can create Flows)
- [ ] Admin users can see role management interface (ready for #6)
- [ ] Viewer-only users can access read-only pages (Flows list, results, history)

### Blocked by
#4 (Workspace Creation)

---

## [04] User Invitation Flow

### What to build
Admins can invite other users to their Workspace by email. Invitees receive an invite link, click it to sign up or log in, and are automatically added to the Workspace with their assigned role.

### Acceptance criteria
- [ ] Admin user can send invite to email address with role selection
- [ ] Invite email contains unique invite link that's valid for 7 days
- [ ] Invitee clicking link signs up with email pre-filled or logs in if existing account
- [ ] On completion, invitee sees Workspace and has assigned role
- [ ] Admin can view pending invites and resend or revoke

### Blocked by
#5 (RBAC Foundation)

---

## [05] Data Provider Integration Management UI

### What to build
Workspace Admins can see and manage Integrations (connections to Apollo, Clearbit, Hunter.io, Gmail, Outlook) in a settings page. Display which integrations are connected, allow connection/reconnection flows.

### Acceptance criteria
- [ ] Settings page shows all available integration types (Apollo, Clearbit, Hunter.io, Gmail, Outlook)
- [ ] Admin can initiate OAuth flow for email providers (Gmail, Outlook)
- [ ] Admin can enter API keys for data providers (Apollo, Clearbit, Hunter.io)
- [ ] Connected integrations show status and last connection time
- [ ] Integrations are scoped to Workspace and available to all Editors

### Blocked by
#5 (RBAC Foundation)

---

## [06] OAuth Email Account Connection (Gmail)

### What to build
Users can authenticate their Gmail account via OAuth 2.0 and grant FlowForge permission to send emails. Credentials are securely stored and refreshed automatically.

### Acceptance criteria
- [ ] OAuth flow opens Google consent screen and requests Mail.send scope
- [ ] Refresh token is securely stored in the Integration record
- [ ] Access token is cached and refreshed before expiration
- [ ] Connection shows Gmail address and last refresh time
- [ ] Users can disconnect and revoke FlowForge access

### Blocked by
#5 (RBAC Foundation)

---

## [07] OAuth Email Account Connection (Outlook)

### What to build
Users can authenticate their Outlook account via OAuth 2.0 and grant FlowForge permission to send emails. Credentials are securely stored and refreshed automatically. Parallels Gmail integration.

### Acceptance criteria
- [ ] OAuth flow opens Microsoft consent screen and requests Mail.send scope
- [ ] Refresh token is securely stored in the Integration record
- [ ] Access token is cached and refreshed before expiration
- [ ] Connection shows Outlook email address and last refresh time
- [ ] Users can disconnect and revoke FlowForge access

### Blocked by
#8 (Gmail OAuth)

---

## [08] Visual Flow Canvas with React Flow

### What to build
Implement an interactive visual canvas where users can see and edit Flows as a directed graph. Users add nodes, delete nodes, and draw edges between them. The canvas saves the Flow definition in the database.

### Acceptance criteria
- [ ] React Flow canvas renders with zoom, pan, and snap-to-grid
- [ ] Users can drag node types from a sidebar to add them to the canvas
- [ ] Users can delete nodes and edges; Flow autosaves every change
- [ ] Canvas shows node counts (Sources, Enrichments, Filters, Generators, Sends)
- [ ] Flow definition (nodes, edges, positions) is correctly serialized to/from database

### Blocked by
#5 (RBAC Foundation)

---

## [09] Source Node: List Upload (CSV)

### What to build
Users can add a List Upload Source Node to their Flow, upload a CSV file, and specify which columns map to Company Record fields (company_name, website, industry, etc.). Headers are auto-detected.

### Acceptance criteria
- [ ] CSV upload accepts tab, comma, pipe delimiters; auto-detects on file extension
- [ ] First row treated as headers; headers displayed in mapping UI
- [ ] User can map CSV columns to Company Record fields (or skip unmapped columns)
- [ ] Preview shows first 3-5 rows with mappings applied
- [ ] Upload validation: reject empty files, unknown delimiters, no headers

### Blocked by
#10 (Visual Flow Canvas)

---

## [10] Source Node: Search (Data Provider Query)

### What to build
Users can add a Search Source Node and write queries (e.g., Apollo, Clearbit API queries) to find companies. The node configuration stores query parameters; Flow Runs execute the query and populate Company Records.

### Acceptance criteria
- [ ] Config UI lets user select data provider (Apollo, Clearbit, Hunter.io)
- [ ] Query builder or raw query field; provider-specific syntax documented
- [ ] Preview option executes sample query and shows record count and field names
- [ ] Node stores query definition; Flow Run execution is deferred to #20
- [ ] Error handling for auth failures, API limits, invalid queries

### Blocked by
#8 (Gmail OAuth), #9 (List Upload)

---

## [11] Enrichment Node Configuration UI

### What to build
Workspace Admins can configure enrichment nodes that call Apollo, Clearbit, or Hunter.io APIs. The UI allows selecting the provider, mapping source fields to API request fields, and selecting output fields.

### Acceptance criteria
- [ ] Config UI lets user select enrichment provider (Apollo, Clearbit, Hunter.io)
- [ ] Field mapping UI: source fields → provider request fields
- [ ] Output field selector: choose which provider fields to enrich into Company Record
- [ ] Rate limit preview: show estimated API costs per run
- [ ] Test button: preview enrichment on sample record

### Blocked by
#10 (Visual Flow Canvas)

---

## [12] Filter Node Configuration UI

### What to build
Users can configure filter nodes with conditional logic (if/and/or/not) on Company Record fields. The UI provides a condition builder and expression editor.

### Acceptance criteria
- [ ] Condition builder UI for field, operator, value
- [ ] Support operators: =, !=, <, >, <=, >=, contains, not contains, is empty, is not empty
- [ ] AND/OR/NOT grouping and nesting
- [ ] Expression preview: show generated filter as text
- [ ] Test conditions button: apply filter to sample data and show pass/fail

### Blocked by
#10 (Visual Flow Canvas)

---

## [13] Generate Message Node Configuration UI

### What to build
Users can configure AI message generation nodes. The UI allows selecting a template, setting LLM model/parameters, and previewing generated output.

### Acceptance criteria
- [ ] Template editor: write prompt template with {{variable}} syntax
- [ ] Variable insertion UI: list available Company Record fields and Flow variables
- [ ] Model selector: Claude 3.5 Sonnet (or latest)
- [ ] Parameter sliders: temperature, max_tokens
- [ ] Preview generator: run template on sample record and show output

### Blocked by
#10 (Visual Flow Canvas)

---

## [14] Send Email Node Configuration UI

### What to build
Users can configure email sending nodes. The UI allows selecting recipient/sender integration, writing subject/body templates with variables, and previewing the generated email.

### Acceptance criteria
- [ ] Integration selector: choose Gmail or Outlook account to send from
- [ ] Recipient selector: pick Company Record field or manual email
- [ ] Subject/body template editor with {{variable}} syntax
- [ ] Variable insertion UI: list available fields from prior nodes
- [ ] Preview email button: render template on sample record

### Blocked by
#10 (Visual Flow Canvas)

---

## [15] Flow Versioning on Edit

### What to build
Track Flow changes by creating a new version each time the Flow definition is edited. Users can view version history, see diffs, and restore to a prior version.

### Acceptance criteria
- [ ] Version table shows: version number, created_at, created_by, summary of changes
- [ ] Diff view: highlight added/removed nodes, changed config
- [ ] Restore button: revert to a prior version (creates new version, doesn't delete history)
- [ ] Version metadata: user who made change, change description (optional)

### Blocked by
#14 (Send Email Node Config)

---

## [16] Celery Worker Setup & Basic Orchestration

### What to build
Set up Celery workers with Redis backend to execute Flow Runs asynchronously. Configure task queuing, job status tracking, and error handling.

### Acceptance criteria
- [ ] Celery workers configured with Redis broker
- [ ] Flow Run execution queued as Celery task
- [ ] Job status tracking: pending, running, completed, failed
- [ ] Error handling: task retry with exponential backoff, dead-letter queue
- [ ] Worker logs accessible in app (basic logging to database)

### Blocked by
#15 (Flow Versioning)

---

## [17] List Upload Source Node Execution

### What to build
Execute List Upload source nodes: parse CSV, apply column mappings, create Company Records in the database, and pass them to downstream nodes.

### Acceptance criteria
- [ ] Parse CSV file with configured delimiter
- [ ] Apply column-to-field mappings
- [ ] Validate required fields present
- [ ] Insert Company Records into database (Flow Run context)
- [ ] Log parse errors and record count in Flow Run log

### Blocked by
#16 (Celery Worker Setup)

---

## [18] Search Source Node Execution

### What to build
Execute Search source nodes: call configured data provider APIs (Apollo, Clearbit, Hunter.io), parse results into Company Records, and handle API errors and rate limits.

### Acceptance criteria
- [ ] Construct API request from node query config
- [ ] Call data provider API with workspace credentials
- [ ] Parse API response into Company Records
- [ ] Handle rate limit: queue for retry with backoff
- [ ] Handle auth errors: surface in Flow Run log

### Blocked by
#16 (Celery Worker Setup), #17 (List Upload Execution)

---

## [19] Enrichment Node Execution (Apollo)

### What to build
Execute Apollo enrichment nodes: call Apollo API with source record data, map response fields to Company Record, and handle partial success.

### Acceptance criteria
- [ ] Extract request fields from source Company Record
- [ ] Call Apollo API with workspace API key
- [ ] Map API response fields to output fields
- [ ] Handle partial enrichment (some records match, some don't)
- [ ] Log enrichment success/failure per record

### Blocked by
#16 (Celery Worker Setup)

---

## [20] Enrichment Node Execution (Clearbit & Hunter.io)

### What to build
Execute Clearbit and Hunter.io enrichment nodes. Parallels Apollo enrichment but supports dual providers in a single node.

### Acceptance criteria
- [ ] Support Clearbit and Hunter.io providers
- [ ] Extract request fields from source Company Record
- [ ] Call provider APIs with workspace credentials
- [ ] Map response fields to output fields
- [ ] Handle partial enrichment and provider-specific errors

### Blocked by
#16 (Celery Worker Setup), #19 (Apollo Enrichment)

---

## [21] Filter Node Execution

### What to build
Execute filter nodes: evaluate conditional logic on Company Records, pass matching records downstream, and track filter stats.

### Acceptance criteria
- [ ] Evaluate filter expression on each Company Record
- [ ] Support all operators and AND/OR/NOT logic
- [ ] Pass matching records to downstream nodes
- [ ] Log filter stats: records in, records out, % pass rate

### Blocked by
#16 (Celery Worker Setup)

---

## [22] AI Message Generation Node Execution

### What to build
Execute message generation nodes: call Anthropic Claude API with template and variables, track token usage, and handle failures with fallback.

### Acceptance criteria
- [ ] Render template with Company Record variables
- [ ] Call Claude API (workspace key or default)
- [ ] Track token usage (input + output)
- [ ] Add generated message to Company Record context
- [ ] Handle API errors: log, do not block downstream

### Blocked by
#16 (Celery Worker Setup)

---

## [23] Credit Pack Metering & Quota Enforcement

### What to build
Track credit usage per workspace for API calls and LLM tokens. Enforce quota limits and prevent overages without paid plan.

### Acceptance criteria
- [ ] Log credit deduction per API call (provider-specific costs)
- [ ] Log token usage (Claude calls) and convert to credits
- [ ] Check quota before executing paid operations
- [ ] Pause Flow Run if quota exceeded, surface error
- [ ] Usage dashboard: credits consumed this month, overage status

### Blocked by
#22 (AI Message Generation)

---

## [24] Bring Your Own Key (BYOK) for Anthropic API

### What to build
Allow users to provide their own Anthropic API key for Claude calls. When provided, use user's key instead of default shared key, and charge differently.

### Acceptance criteria
- [ ] Integration setting: paste Anthropic API key (encrypted storage)
- [ ] Logic switch: if BYOK key present, use it; else use default
- [ ] Flow Run logs indicate which key was used
- [ ] No credits charged for BYOK key usage
- [ ] Key can be revoked/updated from settings

### Blocked by
#5 (RBAC Foundation)

---

## [25] Suppression List CRUD UI

### What to build
Create a UI for managing email suppression lists. Users can add/remove email addresses or domains, import bulk lists, and view suppression reasons.

### Acceptance criteria
- [ ] Add single email or domain to suppression list
- [ ] Remove email/domain from suppression list
- [ ] List view with pagination and search
- [ ] Suppression reason field (bounced, unsubscribed, manual, etc.)
- [ ] Bulk edit: select multiple entries and delete/tag

### Blocked by
#5 (RBAC Foundation)

---

## [26] Suppression List CSV Import/Export

### What to build
Import email suppression lists from CSV files and export current lists as CSV for backup/sharing.

### Acceptance criteria
- [ ] CSV format: email, reason, date_added (optional columns)
- [ ] Import validates email format, rejects invalid rows, shows preview
- [ ] Bulk insert: handle 10k+ rows efficiently
- [ ] Export current list with filters applied
- [ ] Download as CSV with timestamp in filename

### Blocked by
#25 (Suppression List CRUD)

---

## [27] Pre-Send Suppression Check

### What to build
Before sending any email in a Flow Run, check if recipient is on suppression list and skip if present.

### Acceptance criteria
- [ ] Query suppression list for recipient email
- [ ] Skip Send Email node if recipient suppressed
- [ ] Log skip reason in Flow Run log
- [ ] Efficient lookup: use index or cache (not full table scan)
- [ ] Dry-run mode: test suppression check without actual skip

### Blocked by
#25 (Suppression List CRUD)

---

## [28] Unsubscribe Link Footer & Click Tracking

### What to build
Add standard unsubscribe link to email footer (RFC 8058 one-click). Track clicks on unsubscribe links and auto-suppress.

### Acceptance criteria
- [ ] Unsubscribe link footer: `<a href="{{unsubscribe_link}}">Unsubscribe</a>`
- [ ] RFC 8058 compliance: one-click unsubscribe via GET and POST
- [ ] Click tracking: log unsubscribe click with timestamp and recipient
- [ ] Auto-suppress: add recipient to suppression list on click
- [ ] Configurable footer text per Workspace

### Blocked by
#25 (Suppression List CRUD)

---

## [29] Email Bounce Detection & Auto-Suppression

### What to build
Integrate with email provider bounce feedback. Detect bounce notifications from Gmail/Outlook and automatically add bounced addresses to suppression list.

### Acceptance criteria
- [ ] Poll Gmail/Outlook for bounce notifications
- [ ] Parse bounce type: permanent (hard), temporary (soft), complaint
- [ ] Auto-suppress permanent bounces
- [ ] Log bounce detection in Flow Run context
- [ ] Bounce reason field in suppression list entry

### Blocked by
#30 (Send Email Execution)

---

## [30] Send Email Node Execution

### What to build
Execute Send Email nodes: render email template, compose MIME message, call OAuth Gmail/Outlook API, and log delivery.

### Acceptance criteria
- [ ] Render subject/body templates with Company Record variables
- [ ] Compose MIME message with HTML/plain text alternatives
- [ ] Refresh OAuth token if needed before API call
- [ ] Call Gmail/Outlook sendMessage API
- [ ] Log: recipient, subject, delivery status (success/failure/bounced)

### Blocked by
#16 (Celery Worker Setup)

---

## [31] Rate Limiting Enforcement (Hourly/Daily)

### What to build
Enforce per-Flow rate limits (emails per hour, API calls per day, etc.). Pause/queue excess records if limit exceeded.

### Acceptance criteria
- [ ] Rate limit config per Flow: hourly/daily limits, per-recipient limit
- [ ] Token bucket algorithm: allow burst up to limit, then queue
- [ ] Track usage with Redis counters (efficient, per-Flow)
- [ ] Queue excess records: retry after window resets
- [ ] Dashboard: current usage vs. limit, next reset time

### Blocked by
#30 (Send Email Execution)

---

## [32] Test Mode

### What to build
Allow users to run Flows in test mode: no actual sends, no API calls to providers, show predicted results instead.

### Acceptance criteria
- [ ] Test mode toggle: enabled per Flow Run
- [ ] Skip Send Email API call; log as "test send" instead
- [ ] Skip external API calls; mock response with sample data
- [ ] Dry-run suppression check: show which records would be suppressed
- [ ] Results table shows predicted output, not actual sends

### Blocked by
#34 (Supabase Realtime Log)

---

## [33] Per-Flow Cooldown Deduplication

### What to build
Prevent sending duplicate emails to the same recipient within a cooldown window (configurable, e.g., 7 days).

### Acceptance criteria
- [ ] Cooldown config per Flow: e.g., 7 days between sends to same recipient
- [ ] Track sent records in Flow Run context
- [ ] Before Send Email: check if recipient sent within cooldown, skip if yes
- [ ] Log deduplication: recipient skipped due to cooldown
- [ ] Admin override: force send despite cooldown

### Blocked by
#30 (Send Email Execution)

---

## [34] Supabase Realtime Flow Run Log

### What to build
Stream Flow Run logs to frontend in real-time via Supabase Realtime WebSocket subscriptions.

### Acceptance criteria
- [ ] Frontend subscribes to Supabase Realtime channel for Flow Run
- [ ] Backend publishes log events (node start, node complete, error)
- [ ] Frontend updates log display live as Flow progresses
- [ ] Log includes: timestamp, node name, status, error message (if any)
- [ ] Graceful fallback if WebSocket fails

### Blocked by
#16 (Celery Worker Setup)

---

## [35] Pause & Resume on Error

### What to build
When a Flow Run encounters an error (API failure, validation error), pause execution and allow manual retry/resume.

### Acceptance criteria
- [ ] On node error: pause Flow Run, mark as "paused_on_error"
- [ ] Error details surfaced in Flow Run log and summary
- [ ] Admin UI button: "Resume" or "Retry"
- [ ] Resume: restart from paused node with same Company Record context
- [ ] Manual editing: allow editing paused records before resume

### Blocked by
#34 (Supabase Realtime Log)

---

## [36] Inbound Email Polling & Storage

### What to build
Poll Gmail/Outlook for incoming replies to sent emails. Store reply metadata (sender, timestamp, subject, body) in database.

### Acceptance criteria
- [ ] Periodic job: check Gmail/Outlook for new messages (every 5-15 mins)
- [ ] Filter for replies to sent emails (match Message-ID or subject threading)
- [ ] Parse email: extract sender, date, subject, body, attachments
- [ ] Store reply as EmailReply record linked to Flow Run/sent email
- [ ] Handle IMAP errors and retries

### Blocked by
#7 (Outlook OAuth)

---

## [37] AI Reply Classification (Positive/Negative/OOO)

### What to build
Classify inbound email replies using Claude: positive (interested), negative (not interested), OOO (out of office).

### Acceptance criteria
- [ ] Call Claude API on reply body (workspace key or default)
- [ ] Prompt: classify as positive, negative, or OOO
- [ ] Store classification and confidence score on EmailReply record
- [ ] Handle classification errors: log, mark as "unclassified"
- [ ] Track token usage for metering

### Blocked by
#36 (Inbound Email Polling)

---

## [38] Auto-Suppress on Negative Reply Classification

### What to build
When a reply is classified as "negative", automatically add sender to suppression list.

### Acceptance criteria
- [ ] Trigger on reply classification complete
- [ ] If classification = "negative": add sender email to suppression list
- [ ] Suppression reason: "negative_reply"
- [ ] Log auto-suppression in Flow Run context
- [ ] Admin review UI: see recent auto-suppressions and override

### Blocked by
#37 (Reply Classification)

---

## [39] Flow Run Results Table

### What to build
Display results of a completed Flow Run in a paginated, sortable table. Show Company Records with fields and Flow outcomes (sent/skipped/failed).

### Acceptance criteria
- [ ] Table columns: Company fields, enrichment results, send status, any errors
- [ ] Sorting: click column header to sort
- [ ] Pagination: 50/100/250 rows per page
- [ ] Row detail: expand row to see full record, logs, email content
- [ ] Filter: by status (sent/skipped/failed/test)

### Blocked by
#16 (Celery Worker Setup)

---

## [40] Flow Run Summary Statistics

### What to build
Show summary stats for a completed Flow Run: total records, sent, skipped, failed, enrichment success rate, credits used.

### Acceptance criteria
- [ ] Stat cards: records_in, records_sent, records_skipped, records_failed
- [ ] Enrichment success rate by provider
- [ ] Email bounce rate (if replies tracked)
- [ ] Credits used (API + LLM)
- [ ] Timeline: start time, end time, duration

### Blocked by
#39 (Flow Run Results Table)

---

## [41] CSV Export of Flow Run Results

### What to build
Export Flow Run results as CSV file. Include all Company Record fields, enrichment results, and send status.

### Acceptance criteria
- [ ] CSV columns: all Company fields, enrichment outputs, send_status, sent_at
- [ ] Filter: apply current table filters to export
- [ ] Large file handling: stream to browser (don't load into memory)
- [ ] Filename: `flow_{flow_id}_run_{run_id}_{timestamp}.csv`
- [ ] Download link in Flow Run summary

### Blocked by
#39 (Flow Run Results Table)

---

## [42] Flow Scheduling UI (Intervals + Time Picker)

### What to build
Add UI to configure recurring Flow execution schedules. Users pick interval (daily/weekly/monthly) and time of day.

### Acceptance criteria
- [ ] Schedule selector: daily, weekly (select days), monthly (select day of month)
- [ ] Time picker: select hour/minute in user's timezone
- [ ] Timezone auto-detect from browser, editable
- [ ] Preview next 5 run times (formatted in user's timezone)
- [ ] Save schedule to Flow record

### Blocked by
#15 (Flow Versioning)

---

## [43] Celery Beat Scheduled Flow Run Trigger

### What to build
Set up Celery Beat scheduler to trigger recurring Flow Runs according to configured schedules.

### Acceptance criteria
- [ ] Celery Beat task: check for Flows with active schedules every 1 minute
- [ ] For each scheduled Flow: create Flow Run if next run time has passed
- [ ] Celery task: execute Flow Run (same as manual trigger)
- [ ] Scheduler runs on single Beat instance (no duplicates)
- [ ] Observability: last run time, next run time, failure count

### Blocked by
#16 (Celery Worker Setup), #42 (Scheduling UI)

---

## [44] Golden Path Flow Templates

### What to build
Provide pre-built Flow templates for common use cases (e.g., "Apollo + Enrichment + Send Email"). Users can clone a template into their workspace.

### Acceptance criteria
- [ ] Template gallery in Flow creation page
- [ ] Each template shows: name, description, node diagram
- [ ] Clone button: copy template to user's workspace
- [ ] Cloned Flow is editable (not locked)
- [ ] Template documentation: how to configure for your data

### Blocked by
#10 (Visual Flow Canvas)

---

## [45] Email Notifications on Flow Run Completion/Failure

### What to build
Send email notifications to Workspace admins when Flow Runs complete or fail. Include summary stats and link to Flow Run details.

### Acceptance criteria
- [ ] Config per Workspace: email address, notification trigger (completion/failure/both)
- [ ] Email content: Flow name, run ID, stats (records sent/failed), link to app
- [ ] Send email on Flow Run completion: success or failure
- [ ] Handle email send failures gracefully (log, don't block Flow Run)
- [ ] Unsubscribe link in notification email

### Blocked by
#40 (Flow Run Summary Stats)

---

## [46] In-App Notifications

### What to build
Display in-app toast notifications for Flow events (Flow Run started, completed, failed). Persistent notification center for recent events.

### Acceptance criteria
- [ ] Toast notification on Flow Run events
- [ ] Notification types: success, error, info, warning
- [ ] Auto-dismiss after 5s or manual dismiss
- [ ] Notification center (bell icon): list recent notifications (past 24h)
- [ ] Mark notification as read/unread

### Blocked by
#16 (Celery Worker Setup)

---

## [47] Slack Webhook Notification

### What to build
Send Flow Run notifications to Slack via webhook. Include summary stats and link to Flow Run details.

### Acceptance criteria
- [ ] Integration setting: paste Slack webhook URL (encrypted storage)
- [ ] Config per Flow: enable/disable Slack notifications, trigger (completion/failure)
- [ ] Slack message: Flow name, run stats, link to app
- [ ] Message formatting: use Slack blocks for readability
- [ ] Retry on webhook failure (exponential backoff)

### Blocked by
#40 (Flow Run Summary Stats)

---

## [48] Custom Webhook Notification

### What to build
Send Flow Run notifications to arbitrary webhooks. Users configure webhook URL and payload template.

### Acceptance criteria
- [ ] Integration setting: webhook URL and optional auth headers
- [ ] Payload template: JSON with {{variable}} syntax (Flow fields, stats)
- [ ] Config per Flow: enable/disable, trigger (completion/failure)
- [ ] Send POST request to webhook with rendered payload
- [ ] Retry on failure with exponential backoff
- [ ] Log webhook delivery status in Flow Run

### Blocked by
#40 (Flow Run Summary Stats)

---

## [49] Docker Compose Deployment Package

### What to build
Provide Docker Compose configuration for self-hosted FlowForge deployment (frontend, backend, database, Redis, Celery workers).

### Acceptance criteria
- [ ] docker-compose.yml with all services defined
- [ ] .env.example with required environment variables
- [ ] Volume management: database persistence, uploads storage
- [ ] Network setup: services communicate internally
- [ ] Setup instructions: `.env` config, `docker-compose up`, access app
- [ ] Health checks: services report healthy/unhealthy status

### Blocked by
#16 (Celery Worker Setup)

---

## [50] Kubernetes Helm Charts

### What to build
Provide Helm charts for Kubernetes deployment. Support StatefulSet for database, multiple replicas for backend/frontend, horizontal Pod autoscaling.

### Acceptance criteria
- [ ] Helm chart structure: templates, values.yaml, Chart.yaml
- [ ] Services: frontend, backend, Celery workers, PostgreSQL, Redis
- [ ] StatefulSet for database with persistent volumes
- [ ] Horizontal Pod autoscaling for backend/workers
- [ ] ConfigMap for app settings, Secret for sensitive values
- [ ] Ingress template for external access
- [ ] Documentation: values reference, deployment steps, troubleshooting

### Blocked by
#49 (Docker Compose)
