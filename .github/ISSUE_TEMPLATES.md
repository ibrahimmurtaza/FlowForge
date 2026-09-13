# FlowForge Issues Template

This file documents the comprehensive descriptions for all FlowForge MVP issues, organized by feature area. Each issue follows the brieflyy format with "What to build", "Acceptance criteria", and "Blocked by" sections.

## Foundation: Auth & Workspace (Issues #3-6)

### Issue #3: [01] User Registration & Login via Supabase Auth
- **What to build**: Users can create a new account with email/password and log in via Supabase Auth
- **Key acceptance criteria**: Sign-up form, login form, session persistence, protected pages, auth redirects

### Issue #4: [02] Workspace Creation
- **What to build**: Users create a Workspace to organize Flows, team members, and Integrations
- **Key acceptance criteria**: Create workspace form, Admin role assignment, workspace selector, access control

### Issue #5: [03] Role-Based Access Control (RBAC) Foundation
- **What to build**: Implement Admin, Editor, and Viewer roles per Workspace
- **Key acceptance criteria**: Role storage, API permission checks, role management UI foundation

### Issue #6: [04] User Invitation Flow
- **What to build**: Admins invite users by email with configurable roles
- **Key acceptance criteria**: Invite email sending, unique invite link, role assignment, pending invite management

## Integrations: Email & Data Providers (Issues #7-9)

### Issue #7: [05] Data Provider Integration Management UI
- **What to build**: Admins manage connections to Apollo, Clearbit, Hunter.io, Gmail, Outlook
- **Key acceptance criteria**: Integration status display, OAuth initiation, API key entry, workspace-scoped access

### Issue #8: [06] OAuth Email Account Connection (Gmail)
- **What to build**: OAuth 2.0 authentication for Gmail with secure credential storage
- **Key acceptance criteria**: OAuth flow, token refresh, secure storage, connection status display

### Issue #9: [07] OAuth Email Account Connection (Outlook)
- **What to build**: OAuth 2.0 authentication for Outlook (parallels Gmail integration)
- **Key acceptance criteria**: OAuth flow, token refresh, secure storage, connection status display

## Flow Building: Canvas & Configuration (Issues #10-15)

### Issue #10: [08] Visual Flow Canvas with React Flow
- **What to build**: Interactive visual canvas for editing Flows as directed graphs
- **Key acceptance criteria**: Zoom/pan/snap-to-grid, drag-and-drop nodes, edge drawing, Flow autosave

### Issue #11: [09] Source Node: List Upload (CSV)
- **What to build**: Users upload CSV files and map columns to Company Record fields
- **Key acceptance criteria**: Multi-delimiter support, header auto-detection, column mapping UI, row preview

### Issue #12: [10] Source Node: Search (Data Provider Query)
- **What to build**: Query-based source node for Apollo, Clearbit, Hunter.io
- **Key acceptance criteria**: Provider selection, query builder, sample preview, error handling

### Issue #13: [11] Enrichment Node Configuration UI
- **What to build**: Configure enrichment from Apollo, Clearbit, Hunter.io (UI layer)
- **Key acceptance criteria**: Provider selection, field mapping, rate limit configuration, test data preview

### Issue #14: [12] Filter Node Configuration UI
- **What to build**: Configure filtering logic (conditions on Company Record fields)
- **Key acceptance criteria**: Condition builder, expression validation, operator support, test conditions

### Issue #15: [13] Generate Message Node Configuration UI
- **What to build**: Configure AI message generation templates and parameters
- **Key acceptance criteria**: Template editor, variable insertion, preview generation, model selection

## Flow Configuration: Email & Execution (Issues #16-18)

### Issue #16: [14] Send Email Node Configuration UI
- **What to build**: Configure email sending (recipient, subject, body templates)
- **Key acceptance criteria**: Template editor, variable substitution, preview, integration selection

### Issue #17: [15] Flow Versioning on Edit
- **What to build**: Track Flow changes and allow reverting to previous versions
- **Key acceptance criteria**: Version history table, diff view, restore from version, version metadata

### Issue #18: [16] Celery Worker Setup & Basic Orchestration
- **What to build**: Set up Celery workers for Flow execution
- **Key acceptance criteria**: Worker configuration, task queuing, job status tracking, error handling

## Flow Execution: Node Runners (Issues #19-24)

### Issue #19: [17] List Upload Source Node Execution
- **What to build**: Execute List Upload node (parse CSV, create Company Records)
- **Key acceptance criteria**: CSV parsing, field mapping application, error logging, record persistence

### Issue #20: [18] Search Source Node Execution
- **What to build**: Execute Search source node (query data providers, create records)
- **Key acceptance criteria**: Provider API calls, result parsing, rate limit handling, error recovery

### Issue #21: [19] Enrichment Node Execution (Apollo)
- **What to build**: Execute Apollo enrichment on Company Records
- **Key acceptance criteria**: API integration, field updates, error handling, request rate limiting

### Issue #22: [20] Enrichment Node Execution (Clearbit & Hunter.io)
- **What to build**: Execute Clearbit and Hunter.io enrichment
- **Key acceptance criteria**: Dual provider support, field mapping, deduplication, error handling

### Issue #23: [21] Filter Node Execution
- **What to build**: Execute filtering logic on Company Records
- **Key acceptance criteria**: Condition evaluation, record filtering, logging, bulk operations

### Issue #24: [22] AI Message Generation Node Execution
- **What to build**: Execute message generation using Anthropic API
- **Key acceptance criteria**: Claude API calls, token usage tracking, variable substitution, error fallback

## Flow Execution: Sending & Suppression (Issues #25-31)

### Issue #25: [23] Credit Pack Metering & Quota Enforcement
- **What to build**: Track credit usage and enforce plan limits
- **Key acceptance criteria**: Credit deduction per API call, quota checking, overage handling, usage dashboard

### Issue #26: [24] Bring Your Own Key (BYOK) for Anthropic API
- **What to build**: Allow users to provide their own Anthropic API key
- **Key acceptance criteria**: Key storage, API switch logic, fallback to default, usage attribution

### Issue #27: [25] Suppression List CRUD UI
- **What to build**: Create/read/update/delete email suppression list entries
- **Key acceptance criteria**: Entry management UI, bulk operations, search/filter, list status display

### Issue #28: [26] Suppression List CSV Import/Export
- **What to build**: Import/export suppression lists as CSV files
- **Key acceptance criteria**: CSV format validation, bulk import, export with filters, error reporting

### Issue #29: [27] Pre-Send Suppression Check
- **What to build**: Check suppression list before sending emails
- **Key acceptance criteria**: Efficient lookup, skip suppressed records, logging, dry-run mode

### Issue #30: [28] Unsubscribe Link Footer & Click Tracking
- **What to build**: Add unsubscribe links and track clicks
- **Key acceptance criteria**: RFC 8058 compliance, one-click unsubscribe, click tracking, unsubscribe hooks

### Issue #31: [29] Email Bounce Detection & Auto-Suppression
- **What to build**: Detect bounces and automatically suppress invalid emails
- **Key acceptance criteria**: Bounce detection, auto-add to suppression list, bounce type classification, logging

## Flow Execution: Sending & Advanced (Issues #32-37)

### Issue #32: [30] Send Email Node Execution
- **What to build**: Execute email sending via connected Gmail/Outlook accounts
- **Key acceptance criteria**: Token refresh, MIME composition, error handling, delivery logging

### Issue #33: [31] Rate Limiting Enforcement (Hourly/Daily)
- **What to build**: Enforce per-Flow rate limits
- **Key acceptance criteria**: Token bucket algorithm, configurable limits, burst handling, quota tracking

### Issue #34: [32] Test Mode
- **What to build**: Run Flows in test mode (no actual sends, preview results)
- **Key acceptance criteria**: Test data injection, dry-run execution, preview results, log retention

### Issue #35: [33] Per-Flow Cooldown Deduplication
- **What to build**: Prevent duplicate emails to the same recipient within cooldown window
- **Key acceptance criteria**: Recipient/cooldown tracking, dedup logic, exception handling, logging

### Issue #36: [34] Supabase Realtime Flow Run Log
- **What to build**: Stream Flow run logs to frontend in real-time
- **Key acceptance criteria**: WebSocket subscription, log streaming, status updates, error messages

### Issue #37: [35] Pause & Resume on Error
- **What to build**: Pause Flow runs on error and allow manual resume
- **Key acceptance criteria**: Error detection, auto-pause, resume UI, manual retry options

### Issue #38: [36] Inbound Email Polling & Storage
- **What to build**: Poll Gmail/Outlook for replies and store them
- **Key acceptance criteria**: IMAP polling, reply detection, email storage, threading, error recovery

## Flow Execution: AI & Analytics (Issues #39-43)

### Issue #39: [37] AI Reply Classification (Positive/Negative/OOO)
- **What to build**: Classify email replies using AI
- **Key acceptance criteria**: Claude classification, confidence scoring, OOO detection, logging

### Issue #40: [38] Auto-Suppress on Negative Reply Classification
- **What to build**: Automatically add to suppression list on negative reply
- **Key acceptance criteria**: Classification-triggered suppression, logging, override options

### Issue #41: [39] Flow Run Results Table
- **What to build**: Display results of a Flow run in a paginated table
- **Key acceptance criteria**: Column display, row sorting, pagination, record detail views

### Issue #42: [40] Flow Run Summary Statistics
- **What to build**: Show summary stats (records processed, sent, bounced, etc.)
- **Key acceptance criteria**: Stat calculation, display panels, real-time updates, export option

### Issue #43: [41] CSV Export of Flow Run Results
- **What to build**: Export Flow run results as CSV
- **Key acceptance criteria**: Column selection, filter application, large file handling, download link

## Scheduling & Notifications (Issues #44-47)

### Issue #44: [42] Flow Scheduling UI (Intervals + Time Picker)
- **What to build**: Configure recurring Flow execution schedules
- **Key acceptance criteria**: Interval selector, time picker, timezone support, preview next runs

### Issue #45: [43] Celery Beat Scheduled Flow Run Trigger
- **What to build**: Execute scheduled Flows via Celery Beat
- **Key acceptance criteria**: Cron schedule management, timezone handling, job status tracking, alerts

### Issue #46: [44] Golden Path Flow Templates
- **What to build**: Provide pre-built Flow templates for common use cases
- **Key acceptance criteria**: Template library, clone-to-workspace, editable after clone, documentation

### Issue #47: [45] Email Notifications on Flow Run Completion/Failure
- **What to build**: Send email notifications when Flows complete or fail
- **Key acceptance criteria**: Notification trigger configuration, email template, recipient list, logging

## Observability & Deployment (Issues #48-52)

### Issue #48: [46] In-App Notifications
- **What to build**: Display in-app toast/banner notifications for Flow events
- **Key acceptance criteria**: Toast display, notification types, persistence option, dismiss handling

### Issue #49: [47] Slack Webhook Notification
- **What to build**: Send Flow run notifications to Slack
- **Key acceptance criteria**: Webhook URL storage, message formatting, retry logic, error handling

### Issue #50: [48] Custom Webhook Notification
- **What to build**: Send Flow run notifications to arbitrary webhooks
- **Key acceptance criteria**: Webhook URL configuration, payload customization, retry logic, logging

### Issue #51: [49] Docker Compose Deployment Package
- **What to build**: Provide Docker Compose setup for self-hosted FlowForge
- **Key acceptance criteria**: Service definitions, volume management, env config, setup documentation

### Issue #52: [50] Kubernetes Helm Charts
- **What to build**: Provide Helm charts for Kubernetes deployment
- **Key acceptance criteria**: Chart structure, value overrides, StatefulSet management, documentation
