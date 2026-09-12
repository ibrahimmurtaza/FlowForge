## Problem Statement

Sales ops teams running outreach and lead generation rely on a patchwork of separate tools — one to find companies, another to enrich them, a spreadsheet to track progress, and manual effort to write and send personalized messages. This process is slow, error-prone, and must be repeated manually each time. There is no unified, repeatable way to run these workflows, and the manual approach does not scale as a team grows.

## Solution

FlowForge is a purpose-built outreach automation platform. Users build outreach workflows as visual directed graphs (Flows) made of composable Nodes — Source, Enrichment, Filter, AI generation, and email delivery. Once built, a Flow can be run on demand or on a schedule. During execution, users watch it process companies in real time. Compliance guardrails (Suppression Lists, rate limits, unsubscribe links, opt-out detection) are baked in, not bolted on.

## User Stories

### Flow Builder

1. As an Editor, I want to open a drag-and-drop canvas, so that I can visually compose a Flow without writing code.
2. As an Editor, I want to add a Source Node to a Flow, so that I can define where Company Records come from.
3. As an Editor, I want to configure a Search Node with filters (industry, company size, geography, keywords), so that I can target the right companies.
4. As an Editor, I want to upload a CSV as a List Upload Node, so that I can run a Flow against an existing list of companies.
5. As an Editor, I want to add an Enrichment Node for Apollo, Clearbit, or Hunter.io, so that I can add fields to each Company Record.
6. As an Editor, I want to add a Filter Node with AND/OR boolean rules, so that I can drop companies that do not match my criteria.
7. As an Editor, I want to build filter conditions using a form-based rule builder (not code), so that non-technical users can configure filtering logic.
8. As an Editor, I want to add a Generate Message Node, so that AI writes a personalized outreach message for each Company Record.
9. As an Editor, I want to configure a Prompt Configuration (value proposition, persona, pain points, CTA, tone, length, example message), so that AI-generated messages reflect my intended approach.
10. As an Editor, I want to add a Send Email Node, so that generated messages are delivered via my connected email account.
11. As an Editor, I want to connect Nodes in sequence by drawing edges, so that the Flow defines a clear execution order.
12. As an Editor, I want to choose from pre-built Flow templates (golden paths), so that I can start from a working pattern instead of from scratch.
13. As an Editor, I want my Flow to be implicitly versioned on every edit, so that Flow Runs always reference the exact definition that produced them.

### Execution

14. As an Editor, I want to start a Flow Run on demand, so that I can execute the Flow immediately against the current company set.
15. As an Editor, I want to schedule a Flow to run at predefined intervals with a time-of-day picker, so that outreach runs automatically without manual triggering.
16. As an Editor, I want to run a Flow in Test Mode, so that I can preview enrichment, filtering, and message generation without sending any emails.
17. As an Editor, I want Test Mode to process only the first N companies, so that I can validate logic quickly without exhausting API credits.
18. As an Editor, I want to watch a Flow Run execute in real time, so that I can see per-company progress and per-step results as they happen.
19. As an Editor, I want a Flow Run to pause automatically when it encounters an error, so that I can investigate before deciding whether to resume or abort.
20. As an Editor, I want to resume a paused Flow Run from where it stopped, so that partial progress is not lost on transient failures.
21. As an Editor, I want per-Flow deduplication via a Cooldown window, so that the same company is never processed twice within a configurable time period.
22. As an Editor, I want to configure the Cooldown duration per Flow, so that I can control re-engagement timing.

### Rate Limiting and Compliance

23. As an Editor, I want to configure a Rate Limit on the Send Email Node (max emails per hour, max per day), so that my sending does not trigger spam filters.
24. As an Editor, I want every outgoing email to include an unsubscribe link in the footer, so that recipients can opt out in one click.
25. As an Editor, I want opt-out link clicks to automatically add the recipient to the org-level Suppression List, so that I never contact them again.
26. As an Editor, I want email bounces to automatically add the invalid address to the Suppression List, so that I do not repeatedly attempt delivery to dead addresses.
27. As an Editor, I want AI-detected opt-out replies (negative intent replies) to automatically suppress the sender, so that recipients who reply asking to be removed are respected even without clicking a link.
28. As an Editor, I want Reply Classification to categorize inbound replies as positive, negative, or out-of-office, so that I can prioritize follow-up on interested prospects.
29. As an Admin, I want to view and edit the org-level Suppression List, so that I can manage our do-not-contact registry.
30. As an Admin, I want to import and export the Suppression List as CSV, so that I can migrate data from other tools.
31. As an Editor, I want the Send Email Node to check the Suppression List before sending, so that no suppressed address is ever contacted.

### Integrations

32. As an Editor, I want to connect my Apollo account once, so that any of my Flows can use it without re-entering credentials.
33. As an Editor, I want to connect my Clearbit account once, so that enrichment is available across all Flows.
34. As an Editor, I want to connect my Hunter.io account once, so that email finding is available across all Flows.
35. As an Editor, I want to connect my Gmail account via OAuth, so that FlowForge can send emails on my behalf.
36. As an Editor, I want to connect my Outlook account via OAuth, so that I can use Outlook as my sending account.
37. As an Editor, I want FlowForge to read email replies via the connected account's read scope, so that Reply Classification and opt-out detection can work automatically.

### AI and Credit Management

38. As a Free tier user, I want 50 AI message generation credits per month, so that I can evaluate the product at no cost.
39. As a Starter tier user, I want 1,000 AI message generation credits per month, so that I can run meaningful outreach campaigns.
40. As a Pro tier user, I want unlimited AI message generation, so that I am not blocked by credit caps during high-volume campaigns.
41. As any user, I want to bring my own Anthropic API key, so that I can use my own AI budget instead of purchasing Credit Packs.
42. As an Admin, I want to see current Credit Pack usage, so that I can forecast when we will hit the monthly limit.

### Flow Results and Reporting

43. As an Editor, I want to view a Flow Run's per-company results in a table, so that I can see which companies passed filtering, what messages were generated, and what the delivery status was.
44. As an Editor, I want to expand a row to see the full Company Record and generated message for a specific company, so that I can evaluate quality at the individual level.
45. As an Editor, I want to see summary statistics for a Flow Run (companies processed, filtered out, emails sent, replies received), so that I can assess overall performance at a glance.
46. As an Editor, I want to manually export Flow Run results as CSV, so that I can share results or import them into other tools.

### Notifications

47. As an Editor, I want to receive an email notification when a Flow Run completes, so that I do not have to actively monitor the run.
48. As an Editor, I want in-app notifications when a Flow Run completes or fails, so that I stay informed while working in the app.
49. As an Admin, I want to configure a Slack webhook or custom webhook, so that Flow Run events are surfaced in our team's existing communication channels.

### Teams and Access Control

50. As an Admin, I want to invite users to my Workspace, so that my team can collaborate on Flows.
51. As an Admin, I want to assign Roles (Admin, Editor, Viewer) to each user, so that access is controlled appropriately.
52. As a Viewer, I want to view Flow Run results without being able to edit or run Flows, so that stakeholders can access outcomes without risk of changing configurations.
53. As an Admin, I want full control over billing, user management, and Integrations, so that I can manage the Workspace on behalf of our team.

### Self-Hosted Deployment

54. As an enterprise buyer, I want to deploy FlowForge via Docker Compose, so that I can run it on my own infrastructure with a single command.
55. As an enterprise buyer, I want Helm charts for Kubernetes deployment, so that I can run FlowForge in a production-grade, scalable environment.
56. As an enterprise buyer, I want to run Supabase self-hosted, so that all data stays within my own cloud environment.
57. As a self-hosted operator, I want full feature parity with the SaaS offering, so that the deployment model does not limit what my team can do.

## Implementation Decisions

### Architecture

- **Backend**: Python + FastAPI. REST API for all client-server communication.
- **Frontend**: React + React Flow (xyflow). Drag-and-drop canvas for Flow building.
- **Worker Queue**: Celery with Redis as the broker. All node execution (enrichment calls, message generation, email sending) runs in Celery workers. The web server never executes Flow logic directly.
- **Database / Auth / Realtime / Storage**: Supabase (PostgreSQL + Auth + Realtime + Storage). Supabase Realtime powers the live execution log during a Flow Run. Supabase Auth handles user sign-up, login, and session management.
- **AI**: Anthropic Claude for Generate Message Node and Reply Classification.

### Data Model

- The **Company Record** is the implicit shared data object that flows through a Flow Run. It is a dictionary. Each Node reads from it and may add new fields. Field names are standardized (e.g. `company.employee_count`, not `num_employees`). No explicit port mapping between Nodes — the schema is implicit and shared.
- **Flow Versions** are created implicitly on every edit. A Flow Run references the Flow Version that was active when it started, not the current (potentially newer) Flow definition.
- **Integrations** are account-level, not per-Flow. A user connects Apollo once; all of that user's Flows can use it.

### Node Execution

- Celery workers process Nodes. The Source Node produces Company Records; subsequent Nodes process them in parallel batches, respecting Rate Limits for the Send Email Node.
- Flow Runs persist state in PostgreSQL. If a run is paused (user-initiated or on error), it can be resumed from the last checkpoint without reprocessing already-completed company records.
- Per-Flow Cooldown deduplication is checked before processing: a Company Record whose domain was processed by this Flow within the Cooldown window is skipped.

### Scheduling

- Schedules use predefined intervals (daily, weekly, monthly) with a time-of-day picker — not a full cron expression editor. This constrains the surface area for the MVP while meeting the core use case.

### Suppression

- The Suppression List is org-level (one list per Workspace). It is not per-Flow.
- Three triggers add to the list: unsubscribe link click, email bounce, AI-detected opt-out reply (negative Reply Classification).
- The Send Email Node performs a Suppression List check immediately before each send — not at batch start — to handle entries added mid-run.

### Test Mode

- Test Mode is a property of the Flow Run, not a separate Flow. The same Flow definition is used; execution skips the Send Email Node and stops after the first N Company Records.

### Deployment

- SaaS: Hosted and managed. Default offering.
- Self-hosted (small): Docker Compose, single-command setup.
- Self-hosted (enterprise): Helm charts for Kubernetes. Self-hosted Supabase for full data residency.
- A single codebase powers all three deployment models. Feature parity is maintained.

### Credit Pack Model

- Free: 50 AI message generation credits/month.
- Starter: 1,000 credits/month.
- Pro: Unlimited.
- BYOK: Users may supply their own Anthropic API key to bypass Credit Pack metering entirely.

### Notifications

- Default: Email + in-app notifications for Flow Run completion and failure.
- Optional: Slack webhook and custom webhook, configured per Workspace by Admins.

## Testing Decisions

A good test exercises observable, external behavior — what a user or a dependent system sees — not which internal functions were called or how state is stored.

### What to test

- **Node execution correctness**: Given a Flow definition and a set of Company Records, assert the expected records exit each Node type with the expected field mutations on the Company Record.
- **Rate Limit enforcement**: Given a configured rate limit, assert the Send Email Node does not exceed the configured hourly/daily thresholds.
- **Suppression List enforcement**: Given a Suppression List entry, assert the Send Email Node skips that address regardless of where in the batch it appears.
- **Cooldown deduplication**: Given a company processed within the Cooldown window, assert it is skipped on the subsequent Flow Run.
- **Test Mode**: Given a Flow Run in Test Mode, assert the Send Email Node is never invoked and only the first N Company Records are processed.
- **Reply Classification**: Given a reply body, assert the classification (positive / negative / out-of-office) is correct, and that negative classifications trigger Suppression.
- **Implicit versioning**: Given an edit to a Flow while a Flow Run is in progress, assert the running Flow Run references the original Flow Version, not the updated one.
- **Permissions**: Given a Viewer-role user, assert they cannot trigger a Flow Run or edit a Flow.

### Seams to test at

- **Node execution logic**: Test each Node type in isolation, passing in a Company Record and asserting the output Company Record. This is the highest-value seam: it covers enrichment, filtering, message generation, and send logic without requiring a full end-to-end Flow Run.
- **Flow Run orchestrator**: Test the Celery task chain that sequences Nodes and manages Cooldown, pausing, and resuming. Use task-level mocks for external API calls.
- **API layer**: Test the FastAPI routes for CRUD on Flows, Flow Runs, Integrations, and the Suppression List. Assert correct permission enforcement by Role.
- **Suppression and Rate Limit middleware**: Unit-test the pre-send guardrail logic independently of the email provider.

No existing test prior art in the codebase (greenfield repo). Tests should follow standard Python `pytest` conventions for backend logic and React Testing Library for frontend components.

## Out of Scope

- **Plugin marketplace / custom Nodes**: The MVP ships with a fixed set of built-in Nodes. A third-party Node extension system is explicitly out of scope.
- **Per-Flow integrations**: Integrations are account-level in the MVP. Per-Flow API key overrides are not supported.
- **Full cron expression editor**: Scheduling uses predefined intervals only (daily, weekly, monthly + time-of-day). Arbitrary cron syntax is out of scope.
- **CRM integrations**: Direct push to Salesforce, HubSpot, or other CRMs is not in scope for the MVP. Results are available via manual CSV export.
- **Multi-step email sequences**: The MVP supports a single Send Email Node per Flow. Automated follow-up sequences are out of scope.
- **SOC 2 certification**: GDPR compliance is the MVP target. SOC 2 is a near-term priority, not an MVP requirement.
- **Reply thread / conversation tracking**: Reply Classification categorizes inbound replies but does not support multi-turn conversation tracking.
- **Self-hosted billing**: The self-hosted deployment does not include in-app billing management. Licensing for self-hosted is handled out-of-band.

## Further Notes

- Five canonical golden path Flow templates ship with the MVP: (1) Search → Enrich → Filter → Generate Message → Send Email; (2) List Upload → Enrich → Generate Message → Send Email; (3) Search → Filter → Generate Message → Send Email; (4) Search → Enrich → Filter → Generate Message (Test Mode); (5) blank canvas.
- Supabase Realtime is used for live Flow Run progress updates — no polling. Updates are pushed to the frontend as each Company Record completes each Node.
- The implicit schema approach means Nodes must not emit non-standard field names when a standardized equivalent exists. Field name standards need to be documented and enforced at the Node implementation layer.
- GDPR compliance at minimum means: data processing agreements with third-party providers, a privacy policy, the Suppression List mechanism, unsubscribe links, and the ability to delete Company Records on request (right to erasure).
